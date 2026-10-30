import numpy as np
import pytest

from shoplab import customers


class TestRule:
    def test_flags_at_or_above_threshold(self, load):
        rule = load("first_rule.py")
        got = rule.predict_rule(np.array([0, 2, 3, 7]), threshold=3)
        assert list(got) == [0, 0, 1, 1], "At or above the threshold is 1; below is 0."

    def test_accepts_a_list(self, load):
        rule = load("first_rule.py")
        assert list(rule.predict_rule([5, 1], threshold=2)) == [1, 0]

    def test_nobody_is_all_zeros(self, load):
        rule = load("first_rule.py")
        got = rule.predict_nobody(4)
        assert list(got) == [0, 0, 0, 0] and len(got) == 4


class TestAccuracy:
    def test_half_right(self, load):
        rule = load("first_rule.py")
        assert rule.accuracy([1, 0, 1, 1], [1, 1, 1, 0]) == 0.5

    def test_returns_a_plain_float(self, load):
        rule = load("first_rule.py")
        assert type(rule.accuracy(np.array([1]), np.array([1]))) is float, \
            "Wrap the result in float() - a numpy scalar prints oddly in reports."

    def test_refuses_different_shapes(self, load):
        rule = load("first_rule.py")
        with pytest.raises(ValueError):
            rule.accuracy([1, 0, 1], [1, 0])

    def test_no_loops_except_in_best_threshold(self, load, source):
        rule = load("first_rule.py")
        assert rule.accuracy([1, 0], [1, 1]) == 0.5, "Make accuracy work first; then this checks how."
        code = source("first_rule.py", code_only=True).split("def best_threshold")[0]
        assert "for " not in code and "while " not in code, \
            "Today is about arrays: let numpy do the looping (== and .mean())."


def test_finding_the_sensible_rule_loses_to_the_baseline(load):
    rule = load("first_rule.py")
    tickets, churned = customers.arrays(["support_tickets", "churned"])
    nobody = rule.accuracy(churned, rule.predict_nobody(len(churned)))
    three = rule.accuracy(churned, rule.predict_rule(tickets, 3))
    assert round(nobody, 4) == 0.8695, "13.05% of customers churn, so 'nobody' is right 86.95% of the time."
    assert round(three, 4) == 0.855, (
        "The manager's rule is right 85.5% of the time - LESS than predicting nobody "
        "leaves. Accuracy on its own hides this. That is the whole of day 1.")
    assert rule.best_threshold(tickets, churned) == (10, nobody), \
        "No ticket threshold beats the baseline: the best one flags nobody at all."
