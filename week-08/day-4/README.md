# Day 4 — Augmentation, mistakes, and a network trained on a million photos

> **By the end of today** you can fix a model's blind spot by augmenting its data, read
> a confusion matrix, and run a pretrained ResNet on your own photo.

---

## Read first

- [ ] Dive into Deep Learning — [Image augmentation](https://d2l.ai/chapter_computer-vision/image-augmentation.html) — 14.1.1 · 10 min
- [ ] Dive into Deep Learning — [Fine-tuning](https://d2l.ai/chapter_computer-vision/fine-tuning.html) — 14.2.1, the idea only · 10 min

---

## What you need to know

### Augmentation

If the model must handle moved products, show it moved products: every training photo
plus three copies, each rolled by up to three pixels. The dense network, trained on these
8,000, scores about **99.6%** on the moved test set. It works — but it needed to *see*
every position, while the CNN got it from its design.

### The confusion matrix

Rows are the true kind, columns the guess. The plain dense network on moved photos called
54 of 121 shirts books: a shirt moved sideways lights up a book's pixels. Accuracy says
"46%"; the matrix says *which* mistakes, and so what to fix.

### Transfer learning (live)

`pretrained_live.py` loads ResNet-18, trained on 1.2 million real photos, and shows its
top five guesses for any photo you give it. Re-training only its last layer on your own
classes is how most real image models start. It needs `pip install torchvision` and a
download, so no test runs it.

---

## Exercises

```bash
pytest week-08/day-4 -v
```

Copy the three earlier files, then write `augment`, `confusion_matrix` and
`augmented_dense` in `augment.py`.

---

## Predict-then-run

Before running it live: what will ResNet-18 say about one of the shop's 16 × 16 icons?
(`python pretrained_live.py --icon`)

---

## Before you close the laptop

Commit, push, fill in the signal log. Then start Project 2.
