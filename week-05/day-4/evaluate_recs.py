"""Day 4 - did the recommender recommend? Leave the last purchase out.

Copy recommend.py from day 3 into this folder first.
"""

from recommend import cosine_similarity, most_popular, purchase_matrix, recommend


def leave_last_out(orders):
    """Split each customer's purchases: everything but their highest `seq` is history;
    the last one is held out. Returns (history rows, Series customer_id -> held-out item_id)."""
    raise NotImplementedError


def hit_rate(orders, k=10, method="item"):
    """Build the matrix (and, for "item", the similarity) from HISTORY ONLY. For every
    customer, recommend k items with recommend() or, for method="popular", most_popular().
    Return the fraction of customers whose held-out item is in their k."""
    raise NotImplementedError
