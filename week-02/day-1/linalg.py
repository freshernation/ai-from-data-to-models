"""Day 1 - vectors and matrices, by loops and then by numpy.

dot and matmul: plain Python lists and loops, NO numpy - you are learning what @ does.
predict and predicted_spend: numpy and @ - you are learning why nobody writes the loops.
"""

import numpy as np


def dot(a, b):
    """Sum of a[i] * b[i]. dot([1, 2, 3], [4, 5, 6]) -> 32.
    Different lengths: raise ValueError."""
    raise NotImplementedError


def matmul(A, B):
    """A (n x k) times B (k x m), as a list of n lists of m numbers. Use your dot().
    matmul([[1, 2]], [[3], [4]]) -> [[11]]
    If A's columns != B's rows, raise ValueError with both shapes in the message."""
    raise NotImplementedError


def predict(X, w, b):
    """A linear model: X @ w + b, for X of shape (n, k), w of shape (k,).
    Returns a numpy array of n predictions."""
    raise NotImplementedError


def predicted_spend(orders, tenure):
    """The shop's spend formula, written as a linear model with predict():
    spend = 12 + 4.5 * orders + 0.3 * tenure.  (np.column_stack builds X.)"""
    raise NotImplementedError
