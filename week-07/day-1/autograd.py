"""Day 1 - week 6's network again, with the gradients done by PyTorch.

params is week 6's dict of numpy arrays: W1, b1, W2, b2.
"""

import torch
import torch.nn.functional as F


def to_tensors(params, dtype=torch.float64):
    """A dict of the same names: each array as a torch tensor of `dtype` with
    requires_grad=True, so autograd tracks it."""
    raise NotImplementedError


def loss_torch(params, X, y):
    """Week 6's forward pass in torch: relu(X @ W1 + b1) @ W2 + b2, then
    F.cross_entropy(logits, y) - it takes LOGITS, and applies softmax itself.
    Convert X to params' dtype and y to torch.long."""
    raise NotImplementedError


def gradients(params, X, y, dtype=torch.float64):
    """Call loss_torch(...).backward() and return {name: gradient as a float64 numpy array}."""
    raise NotImplementedError
