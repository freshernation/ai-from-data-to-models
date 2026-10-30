import torch

from shoplab import images


def test_shapes_and_size(load):
    cnn = load("cnn.py")
    model = cnn.SmallCNN()
    assert model(torch.zeros(5, 1, 16, 16)).shape == (5, 4)
    assert sum(p.numel() for p in model.parameters()) == 1316, \
        "8*(9+1) + 16*(8*9+1) + 16*4+4 = 1,316 weights."


def test_split(load):
    cnn = load("cnn.py")
    d = images.load()
    Xf, yf, Xv, yv = cnn.split_validation(d["X_train"], d["y_train"])
    assert (len(Xf), len(Xv)) == (1600, 400)


def test_finding_thirteen_hundred_weights_are_enough(load):
    cnn = load("cnn.py")
    d = images.load()
    torch.manual_seed(0)
    model = cnn.SmallCNN()
    cnn.train_model(model, d["X_train"], d["y_train"])
    assert cnn.accuracy(model, d["X_test"], d["y_test"]) > 0.97, \
        "1,316 weights sort mugs, shirts, books and balls almost perfectly (100% in the reference run)."
