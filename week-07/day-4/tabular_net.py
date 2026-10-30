"""Day 4 - churn as a network, against week 4's models."""

import copy

import numpy as np
import torch
from sklearn.metrics import roc_auc_score
from torch import nn

from shoplab.customers import FEATURES, TARGET


def tensors(df, mean, std):
    """(X standardised with the given mean and std, as float32; y as float32)."""
    raise NotImplementedError


def validation_split(df, fraction=0.2, seed=0):
    """Hold back round(n * fraction) rows of the TRAINING frame, chosen with
    default_rng(seed).choice(n, k, replace=False). Returns (fit_df, val_df), indexes reset."""
    raise NotImplementedError


def churn_net(hidden=32, dropout=0.2):
    """Linear(6, hidden) -> ReLU -> Dropout -> Linear(hidden, 1): one logit per customer."""
    raise NotImplementedError


def fit(train_df, epochs=200, lr=0.01, weight_decay=1e-3, seed=0):
    """torch.manual_seed(seed). Split off validation; standardise with the FIT part's mean
    and std; full-batch Adam with nn.BCEWithLogitsLoss (squeeze the logit to shape (n,)).
    Keep the state with the lowest validation loss and load it at the end; model.eval().
    Returns (model, mean, std, best_epoch)."""
    raise NotImplementedError


@torch.no_grad()
def predict_proba(model, mean, std, df):
    """sigmoid of the logits, as a numpy array."""
    raise NotImplementedError


def test_auc(model, mean, std, df):
    raise NotImplementedError
