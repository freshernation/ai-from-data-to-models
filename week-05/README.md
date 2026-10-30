# Week 5 — Without labels

> **Destination**
> You can group the shop's customers by what they buy with k-means you wrote, draw them in
> two dimensions with PCA you wrote, recommend items from what other customers bought, and
> prove the recommender beats "most popular" on purchases it was never shown.

Every week so far had an answer column. This week it is gone. Nobody labelled the
customers' segments, and nobody wrote down what each customer should buy next. So the
week's real question is not "how do I cluster?" but "with no answer column, how do I know
it worked?" Two answers: compare against an answer key the course hid (only the tests
read it), and hide some real data from yourself and see whether you predict it.

---

## The week

| Day | Folder | What you'll be able to do |
|---|---|---|
| Mon | `day-1/` | Write k-means, read an elbow curve, and measure a clustering against a hidden answer |
| Tue | `day-2/` | Write PCA with one SVD and draw six columns on a page |
| Wed | `day-3/` | Build "customers who bought this also bought" from co-purchases |
| Thu | `day-4/` | Hide each customer's last purchase and measure the hit rate |
| Fri | `milestone/` | Segments and a recommender for the shop, and `SEGMENTS.md` |

---

## The rule from this week on

**No label? Hide something you know, and predict it.** An unsupervised method you have
not tested against held-back data is a picture, not a result.

---

## Before Monday

Nothing new. The orders are in `data/orders.csv`; `shoplab.orders` loads them.

---

## Outside-view question

> *A librarian gets a box of books with no catalogue numbers. How do they decide which
> shelf each goes on — and how do they know the shelving is any good?*
