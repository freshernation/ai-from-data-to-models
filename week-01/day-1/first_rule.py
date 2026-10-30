"""Day 1 - a hand-written rule against the dumbest possible baseline.

A shop manager says: "customers who raise three or more support tickets are about
to leave." Turn that into code, then find out whether it is any good.

No loops in the first three functions: they work on whole numpy arrays at once.
best_threshold may loop over the thresholds - there are only eleven.
"""

import numpy as np


def predict_rule(tickets, threshold=3):
    """1 for every customer with at least `threshold` tickets, else 0.

    predict_rule(np.array([0, 3, 5]), threshold=3) -> array([0, 1, 1])
    Accepts a list too: convert with np.asarray first.
    """
    raise NotImplementedError


def predict_nobody(n):
    """The baseline: predict 0 ("stays") for all n customers. An int array of zeros."""
    raise NotImplementedError


def accuracy(y_true, y_pred):
    """The fraction of positions where the two arrays agree, as a plain float.

    accuracy([1, 0, 1, 1], [1, 1, 1, 0]) -> 0.5
    If the shapes differ, raise ValueError - never compare arrays of different lengths.
    """
    raise NotImplementedError


def best_threshold(tickets, y, thresholds=range(0, 11)):
    """Try every threshold; return (threshold, accuracy) for the most accurate.

    On a tie, return the HIGHEST threshold (it flags the fewest customers).
    """
    raise NotImplementedError
