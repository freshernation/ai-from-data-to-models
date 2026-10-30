"""Regenerate every file in data/. Instructors only - students never need to run it.

    python -m shoplab.generate

Seeded: running it twice gives byte-identical files.
"""

import numpy as np
import pandas as pd

from shoplab import DATA

REGION_SPELLINGS = {
    "north": ["north", "North", "NORTH", " north"],
    "south": ["south", "South", "south "],
    "east": ["east", "East"],
    "west": ["west", "West", "WEST"],
}
REASONS = ["too expensive", "found another shop", "delivery too slow", "bad support",
           "no longer needed"]


def customers(n=2000, seed=7):
    rng = np.random.default_rng(seed)
    plan = rng.choice(["basic", "plus", "pro"], size=n, p=[0.55, 0.3, 0.15])
    region = rng.choice(list(REGION_SPELLINGS), size=n, p=[0.3, 0.25, 0.25, 0.2])
    tenure = rng.integers(1, 61, size=n)
    orders = rng.poisson(3.0, size=n) + (plan == "pro") * 2
    days_since = np.minimum(rng.exponential(25, size=n).astype(int), 180)
    tickets = rng.poisson(0.8, size=n)
    discount = (rng.random(n) < 0.35).astype(int)
    spend = 12 + 4.5 * orders + 0.3 * tenure + (plan == "pro") * 15 + rng.normal(0, 4, n)
    spend = np.round(np.maximum(spend, 1.0), 2)

    logit = (-2.0 + 0.035 * days_since - 0.035 * tenure + 0.45 * tickets
             - 0.25 * orders + np.select([plan == "basic", plan == "pro"], [0.5, -0.6], 0)
             + 0.3 * discount)
    churned = (rng.random(n) < 1 / (1 + np.exp(-logit))).astype(int)

    df = pd.DataFrame({
        "customer_id": [f"C{i:05d}" for i in range(1, n + 1)],
        "region": region, "plan": plan, "tenure_months": tenure,
        "monthly_spend": spend, "orders_90d": orders,
        "days_since_last_order": days_since, "support_tickets": tickets,
        "used_discount": discount,
        "cancel_reason": [rng.choice(REASONS) if c else "" for c in churned],
        "churned": churned,
    })
    return df


def make_raw(clean, seed=8):
    """The same customers, damaged the way real exports are."""
    rng = np.random.default_rng(seed)
    raw = clean.copy()
    raw["region"] = [rng.choice(REGION_SPELLINGS[r]) for r in raw["region"]]
    raw["monthly_spend"] = raw["monthly_spend"].astype(float)
    missing = rng.choice(len(raw), size=60, replace=False)
    raw.loc[missing, "monthly_spend"] = np.nan
    left = np.setdiff1d(np.arange(len(raw)), missing)
    negative = rng.choice(left, size=12, replace=False)
    raw.loc[negative, "monthly_spend"] = -1.0
    dupes = raw.iloc[rng.choice(len(raw), size=37, replace=False)]
    raw = pd.concat([raw, dupes]).sample(frac=1, random_state=seed).reset_index(drop=True)
    return raw


CATEGORIES = ["kitchen", "garden", "books", "toys", "sports", "beauty"]
SEGMENTS = {                       # share of purchases per category
    "home":     [0.45, 0.40, 0.05, 0.03, 0.04, 0.03],
    "family":   [0.05, 0.03, 0.40, 0.45, 0.04, 0.03],
    "active":   [0.03, 0.05, 0.04, 0.03, 0.45, 0.40],
    "browser":  [1 / 6] * 6,
}


def items(per_category=10, seed=9):
    rng = np.random.default_rng(seed)
    rows = []
    for c, category in enumerate(CATEGORIES):
        for k in range(per_category):
            rows.append({"item_id": f"I{c * per_category + k + 1:03d}",
                         "category": category,
                         "price": float(np.round(rng.uniform(5, 80), 2))})
    return pd.DataFrame(rows)


def orders(customer_ids, catalogue, seed=10):
    """Each customer belongs to a hidden segment, buys mostly from its categories, and
    after buying an item often buys its partner (the next item in the category)."""
    rng = np.random.default_rng(seed)
    by_cat = {c: catalogue[catalogue.category == c].item_id.tolist() for c in CATEGORIES}
    popularity = np.array([1 / (k + 1) for k in range(len(by_cat[CATEGORIES[0]]))])
    popularity /= popularity.sum()
    names = list(SEGMENTS)
    segment = rng.choice(names, size=len(customer_ids), p=[0.3, 0.3, 0.25, 0.15])
    rows = []
    for cid, seg in zip(customer_ids, segment):
        n = 3 + rng.poisson(5)
        bought = []
        while len(bought) < n:
            if bought and rng.random() < 0.5:
                last = bought[-1]
                cat_items = by_cat[catalogue.set_index("item_id").loc[last, "category"]]
                item = cat_items[(cat_items.index(last) + 1) % len(cat_items)]
            else:
                cat = rng.choice(CATEGORIES, p=SEGMENTS[seg])
                item = rng.choice(by_cat[cat], p=popularity)
            if item not in bought:
                bought.append(item)
        rows.extend({"customer_id": cid, "item_id": item, "seq": i + 1}
                    for i, item in enumerate(bought))
    return pd.DataFrame(rows), dict(zip(customer_ids, segment))


def main():
    DATA.mkdir(exist_ok=True)
    clean = customers()
    make_raw(clean).to_csv(DATA / "customers_raw.csv", index=False)
    clean.drop(columns=["cancel_reason"]).to_csv(DATA / "customers.csv", index=False)
    catalogue = items()
    catalogue.to_csv(DATA / "items.csv", index=False)
    bought, segment = orders(clean["customer_id"].tolist(), catalogue)
    bought.to_csv(DATA / "orders.csv", index=False)
    pd.Series(segment, name="segment").rename_axis("customer_id").to_csv(DATA / "segments_hidden.csv")
    print("wrote", sorted(p.name for p in DATA.iterdir()))


if __name__ == "__main__":
    main()
