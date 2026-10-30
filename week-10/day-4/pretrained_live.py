"""Given, and run live only - a pretrained transformer reads the shop's reviews.

    pip install transformers          # not in requirements.txt: it downloads ~260 MB
    python pretrained_live.py

Runs a sentiment model trained by others on hundreds of thousands of real film reviews
(DistilBERT fine-tuned on SST-2) on twenty of the shop's test reviews and its hardest
cases. No test runs it: it downloads a model.
"""

from shoplab.reviews import frozen_split

HARD = ["not bad at all !", "honestly not really excellent !", "the mug is not that awful !"]


def main():
    from transformers import pipeline
    classify = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    _, test = frozen_split()
    rows = test.head(20)
    right = 0
    for text, label in zip(rows["text"], rows["positive"]):
        guess = classify(text)[0]["label"] == "POSITIVE"
        right += guess == bool(label)
        print(f"{'ok ' if guess == bool(label) else 'XX '} {text}")
    print(f"\n{right}/20 right with no training on the shop's data.\n")
    for text in HARD:
        print(classify(text)[0], text)


if __name__ == "__main__":
    main()
