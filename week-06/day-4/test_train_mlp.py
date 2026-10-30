import numpy as np

XOR = (np.array([[0, 0], [0, 1], [1, 0], [1, 1]]), np.array([0, 1, 1, 0]))


def test_loss_falls(load):
    tm = load("train_mlp.py")
    params, losses = tm.train(*XOR, epochs=200)
    assert len(losses) == 200 and losses[-1] < losses[0]


def test_finding_every_he_start_learns_xor(load):
    tm = load("train_mlp.py")
    for seed in range(5):
        params, losses = tm.train(*XOR, seed=seed)
        assert tm.accuracy(params, *XOR) == 1.0, f"seed {seed}: He initialisation should reach 100%."


def test_finding_zeros_never_move(load):
    tm = load("train_mlp.py")
    params, losses = tm.train(*XOR, scheme="zeros")
    assert tm.accuracy(params, *XOR) == 0.5
    assert round(losses[0], 4) == round(losses[-1], 4) == 0.6931, (
        "Loss stuck at ln 2 for 2,000 steps. With every weight zero, every hidden unit "
        "outputs 0, relu passes no gradient back, and nothing ever changes.")


def test_finding_the_step_size_window(load):
    tm = load("train_mlp.py")
    _, slow_losses = tm.train(*XOR, lr=0.01)
    big, big_losses = tm.train(*XOR, lr=5)
    assert round(slow_losses[-1], 3) == 0.165, "lr 0.01: right answers, but the loss is still 0.165 after 2,000 steps."
    assert tm.accuracy(big, *XOR) == 0.5, "lr 5: it overshoots and never recovers - stuck at a coin after 2,000 steps."
