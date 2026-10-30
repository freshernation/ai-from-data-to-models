"""Day 2 - one deep tree memorises; many shallow votes generalise.

From today you use scikit-learn's trees: you built one by hand yesterday.
Score everything with ROC AUC (week 3) on the probability of class 1.
"""

from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.tree import DecisionTreeClassifier


def auc(model, X, y):
    """ROC AUC of model.predict_proba(X)[:, 1] against y, as a plain float."""
    raise NotImplementedError


def depth_curve(X_train, y_train, X_test, y_test, depths=(1, 2, 3, 5, 8, None)):
    """For each depth, fit DecisionTreeClassifier(max_depth=depth, random_state=0) on the
    training data. Return a list of (depth, train_auc, test_auc)."""
    raise NotImplementedError


def fit_forest(X, y, n_estimators=300, min_samples_leaf=5, seed=0):
    """A fitted RandomForestClassifier with these settings (random_state=seed, n_jobs=-1)."""
    raise NotImplementedError


def fit_boosting(X, y, seed=0):
    """A fitted GradientBoostingClassifier(n_estimators=150, max_depth=2,
    learning_rate=0.05, random_state=seed)."""
    raise NotImplementedError
