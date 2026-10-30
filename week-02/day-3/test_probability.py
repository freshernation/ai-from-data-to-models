import math

import numpy as np

from shoplab import customers


class TestStatistics:
    def test_mean_and_variance(self, load):
        p = load("probability.py")
        xs = [2, 4, 4, 4, 5, 5, 7, 9]
        assert p.mean(xs) == 5 and p.variance(xs) == 4
        assert abs(p.variance(xs, sample=True) - 32 / 7) < 1e-12

    def test_matches_numpy(self, load):
        p = load("probability.py")
        xs = list(np.random.default_rng(1).normal(size=50))
        assert abs(p.variance(xs, sample=True) - np.var(xs, ddof=1)) < 1e-12

    def test_normal_pdf(self, load):
        p = load("probability.py")
        assert abs(p.normal_pdf(0) - 1 / math.sqrt(2 * math.pi)) < 1e-12
        assert abs(p.normal_pdf(12, mu=10, sigma=2) - p.normal_pdf(1) / 2) < 1e-12


class TestBayes:
    def test_textbook(self, load):
        p = load("probability.py")
        assert abs(p.bayes(0.5, 0.9, 0.1) - 0.9) < 1e-12

    def test_simulation_agrees(self, load):
        p = load("probability.py")
        assert abs(p.simulate_alarm(0.3, 0.8, 0.2) - p.bayes(0.3, 0.8, 0.2)) < 0.01


def test_finding_a_90_percent_alarm_is_wrong_four_times_in_ten(load):
    p = load("probability.py")
    rate = customers.load()["churned"].mean()
    assert round(p.bayes(rate, 0.9, 0.1), 3) == 0.575, (
        "Catches 90% of leavers, wrongly flags 10% of stayers - and still only 57.5% of "
        "its alarms are real, because stayers outnumber leavers almost seven to one.")
