"""Day 3 - words as learned vectors: an embedding, averaged.

Copy text.py (day 1) and trainer.py (week 7 milestone) into this folder first.
"""

import numpy as np
import torch
from torch import nn

from text import build_vocab, encode, pad
from trainer import fit


class MeanEmbedding(nn.Module):
    """embed: nn.Embedding(vocab_size, dim, padding_idx=0); head: nn.Linear(dim, 2).
    forward(ids): the mean of the embeddings of the NON-pad tokens, then head."""

    def __init__(self, vocab_size, dim=16):
        raise NotImplementedError

    def forward(self, ids):
        raise NotImplementedError


def tensorise(texts, vocab, length=None):
    """encode every text, pad, return a torch.long tensor (n, length)."""
    raise NotImplementedError


def split_validation(n, fraction=0.2, seed=0):
    """A boolean numpy mask with round(n * fraction) True entries
    (default_rng(seed).choice(n, k, replace=False))."""
    raise NotImplementedError


def train_text_model(model, texts, y, vocab, seed=0, epochs=300, lr=0.02, patience=30):
    """tensorise, hold back the validation rows, torch.manual_seed(seed), and call
    fit(model, nn.CrossEntropyLoss(), ...). Returns fit's history.
    Convert y with torch.as_tensor(np.array(y))."""
    raise NotImplementedError


@torch.no_grad()
def predict(model, texts, vocab):
    """model.eval(); argmax class per text, as a numpy array."""
    raise NotImplementedError


def nearest(model, vocab, word, k=5):
    """The k words whose embeddings have the highest cosine similarity with `word`'s,
    leaving out the word itself, <pad> and <unk>."""
    raise NotImplementedError


def sentiment_scores(model, vocab):
    """{word: score} for every real word (id > 1): its embedding dotted with
    head.weight[1] - head.weight[0], the model's own positive-minus-negative direction."""
    raise NotImplementedError
