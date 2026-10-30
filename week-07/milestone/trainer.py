"""Milestone - one training loop for every network in the rest of the course.

    history = fit(model, loss_fn, X, y, X_val, y_val, patience=20)

Weeks 8 to 10 import this file. Write it once, carefully.
"""

import copy

import torch


def fit(model, loss_fn, X, y, X_val, y_val, epochs=500, lr=0.01, weight_decay=0.0,
        patience=20, seed=0):
    """Full-batch Adam(lr, weight_decay), after torch.manual_seed(seed).

    Each epoch: one training step (model.train()), then the validation loss
    (model.eval(), torch.no_grad()). Append both to history["train"] / history["val"].
    Keep a deepcopy of the state_dict whenever validation loss improves. Stop when
    `patience` epochs have passed since the best one.

    At the end: load the best state, model.eval(), and add history["best_epoch"] and
    history["stopped_epoch"]. Return history."""
    raise NotImplementedError
