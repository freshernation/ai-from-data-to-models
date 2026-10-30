"""Day 3 - a network bigger than its data, and three ways to stop it memorising.

Sixty training points, a thousand validation points, and a network with 66,000 weights.
"""

import copy

import numpy as np
import torch
from torch import nn


def small_noisy_moons(seed=0):
    """Given: 60 training points, 1,000 validation points."""
    from sklearn.datasets import make_moons
    X, y = make_moons(n_samples=1060, noise=0.35, random_state=seed)
    return X[:60], y[:60], X[60:], y[60:]


def big_net(dropout=0.0, hidden=256):
    """Linear(2, hidden) -> ReLU -> Dropout -> Linear(hidden, hidden) -> ReLU -> Dropout
    -> Linear(hidden, 2), as one nn.Sequential."""
    raise NotImplementedError


def fit_curves(model, X, y, X_val, y_val, epochs=300, lr=0.01, weight_decay=0.0, seed=0):
    """Full-batch Adam(lr, weight_decay) with CrossEntropyLoss. Each epoch: one training
    step (model.train()), then the validation loss (model.eval(), torch.no_grad()).
    Track the best validation loss: (loss, epoch, copy.deepcopy(model.state_dict())).
    Returns (train_losses, val_losses, best)."""
    raise NotImplementedError


@torch.no_grad()
def accuracy(model, X, y):
    raise NotImplementedError


def compare(seed=0):
    """For ("none", dropout 0, decay 0), ("dropout", 0.5, 0), ("weight_decay", 0, 0.05):
    torch.manual_seed(seed), build big_net, fit_curves, and record
        {"train_loss", "val_loss" (last epoch), "best_epoch", "best_val_loss", "accuracy"}.
    After "none", also load its best state and record "early_stopping":
        {"best_epoch", "val_loss" (the best), "accuracy"}.
    Returns {name: dict}."""
    raise NotImplementedError
