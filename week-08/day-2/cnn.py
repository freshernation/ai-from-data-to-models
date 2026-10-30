"""Day 2 - a small CNN for product photos, trained with week 7's trainer.

Copy trainer.py from your week 7 milestone into this folder first.
"""

import numpy as np
import torch
from torch import nn

from trainer import fit
from shoplab.images import as_float


class SmallCNN(nn.Module):
    """features: Conv2d(1, 8, 3, padding=1) -> ReLU -> MaxPool2d(2)
                 -> Conv2d(8, 16, 3, padding=1) -> ReLU          (in an nn.Sequential)
    then the max of each of the 16 channels over the whole image (.amax(dim=(2, 3)))
    head: Linear(16, classes)."""

    def __init__(self, classes=4):
        raise NotImplementedError

    def forward(self, x):
        raise NotImplementedError


def split_validation(X, y, fraction=0.2, seed=0):
    """Hold back round(n * fraction) rows (default_rng(seed).choice, replace=False).
    Returns X_fit, y_fit, X_val, y_val."""
    raise NotImplementedError


def train_model(model, X, y, seed=0, epochs=80, lr=0.03, patience=20):
    """Split off validation, convert with as_float (and torch.as_tensor), seed torch, and
    call fit(model, nn.CrossEntropyLoss(), ...). Returns fit's history."""
    raise NotImplementedError


@torch.no_grad()
def accuracy(model, X, y):
    """model.eval(); accuracy of the argmax class on uint8 images X. A plain float."""
    raise NotImplementedError
