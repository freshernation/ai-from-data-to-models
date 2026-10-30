"""Day 2 - first questions to a table, with pandas.

Work on the RAW export (data/customers_raw.csv). Do not clean anything today -
tomorrow you will find out why some of today's numbers are slightly wrong.
"""

import pandas as pd


def load(path):
    """Read the CSV at `path` into a DataFrame."""
    raise NotImplementedError


def churn_rate(df):
    """The fraction of rows with churned == 1, as a plain float."""
    raise NotImplementedError


def churn_by_plan(df):
    """A Series: plan -> churn rate, highest first."""
    raise NotImplementedError


def top_spenders(df, n=5):
    """The n rows with the highest monthly_spend, only the columns
    customer_id, plan, monthly_spend, highest first."""
    raise NotImplementedError


def count_where(df, column, value):
    """How many rows have df[column] == value, as an int."""
    raise NotImplementedError
