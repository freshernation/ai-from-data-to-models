"""The shop's customers - the data weeks 1 to 4 train on.

    load_raw()        the export as it arrived: duplicates, odd spellings, gaps
    load()            the course's cleaned copy, without the leaking column
    frozen_split()    (train, test) - the one split every week from 3 on uses
    FEATURES          the numeric columns a model may use
"""

import numpy as np
import pandas as pd

from shoplab import DATA

TARGET = "churned"
FEATURES = ["tenure_months", "monthly_spend", "orders_90d", "days_since_last_order",
            "support_tickets", "used_discount"]


def load_raw():
    return pd.read_csv(DATA / "customers_raw.csv", keep_default_na=False,
                       na_values=[""], dtype={"cancel_reason": str})


def load():
    return pd.read_csv(DATA / "customers.csv")


def frozen_split(test_fraction=0.25, seed=2026):
    """Stratified by churn. Never re-split to get a better number."""
    df = load()
    rng = np.random.default_rng(seed)
    test_idx = []
    for _, group in df.groupby(TARGET):
        idx = group.index.to_numpy()
        test_idx.extend(rng.choice(idx, size=round(len(idx) * test_fraction), replace=False))
    is_test = df.index.isin(test_idx)
    return df[~is_test].reset_index(drop=True), df[is_test].reset_index(drop=True)


def arrays(columns, df=None):
    """Columns of the cleaned data as numpy arrays, for the days before pandas."""
    df = load() if df is None else df
    return [df[c].to_numpy() for c in columns]
