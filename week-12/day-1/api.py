"""Day 1 - every model behind one validated HTTP API.

The models are passed IN, as plain functions, so this file can be tested with stand-ins
and run with the real ones (the milestone does that).
"""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator


class Customer(BaseModel):
    """The seven fields the churn model needs, each with its allowed range:
        plan                    "basic" | "plus" | "pro"
        tenure_months           int, 1 to 120
        monthly_spend           float, 0 to 10,000
        orders_90d              int, 0 to 500
        days_since_last_order   int, 0 to 3,650
        support_tickets         int, 0 to 100
        used_discount           0 or 1
    Use Literal and Field(ge=..., le=...)."""


class Review(BaseModel):
    """text: 1 to 500 characters."""


class Photo(BaseModel):
    """pixels: a list of lists of ints. A field_validator must reject anything that is not
    16 rows of 16 values, each 0 to 255, with a ValueError that says which."""


def create_app(churn, sentiment, product, version="dev"):
    """A FastAPI app with:
        GET  /health      -> {"status": "ok", "version": version}
        POST /churn       Customer -> {"probability": float(churn(customer as a dict))}
        POST /sentiment   Review   -> {"label": sentiment(text)}
        POST /product     Photo    -> {"label": product(pixels)}
    Invalid input must get FastAPI's automatic 422 - never reach a model."""
    raise NotImplementedError
