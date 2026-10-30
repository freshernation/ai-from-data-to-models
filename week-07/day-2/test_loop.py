import numpy as np
import torch
from sklearn.datasets import make_moons


def moons():
    X, y = make_moons(600, noise=0.25, random_state=0)
    return X[:450], y[:450], X[450:], y[450:]


def test_loader_batches(load):
    lp = load("loop.py")
    X, y, _, _ = moons()
    xb, yb = next(iter(lp.make_loader(X, y, 32)))
    assert xb.shape == (32, 2) and xb.dtype == torch.float32 and yb.dtype == torch.int64
    assert len(lp.make_loader(X, y, 32)) == 15


def test_net_is_a_module(load):
    lp = load("loop.py")
    net = lp.Net(2, 16, 2)
    assert isinstance(net, torch.nn.Module) and isinstance(net.layers, torch.nn.Sequential)
    assert net(torch.zeros(5, 2)).shape == (5, 2)
    assert sum(p.numel() for p in net.parameters()) == 2 * 16 + 16 + 16 * 2 + 2


def test_finding_small_batches_learn_more_per_pass(load):
    lp = load("loop.py")
    X, y, Xt, yt = moons()
    results = {}
    for batch in (450, 32):
        torch.manual_seed(0)
        model = lp.Net(2, 16, 2)
        losses = lp.train(model, lp.make_loader(X, y, batch), epochs=100, lr=0.5 if batch == 450 else 0.1)
        results[batch] = (round(losses[-1], 2), lp.accuracy(model, Xt, yt))
    assert results[450][1] <= 0.9 < results[32][1], (
        "One hundred passes over the same 450 points: the full batch takes 100 steps and "
        "reaches about 90%; batches of 32 take 1,500 steps and reach about 92%.")
    assert results[32][0] < results[450][0]
