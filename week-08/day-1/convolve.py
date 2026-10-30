"""Day 1 - images are arrays; convolution by hand. numpy only."""

import numpy as np

EDGE = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], dtype=float)


def convolve2d(image, kernel):
    """Slide the kernel over the image with no padding ("valid"): output entry (i, j) is
    sum(image[i:i+kh, j:j+kw] * kernel). Output shape (H - kh + 1, W - kw + 1).
    No flipping - this is what PyTorch's conv2d computes (strictly, cross-correlation)."""
    raise NotImplementedError


def max_pool(image, size=2):
    """The max of each non-overlapping size x size block. A 16 x 16 image -> 8 x 8.
    Hint: reshape to (h, size, w, size) and take the max over axes 1 and 3."""
    raise NotImplementedError


def shift(image, dy, dx):
    """The image moved dy rows down and dx columns right, wrapping round (np.roll twice)."""
    raise NotImplementedError
