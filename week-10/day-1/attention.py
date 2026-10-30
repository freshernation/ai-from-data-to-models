"""Day 1 - attention by hand, in numpy. Works on any leading batch axes."""

import numpy as np


def softmax(x, axis=-1):
    """Stable softmax along `axis` (subtract the max first). -inf entries become 0."""
    raise NotImplementedError


def attention(Q, K, V, mask=None):
    """Scaled dot-product attention.
        scores  = Q @ K^T / sqrt(d)          (K^T: swap the last two axes)
        where mask is False, the score is -inf (that position is not looked at)
        weights = softmax(scores) over the last axis
    Returns (weights @ V, weights)."""
    raise NotImplementedError


def self_attention(X, Wq, Wk, Wv, mask=None):
    """Queries, keys and values are all made from the same X: attention(X@Wq, X@Wk, X@Wv)."""
    raise NotImplementedError
