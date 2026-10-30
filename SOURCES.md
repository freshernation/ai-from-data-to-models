# Sources

Chosen by one rule: an official source for how the thing works, an engineering account
from people who build with it for why, and nothing that is a vendor selling the answer
without saying so. Three or four a week, not ten.

Need something that is not here? `ai/librarian.md`.

---

## The ones worth reading twice

| Read | Why |
|---|---|
| [Google — Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | Short, correct, and honest about metrics; weeks 1 to 4 lean on it |
| [Dive into Deep Learning](https://d2l.ai/) | Free, runnable, and the maths written for people who code; weeks 2 and 6 to 10 |
| [scikit-learn — Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | Leakage and inconsistent preprocessing, the two bugs that make numbers lie |

---

## Week 1 — Data before models

| Read | Why |
|---|---|
| [NumPy — the absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html) | Arrays and whole-column operations |
| [pandas — 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) | The table operations every week uses |
| [pandas — Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) | What NaN is, and how it is filled |
| [Matplotlib — Quick start](https://matplotlib.org/stable/users/explain/quick_start.html) | Figures and axes, saved to files |

**Ignore for now:** seaborn, plotly, notebooks, and any "automatic EDA" tool.

## Week 2 — The maths, in code

| Read | Why |
|---|---|
| [3Blue1Brown — Essence of linear algebra](https://www.3blue1brown.com/topics/linear-algebra) | What a matrix product means, in pictures |
| [d2l — Calculus](https://d2l.ai/chapter_preliminaries/calculus.html) | Derivatives and gradients as a programmer needs them |
| [3Blue1Brown — Bayes theorem](https://www.3blue1brown.com/lessons/bayes-theorem) | Base rates, the idea Wednesday turns on |
| [Google MLCC — Gradient descent](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent) | Learning rate and convergence, with the same pictures you will draw |

**Ignore for now:** proofs, eigenvalues, measure theory, and any course that starts with three weeks of maths before code.

## Week 3 — A first classifier, honestly measured

| Read | Why |
|---|---|
| [Google MLCC — Logistic regression](https://developers.google.com/machine-learning/crash-course/logistic-regression) | Sigmoid and log loss |
| [Google MLCC — Accuracy, precision, recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) | Why accuracy lies on imbalanced data |
| [Google MLCC — ROC and AUC](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) | Ranking quality, separate from the threshold |
| [scikit-learn — Tuning the decision threshold](https://scikit-learn.org/stable/modules/classification_threshold.html) | Thresholds chosen from costs, by the library you will use |

**Ignore for now:** SMOTE and resampling, calibration, and regularisation (week 4).

## Week 4 — Trees, ensembles and tuning

| Read | Why |
|---|---|
| [Google — Decision forests](https://developers.google.com/machine-learning/decision-forests) | How a tree grows, and why forests vote, without the maths |
| [scikit-learn — Ensembles](https://scikit-learn.org/stable/modules/ensemble.html) | Forests and boosting, as you will call them |
| [scikit-learn — Tuning hyper-parameters](https://scikit-learn.org/stable/modules/grid_search.html) | Grid search inside cross-validation |
| [Mitchell et al. — Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) | What a model card is for, from the people who proposed it |

**Ignore for now:** XGBoost, LightGBM and CatBoost tutorials; SHAP; Kaggle "top 1%" notebooks.

## Week 5 — Without labels

| Read | Why |
|---|---|
| [Google — Clustering](https://developers.google.com/machine-learning/clustering) | k-means and how to judge a clustering |
| [scikit-learn — PCA](https://scikit-learn.org/stable/modules/decomposition.html#pca) | The library version of Tuesday's SVD |
| [Shlens — A tutorial on PCA](https://arxiv.org/abs/1404.1100) | Why the SVD gives the directions of most variance |
| [Google — Recommendation systems](https://developers.google.com/machine-learning/recommendation/collaborative/basics) | Collaborative filtering, the idea behind Wednesday |

**Ignore for now:** t-SNE and UMAP plots, matrix factorisation, deep recommenders.

## Week 6 — A neural network by hand

| Read | Why |
|---|---|
| [3Blue1Brown — Neural networks](https://www.3blue1brown.com/topics/neural-networks) | What a layer is, and what backprop does, in pictures |
| [Stanford CS231n — Backpropagation](https://cs231n.github.io/optimization-2/) | The chain rule as gates passing gradient back |
| [d2l — Numerical stability and initialisation](https://d2l.ai/chapter_multilayer-perceptrons/numerical-stability-and-init.html) | Why starting weights decide whether training starts |
| [Karpathy — A recipe for training neural networks](http://karpathy.github.io/2019/04/25/recipe/) | The judgement no tutorial gives you |

**Ignore for now:** activation-function zoos, optimiser comparisons, and anything with "from scratch in 10 lines".

## Week 7 — PyTorch, properly

| Read | Why |
|---|---|
| [PyTorch — Learn the basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | The official path: tensors, autograd, modules, the loop |
| [d2l — Dropout](https://d2l.ai/chapter_multilayer-perceptrons/dropout.html) | What dropout does and why it helps |
| [Grinsztajn et al. — Why do tree-based models still outperform deep learning on tabular data?](https://arxiv.org/abs/2207.08815) | Thursday's finding, measured on 45 datasets |

**Ignore for now:** PyTorch Lightning, GPUs and `torch.compile`, learning-rate schedules.

## Week 8 — Images: CNNs

| Read | Why |
|---|---|
| [d2l — Convolutions for images](https://d2l.ai/chapter_convolutional-neural-networks/conv-layer.html) | What a filter computes, by hand |
| [Stanford CS231n — Convolutional networks](https://cs231n.github.io/convolutional-networks/) | Channels, pooling and why weights are shared |
| [d2l — From fully connected layers to convolutions](https://d2l.ai/chapter_convolutional-neural-networks/why-conv.html) | Wednesday's finding, argued from first principles |
| [d2l — Image augmentation](https://d2l.ai/chapter_computer-vision/image-augmentation.html) | Thursday's fix, and its limits |

**Ignore for now:** YOLO and detection tutorials, OpenCV, "state of the art" model zoos.

## Week 9 — Text: counts to sequences

| Read | Why |
|---|---|
| [scikit-learn — Text feature extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction) | Bag of words and TF-IDF, as the library builds them |
| [Jurafsky and Martin — Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/) | The standard textbook; chapter 4 on sentiment and negation |
| [d2l — Word embedding (word2vec)](https://d2l.ai/chapter_natural-language-processing-pretraining/word2vec.html) | Where learned word vectors came from |
| [Olah — Understanding LSTM networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) | The clearest picture of an LSTM's gates |

**Ignore for now:** NLTK and spaCy pipelines, stop-word lists, stemming, pretrained GloVe files.

## Week 10 — Attention and transformers

| Read | Why |
|---|---|
| [Alammar — The illustrated transformer](https://jalammar.github.io/illustrated-transformer/) | Every matrix in attention, drawn |
| [d2l — Self-attention and positional encoding](https://d2l.ai/chapter_attention-mechanisms-and-transformers/self-attention-and-positional-encoding.html) | Why attention needs positions |
| [Vaswani et al. — Attention is all you need](https://arxiv.org/abs/1706.03762) | The original paper; sections 3.2 and 3.5 are readable now |
| [Hugging Face — Byte-pair encoding](https://huggingface.co/learn/llm-course/chapter6/5) | Thursday's tokenizer, as real models use it |

**Ignore for now:** fine-tuning BERT (the `fine-tuning` course), "build GPT in an hour" videos, efficient-attention variants.
