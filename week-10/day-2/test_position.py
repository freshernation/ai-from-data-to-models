import numpy as np


def setup():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(6, 8))
    return X, [rng.normal(size=(8, 8)) / 3 for _ in range(3)]


def test_sinusoidal(load):
    po = load("position.py")
    pe = po.sinusoidal(4, 6)
    assert pe.shape == (4, 6)
    assert np.allclose(pe[0], [0, 1, 0, 1, 0, 1]), "Position 0: every sine is 0, every cosine is 1."
    assert np.isclose(pe[1, 0], np.sin(1)) and np.isclose(pe[1, 3], np.cos(1 / 10000 ** (2 / 6)))


def test_finding_without_position_a_sentence_is_a_bag(load):
    po = load("position.py")
    X, W = setup()
    backwards = np.arange(6)[::-1]
    assert po.order_gap(X, *W, backwards) < 1e-12, (
        "Reverse the sentence: the pooled output is identical, to rounding. Attention compares "
        "every word with every other word and has no idea where any of them is.")
    assert po.order_gap(X, *W, backwards, with_position=True) > 0.05, \
        "Add the position code and the reversed sentence is a different sentence."
