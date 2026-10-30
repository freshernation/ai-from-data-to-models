# Week 5 — Concept fence

## Allowed

**Everything from weeks 1 to 4**, plus:

- k-means, inertia, the elbow, purity — by hand in numpy
- `np.linalg.svd`, `np.linalg.norm`, `pd.crosstab`
- scikit-learn's `KMeans` and `PCA` — **only** in tests, to check yours
- cosine similarity, item-item recommendation, leave-last-out hit rate

## Not yet

embeddings learned by a network (week 9) · matrix factorisation · DBSCAN, hierarchical clustering,
Gaussian mixtures · t-SNE, UMAP · silhouette scores · implicit-feedback libraries

---

## Why no matrix factorisation

It is how the famous recommenders work, and it would score better than co-purchase
counting. It is cut because it learns a vector for every item — an embedding — and that
idea arrives properly in week 9, trained by a network you understand. This week's
recommender has nothing learned in it at all: it is counting and a cosine. If counting
already beats "most popular" by 42 points, the student has a baseline worth beating later.
