___
## 🎯 Purpose

Use this decision card to guide your early exploratory data analysis (EDA) decisions. It helps determine which tools, techniques, or visual strategies to apply based on data types, modeling goals, and time constraints.

---

## 🧱 1. EDA Entry Point

| If you...                              | Then start with...                         |
| -------------------------------------- | ------------------------------------------ |
| Just need a quick overview             | `df.info()`, `df.describe()`               |
| Are exploring a brand-new dataset      | Use full EDA checklist                     |
| Know your model type (regression, etc) | Run model-specific EDA checklist           |
| Have no idea what matters yet          | Profile all fields (types, nulls, uniques) |

---

## 🔍 2. Univariate Exploration

| Feature Type | Tool or Metric                    |
| ------------ | --------------------------------- |
| Numeric      | Histogram, boxplot, `.describe()` |
| Categorical  | Bar plot, `.value_counts()`       |
| Timestamp    | Time series plot, `.dt` accessor  |
| Text         | Length distribution, word clouds  |

✔️ Use `nunique()` to distinguish categorical vs ID vs freeform

---

## 📊 3. Bivariate + Relationship Checks

| Scenario                           | Use This                          |
| ---------------------------------- | --------------------------------- |
| 2 numeric vars                     | Scatterplot, correlation matrix   |
| 1 cat + 1 numeric                  | Groupby summary, barplot, boxplot |
| 2 categorical                      | Crosstab, stacked bar plot        |
| Large categorical with many levels | Consider grouping rare categories |

---

## ⚖️ 4. Depth of Analysis: How Deep Should You Go?

| Goal                         | Strategy Tier                          |
| ---------------------------- | -------------------------------------- |
| Just checking data health    | Basic EDA QuickRef + visual scan       |
| Prepping for linear model    | Add: skew check, correlation, outliers |
| Prepping for clustering      | Add: PCA/UMAP, pairplots, scale check  |
| Research or publishable work | Full EDA guide + advanced visuals      |

✔️ Use checklist levels to right-size your time investment

---

## 🧠 5. Transformation Triggers (Early Flags)

| Flag                     | Suggestion                        |
| ------------------------ | --------------------------------- |
| Skew > ±1                | Log/sqrt or Yeo-Johnson transform |
| Missing > 20%            | Plan for imputation or drop       |
| Correlation > 0.85       | Review for redundancy             |
| Flat or constant columns | Consider dropping                 |

---

## ✅ EDA Strategy Checklist

* [ ] Dataset type and goals clarified
* [ ] Data types, nulls, and uniques checked
* [ ] Univariate visuals reviewed
* [ ] Relationships explored where needed
* [ ] Transformation needs flagged early

---

## 💡 Tip

> “The purpose of EDA isn’t just inspection — it’s preparation for better decisions.”
