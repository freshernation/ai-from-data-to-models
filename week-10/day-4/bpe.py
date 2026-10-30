"""Day 4 - subword tokens: byte-pair encoding, one merge at a time. Plain Python.

A word is a tuple of symbols, starting as its characters plus an end marker "_":
"mug" -> ("m", "u", "g", "_").
"""

from collections import Counter

END = "_"


def split_word(word):
    raise NotImplementedError


def pair_counts(words):
    """words: Counter {symbol tuple: frequency}. Count every adjacent pair of symbols,
    weighted by the word's frequency. Returns a Counter {(a, b): count}."""
    raise NotImplementedError


def merge(symbols, pair):
    """Replace every non-overlapping occurrence of `pair`, left to right, by the joined
    symbol. merge(("a","a","a"), ("a","a")) -> ("aa","a")."""
    raise NotImplementedError


def learn_merges(word_counts, n_merges):
    """word_counts: {word: frequency}. Repeat n_merges times: find the most frequent pair
    (ties: the largest pair by normal tuple comparison), record it, merge it in every
    word. Stop early if no pairs are left. Returns the list of merged pairs, in order."""
    raise NotImplementedError


def segment(word, merges):
    """Split a word, then apply every merge in the order learned. A list of symbols."""
    raise NotImplementedError
