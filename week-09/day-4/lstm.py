"""Day 4 - reading in order: an LSTM over the review.

Copy text.py, trainer.py and embeddings.py into this folder first; train it with
embeddings.train_text_model and score it with embeddings.predict.
"""

import torch
from torch import nn


class LSTMClassifier(nn.Module):
    """embed: nn.Embedding(vocab_size, dim, padding_idx=0)
    lstm:  nn.LSTM(dim, hidden, batch_first=True)
    head:  nn.Linear(hidden, 2)
    forward(ids): run the LSTM, then take each review's output at its LAST REAL token
    (position = number of non-pad ids - 1), not at the end of the padding."""

    def __init__(self, vocab_size, dim=16, hidden=32):
        raise NotImplementedError

    def forward(self, ids):
        raise NotImplementedError
