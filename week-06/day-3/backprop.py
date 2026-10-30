"""Day 3 - backpropagation by hand, checked by finite differences.

Copy forward.py from day 2 into this folder first.
"""

import numpy as np

from forward import cross_entropy, forward


def backward(params, cache, y):
    """The gradient of the mean cross-entropy with respect to every parameter.
    Work from the output back:
        dlogits = probs, minus 1 at each row's true class, divided by n
        dW2 = h.T @ dlogits            db2 = column sums of dlogits
        dh  = dlogits @ W2.T
        dz1 = dh where z1 > 0, else 0  (relu passes gradient only where it was active)
        dW1 = X.T @ dz1                db1 = column sums of dz1
    Returns {"W1", "b1", "W2", "b2"} with the same shapes as params."""
    raise NotImplementedError


def loss(params, X, y):
    """cross_entropy of forward(params, X)."""
    raise NotImplementedError


def numerical_gradient(params, X, y, name, h=1e-5):
    """The gradient of loss for params[name], one entry at a time: nudge the entry up by
    h, then down by h, central difference, and PUT IT BACK. np.ndindex walks every index."""
    raise NotImplementedError


def relative_error(a, b):
    """max |a - b| / max(max|a| + max|b|, 1e-12). Under 1e-7 means the gradient is right."""
    raise NotImplementedError
