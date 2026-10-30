import numpy as np


def test_step(load):
    pc = load("perceptron.py")
    assert list(pc.step(np.array([-0.1, 0.0, 2.0]))) == [0, 1, 1]


def test_learns_and_and_or(load):
    pc = load("perceptron.py")
    for X, y in (pc.AND, pc.OR):
        model = pc.Perceptron().fit(X, y)
        assert list(model.predict(X)) == list(y)
        assert len(model.history_) == 20 and model.history_[-1] == 1.0


def test_finding_xor_is_out_of_reach(load):
    pc = load("perceptron.py")
    X, y = pc.XOR
    model = pc.Perceptron(epochs=100).fit(X, y)
    assert max(model.history_) == 0.5, (
        "A hundred epochs and never better than a coin. No straight line puts (0,1) and "
        "(1,0) on one side and (0,0) and (1,1) on the other. One layer cannot do XOR.")
