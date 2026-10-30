"""Day 2 - PCA by singular value decomposition. numpy only."""

import numpy as np


def pca(X, n_components=2):
    """Centre X (subtract each column's mean), then U, s, Vt = np.linalg.svd(centred,
    full_matrices=False). Returns:
        components   the first n rows of Vt                      shape (n, d)
        ratio        s**2 of those, divided by the sum of all s**2  shape (n,)
        projected    centred @ components.T                       shape (rows, n)
    """
    raise NotImplementedError
