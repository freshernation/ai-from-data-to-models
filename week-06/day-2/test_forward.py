import numpy as np


class TestPieces:
    def test_relu(self, load):
        fw = load("forward.py")
        assert list(fw.relu(np.array([-2.0, 0.0, 3.0]))) == [0, 0, 3]

    def test_softmax_is_stable_and_sums_to_one(self, load):
        fw = load("forward.py")
        out = fw.softmax(np.array([[1000.0, 1000.0], [0.0, np.log(3)]]))
        assert np.allclose(out, [[0.5, 0.5], [0.25, 0.75]])

    def test_cross_entropy(self, load):
        fw = load("forward.py")
        probs = np.array([[0.5, 0.5], [0.1, 0.9]])
        assert abs(fw.cross_entropy(probs, np.array([0, 1])) - (np.log(2) - np.log(0.9)) / 2) < 1e-9

    def test_init_shapes_and_scale(self, load):
        fw = load("forward.py")
        p = fw.init_params(200, 100, 3, seed=0)
        assert p["W1"].shape == (200, 100) and p["b2"].shape == (3,)
        assert abs(p["W1"].std() - np.sqrt(2 / 200)) < 0.005
        z = fw.init_params(2, 4, 2, scheme="zeros")
        assert all((v == 0).all() for v in z.values())


def test_finding_two_layers_can_do_xor(load):
    fw = load("forward.py")
    params = {"W1": np.array([[1.0, 1.0], [1.0, 1.0]]), "b1": np.array([0.0, -1.0]),
              "W2": np.array([[-10.0, 10.0], [30.0, -30.0]]), "b2": np.array([0.0, 0.0])}
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    probs, cache = fw.forward(params, X)
    assert list(probs.argmax(axis=1)) == [0, 1, 1, 0], (
        "Hand-set weights: one hidden unit counts the 1s, the other fires only for two. "
        "What one line cannot do, two layers do. On Thursday the network finds weights like these.")
    assert set(cache) == {"X", "z1", "h", "probs"}
