import numpy as np
import pandas as pd

from shoplab import orders

TINY = pd.DataFrame({"customer_id": ["a", "a", "b", "b", "c", "c"],
                     "item_id": ["x", "y", "x", "y", "y", "z"], "seq": [1, 2, 1, 2, 1, 2]})


class TestPieces:
    def test_matrix(self, load):
        rc = load("recommend.py")
        m = rc.purchase_matrix(TINY)
        assert list(m.columns) == ["x", "y", "z"] and list(m.index) == ["a", "b", "c"]
        assert m.loc["c"].tolist() == [0.0, 1.0, 1.0]

    def test_cosine(self, load):
        rc = load("recommend.py")
        s = rc.cosine_similarity(np.array([[1.0, 1.0, 0.0], [1.0, 0.0, 0.0]]))
        assert np.allclose(s[0, 0], 1) and np.allclose(s[0, 1], 1 / np.sqrt(2)) and s[0, 2] == 0

    def test_never_recommends_what_you_own(self, load):
        rc = load("recommend.py")
        m = rc.purchase_matrix(TINY)
        s = rc.cosine_similarity(m.to_numpy())
        assert rc.recommend(m, s, "c", k=1) == ["x"], "c bought y and z; x is what y-buyers also bought."
        assert rc.most_popular(m, "c", k=1) == ["x"]


def test_finding_the_partner_comes_first(load):
    rc = load("recommend.py")
    m = rc.purchase_matrix(orders.load())
    s = rc.cosine_similarity(m.to_numpy())
    assert m.shape == (2000, 60)
    assert rc.recommend(m, s, "C00001", 5) == ["I003", "I012", "I039", "I031", "I013"], \
        "C00001 bought I001, I002 and I011: the next items in those runs come first."
