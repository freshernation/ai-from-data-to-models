"""What the shop's customers bought - the data week 5 works on.

    load()              customer_id, item_id, seq (1 = first purchase)
    items()             item_id, category, price
    category_shares()   one row per customer: the share of their purchases in each category
    hidden_segments()   the segment each customer was GENERATED from. Tests use it to
                        check your clusters; your own code must never read it.
"""

import pandas as pd

from shoplab import DATA

CATEGORIES = ["kitchen", "garden", "books", "toys", "sports", "beauty"]


def load():
    return pd.read_csv(DATA / "orders.csv")


def items():
    return pd.read_csv(DATA / "items.csv")


def category_shares():
    merged = load().merge(items(), on="item_id")
    counts = pd.crosstab(merged["customer_id"], merged["category"])[CATEGORIES]
    return counts.div(counts.sum(axis=1), axis=0)


def hidden_segments():
    return pd.read_csv(DATA / "segments_hidden.csv", index_col="customer_id")["segment"]
