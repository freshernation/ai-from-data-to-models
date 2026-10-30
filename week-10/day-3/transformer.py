"""Day 3 - a tiny transformer encoder that reads reviews.

Copy text.py, trainer.py and embeddings.py into this folder first; train it with
embeddings.train_text_model(..., lr=0.005).
"""

import math

import torch
from torch import nn


def sinusoidal(length, dim):
    """Tuesday's position code, in torch (float32), shape (length, dim)."""
    raise NotImplementedError


class TinyTransformer(nn.Module):
    """embed:    nn.Embedding(vocab_size, dim, padding_idx=0)
    position: sinusoidal(max_len, dim), stored with self.register_buffer("position", ...)
    encoder:  nn.TransformerEncoder of `layers` nn.TransformerEncoderLayer(dim, heads,
              dim_feedforward=2 * dim, dropout=0.1, batch_first=True),
              with enable_nested_tensor=False
    head:     nn.Linear(dim, 2)

    forward(ids):
        pad = ids == 0
        x = embed(ids) * sqrt(dim);  add position[:length] if use_position
        x = encoder(x, src_key_padding_mask=pad)
        the mean of x over the NON-pad positions -> head
    """

    def __init__(self, vocab_size, dim=32, heads=2, layers=1, max_len=32, use_position=True):
        raise NotImplementedError

    def forward(self, ids):
        raise NotImplementedError
