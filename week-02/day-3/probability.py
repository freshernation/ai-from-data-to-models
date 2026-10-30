"""Day 3 - the probability a model's output rests on.

mean and variance: plain Python, no numpy - so you know what np.var does.
"""

import math

import numpy as np


def mean(xs):
    raise NotImplementedError


def variance(xs, sample=False):
    """Average squared distance from the mean. sample=True divides by n - 1 instead of n."""
    raise NotImplementedError


def normal_pdf(x, mu=0.0, sigma=1.0):
    """The height of the normal (bell) curve at x."""
    raise NotImplementedError


def bayes(prior, sensitivity, false_positive_rate):
    """P(leaves | alarm), when:
        prior               P(leaves)
        sensitivity         P(alarm | leaves)
        false_positive_rate P(alarm | stays)
    """
    raise NotImplementedError


def simulate_alarm(prior, sensitivity, false_positive_rate, n=100_000, seed=0):
    """The same question by experiment: simulate n customers with numpy
    (rng = np.random.default_rng(seed)), sound the alarm for each with the right
    probability, and return the fraction of alarmed customers who actually leave."""
    raise NotImplementedError
