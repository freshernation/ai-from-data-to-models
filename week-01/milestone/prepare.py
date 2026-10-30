"""Milestone - the raw export in, a file a model can train on out.

    python prepare.py            # writes customers_prepared.csv next to this file

Uses your clean.py and eda.py (copy them into this folder first).
"""

from pathlib import Path

from shoplab import DATA

HERE = Path(__file__).parent


def prepare(raw_path, out_path):
    """Read raw_path, clean it, drop every leaking column, write out_path.

    Returns (frame, report): report is clean()'s report plus "leaks": the list of
    column names dropped. The written CSV has no index column.
    Find the leaks with find_leaks on the CLEANED frame - never by naming them.
    """
    raise NotImplementedError


if __name__ == "__main__":
    df, report = prepare(DATA / "customers_raw.csv", HERE / "customers_prepared.csv")
    print(report)
