"""Milestone - linear regression from scratch, with scikit-learn's interface.

    model = LinearRegressionGD().fit(X, y)
    model.coef_, model.intercept_      # in the ORIGINAL units of X
    model.predict(X_new)
    model.score(X_test, y_test)        # R squared

Uses your regression.py (copy it into this folder).
"""

import numpy as np

from regression import gradient_descent, standardise


class LinearRegressionGD:
    def __init__(self, lr=0.1, steps=5000, tol=1e-8):
        """Store the settings. Nothing is learned here."""
        raise NotImplementedError

    def fit(self, X, y):
        """Standardise X, run gradient_descent, then convert the weights back:
            coef_      = w / std
            intercept_ = b - sum(coef_ * mean)          (a plain float)
            steps_taken_ = the steps gradient_descent reports
        Return self, so fit(...).predict(...) works."""
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

    def score(self, X, y):
        """R squared: 1 - (sum of squared residuals) / (sum of squared deviations from mean y)."""
        raise NotImplementedError
