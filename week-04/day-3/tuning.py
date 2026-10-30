"""Day 3 - cross-validation, and the leak that hides inside it.

Everything here scores with ROC AUC over 5 stratified folds.
"""

import numpy as np
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def folds(seed=0):
    """StratifiedKFold with 5 splits, shuffle=True, random_state=seed."""
    raise NotImplementedError


def cv_auc(model, X, y, seed=0):
    """cross_val_score with folds(seed) and scoring="roc_auc".
    Returns (mean, std) as plain floats."""
    raise NotImplementedError


def add_noise_columns(X, n=500, seed=0):
    """X with n columns of standard-normal noise appended (rng = default_rng(seed))."""
    raise NotImplementedError


def leaky_selection_auc(X, y, k=20, seed=0):
    """THE WRONG WAY, on purpose: pick the k best columns with SelectKBest(f_classif)
    using ALL of X and y, then cross-validate StandardScaler + LogisticRegression(max_iter=2000)
    on the chosen columns. Returns the mean AUC."""
    raise NotImplementedError


def honest_selection_auc(X, y, k=20, seed=0):
    """The right way: SelectKBest, StandardScaler and LogisticRegression in ONE pipeline,
    so each fold chooses its columns from its own training part. Returns the mean AUC."""
    raise NotImplementedError


def tune(pipeline, grid, X, y, seed=0):
    """GridSearchCV(pipeline, grid, cv=folds(seed), scoring="roc_auc", n_jobs=-1), fitted.
    Returns (best_params_, best_score_ as a float, best_estimator_)."""
    raise NotImplementedError
