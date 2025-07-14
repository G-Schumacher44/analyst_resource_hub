## 🎯 Purpose

Use this decision card to evaluate and decide how to handle flagged outliers — based on method of detection, severity, domain impact, and modeling goals.

---

## 🧪 1. Outlier Detection Techniques

| Method             | Use Case                          |
| ------------------ | --------------------------------- |
| Z-Score (>3)       | General flag for numeric features |
| IQR Rule (1.5×IQR) | Detects extreme high/low values   |
| Cook’s Distance    | Regression leverage + influence   |
| Domain Thresholds  | Based on known valid ranges       |

---

## ⚠️ 2. Decision Matrix

| Outlier Scenario                       | Suggested Action                             |
| -------------------------------------- | -------------------------------------------- |
| Z-Score between 3–5                    | Flag but keep (informative variation)        |
| Z-Score > 5 or implausible value       | Flag or set to NaN for review                |
| Cook’s D high & leverage high          | Flag row; consider robust regression         |
| Common placeholder outliers (9999, -1) | Convert to NaN and flag                      |
| Repeating junk value                   | Normalize or treat as structured missingness |

```python
# Z-Score example
from scipy.stats import zscore
z_scores = zscore(df['income'])
df['income_outlier_flag'] = (abs(z_scores) > 3)
```

---

## ⚖️ 3. Remove, Cap, or Flag?

| Condition                                      | Action                                 |
| ---------------------------------------------- | -------------------------------------- |
| Small % of true outliers with domain noise     | Flag only                              |
| Values are invalid (negative age, zero income) | Replace or drop                        |
| Feature heavily impacts model coefficients     | Try log transform or robust fit        |
| Highly skewed feature                          | Consider transformation before removal |

---

## 🧰 4. Transformation Options

| Transformation | Use Case                            |
| -------------- | ----------------------------------- |
| `np.log1p(x)`  | For long-tailed distributions       |
| Winsorization  | Cap values at upper/lower quantiles |
| Clipping       | Set min/max bounds manually         |

---

## ✅ Outlier Handling Checklist

* [ ] Detection method applied (Z, IQR, Cook’s D, etc.)
* [ ] Flag column created where needed
* [ ] Domain review for false flags or valid edge cases
* [ ] Strategy documented (flag/drop/transform)
* [ ] Post-action visual recheck (boxplot, hist)

---

## 💡 Tip

> “Don’t just delete outliers — investigate them. They often tell the real story.”
