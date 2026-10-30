"""Day 4 - how fast is it, for the slowest customers? Plain Python."""

import math
import time


def percentile(values, q):
    """Nearest rank: sort, take the value at rank ceil(q / 100 * n) (counting from 1,
    at least 1). percentile([5, 1, 3, 2, 4], 50) -> 3."""
    raise NotImplementedError


def time_requests(client, path, payload, n=200):
    """POST payload to path n times; the milliseconds each took (time.perf_counter).
    Raise if any response is not a success (response.raise_for_status())."""
    raise NotImplementedError


def summary(times):
    """{"p50", "p95", "p99", "max"}"""
    raise NotImplementedError
