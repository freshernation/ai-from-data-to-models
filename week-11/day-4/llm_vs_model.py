"""Day 4 - someone else's model behind an API, against the one you trained.

Copy text.py, trainer.py, embeddings.py, lstm.py and sentiment.py from week 9, and
ask.py and structured.py from this week, into this folder.

With the fake, the LLM column measures your CODE (calls, retries, tokens, cost
arithmetic), not any real model. Run it live (SHOPLAB_LLM=anthropic) to measure Claude.
"""

import time

import numpy as np

from ask import cost
from embeddings import predict
from sentiment import FAR, train
from structured import classify


def llm_labels(llm, texts):
    """Classify every text with structured.classify (one retry). A failed answer counts
    as negative (0). Also collect EVERY Reply the llm returned, retries included: wrap
    llm.complete so each call is recorded, and put the original back afterwards.
    Returns (labels as a numpy array of 0/1, list of Replies)."""
    raise NotImplementedError


def accuracy(pred, df):
    """{"all": accuracy, "far negation": accuracy on texts containing FAR}."""
    raise NotImplementedError


def compare(llm, train_df, test_df, model_id="claude-opus-5-5"):
    """Two rows:
        "llm": accuracy(...) plus "calls", "dollars_per_1000" (cost at model_id prices,
               per 1,000 reviews) and "ms_per_review" (mean Reply.latency_ms)
        "own": your week 9 LSTM (sentiment.train, embeddings.predict): accuracy(...),
               calls 0, dollars 0.0, and ms_per_review measured with time.perf_counter
               over the whole test set, divided by its length."""
    raise NotImplementedError


def break_even(dollars_per_1000, setup_dollars):
    """How many reviews the LLM can classify before it has cost setup_dollars."""
    raise NotImplementedError
