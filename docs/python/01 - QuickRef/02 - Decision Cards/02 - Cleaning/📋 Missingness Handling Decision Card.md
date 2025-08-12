___
## 🎯 Purpose

Use this card to decide how to handle missing values — whether to drop, impute, or flag — based on the type of missingness, percent nulls, and modeling implications.

---

## 🔍 1. Classify the Missingness

| Type     | Description                               | Action                               |
| -------- | ----------------------------------------- | ------------------------------------ |
| **MCAR** | Missing Completely At Random              | Safe to drop or mean/median impute   |
| **MAR**  | Missing At Random (depends on other vars) | Impute using correlated fields, flag |
| **MNAR** | Missing Not At Random (systematic)        | Avoid silent fill; flag and document |

✔️ Use groupby, domain logic, or visual patterns to infer MAR/MNAR

---

## 📊 2. Threshold-Based Drop/Impute Rules

| % Missing | Recommended Action                           |
| --------- | -------------------------------------------- |
| < 5%      | Drop rows or impute (safe)                   |
| 5–30%     | Impute with flag (especially MAR)            |
| > 30%     | Assess necessity — drop if low importance    |
| > 50%     | Usually drop unless core to target or domain |

```python
# Flag before filling
df['income_flag'] = df['income'].isnull()
df['income'] = df['income'].fillna(df['income'].median())
```

---

## 🧪 3. Strategy by Column Type

| Type        | Preferred Strategy                             |
| ----------- | ---------------------------------------------- |
| Numeric     | Median, regression, KNN imputation             |
| Categorical | Mode, 'Missing' tag, frequency-based fill      |
| Dates       | Interpolation, median by group, drop if sparse |
| Identifiers | Never impute — drop or flag                    |

✔️ Always log imputation strategy + flag when filling

---

## ✅ Decision Checklist

* [ ] % nulls calculated and reviewed
* [ ] Cause of missingness identified or inferred (MCAR/MAR/MNAR)
* [ ] Strategy documented per column
* [ ] Imputation flags created for critical fields
* [ ] Columns >50% missing either dropped or justified

---

## 💡 Tip

> “Don’t just fill in the blanks. Every null is a clue.”
