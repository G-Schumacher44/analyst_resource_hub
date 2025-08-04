___
## 🎯 Purpose

Use this card to choose the most appropriate clustering algorithm — **KMeans**, **DBSCAN**, **HDBSCAN**, or **Gaussian Mixture Models (GMM)** — based on your dataset’s structure, goals, and interpretability needs.

---

## 📦 1. When to Use Each Model

| Scenario                                                          | Best Model |
| ----------------------------------------------------------------- | ---------- |
| You want fast, scalable clustering with `k` known                 | ✅ KMeans   |
| You want automatic outlier detection and non-spherical clusters   | ✅ DBSCAN   |
| You want DBSCAN but with better performance on variable densities | ✅ HDBSCAN  |
| You want soft clustering with probability estimates               | ✅ GMM      |

---

## 🧪 2. Model Assumptions & Strengths

| Model   | Shape Assumed                 | Strengths                          |
| ------- | ----------------------------- | ---------------------------------- |
| KMeans  | Spherical, equal size         | Fast, simple, scalable             |
| DBSCAN  | Arbitrary shape, same density | Detects outliers, no `k` needed    |
| HDBSCAN | Arbitrary, variable density   | Better noise handling, soft labels |
| GMM     | Elliptical (Gaussian)         | Soft clustering, density modeling  |

---

## ⚠️ 3. When to Avoid

| Situation                               | Avoid...                                  |
| --------------------------------------- | ----------------------------------------- |
| High-dimensional sparse data            | DBSCAN (slow, unreliable)                 |
| Need explainability                     | GMM (less intuitive)                      |
| You don’t know `k` and can’t guess      | KMeans, GMM (require predefined clusters) |
| Clusters are non-Gaussian or non-convex | GMM (biased results)                      |

---

## ✅ Decision Checklist

* [ ] Are clusters expected to be well-separated and spherical? → Try **KMeans**
* [ ] Do you expect noise or arbitrary shapes? → Try **DBSCAN** or **HDBSCAN**
* [ ] Is cluster *density* varied across space? → Prefer **HDBSCAN**
* [ ] Do you need probabilistic (soft) clustering? → Use **GMM**
* [ ] Will you tune `k`? → Use **KMeans** or **GMM**

---

## 💡 Tip

> “Start with KMeans for speed. Switch to DBSCAN or HDBSCAN for shape. Reach for GMM when you want probabilities — or elegance.”
