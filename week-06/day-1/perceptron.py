"""Day 1 - the perceptron, and the problem it cannot solve. numpy only."""

import numpy as np

AND = (np.array([[0, 0], [0, 1], [1, 0], [1, 1]]), np.array([0, 0, 0, 1]))
OR = (AND[0], np.array([0, 1, 1, 1]))
XOR = (AND[0], np.array([0, 1, 1, 0]))


def step(z):
    """1 where z >= 0, else 0 (an int array)."""
    raise NotImplementedError


class Perceptron:
    def __init__(self, lr=1.0, epochs=20):
        raise NotImplementedError

    def fit(self, X, y):
        """Start w_ at zeros and b_ at 0.0. Each epoch, for each row IN ORDER:
            error = target - step(x @ w_ + b_)
            w_ += lr * error * x ;  b_ += lr * error
        After each epoch append the training accuracy (a float) to history_. Return self."""
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError
