import numpy as np
from sklearn.cluster import KMeans

from shoplab import orders


def two_blobs():
    return np.array([[0, 0], [0, 1], [1, 0], [10, 10], [10, 11], [11, 10]], dtype=float)


class TestPieces:
    def test_assign(self, load):
        km = load("kmeans.py")
        got = km.assign(two_blobs(), np.array([[0.0, 0.0], [10.0, 10.0]]))
        assert list(got) == [0, 0, 0, 1, 1, 1]

    def test_inertia(self, load):
        km = load("kmeans.py")
        X = np.array([[0.0, 0.0], [2.0, 0.0]])
        assert km.inertia(X, np.array([[1.0, 0.0]]), np.array([0, 0])) == 2.0

    def test_finds_two_blobs(self, load):
        km = load("kmeans.py")
        centroids, labels, total = km.best_of(two_blobs(), 2)
        assert len(set(labels[:3])) == 1 and len(set(labels[3:])) == 1 and labels[0] != labels[3]
        assert abs(total - 8 / 3) < 1e-9

    def test_purity(self, load):
        km = load("kmeans.py")
        assert km.purity([0, 0, 1, 1], ["a", "b", "b", "b"]) == 0.75


def test_matches_scikit_learn(load):
    km = load("kmeans.py")
    X = orders.category_shares().to_numpy()
    _, _, mine = km.best_of(X, 4)
    assert abs(mine - KMeans(4, n_init=10, random_state=0).fit(X).inertia_) < 1e-6


def test_finding_the_elbow_says_three_the_shop_has_four(load):
    km = load("kmeans.py")
    shares = orders.category_shares()
    curve = {k: round(v, 1) for k, v in km.elbow(shares.to_numpy(), range(1, 7)).items()}
    assert curve == {1: 672.3, 2: 487.8, 3: 327.4, 4: 270.3, 5: 223.0, 6: 181.8}, \
        "Big drops to k=3 (185, 160), then small ones (57, 47, 41): the elbow is at 3."
    _, labels, _ = km.best_of(shares.to_numpy(), 3)
    truth = orders.hidden_segments().loc[shares.index]
    assert km.purity(labels, list(truth)) == 0.78, (
        "The shop was generated with FOUR segments. The fourth - browsers who buy a bit of "
        "everything - is not a cluster but a cloud between the other three, so k-means "
        "cannot find it. 78% purity: the 15% who are browsers, and a few more.")
