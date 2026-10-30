"""Day 1 - a split you can trust, and the baseline to beat.

Splits return INDEX arrays (sorted), not frames: (train_idx, test_idx).
Use rng = np.random.default_rng(seed) for every random choice.
"""

import numpy as np


def random_split(n, test_fraction=0.25, seed=0):
    """Shuffle 0..n-1 with rng.permutation; the first round(n * test_fraction)
    shuffled positions are the test set. Returns (train_idx, test_idx), each sorted."""
    raise NotImplementedError


def stratified_split(y, test_fraction=0.25, seed=0):
    """For each label (in np.unique order), pick round(count * test_fraction) of its
    positions with rng.choice(..., replace=False) for the test set; the rest is train.
    Every label then has the same share in train and test."""
    raise NotImplementedError


def majority_class(y):
    """The most common label, as a plain Python value (use .item())."""
    raise NotImplementedError


def test_rate_spread(y, splitter, seeds=range(20)):
    """For each seed, call splitter(seed) -> (train_idx, test_idx) and compute the
    mean of y over the test indices. Return (lowest, highest) as plain floats."""
    raise NotImplementedError
