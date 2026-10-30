# Week 4 — Concept fence

## Allowed

**Everything from weeks 1 to 3**, plus:

- Gini impurity and splits by hand
- `DecisionTreeClassifier`, `RandomForestClassifier`, `GradientBoostingClassifier`, `SVC`
- `StratifiedKFold`, `cross_val_score`, `GridSearchCV`, `Pipeline` / `make_pipeline`, `SelectKBest`
- `sklearn.metrics.roc_auc_score` in your own files (you wrote it by hand last week)
- permutation importance by hand; `joblib`

## Not yet

neural networks (week 6) · XGBoost, LightGBM, CatBoost · SHAP · random or Bayesian search ·
stacking · imbalance tricks (resampling, class weights)

---

## Why no XGBoost or LightGBM

They win competitions on tables, and they will be the first thing a job asks about.
They are left out because they are gradient boosting — Tuesday's model — made faster and
given more settings, and on this table plain boosting already loses to a line. A student
who reaches for XGBoost before running a cross-validated line has learned a library; one
who ran the line first has learned when a library is worth it.
