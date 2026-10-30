"""Day 2 - bag of words and TF-IDF by hand, and week 3's line on top.

Copy text.py from day 1 into this folder first.
"""

import numpy as np
from sklearn.linear_model import LogisticRegression

from text import tokenize


def word_vocab(texts):
    """{word: column} for every word in texts, alphabetical, from 0. (No pad or unk.)"""
    raise NotImplementedError


def count_matrix(texts, vocab):
    """(n_texts, n_words) array: how often each vocab word appears in each text.
    Words not in vocab are ignored."""
    raise NotImplementedError


def idf(counts):
    """Inverse document frequency per column, scikit-learn's smoothed form:
    ln((1 + n) / (1 + df)) + 1, where df = how many rows contain the word."""
    raise NotImplementedError


def tfidf(counts, weights):
    """counts * weights, then each row divided by its length (rows of zeros stay zero)."""
    raise NotImplementedError


def fit_sentiment(texts, y):
    """word_vocab and idf from the TRAINING texts, then LogisticRegression(max_iter=2000)
    on their TF-IDF. Returns (vocab, weights, model)."""
    raise NotImplementedError


def predict(vocab, weights, model, texts):
    raise NotImplementedError


def scores(y, pred, negated):
    """{"all", "negated", "plain"}: accuracy over all rows, rows with negated == 1, and
    rows with negated == 0. Plain floats."""
    raise NotImplementedError
