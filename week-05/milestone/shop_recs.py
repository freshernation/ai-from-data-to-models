"""Milestone - segments and "customers also bought", for the shop.

    python shop_recs.py

Uses your kmeans.py and recommend.py (copy them into this folder).
Never read shoplab.orders.hidden_segments() here: that is the answer key.
"""

import numpy as np
import pandas as pd

from kmeans import best_of
from recommend import cosine_similarity, purchase_matrix, recommend
from shoplab import orders


def segment_customers(k=3):
    """Cluster orders.category_shares() with best_of(..., k).
    Returns (labels, profiles):
        labels    a Series customer_id -> cluster number, named "segment"
        profiles  a DataFrame, one row per cluster: the centroid's share in each category
                  (rounded to 3 places) and a "customers" column with the cluster's size
    """
    raise NotImplementedError


class Recommender:
    def __init__(self, order_rows=None):
        """Build the purchase matrix and item similarity from order_rows
        (default: all of orders.load())."""
        raise NotImplementedError

    def also_bought(self, item_id, k=5):
        """The k items most similar to item_id, never item_id itself, best first."""
        raise NotImplementedError

    def for_customer(self, customer_id, k=10):
        """recommend() for one customer."""
        raise NotImplementedError


if __name__ == "__main__":
    labels, profiles = segment_customers()
    print(profiles)
    rec = Recommender()
    print("also bought with I001:", rec.also_bought("I001"))
