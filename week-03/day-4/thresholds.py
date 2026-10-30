"""Day 4 - choosing a threshold with money, not with 0.5.

The shop's numbers: a retention offer costs 10. A customer who leaves is worth 200 a
year. An offer to someone about to leave keeps them 30% of the time.
"""

import numpy as np

OFFER_COST = 10
CUSTOMER_VALUE = 200
SAVE_RATE = 0.3


def value(y, scores, threshold, offer_cost=OFFER_COST, customer_value=CUSTOMER_VALUE,
          save_rate=SAVE_RATE):
    """Money made by sending an offer to everyone with score >= threshold:
        (flagged churners) * save_rate * customer_value  -  (everyone flagged) * offer_cost
    A plain float."""
    raise NotImplementedError


def best_threshold(y, scores, grid=None):
    """The threshold with the highest value. Default grid: 0.05, 0.10, ... 0.95
    (np.round(np.arange(0.05, 0.96, 0.05), 2)). Returns (threshold, value), floats.
    On a tie, the first (lowest) threshold."""
    raise NotImplementedError
