"""Day 1 - k-means by hand, and the elbow.

numpy only. The data: shoplab.orders.category_shares() - one row per customer, the
share of their purchases in each of six categories.
"""

import numpy as np


def assign(X, centroids):
    """For each row of X (n, d), the index of the nearest centroid (k, d), by squared
    distance. Broadcast: X[:, None, :] - centroids[None, :, :] has shape (n, k, d)."""
    raise NotImplementedError


def inertia(X, centroids, labels):
    """Sum over rows of the squared distance to their own centroid. A plain float."""
    raise NotImplementedError


def kmeans(X, k, seed=0, iterations=100):
    """Start from k distinct rows of X chosen with default_rng(seed).choice(n, k, replace=False).
    Repeat: assign, then move each centroid to the mean of its rows (a centroid with no
    rows stays put); stop when the centroids stop moving (np.allclose) or after
    `iterations`. Returns (centroids, labels, inertia)."""
    raise NotImplementedError


def best_of(X, k, starts=10):
    """Run kmeans with seeds 0..starts-1; return the result with the lowest inertia."""
    raise NotImplementedError


def elbow(X, ks=range(1, 9), starts=10):
    """{k: inertia of best_of(X, k, starts)} for each k."""
    raise NotImplementedError


def purity(labels, truth):
    """For each cluster, count its most common true label; add those up; divide by n.
    1.0 means every cluster holds one kind of customer."""
    raise NotImplementedError
