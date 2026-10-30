import numpy as np
import pytest


class TestByHand:
    def test_dot(self, load):
        la = load("linalg.py")
        assert la.dot([1, 2, 3], [4, 5, 6]) == 32

    def test_dot_refuses_mismatched(self, load):
        la = load("linalg.py")
        with pytest.raises(ValueError):
            la.dot([1, 2], [1, 2, 3])

    def test_matmul_matches_numpy(self, load):
        la = load("linalg.py")
        A, B = [[1, 2, 3], [4, 5, 6]], [[1, 0], [0, 1], [2, 2]]
        assert np.allclose(la.matmul(A, B), np.array(A) @ np.array(B))

    def test_matmul_shape_error_names_the_shapes(self, load):
        la = load("linalg.py")
        with pytest.raises(ValueError, match="2x3"):
            la.matmul([[1, 2, 3], [4, 5, 6]], [[1, 2], [3, 4]])

    def test_by_hand_means_no_numpy(self, load, source):
        la = load("linalg.py")
        assert la.dot([1], [2]) == 2, "Make dot work first."
        code = source("linalg.py", code_only=True).split("def predict")[0]
        assert "np." not in code and "@" not in code, "dot and matmul use loops, not numpy."


class TestLinearModel:
    def test_predict(self, load):
        la = load("linalg.py")
        got = la.predict([[1, 2], [3, 4]], [10, 1], 0.5)
        assert list(got) == [12.5, 34.5]

    def test_finding_a_formula_is_a_model_with_its_weights_typed_in(self, load):
        la = load("linalg.py")
        assert list(la.predicted_spend([2, 0], [10, 60])) == [24.0, 30.0], \
            "12 + 4.5*2 + 0.3*10 = 24. On Thursday the computer finds 4.5 and 0.3 itself."
