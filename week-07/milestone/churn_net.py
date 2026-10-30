"""Milestone - the churn network, trained by trainer.fit.

    python churn_net.py
"""

import numpy as np
import torch
from sklearn.metrics import roc_auc_score
from torch import nn

from trainer import fit
from shoplab.customers import FEATURES, TARGET


class Squeeze(nn.Module):
    """Given: turns the (n, 1) logits into (n,), so BCEWithLogitsLoss gets matching shapes."""

    def forward(self, x):
        return x.squeeze(1)


def churn_net(hidden=32, dropout=0.2):
    """Linear(6, hidden) -> ReLU -> Dropout -> Linear(hidden, 1) -> Squeeze()."""
    raise NotImplementedError


def train(train_df, seed=0):
    """Hold back 20% of train_df for validation: a boolean mask with
    round(n * 0.2) True entries chosen by default_rng(seed).choice(n, k, replace=False).
    Standardise with the mean and std of the rows NOT held back. torch.manual_seed(seed),
    build churn_net(), and call fit(..., nn.BCEWithLogitsLoss(), epochs=500, lr=0.01,
    weight_decay=1e-3, patience=30, seed=seed). Returns (model, mean, std, history)."""
    raise NotImplementedError


@torch.no_grad()
def predict_proba(model, mean, std, df):
    raise NotImplementedError


if __name__ == "__main__":
    from shoplab.customers import frozen_split
    train_df, test_df = frozen_split()
    model, mean, std, history = train(train_df)
    auc = roc_auc_score(test_df[TARGET], predict_proba(model, mean, std, test_df))
    print("best epoch", history["best_epoch"], "stopped", history["stopped_epoch"], "test AUC", round(auc, 3))
