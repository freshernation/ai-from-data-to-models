import numpy as np

from shoplab import customers


class TestSplits:
    def test_random_split_covers_everything_once(self, load):
        sp = load("split.py")
        train, test = sp.random_split(100, 0.25, seed=1)
        assert len(test) == 25 and len(train) == 75
        assert sorted(np.concatenate([train, test])) == list(range(100))
        assert list(test) == sorted(test), "Return sorted indices."

    def test_stratified_keeps_the_rate(self, load):
        sp = load("split.py")
        y = np.array([1] * 20 + [0] * 80)
        train, test = sp.stratified_split(y, 0.25, seed=3)
        assert y[test].sum() == 5 and len(test) == 25
        assert set(train).isdisjoint(test)

    def test_same_seed_same_split(self, load):
        sp = load("split.py")
        y = np.array([0, 1] * 50)
        a = sp.stratified_split(y, 0.2, seed=9)[1]
        assert list(a) == list(sp.stratified_split(y, 0.2, seed=9)[1])

    def test_majority(self, load):
        sp = load("split.py")
        assert sp.majority_class([0, 1, 0, 0]) == 0 and type(sp.majority_class(np.array([1, 1]))) is int


def test_finding_an_unlucky_split_changes_the_question(load):
    sp = load("split.py")
    y = customers.load()["churned"].to_numpy()
    lo, hi = sp.test_rate_spread(y, lambda s: sp.random_split(len(y), 0.25, s))
    assert (round(lo, 3), round(hi, 3)) == (0.112, 0.152), (
        "Over 20 random splits the test set's churn rate ran from 11.2% to 15.2%: the "
        "baseline you must beat moves by four points before you train anything.")
    assert sp.test_rate_spread(y, lambda s: sp.stratified_split(y, 0.25, s)) == (0.13, 0.13), \
        "Stratified, it is 13.0% every time."
