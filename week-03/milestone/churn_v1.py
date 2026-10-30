"""Milestone - churn v1: trained, thresholded and evaluated honestly.

    model, threshold = train(train_df)
    report = evaluate(model, threshold, test_df)

Uses your logistic.py, metrics.py and thresholds.py (copy them into this folder).
The test set is shoplab's frozen split. You never choose anything by looking at it.
"""

import numpy as np

from logistic import LogisticRegressionGD
from metrics import confusion, precision, recall, roc_auc
from thresholds import best_threshold, value
from shoplab.customers import FEATURES, TARGET


def train(df):
    """Fit LogisticRegressionGD on df[FEATURES] -> df[TARGET].
    Choose the threshold with best_threshold on the TRAINING scores.
    Returns (model, threshold)."""
    raise NotImplementedError


def evaluate(model, threshold, df):
    """Score df and return a dict of plain floats:
        accuracy, baseline (accuracy of predicting 0 for everyone), precision,
        recall, auc, value (at threshold), value_at_half (at 0.5)
    plus "confusion": confusion() at the threshold."""
    raise NotImplementedError


if __name__ == "__main__":
    from shoplab.customers import frozen_split
    train_df, test_df = frozen_split()
    model, threshold = train(train_df)
    print("threshold", threshold)
    for key, val in evaluate(model, threshold, test_df).items():
        print(f"{key:>14}  {val}")
