"""Day 3 - the measures that accuracy hides. By hand; no scikit-learn in this file."""

import numpy as np


def confusion(y, y_hat):
    """{"tp": ..., "fp": ..., "tn": ..., "fn": ...} as plain ints. 1 means "churns"."""
    raise NotImplementedError


def precision(y, y_hat):
    """Of those flagged, the fraction who churn. 0.0 if nobody was flagged."""
    raise NotImplementedError


def recall(y, y_hat):
    """Of those who churn, the fraction flagged. 0.0 if nobody churns."""
    raise NotImplementedError


def f1(y, y_hat):
    """Harmonic mean of precision and recall; 0.0 if both are 0."""
    raise NotImplementedError


def roc_auc(y, scores):
    """The chance a random churner scores higher than a random stayer; ties count half.
    Compare every churner with every stayer at once by broadcasting:
    pos[:, None] > neg[None, :]."""
    raise NotImplementedError
