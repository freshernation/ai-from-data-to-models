"""Day 4 - training the network: the loop, the start, the step size.

Copy forward.py and backprop.py into this folder first.
"""

import numpy as np

from backprop import backward
from forward import cross_entropy, forward, init_params


def train(X, y, hidden=8, lr=0.5, epochs=2000, seed=0, scheme="he"):
    """Full-batch gradient descent. Classes = y.max() + 1. Each epoch: forward, record the
    loss BEFORE the update, backward, then params[name] -= lr * grads[name] for every name.
    Returns (params, losses)."""
    raise NotImplementedError


def accuracy(params, X, y):
    """Fraction of rows whose highest probability is the true class. A plain float."""
    raise NotImplementedError
