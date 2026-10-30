"""Day 2 - nn.Module, DataLoader, and the training loop."""

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def make_loader(X, y, batch_size=32, seed=0, shuffle=True):
    """A DataLoader over TensorDataset(X as float32, y as long), with
    generator=torch.Generator().manual_seed(seed) so the shuffling repeats."""
    raise NotImplementedError


class Net(nn.Module):
    """Week 6's network: Linear(n_in, hidden) -> ReLU -> Linear(hidden, n_out).
    Keep the layers in self.layers (an nn.Sequential); forward returns logits."""

    def __init__(self, n_in, hidden, n_out):
        raise NotImplementedError

    def forward(self, x):
        raise NotImplementedError


def train(model, loader, epochs=100, lr=0.1):
    """SGD with lr and nn.CrossEntropyLoss. For each epoch, for each batch:
    zero_grad, loss, backward, step. Return the list of per-epoch mean losses,
    weighted by batch size."""
    raise NotImplementedError


@torch.no_grad()
def accuracy(model, X, y):
    """model.eval(), predict the argmax class for X, return the accuracy as a float."""
    raise NotImplementedError
