# Week 12 Milestone — Project 3: the shop's AI service

> Every model trained once into a fingerprinted bundle, served behind one validated API
> with a drift check, packaged in a container, and `REVIEW.md` for the engineer on call.

---

## The files

| File | Where it comes from |
|---|---|
| `tuning.py`, `features.py`, `churn_model.py` | **copy** from week 4 |
| `trainer.py` | **copy** from week 7's milestone |
| `cnn.py`, `shift_test.py`, `augment.py`, `product_classifier.py` | **copy** from week 8 |
| `text.py`, `embeddings.py`, `lstm.py`, `sentiment.py` | **copy** from week 9 |
| `api.py`, `artifacts.py`, `monitor.py` | **copy** from this week's days |
| `train_all.py` | new: `build()` writes the bundle and its manifest |
| `service.py` | new: `load_service()` checks the bundle and builds the app |
| `serve.py`, `requirements-serve.txt` | given |
| `Dockerfile` | new — the comments say what goes in it |
| `REVIEW.md` | new |

## `REVIEW.md`

| Section | What goes in it |
|---|---|
| What is running | The version, each model and its test number, the manifest |
| How fast, and how it fails | Your load test, and what bad input and a changed file do |
| What we watch | The drift check, its numbers on next month, and when to retrain |
| Who it could treat unfairly | Recall by group, with the counts |
| What I would fix first | In order |

At least 60 words each.

---

## Check it

```bash
pytest week-12/milestone -v          # about 30 seconds: it trains every model
python week-12/milestone/train_all.py
docker build -f week-12/milestone/Dockerfile -t shop-ai .
docker run -p 8000:8000 shop-ai      # then open http://localhost:8000/docs
```

## Friday

Fresh clone, build, run, and the instructor's requests — then the mock interview.
