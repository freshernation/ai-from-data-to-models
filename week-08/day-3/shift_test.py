"""Day 3 - a dense network and a CNN, when the product moves in the frame.

Copy trainer.py and cnn.py into this folder first.
"""

import torch
from torch import nn

from cnn import SmallCNN, accuracy, train_model


def dense_net(hidden=64, classes=4):
    """Flatten -> Linear(256, hidden) -> ReLU -> Linear(hidden, classes)."""
    raise NotImplementedError


def compare(data, seed=0):
    """For ("dense", dense_net) and ("cnn", SmallCNN): torch.manual_seed(seed), build, train
    with train_model on X_train/y_train, and record
        {"params": number of weights, "centred": test accuracy, "shifted": shifted accuracy}.
    Returns {"dense": {...}, "cnn": {...}}."""
    raise NotImplementedError
