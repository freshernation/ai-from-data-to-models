"""Project 3 - train every model once and write them, with a manifest, to one folder.

    python train_all.py          # writes bundle/ next to this file (git ignores it)

Uses the files you copied in from weeks 4, 8, 9 and 12.
"""

import json
from pathlib import Path

import torch
from sklearn.metrics import roc_auc_score

import churn_model
import product_classifier
import sentiment
from artifacts import write_manifest
from embeddings import predict
from shoplab import customers, images, reviews
from shoplab.customers import FEATURES

VERSION = "1.0.0"


def build(bundle, seed=0):
    """Create the folder and write into it:
        churn.joblib     churn_model.train on the frozen training customers, churn_model.save
        reference.csv    the training customers' FEATURES columns (index=False) - for /drift
        sentiment.pt     sentiment.train(review training set, seed=seed); torch.save its state_dict
        vocab.json       its vocabulary, as JSON
        product.pt       product_classifier.train(images.load(), seed=seed); product_classifier.save
    Then write_manifest(bundle, VERSION, metrics) with metrics, each rounded to 3 places:
        churn_auc                 test AUC of the churn model
        sentiment_accuracy        accuracy on the review test set
        product_accuracy_moved    product_classifier.report(...)["shifted"]
    Return the manifest."""
    raise NotImplementedError


if __name__ == "__main__":
    print(json.dumps(build(Path(__file__).parent / "bundle"), indent=2))
