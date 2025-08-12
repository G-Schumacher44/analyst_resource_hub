___
## 🎯 Purpose

Use this card to choose between **Naive Bayes (NB)** and **K-Nearest Neighbors (KNN)** for fast, interpretable classification — especially in early exploration or small-to-medium-sized projects.

---

## 📦 1. Model Comparison

| Model           | Key Feature                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| **Naive Bayes** | Probabilistic model using Bayes’ theorem with strong independence assumption |
| **KNN**         | Instance-based model using distance metrics and majority vote                |

---

## 🔍 2. When to Use Each

| Scenario                                                    | Best Model                          |
| ----------------------------------------------------------- | ----------------------------------- |
| Features are categorical or count-based (e.g., word counts) | ✅ Naive Bayes                       |
| Numeric, dense data where proximity makes sense             | ✅ KNN                               |
| Very small dataset (training speed needed)                  | ✅ Naive Bayes                       |
| You want local, example-driven decisions                    | ✅ KNN                               |
| You want fast inference at scale                            | ✅ Naive Bayes                       |
| You need class probability estimates                        | ✅ Both (KNN with `predict_proba()`) |

---

## ⚙️ 3. Performance Tradeoffs

| Factor           | Naive Bayes                | KNN                                        |
| ---------------- | -------------------------- | ------------------------------------------ |
| Training Time    | ✅ Extremely fast           | ✅ No training (lazy learner)               |
| Prediction Time  | ✅ Very fast                | 🔴 Can be slow (distance to all points)    |
| Interpretability | ✅ Moderate (probabilities) | 🟡 Local logic but less intuitive globally |
| Scaling Required | ❌ Not critical             | ✅ Mandatory for numeric features           |

---

## ✅ Decision Checklist

* [ ] Data type reviewed (categorical → NB, numeric → KNN)
* [ ] Feature independence considered (NB assumption)
* [ ] Scaling applied before KNN
* [ ] Performance vs interpretability needs clarified
* [ ] Class probabilities used responsibly in either model

---

## 💡 Tip

> “Use Naive Bayes when your data is text or tabular — use KNN when your data is shaped by space.”
