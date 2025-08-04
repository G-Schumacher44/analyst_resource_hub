___
🎯 Purpose

This QuickRef covers **Naive Bayes Classifiers** — fast, probabilistic models ideal for text classification, categorical data, and scenarios where independence assumptions are tolerable.

---

## 📦 1. When to Use

| Condition                            | Use NB Classifier?         |
| ------------------------------------ | -------------------------- |
| You need fast, interpretable results | ✅ Yes                      |
| Text or count-based features         | ✅ Yes (use Multinomial NB) |
| Features are mostly categorical      | ✅ Yes                      |
| Strong feature interactions present  | ❌ Try trees or SVMs        |

---

## 🧮 2. Core Logic

* Based on Bayes' Theorem:

$$
P(y \mid x_1, x_2, ..., x_n) \propto P(y) \prod_{i=1}^n P(x_i \mid y)
$$

* Assumes conditional independence between features given the class label

---

## 🧪 3. Naive Bayes Variants

| Variant           | Use Case                                            |
| ----------------- | --------------------------------------------------- |
| **GaussianNB**    | Continuous data (assumes normal distribution)       |
| **MultinomialNB** | Text classification, word counts, discrete data     |
| **BernoulliNB**   | Binary features (e.g., presence/absence)            |
| **CategoricalNB** | Explicitly labeled categories (since sklearn v0.22) |

---

## 🛠️ 4. Fitting in sklearn

```python
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train, y_train)
```

```python
# For continuous features:
from sklearn.naive_bayes import GaussianNB
```

---

## 📊 5. Output Interpretation

| Output                    | Meaning                                  |
| ------------------------- | ---------------------------------------- |
| `model.class_log_prior_`  | Log prior of each class                  |
| `model.feature_log_prob_` | Log likelihood of each feature per class |
| `predict()`               | Predicted class label                    |
| `predict_proba()`         | Class probability estimates              |

---

## ⚠️ 6. Limitations

* Assumes **independence** between features — rarely true, but often effective
* Can be **overconfident** with highly correlated inputs
* Works best when features **map cleanly to likelihoods** (e.g., word counts)

---

## ✅ Checklist

* [ ] Feature type matched to NB variant (Gaussian, Multinomial, etc.)
* [ ] Categorical/binary features encoded cleanly
* [ ] Priors interpreted if class imbalance exists
* [ ] Assumptions of feature independence acknowledged
* [ ] Evaluation includes AUC or log loss if using probabilities

---

## 💡 Tip

> “Naive Bayes assumes the worst — and still often performs surprisingly well.”
