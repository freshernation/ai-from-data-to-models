import numpy as np
import torch
import torch.nn.functional as F

from shoplab import images


def photo():
    return images.load()["X_train"][0] / 255.0


def test_tiny_convolution(load):
    cv = load("convolve.py")
    image = np.arange(16.0).reshape(4, 4)
    out = cv.convolve2d(image, np.array([[1.0, 0.0], [0.0, -1.0]]))
    assert out.shape == (3, 3) and (out == -5).all(), "Each entry is image[i, j] - image[i+1, j+1] = -5."


def test_matches_pytorch(load):
    cv = load("convolve.py")
    img = photo()
    ref = F.conv2d(torch.tensor(img)[None, None], torch.tensor(cv.EDGE)[None, None])[0, 0].numpy()
    assert np.allclose(cv.convolve2d(img, cv.EDGE), ref), "Do not flip the kernel: PyTorch does not."


def test_max_pool(load):
    cv = load("convolve.py")
    out = cv.max_pool(np.arange(16.0).reshape(4, 4))
    assert out.tolist() == [[5, 7], [13, 15]]


def test_finding_move_the_photo_and_the_features_move_with_it(load):
    cv = load("convolve.py")
    img = photo()
    a = cv.convolve2d(cv.shift(img, 2, 1), cv.EDGE)
    b = cv.shift(cv.convolve2d(img, cv.EDGE), 2, 1)
    assert np.allclose(a[3:-3, 3:-3], b[3:-3, 3:-3]), (
        "Away from the wrapped edges, convolving a moved photo gives exactly the moved "
        "result. The same kernel looks everywhere - so a mug is a mug wherever it sits.")
