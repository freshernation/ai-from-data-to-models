# Week 8 Milestone — Project 2: the product classifier

> A CNN trained on augmented photos, saved and reloaded, with an error gallery, a stress
> test, and a model card that says where it breaks.

---

## The files

| File | Where it comes from |
|---|---|
| `trainer.py` | **copy** from `week-07/milestone/` |
| `cnn.py` | **copy** from `day-2/` |
| `shift_test.py` | **copy** from `day-3/` |
| `augment.py` | **copy** from `day-4/` |
| `product_classifier.py` | new: train, save, load, predict, error gallery, stress, report |
| `MODEL_CARD.md` | new |

## `MODEL_CARD.md`

| Section | What goes in it |
|---|---|
| Intended use | What it sorts, and what it must not be used for |
| Data | Training and test photos, and how they differ |
| The model, and why a CNN | Its size, and the dense network's numbers beside it |
| Performance | Both test sets, the confusion matrix, a baseline |
| Where it breaks | The stress test, in numbers |
| Limits and risks | Synthetic data, a forced choice, and what to add |

At least 50 words each.

---

## Check it

```bash
pytest week-08/milestone -v
python week-08/milestone/product_classifier.py
```

## Friday

You load your saved model in a fresh session, then move and darken a photo live.
