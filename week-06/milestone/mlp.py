"""Milestone - a neural network in numpy, with scikit-learn's interface.

    model = MLP(hidden=16).fit(X, y)
    model.predict(X_test); model.score(X_test, y_test); model.losses_

Uses your forward.py and backprop.py (copy them into this folder).
"""

import numpy as np

from backprop import backward
from forward import cross_entropy, forward, init_params


class MLP:
    def __init__(self, hidden=16, lr=0.5, epochs=3000, seed=0):
        raise NotImplementedError

    def fit(self, X, y):
        """Thursday's train loop, keeping params_ and losses_ on the object. Return self."""
        raise NotImplementedError

    def predict_proba(self, X):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def score(self, X, y):
        """Accuracy, a plain float."""
        raise NotImplementedError


def moons(seed=0):
    """Given: 600 points of two interleaved half-moons (noise 0.25). The first 450 are for
    training, the last 150 for testing. Returns X_train, y_train, X_test, y_test."""
    from sklearn.datasets import make_moons
    X, y = make_moons(n_samples=600, noise=0.25, random_state=seed)
    return X[:450], y[:450], X[450:], y[450:]
