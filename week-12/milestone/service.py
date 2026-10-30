"""Project 3 - the shop's AI service: every model, one API, a drift check."""

import json
from pathlib import Path

import numpy as np
import pandas as pd
import torch

import churn_model
import product_classifier
from api import Customer, create_app
from artifacts import read_manifest, verify
from embeddings import predict
from lstm import LSTMClassifier
from monitor import drift_report, verdict
from shoplab.customers import FEATURES


def load_service(bundle):
    """1. verify(bundle): if anything is wrong, raise RuntimeError naming the files.
    2. Load the three models and reference.csv.
    3. create_app with three plain functions:
         churn:     customer dict -> churn_model.predict_one
         sentiment: text -> "positive" / "negative" from your LSTM
         product:   16x16 pixel lists -> a class name (np.array(..., dtype=np.uint8))
       and version = the manifest's version.
    4. Add two routes to that app:
         GET  /version -> the whole manifest
         POST /drift   a list of Customer -> {column: {"psi": ..., "verdict": ...}} against
                       reference.csv; fewer than 50 customers -> {"error": "send at least 50 customers"}
    Return the app."""
    raise NotImplementedError
