"""Product reviews - the text weeks 9 to 11 work on.

    load()            review_id, text, positive (1/0), negated (1 if the review negates
                      its adjective: "not bad at all"), split ("train" / "test")
    frozen_split()    (train, test) frames. The test set is touched once per model.
"""

import pandas as pd

from shoplab import DATA


def load():
    return pd.read_csv(DATA / "reviews.csv")


def frozen_split():
    df = load()
    return (df[df["split"] == "train"].reset_index(drop=True),
            df[df["split"] == "test"].reset_index(drop=True))
