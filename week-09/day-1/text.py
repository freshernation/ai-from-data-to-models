"""Day 1 - from a review to a list of numbers. Plain Python: re and Counter."""

import re
from collections import Counter

PAD, UNK = "<pad>", "<unk>"


def clean(text):
    """Lower-case; turn every character that is not a-z or an apostrophe into a space;
    then collapse runs of spaces into one and strip the ends.
    clean("Not BAD!!  at all.") -> "not bad at all"."""
    raise NotImplementedError


def tokenize(text):
    """clean, then split on whitespace."""
    raise NotImplementedError


def build_vocab(texts, min_count=1):
    """{word: id}. "<pad>" is 0 and "<unk>" is 1; then every word seen at least min_count
    times, most frequent first, ties in alphabetical order, numbered from 2."""
    raise NotImplementedError


def encode(text, vocab):
    """Token ids; a word not in vocab becomes vocab["<unk>"]."""
    raise NotImplementedError


def pad(sequences, length=None):
    """Cut or pad every list with 0 to `length` (default: the longest). A list of lists."""
    raise NotImplementedError
