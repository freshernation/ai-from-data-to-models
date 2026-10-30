"""Day 3 - is next month like last month, and is the model fair to everyone? numpy only."""

import numpy as np


def psi(expected, actual, bins=10):
    """Population stability index of `actual` against `expected`.
    Bin edges: np.unique of the expected values' quantiles at 0, 0.1, ..., 1; then set the
    first edge to -inf and the last to +inf. e and a: the share of each set in each bin,
    clipped below at 1e-4. PSI = sum((a - e) * ln(a / e)). A plain float."""
    raise NotImplementedError


def drift_report(reference, current, columns):
    """{column: psi rounded to 3 places}, largest first."""
    raise NotImplementedError


def verdict(score):
    """"stable" below 0.1, "watch" below 0.25, otherwise "drifted"."""
    raise NotImplementedError


def recall_by_group(y, scores, groups, threshold):
    """For each group (sorted): the share of that group's leavers (y == 1) whose score is
    >= threshold. NaN for a group with no leavers."""
    raise NotImplementedError


def contributions(scaler, model, columns, row):
    """Why a logistic regression gave one customer its score: for each column,
    (value - scaler.mean_) / scaler.scale_ * model.coef_[0], rounded to 3 places.
    A dict, largest absolute contribution first."""
    raise NotImplementedError
