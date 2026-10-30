import numpy as np
from sklearn.tree import DecisionTreeClassifier

from shoplab import customers


class TestImpurity:
    def test_gini(self, load):
        t = load("tree.py")
        assert t.gini(np.array([0, 0, 1, 1])) == 0.5
        assert t.gini(np.array([1, 1, 1])) == 0.0 and t.gini(np.array([], dtype=int)) == 0.0

    def test_gain(self, load):
        t = load("tree.py")
        x, y = np.array([1, 2, 3, 4]), np.array([0, 0, 1, 1])
        assert t.split_gain(x, y, 2.5) == 0.5, "A perfect split removes all 0.5 of the impurity."
        assert t.split_gain(x, y, 10) == 0.0, "One side empty: no gain."

    def test_best_split_on_a_tiny_table(self, load):
        t = load("tree.py")
        X = np.array([[1, 5], [2, 1], [3, 6], [4, 2]])
        feature, threshold, gain = t.best_split(X, np.array([0, 1, 0, 1]))
        assert (feature, threshold) == (1, 3.5), "Column 1 separates them perfectly at 3.5."


def test_finding_the_first_question_is_silence(load):
    t = load("tree.py")
    train, _ = customers.frozen_split()
    F = customers.FEATURES
    stump = t.Stump().fit(train[F], train["churned"])
    ref = DecisionTreeClassifier(max_depth=1).fit(train[F], train["churned"])
    assert (stump.feature_, stump.threshold_) == (ref.tree_.feature[0], ref.tree_.threshold[0]), \
        "Your stump should ask the same question scikit-learn's does."
    assert F[stump.feature_] == "days_since_last_order" and stump.threshold_ == 75.5
    assert (round(stump.left_rate_, 3), round(stump.right_rate_, 3)) == (0.105, 0.605), (
        "Silent for more than 75 days: 60.5% leave. Otherwise 10.5%. The same signal "
        "you plotted in week 1, found by a machine in 0.1 seconds.")
