"""Milestone - the shop's review sentiment model, and where it still goes wrong.

    python sentiment.py      # trains, prints the breakdown and every mistake

Uses your text.py, trainer.py, embeddings.py and lstm.py (copy them into this folder).
"""

import numpy as np
import pandas as pd
import torch

from embeddings import predict, train_text_model
from lstm import LSTMClassifier
from text import build_vocab

FAR = r"not (?:really|very|that) "


def train(train_df, seed=0):
    """Vocab from the training texts; torch.manual_seed(seed); an LSTMClassifier trained
    with train_text_model. Returns (model, vocab)."""
    raise NotImplementedError


def breakdown(pred, df):
    """Accuracy, as plain floats, on four groups of df's rows:
        "all"
        "plain"          negated == 0
        "near negation"  negated == 1 and the text does NOT contain FAR
        "far negation"   the text contains FAR ("not really ...", "not very ...")
    (df["text"].str.contains(FAR))"""
    raise NotImplementedError


def errors(pred, df):
    """The rows the model got wrong: columns review_id, text, positive; index reset."""
    raise NotImplementedError


if __name__ == "__main__":
    from shoplab.reviews import frozen_split
    train_df, test_df = frozen_split()
    model, vocab = train(train_df)
    pred = predict(model, test_df["text"], vocab)
    print(breakdown(pred, test_df))
    print(errors(pred, test_df).to_string())
