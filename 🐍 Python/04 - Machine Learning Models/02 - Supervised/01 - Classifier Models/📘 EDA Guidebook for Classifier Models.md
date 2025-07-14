___
🎯 Purpose

This guidebook outlines how to prepare and explore data for binary or multiclass classification. It focuses on evaluating class structure, feature relevance, balance, and the modeling assumptions relevant to tree-based, linear, or probabilistic classifiers.

---

## 🧠 1. Confirm Problem Structure

* [ ] ✅ Target variable is **categorical**
* [ ] ✅ Task is **binary** or **multiclass**
* [ ] ✅ Labels are clean, interpretable, and non-null
* [ ] ✅ Goal is **classification** (not regression or clustering)

---

## 🧪 2. Class Distribution Assessment

### 🔹 Frequency Plot

```python
sns.countplot(x='target', data=df)
```

* Check for class imbalance
* Consider resampling if imbalance is severe (> 90/10)

### 🔹 Percent Breakdown

```python
df['target'].value_counts(normalize=True)
```

---

## 📊 3. Feature Distribution by Class

### 🔹 Continuous Features (Numeric)

```python
sns.boxplot(x='target', y='feature', data=df)
sns.kdeplot(data=df, x='feature', hue='target', common_norm=False)
```

* Use boxplots or KDEs to compare feature separation by class
* Assess if numeric predictors differ meaningfully between classes

### 🔹 Categorical Features

```python
pd.crosstab(df['feature'], df['target'], normalize='index').plot(kind='bar', stacked=True)
```

* Use stacked bar plots or heatmaps to compare class proportions

---

## 🔍 4. Feature Importance Exploration

### 🔹 Correlation Matrix (for numeric-only)

```python
sns.heatmap(df.corr(), cmap='coolwarm', annot=False)
```

### 🔹 Chi-Squared or Mutual Info (categorical vs target)

```python
from sklearn.feature_selection import mutual_info_classif
```

* Use for early screening of features when label is discrete

---

## 📦 5. Missingness and Preprocessing Flags

* [ ] Features with >30% missing reviewed
* [ ] Categorical variables encoded or grouped
* [ ] Cardinality checked (very high cardinality may need grouping)
* [ ] Potential data leakage fields flagged and excluded

---

## 📈 6. Linearity or Separability (for linear classifiers)

* [ ] Basic scatterplots for top features
* [ ] Pair plots grouped by class
* [ ] Optional: PCA/UMAP to check if data clusters by class

```python
from sklearn.decomposition import PCA
```

* Use for visualizing 2D class separability

---

## 🧩 7. Feature Interactions (Optional)

* [ ] Feature-feature scatterplots by class
* [ ] Cross-feature binned grouping (e.g., feature A ranges vs feature B categories)

---

## 📋 Analyst EDA Checklist for Classifiers

* [ ] Target label is clean and categorical
* [ ] Class imbalance noted (and strategy defined if needed)
* [ ] Feature distributions assessed by class
* [ ] Numeric features inspected for separation
* [ ] Categorical variables analyzed for group skew
* [ ] Key predictors and weak features identified
* [ ] PCA/UMAP used to assess broad structure (optional)
* [ ] Missing data and leakage reviewed

---

## 💡 Final Tip

> “Good classification starts with clean, interpretable classes and predictive features. Let structure—not algorithms—guide model design.”

Use this before: training logistic regression, tree-based classifiers, or ensemble models.
