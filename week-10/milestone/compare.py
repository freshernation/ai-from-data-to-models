"""Milestone - three ways to read a review, on one frozen test set.

    python compare.py

Uses text.py, trainer.py, embeddings.py, lstm.py and bow.py from week 9 and your
transformer.py from day 3 (copy them all into this folder).
"""

import time

import numpy as np
import torch

import bow
from embeddings import predict, train_text_model
from lstm import LSTMClassifier
from text import build_vocab, tokenize
from transformer import TinyTransformer

FAR = r"not (?:really|very|that) "


def shuffled(texts, seed=0):
    """Every text with its words in a random order: tokenize, rng.permutation (one
    rng = default_rng(seed) for the whole list), join with spaces."""
    raise NotImplementedError


def row(pred, pred_shuffled, df, params, seconds):
    """{"all", "negated", "far negation", "shuffled"} accuracies as plain floats, plus
    "params" (an int) and "seconds" (rounded to 1 place)."""
    raise NotImplementedError


def compare(train_df, test_df, seed=0):
    """Three rows, each trained on train_df and scored on test_df and on
    shuffled(test_df["text"], seed):
        "tfidf line"   bow.fit_sentiment; params = coef_.size + 1
        "lstm"         LSTMClassifier, train_text_model(..., lr=0.02)
        "transformer"  TinyTransformer, train_text_model(..., lr=0.005)
    torch.manual_seed(seed) before building each network. Time each training.
    Returns {name: row}."""
    raise NotImplementedError


if __name__ == "__main__":
    import pandas as pd
    from shoplab.reviews import frozen_split
    print(pd.DataFrame(compare(*frozen_split())).T.to_string())
