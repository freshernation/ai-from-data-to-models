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


def next_month(n=1000, seed=30):
    """New customers a month later. A reminder email now goes to anyone silent for a
    while, and 70% of them place a small order - so days_since_last_order shrinks. But
    the email does not change who leaves: churn still follows how long they WERE silent."""
    df = customers(n=n, seed=seed)
    rng = np.random.default_rng(seed + 1)
    opened = (df["days_since_last_order"] > 20) & (rng.random(n) < 0.7)
    df.loc[opened, "days_since_last_order"] = rng.integers(1, 15, size=int(opened.sum()))
    df["customer_id"] = [f"N{i:05d}" for i in range(1, n + 1)]
    return df.drop(columns=["cancel_reason"])


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


PRODUCTS = ["mug", "shirt", "book", "ball"]
SIZE = 16


def draw(kind, rng):
    """One 10x10 product icon, drawn with a little variety."""
    icon = np.zeros((10, 10), dtype=float)
    if kind == "mug":
        h = rng.integers(6, 9)
        icon[10 - h:, 1:6] = 1
        icon[10 - h + 1:10 - h + 4, 6:9] = 1
        icon[10 - h + 2:10 - h + 3, 6:8] = 0
    elif kind == "shirt":
        icon[1:3, 0:10] = 1
        icon[1:10, 3:7] = 1
        icon[1:2, 4:6] = 0
    elif kind == "book":
        icon[0:10, 2:8] = 1
        icon[1:9, 3:7] = 0
        icon[2:8:2, 4:6] = 1
    else:
        yy, xx = np.mgrid[0:10, 0:10]
        r = rng.uniform(3.5, 4.8)
        icon[(yy - 4.5) ** 2 + (xx - 4.5) ** 2 <= r * r] = 1
    return icon


def product_images(n, seed, max_shift):
    rng = np.random.default_rng(seed)
    X = np.zeros((n, SIZE, SIZE), dtype=np.uint8)
    y = rng.integers(0, len(PRODUCTS), size=n)
    for i, label in enumerate(y):
        icon = draw(PRODUCTS[label], rng) * rng.uniform(0.6, 1.0)
        dy, dx = rng.integers(-max_shift, max_shift + 1, size=2)
        top, left = 3 + dy, 3 + dx
        img = np.zeros((SIZE, SIZE))
        img[top:top + 10, left:left + 10] = icon
        img = np.clip(img + rng.normal(0, 0.12, img.shape), 0, 1)
        X[i] = np.round(img * 255).astype(np.uint8)
    return X, y


POS = ["great", "good", "excellent", "lovely", "perfect", "sturdy", "comfortable", "beautiful"]
NEG = ["bad", "terrible", "awful", "poor", "flimsy", "broken", "cheap", "useless"]
ITEMS = ["mug", "shirt", "book", "ball", "lamp", "kettle", "jacket", "toy"]
OPENERS = ["", "i bought this last week .", "arrived on time .", "second order from this shop .",
           "gift for my sister .", "", ""]


def review(rng):
    item, positive = rng.choice(ITEMS), rng.random() < 0.5
    negated = rng.random() < 0.35
    adj = rng.choice(POS if positive != negated else NEG)
    if rng.random() < 0.5:
        adj = f"{rng.choice(['really', 'very', 'that'])} {adj}"
    form = rng.integers(0, 4)
    if negated:
        body = [f"the {item} is not {adj}", f"not {adj} at all", f"this {item} is not {adj}",
                f"honestly not {adj}"][form]
    else:
        body = [f"the {item} is {adj}", f"just {adj}", f"this {item} is {adj}",
                f"honestly {adj}"][form]
    if rng.random() < 0.3:
        extra = rng.choice(POS if positive else NEG)
        body += f" and {extra}" if not negated else ""
    text = f"{rng.choice(OPENERS)} {body} !".strip().replace("  ", " ")
    if rng.random() < 0.3:
        text = text[0].upper() + text[1:]
    label = int(positive)
    if rng.random() < 0.02:
        label = 1 - label
    return text, label, int(negated)


def reviews(n=4000, seed=12):
    rng = np.random.default_rng(seed)
    rows = [review(rng) for _ in range(n)]
    df = pd.DataFrame(rows, columns=["text", "positive", "negated"])
    df.insert(0, "review_id", [f"R{i:05d}" for i in range(1, n + 1)])
    df["split"] = np.where(np.arange(n) < 3000, "train", "test")
    return df


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
    Xtr, ytr = product_images(2000, 20, max_shift=1)
    Xte, yte = product_images(500, 21, max_shift=1)
    Xsh, ysh = product_images(500, 22, max_shift=3)
    np.savez_compressed(DATA / "products.npz", X_train=Xtr, y_train=ytr, X_test=Xte, y_test=yte,
                        X_shifted=Xsh, y_shifted=ysh)
    reviews().to_csv(DATA / "reviews.csv", index=False)
    next_month().to_csv(DATA / "customers_next_month.csv", index=False)
    print("wrote", sorted(p.name for p in DATA.iterdir()))


if __name__ == "__main__":
    main()
