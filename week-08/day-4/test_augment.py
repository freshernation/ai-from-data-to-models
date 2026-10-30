import numpy as np

from shoplab import images


def test_augment_shapes_and_moves(load):
    au = load("augment.py")
    X = np.zeros((2, 16, 16), dtype=np.uint8)
    X[:, 8, 8] = 255
    Xa, ya = au.augment(X, np.array([0, 1]), copies=3)
    assert Xa.shape == (8, 16, 16) and list(ya) == [0, 1] * 4
    assert (Xa[:2] == X).all(), "Originals first."
    assert all(img.sum() == 255 for img in Xa), "A roll moves pixels; it never adds or removes them."


def test_confusion_matrix(load):
    au = load("augment.py")
    import torch

    class Always(torch.nn.Module):
        def forward(self, x):
            return torch.tensor([[0.0, 1.0, 0.0, 0.0]]).repeat(len(x), 1)

    table = au.confusion_matrix(Always(), np.zeros((3, 16, 16)), np.array([0, 1, 1]))
    assert table.tolist() == [[0, 1, 0, 0], [0, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def test_finding_show_it_moved_mugs_and_it_learns_moved_mugs(load):
    au = load("augment.py")
    cnn = load("cnn.py")
    d = images.load()
    model = au.augmented_dense(d)
    assert cnn.accuracy(model, d["X_shifted"], d["y_shifted"]) > 0.97, (
        "Trained on four copies of every photo, three of them moved, the dense network "
        "handles moved products too (99.6% in the reference run). It had to SEE every "
        "position; the CNN gets it from its design.")
