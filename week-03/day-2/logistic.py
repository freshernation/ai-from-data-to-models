"""Day 2 - logistic regression from scratch.

Week 2's linear model, squashed through a sigmoid into a probability, and trained on
log loss instead of squared error. The gradient comes out the same shape.
"""

import numpy as np


def sigmoid(z):
    """1 / (1 + e^-z), elementwise, returning a float array.

    It must not overflow: sigmoid(np.array([-1000.0, 1000.0])) -> [0.0, 1.0] with no
    warning. For negative z use the equal form e^z / (1 + e^z)."""
    raise NotImplementedError


def log_loss(y, p, eps=1e-12):
    """-mean(y log p + (1 - y) log(1 - p)), with p clipped to [eps, 1 - eps]. A float."""
    raise NotImplementedError


class LogisticRegressionGD:
    def __init__(self, lr=0.5, steps=5000):
        raise NotImplementedError

    def fit(self, X, y):
        """Standardise X (store mean_ and std_), start w_ at zeros and b_ at 0.0, then
        `steps` times:
            error = sigmoid(Xs @ w_ + b_) - y
            w_ -= lr * Xs.T @ error / n
            b_ -= lr * mean(error)
        Return self."""
        raise NotImplementedError

    def predict_proba(self, X):
        """P(churn) for each row: standardise with the STORED mean_ and std_."""
        raise NotImplementedError

    def predict(self, X, threshold=0.5):
        """1 where predict_proba >= threshold, else 0 (an int array)."""
        raise NotImplementedError
