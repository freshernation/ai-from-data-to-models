"""Day 2 - know exactly which model files are running.

A bundle is a folder of model files plus manifest.json:
    {"version": "1.0.0", "files": {"churn.joblib": "<fingerprint>", ...}, "metrics": {...}}
"""

import hashlib
import json
from pathlib import Path

MANIFEST = "manifest.json"


def fingerprint(path):
    """The first 16 hex characters of the SHA-256 of the file's bytes."""
    raise NotImplementedError


def write_manifest(directory, version, metrics):
    """Fingerprint every file in directory except manifest.json, write the manifest
    (json.dumps(..., indent=2, sort_keys=True)) and return it as a dict."""
    raise NotImplementedError


def read_manifest(directory):
    raise NotImplementedError


def verify(directory):
    """Sorted names of every file that is missing, changed, or not in the manifest.
    An empty list means the folder is exactly what was written."""
    raise NotImplementedError
