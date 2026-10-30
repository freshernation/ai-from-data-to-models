"""Day 3 - asking for JSON, checking it, and asking again."""

import json
from typing import Literal

from pydantic import BaseModel, ValidationError

SYSTEM = ("You classify the sentiment of a product review. Answer with JSON only, exactly "
          'like {"label": "positive", "reason": "..."}. label is "positive" or "negative".')


class Sentiment(BaseModel):
    """label must be exactly "positive" or "negative" (typing.Literal); reason is a str."""
    label: Literal["positive", "negative"]
    reason: str


def parse(text):
    """json.loads, then Sentiment.model_validate. Let both kinds of error escape."""
    raise NotImplementedError


def classify(llm, review, retries=1):
    """Send the review (system=SYSTEM). If the answer does not parse, and retries remain,
    append the bad answer as an assistant message and a user message saying what was
    wrong and asking for the JSON only, and ask again.
    Returns (Sentiment or None if every attempt failed, number of calls made)."""
    raise NotImplementedError


def survey(llm, reviews, retries=1):
    """{"failed": reviews with no valid answer, "retried": reviews that needed more than
    one call, "calls": total calls}."""
    raise NotImplementedError
