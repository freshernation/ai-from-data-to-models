"""Day 4 - look before you model: a plot, rates by bucket, and leaks."""

import matplotlib

matplotlib.use("Agg")          # draw to files, never open a window
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_histogram(values, path, bins=20, title=""):
    """Save a histogram of `values` to `path` (a .png). Return the bin counts
    (a numpy array of length `bins`) - np.histogram gives you them."""
    raise NotImplementedError


def rate_by_bucket(df, column, edges, target="churned"):
    """Churn rate inside each bucket of `column`. Buckets are [edges[i], edges[i+1]).
    Returns a Series with one value per bucket, in order. (pd.cut, right=False)"""
    raise NotImplementedError


def leak_score(df, column, target="churned"):
    """How well this ONE column predicts the target on its own.

    Group by the column's value (or, if it has any missing values, by whether it
    is missing). Predict each group's most common target. Return the accuracy.
    """
    raise NotImplementedError


def find_leaks(df, target="churned", limit=0.99, max_values=20):
    """Columns (other than target) with at most `max_values` distinct values whose
    leak_score is >= limit. A list of names, in column order."""
    raise NotImplementedError
