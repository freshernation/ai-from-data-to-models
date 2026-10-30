# Week 8 — Images: CNNs (Project 2)

> **Destination**
> You can convolve an image by hand, train a small CNN on the shop's product photos, show
> with numbers why it survives a moved product when a dense network does not, and ship a
> saved classifier with a model card that says exactly where it breaks.

On the shop's table, the network only tied the line. Photos are different. A line — or a
dense network — sees 256 separate pixels and must learn a mug at every position
separately. A convolutional network slides one small filter over the whole image, so a
mug is a mug wherever it sits. This is the first week where a network wins outright, and
the first where a perfect test score is the start of the model card, not the end.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Convolve and pool an image by hand, and see features move with the photo |
| Tue | `day-2/` | Build and train a 1,316-weight CNN with week 7's trainer |
| Wed | `day-3/` | Show a dense network fail on moved products while the CNN does not |
| Thu | `day-4/` | Fix the dense network with augmentation, read a confusion matrix, try a pretrained model live |
| Fri | `milestone/` | **Project 2**: the saved, stress-tested product classifier, and `MODEL_CARD.md` |

---

## The rule from this week on

**Test outside the training conditions.** Every model gets a test set that differs from
its training data in a way the real world will: moved, noisier, darker.

---

## Before Monday

Your week 7 `trainer.py` must pass its tests: every day this week copies it.
Optional, for Thursday's live demo only: `pip install torchvision`.

---

## Outside-view question

> *A radiologist reads a scan that was taken rotated by ten degrees. What changes for
> them — and what would change for a trainee who had only ever seen straight scans?*
