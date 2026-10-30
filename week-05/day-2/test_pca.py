import numpy as np
from sklearn.decomposition import PCA

from shoplab import orders


def test_a_line_has_one_direction(load):
    pc = load("pca.py")
    X = np.array([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])
    components, ratio, projected = pc.pca(X, 1)
    assert np.allclose(np.abs(components[0]), np.array([1, 2]) / np.sqrt(5))
    assert np.allclose(ratio, [1.0]) and projected.shape == (3, 1)


def test_matches_scikit_learn_up_to_sign(load):
    pc = load("pca.py")
    X = orders.category_shares().to_numpy()
    components, ratio, projected = pc.pca(X, 2)
    ref = PCA(2).fit(X)
    assert np.allclose(np.abs(components), np.abs(ref.components_), atol=1e-9), \
        "Same directions; a direction and its negative are the same axis."
    assert np.allclose(ratio, ref.explained_variance_ratio_)
    assert np.allclose(np.abs(projected), np.abs(ref.transform(X)), atol=1e-9)


def test_finding_six_columns_two_numbers(load):
    pc = load("pca.py")
    _, ratio, _ = pc.pca(orders.category_shares().to_numpy(), 2)
    assert [round(r, 3) for r in ratio] == [0.332, 0.29], (
        "Two directions hold 62% of how customers differ across six categories: enough "
        "to draw every customer on a page and see three clouds.")
