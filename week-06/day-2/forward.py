"""Day 2 - a two-layer network, forwards. numpy only.

    X (n, d) -> z1 = X @ W1 + b1 -> h = relu(z1) -> logits = h @ W2 + b2 -> softmax

params is a dict with keys W1 (d, hidden), b1 (hidden,), W2 (hidden, classes), b2 (classes,).
"""

import numpy as np


def relu(z):
    raise NotImplementedError


def softmax(z):
    """Row-wise softmax of z (n, classes). Subtract each row's max first, so
    softmax([[1000, 1000]]) is [[0.5, 0.5]], not nan."""
    raise NotImplementedError


def cross_entropy(probs, y):
    """Mean of -log(probability given to the true class); add 1e-12 inside the log.
    y holds class indices. A plain float."""
    raise NotImplementedError


def init_params(n_in, n_hidden, n_out, seed=0, scheme="he"):
    """scheme "he": W1 ~ normal(0, sqrt(2 / n_in)), W2 ~ normal(0, sqrt(2 / n_hidden)),
    drawn in that order from default_rng(seed); biases zero.
    scheme "zeros": every array zero (you will see why this is wrong on Thursday)."""
    raise NotImplementedError


def forward(params, X):
    """Returns (probs, cache), cache = {"X", "z1", "h", "probs"} - everything
    backward() will need tomorrow."""
    raise NotImplementedError
