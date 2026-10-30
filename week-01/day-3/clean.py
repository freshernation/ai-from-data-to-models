"""Day 3 - cleaning, one fault at a time, each one counted.

Every function returns the cleaned frame AND a count, so your report can say
exactly what was wrong. None of them may change the frame they were given.
"""

import numpy as np


def drop_duplicates(df):
    """Keep the first row for each customer_id.
    Returns (frame with a fresh 0..n-1 index, how many rows were dropped)."""
    raise NotImplementedError


def normalise_region(series):
    """' North' -> 'north', 'WEST' -> 'west': strip spaces, lower-case. Returns a Series."""
    raise NotImplementedError


def fix_impossible(df):
    """A negative monthly_spend is impossible: make it missing (NaN), not 0.
    Returns (frame, how many values were changed)."""
    raise NotImplementedError


def fill_missing(df):
    """Fill missing monthly_spend with the MEDIAN spend of that customer's plan.
    Returns (frame, how many values were filled)."""
    raise NotImplementedError


def clean(df):
    """All four, in this order: duplicates, region, impossible, missing.

    Returns (frame, report) where report is a dict:
        {"duplicates": int, "region_spellings": (before, after),
         "impossible": int, "filled": int}
    The order matters: fix impossible values BEFORE filling, or the -1s count as real.
    """
    raise NotImplementedError
