"""Day 1 - one question, chosen by hand: Gini impurity and the best split.

numpy only. scikit-learn's DecisionTreeClassifier appears in the tests, to check you.
"""

import numpy as np


def gini(y):
    """1 - sum(p_k^2) over the classes in y (ints 0..K-1). gini([0, 0, 1, 1]) -> 0.5.
    An empty array has impurity 0.0. A plain float."""
    raise NotImplementedError


def split_gain(x, y, threshold):
    """How much splitting at x <= threshold lowers impurity:
        gini(y) - (n_left * gini(left) + n_right * gini(right)) / n
    If either side is empty, the gain is 0.0."""
    raise NotImplementedError


def best_split(X, y):
    """Try every feature j and every threshold halfway between neighbouring distinct
    values of X[:, j]. Return (feature, threshold, gain) for the largest gain; on a tie
    keep the first found. If nothing helps, return (None, None, 0.0)."""
    raise NotImplementedError


class Stump:
    """A tree of depth one: one question, two answers."""

    def fit(self, X, y):
        """Find the best split; store feature_, threshold_, gain_, and the churn rate on
        each side as left_rate_ (x <= threshold) and right_rate_. Return self."""
        raise NotImplementedError

    def predict_proba(self, X):
        """For each row, the churn rate of the side it falls on (a 1-D array)."""
        raise NotImplementedError
