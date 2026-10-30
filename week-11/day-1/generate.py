"""Day 1 - generation is next-word prediction, plus a dice roll.

A bigram model: the chance of each word given only the word before it, counted from
the training reviews. Copy text.py from week 9 day 1 into this folder first.
"""

import numpy as np

from text import tokenize

START, END = "<s>", "</s>"


def fit_bigram(texts):
    """vocab: [START, END] + every word in texts, sorted.
    counts: (len(vocab), len(vocab)) array; counts[i, j] = how often word j follows word i,
    with START before each review's first word and END after its last.
    Returns (vocab, counts)."""
    raise NotImplementedError


def next_probs(counts, row, temperature=1.0, top_k=None):
    """The distribution of the next word after vocab[row]:
        logits = log(counts[row] + 1e-12)
        top_k: keep only the k largest logits (the rest become -inf)
        divide by temperature, softmax (subtract the max first)."""
    raise NotImplementedError


def sample(vocab, counts, rng, temperature=1.0, top_k=None, max_len=20):
    """Start at START. Repeatedly draw the next word with rng.choice(len(vocab), p=...)
    until END or max_len words. Return the words joined by spaces (no START/END)."""
    raise NotImplementedError


def survey(texts, n=200, temperature=1.0, top_k=None, seed=0):
    """Fit on texts, draw n samples with one rng = default_rng(seed). Returns
        {"distinct": share of samples that are different from each other,
         "copied":   share that are word-for-word a training review (compare tokenized,
                     space-joined forms),
         "examples": the first three samples}."""
    raise NotImplementedError
