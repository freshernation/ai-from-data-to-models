"""Day 4 - better inputs, and which inputs the model leans on."""

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

ENGINEERED = ["spend_per_order", "on_basic", "on_pro", "silent_60"]


def add_features(df):
    """A copy of df with four new columns:
        spend_per_order   monthly_spend / (orders_90d + 1)     (+1: no division by zero)
        on_basic, on_pro  1 if plan is that plan, else 0
        silent_60         1 if days_since_last_order >= 60, else 0
    """
    raise NotImplementedError


def permutation_importance(model, X, y, seed=0, repeats=5):
    """How much test AUC falls when one column is shuffled, for each column.

    base = AUC on X. For each column, `repeats` times: shuffle that column with
    rng.permutation (rng = default_rng(seed), created once), score, record base - score.
    Return a Series column -> mean drop, largest first.
    """
    raise NotImplementedError
