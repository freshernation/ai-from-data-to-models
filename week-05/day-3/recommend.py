"""Day 3 - customers who bought this also bought...

The matrix is customers x items: 1 if they bought it. Two items are similar when the
same customers bought both.
"""

import numpy as np
import pandas as pd


def purchase_matrix(orders):
    """A DataFrame, one row per customer_id, one column per item_id (sorted, as
    pd.crosstab gives them), 1.0 if bought else 0.0."""
    raise NotImplementedError


def cosine_similarity(M):
    """Item-by-item cosine similarity of the columns of M (a numpy array), shape
    (items, items). Divide each column by its length; a column of zeros stays zeros."""
    raise NotImplementedError


def recommend(matrix, similarity, customer_id, k=10):
    """Score every item as similarity @ (that customer's row). Never recommend what they
    already bought (score -inf). Return the k best item_ids, best first
    (np.argsort(-scores, kind="stable"), so ties keep column order)."""
    raise NotImplementedError


def most_popular(matrix, customer_id, k=10):
    """The baseline: the k items bought by the most customers, excluding the customer's
    own purchases. Same tie rule."""
    raise NotImplementedError
