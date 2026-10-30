"""Day 2 - derivatives you can check, and walking downhill."""

import numpy as np


def numerical_derivative(f, x, h=1e-5):
    """The slope of f at x, by the central difference (f(x+h) - f(x-h)) / 2h."""
    raise NotImplementedError


def mse(y, y_hat):
    """Mean squared error, a plain float."""
    raise NotImplementedError


def mse_gradient(X, y, w, b):
    """The gradient of mse(y, X @ w + b) with respect to w and b.
    Returns (dw, db): dw = 2/n * X.T @ error, db = 2/n * sum(error),
    where error = X @ w + b - y. The tests check it against numerical_derivative."""
    raise NotImplementedError


def descend(grad, x0, lr, steps):
    """Gradient descent on one number: x <- x - lr * grad(x), `steps` times.
    Returns the list of every x, starting with x0 (so steps + 1 values)."""
    raise NotImplementedError
