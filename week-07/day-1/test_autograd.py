import numpy as np
import torch


def hand_backprop(params, X, y):
    """Week 6's backward pass, written out, as the reference."""
    z1 = X @ params["W1"] + params["b1"]
    h = np.maximum(0, z1)
    logits = h @ params["W2"] + params["b2"]
    e = np.exp(logits - logits.max(1, keepdims=True))
    d = e / e.sum(1, keepdims=True)
    d[np.arange(len(y)), y] -= 1
    d /= len(y)
    dz1 = (d @ params["W2"].T) * (z1 > 0)
    return {"W1": X.T @ dz1, "b1": dz1.sum(0), "W2": h.T @ d, "b2": d.sum(0)}


def setup():
    rng = np.random.default_rng(0)
    X, y = rng.normal(size=(5, 3)), np.array([0, 1, 2, 1, 0])
    r = np.random.default_rng(1)
    params = {"W1": r.normal(0, 0.8, (3, 4)), "b1": np.zeros(4),
              "W2": r.normal(0, 0.7, (4, 3)), "b2": np.zeros(3)}
    return params, X, y


def test_tensors_track_gradients(load):
    ag = load("autograd.py")
    t = ag.to_tensors(setup()[0])
    assert t["W1"].requires_grad and t["W1"].dtype == torch.float64


def test_loss_is_cross_entropy(load):
    ag = load("autograd.py")
    params, X, y = setup()
    loss = ag.loss_torch(ag.to_tensors(params), X, y)
    assert loss.shape == () and 0 < loss.item() < 5


def test_finding_forty_lines_become_one_call(load):
    ag = load("autograd.py")
    params, X, y = setup()
    mine, ref = ag.gradients(params, X, y), hand_backprop(params, X, y)
    gap64 = max(np.abs(mine[k] - ref[k]).max() for k in ref)
    assert gap64 < 1e-14, "In float64, autograd and week 6's hand-written backprop agree to 1e-16."
    g32 = ag.gradients(params, X, y, torch.float32)
    gap32 = max(np.abs(g32[k] - ref[k]).max() for k in ref)
    assert 1e-9 < gap32 < 1e-6, (
        "In float32, PyTorch's default, they differ around 1e-8. Not a bug: float32 holds "
        "about seven digits. Every network from now on trains in it.")
