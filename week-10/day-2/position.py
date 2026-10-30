"""Day 2 - attention cannot see order until you tell it where each word is.

Copy attention.py from day 1 into this folder first.
"""

import numpy as np

from attention import self_attention


def sinusoidal(length, dim):
    """The transformer paper's position code, shape (length, dim):
        even columns 2i:  sin(pos / 10000 ** (2i / dim))
        odd columns 2i+1: cos(pos / 10000 ** (2i / dim))"""
    raise NotImplementedError


def pooled(X, Wq, Wk, Wv, with_position=False):
    """Self-attention over X (length, dim), then the mean over positions: one vector for
    the whole sentence. With with_position, add sinusoidal(length, dim) to X first."""
    raise NotImplementedError


def order_gap(X, Wq, Wk, Wv, order, with_position=False):
    """The largest absolute difference between pooled(X) and pooled(X[order]). A float."""
    raise NotImplementedError
