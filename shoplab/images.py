"""Product photos, 16 x 16 grey pixels - the data week 8 works on.

    load()   dict of uint8 arrays: X_train (2000, 16, 16), y_train, X_test, y_test,
             and X_shifted / y_shifted: the same kinds of photo, with the product up to
             three pixels further from the centre than any training photo.
    CLASSES  the label names, in label order
"""

import numpy as np

from shoplab import DATA

CLASSES = ["mug", "shirt", "book", "ball"]


def load():
    with np.load(DATA / "products.npz") as data:
        return {k: data[k] for k in data.files}


def as_float(X):
    """uint8 pixels 0..255 -> float32 0..1, with a channel axis: (n, 1, 16, 16)."""
    return (np.asarray(X, dtype=np.float32) / 255.0)[:, None, :, :]
