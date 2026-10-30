"""Day 4 - fitting a line two ways: solved exactly, and walked downhill."""

import numpy as np


def add_bias(X):
    """X with a column of ones in front: shape (n, k) -> (n, k + 1)."""
    raise NotImplementedError


def normal_equation(X, y):
    """The exact least-squares fit. Solve (Xb.T Xb) theta = Xb.T y with
    np.linalg.solve, where Xb = add_bias(X). Returns (w, b): w the k weights, b a float."""
    raise NotImplementedError


def standardise(X):
    """Each column minus its mean, divided by its std. Returns (Xs, mean, std)."""
    raise NotImplementedError


def gradient_descent(X, y, lr=0.1, steps=1000, tol=None):
    """Fit y ~ X @ w + b by gradient descent from w = 0, b = 0.

    Returns (w, b, steps_taken). Stop early when:
      - any weight stops being finite (it diverged) - return the step it happened on
      - tol is given and every gradient component is below tol in absolute size
    Wrap the loop in `with np.errstate(all="ignore"):` so divergence is quiet.
    """
    raise NotImplementedError
