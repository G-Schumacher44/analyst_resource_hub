___
## 🎯 Purpose

This decision card helps analysts choose the most appropriate clustering method based on data characteristics, project goals, and modeling constraints. Use it during early-stage exploration, segmentation design, or stakeholder alignment.

---

## ⚙️ Step 1: Problem Characteristics

| Question                                             | If Yes... | Then Consider...                       |
| ---------------------------------------------------- | --------- | -------------------------------------- |
| Are clusters expected to be spherical/equally sized? | ✅         | K-Means, GMM                           |
| Is there significant noise or outliers?              | ✅         | DBSCAN, HDBSCAN                        |
| Do clusters vary in density or size?                 | ✅         | HDBSCAN, OPTICS                        |
| Should cluster shape be non-convex?                  | ✅         | Spectral, DBSCAN                       |
| Do you expect overlapping clusters?                  | ✅         | GMM (soft assignments)                 |
| Is interpretability or hierarchy required?           | ✅         | Hierarchical, Agglomerative Clustering |
| Is the dataset large (10k+ rows)?                    | ✅         | K-Means, MiniBatchKMeans               |
| Is the data mixed or categorical?                    | ✅         | K-Medoids, specialized encoders        |

---

## 🧰 Step 2: Model Preference Guide

| Preference                  | Recommended Models               |
| --------------------------- | -------------------------------- |
| 🔎 Interpretability         | K-Means, Hierarchical, K-Medoids |
| 🌐 Irregular boundaries     | DBSCAN, Spectral, HDBSCAN        |
| 🔀 Overlapping groups       | GMM (Gaussian Mixture Model)     |
| 🧱 Density-based logic      | DBSCAN, HDBSCAN, OPTICS          |
| 🔁 No need to predefine `k` | DBSCAN, HDBSCAN, Hierarchical    |
| ⚡️ Speed on large sets      | K-Means, MiniBatchKMeans         |

---

## 📊 Step 3: Validation Strategy by Model

| Model Type   | Suggested Validation Methods               |
| ------------ | ------------------------------------------ |
| K-Means      | Elbow, Silhouette, CH Index                |
| GMM          | Log-Likelihood, BIC, Silhouette            |
| DBSCAN       | Cluster count, noise %, visual inspection  |
| HDBSCAN      | Soft probabilities, cluster stability plot |
| Hierarchical | Dendrogram, Cophenetic Correlation         |
| Spectral     | Silhouette, visual structure via UMAP      |

---

## 📎 Step 4: Visual Aids for Stakeholders

| Goal                         | Visual                                |
| ---------------------------- | ------------------------------------- |
| Show cluster separation      | PCA / UMAP scatter with cluster color |
| Compare cluster quality      | Silhouette plot                       |
| Show feature patterns        | Heatmaps, radar plots                 |
| Show relative size           | Bar charts, pie charts                |
| Map clusters to known groups | Overlay plot or confusion matrix      |

---

## 🧠 Final Reminders

* There is **no one true clustering solution** — test multiple methods.
* Use both **quantitative metrics** and **domain insight** to validate clusters.
* Always include visual evidence when presenting clusters.

Use this decision card alongside the Clustering Evaluation Checklist and Visual Guide to support structured, flexible analysis.
