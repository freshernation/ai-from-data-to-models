"""Day 4 - teach the dense network what the CNN gets for free, and look at its mistakes.

Copy trainer.py, cnn.py and shift_test.py into this folder first.
"""

import numpy as np
import torch

from cnn import accuracy, train_model
from shift_test import dense_net


def augment(X, y, copies=3, max_shift=3, seed=0):
    """The originals plus `copies` moved copies of every image. Each copy of each image
    gets its own (dy, dx) from rng.integers(-max_shift, max_shift + 1, size=2), applied
    with np.roll on axis 0 then axis 1. Returns (X_all, y_all), originals first."""
    raise NotImplementedError


@torch.no_grad()
def confusion_matrix(model, X, y, classes=4):
    """table[true, predicted] = count, an int array (classes, classes)."""
    raise NotImplementedError


def augmented_dense(data, seed=0):
    """A dense_net trained (train_model) on augment(X_train, y_train, seed=seed),
    after torch.manual_seed(seed). Returns the model."""
    raise NotImplementedError
