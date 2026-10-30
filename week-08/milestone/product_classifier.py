"""Project 2 - the shop's product classifier: trained, saved, stress-tested, explained.

    python product_classifier.py     # trains, prints the report and the stress test,
                                     # saves product_classifier.pt and errors.png here

Uses your trainer.py, cnn.py, shift_test.py and augment.py (copy them into this folder).
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch

from augment import augment, confusion_matrix
from cnn import SmallCNN, accuracy, train_model
from shoplab.images import CLASSES, as_float


def train(data, seed=0):
    """A SmallCNN trained (train_model) on augment(X_train, y_train, seed=seed), after
    torch.manual_seed(seed). Returns (model, history)."""
    raise NotImplementedError


def save(model, path):
    """torch.save the model's state_dict (the weights, not the whole object)."""
    raise NotImplementedError


def load(path):
    """A fresh SmallCNN with the saved weights loaded, in eval mode."""
    raise NotImplementedError


@torch.no_grad()
def predict(model, X):
    """Class NAMES for uint8 images X: ["mug", "ball", ...]."""
    raise NotImplementedError


def error_gallery(model, X, y, path, limit=16):
    """Save a PNG showing up to `limit` misclassified images, each titled
    "true -> predicted". Return how many images were wrong in total (an int).
    With no mistakes, still save a figure (one empty panel) and return 0."""
    raise NotImplementedError


def stress(model, X, y, noise=(0.0, 0.2, 0.4, 0.6), brightness=(1.0, 0.5, 0.3), seed=0):
    """Accuracy on damaged copies of X:
      "noise {sigma}":       X / 255 plus normal(0, sigma) noise from a FRESH
                             default_rng(seed) for every sigma, clipped to 0..1, back to uint8
                             with np.round(... * 255)
      "brightness {factor}": (X * factor).astype(np.uint8)
    Returns {name: accuracy}."""
    raise NotImplementedError


def report(model, data):
    """{"centred": test accuracy, "shifted": shifted accuracy,
        "confusion": confusion_matrix on the shifted set, as a list of lists}."""
    raise NotImplementedError


if __name__ == "__main__":
    from shoplab import images
    here = Path(__file__).parent
    data = images.load()
    model, history = train(data)
    print(report(model, data))
    print(stress(model, data["X_test"], data["y_test"]))
    save(model, here / "product_classifier.pt")
    print("errors:", error_gallery(model, data["X_shifted"], data["y_shifted"], here / "errors.png"))
