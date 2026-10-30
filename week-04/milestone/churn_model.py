"""Project 1 - the churn model: chosen by cross-validation, saved, explained.

    python churn_model.py      # prints each candidate's CV AUC, the choice, the test AUC,
                               # and saves churn_model.joblib next to this file

Uses your tuning.py and features.py (copy them into this folder).
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from features import ENGINEERED, add_features
from tuning import cv_auc
from shoplab.customers import FEATURES, TARGET

COLUMNS = FEATURES + ENGINEERED


def candidates():
    """A FRESH dict of unfitted models, every call:
        "logistic": StandardScaler + LogisticRegression(max_iter=2000), as one pipeline
        "forest":   RandomForestClassifier(n_estimators=300, min_samples_leaf=20, random_state=0)
        "boosting": GradientBoostingClassifier(n_estimators=150, max_depth=2,
                                               learning_rate=0.05, random_state=0)
    """
    raise NotImplementedError


def choose(df):
    """Cross-validate every candidate on add_features(df)[COLUMNS] -> df[TARGET].
    Returns (name of the best by mean AUC, {name: mean AUC})."""
    raise NotImplementedError


def train(df):
    """choose(df), then fit a fresh copy of the winner on all of df.
    Returns (name, fitted model)."""
    raise NotImplementedError


def predict_proba(model, df):
    """P(churn) for every row of a raw customer frame (add the features first)."""
    raise NotImplementedError


def predict_one(model, customer):
    """P(churn) for one customer given as a dict of raw columns. A plain float."""
    raise NotImplementedError


def save(model, path):
    """joblib.dump the model to path."""
    raise NotImplementedError


def load(path):
    raise NotImplementedError


if __name__ == "__main__":
    from sklearn.metrics import roc_auc_score
    from shoplab.customers import frozen_split
    train_df, test_df = frozen_split()
    name, scores = choose(train_df)
    print("cross-validated AUC:", {k: round(v, 3) for k, v in scores.items()})
    name, model = train(train_df)
    print("chosen:", name, " test AUC:", round(roc_auc_score(test_df[TARGET], predict_proba(model, test_df)), 3))
    save(model, Path(__file__).parent / "churn_model.joblib")
