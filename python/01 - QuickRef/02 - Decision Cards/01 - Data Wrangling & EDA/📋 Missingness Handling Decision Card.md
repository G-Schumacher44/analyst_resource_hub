___
## 🎯 Purpose

Use this card to decide whether to drop, flag, or impute missing values — based on quantity, cause, downstream impact, and modeling goals.

---

## 🔍 1. Estimate Severity

```python
# Basic missingness check
df.isnull().sum()
df.isnull().mean() * 100
```

| Rule of Thumb | Action                             |
| ------------- | ---------------------------------- |
| < 5% missing  | Safe to drop or fill silently      |
| 5–30% missing | Flag or impute, especially for MAR |
| > 30% missing | Assess necessity or drop field     |
| > 50% missing | Usually drop unless critical       |

---

## 🔎 2. Identify the Pattern

| Pattern Type | Description                             | Common Actions                          |
| ------------ | --------------------------------------- | --------------------------------------- |
| **MCAR**     | Missing Completely At Random            | Drop or fill with mean/median           |
| **MAR**      | Missing At Random (based on other vars) | Impute + flag or model conditionally    |
| **MNAR**     | Not At Random (systematic loss)         | Flag, impute cautiously, document cause |

✔️ Use `groupby` or visuals to detect MAR/MNAR patterns

---

## ⚖️ 3. Choose an Action Path

| If...                                  | Then...                                                 |
| -------------------------------------- | ------------------------------------------------------- |
| Field is missing randomly and <10%     | Drop or impute with mean/median                         |
| Missingness depends on another feature | Use model-based imputation or conditional fill          |
| Field is categorical with few values   | Impute with mode or add "Missing" label                 |
| Field is an ID or timestamp            | Do not impute — review or flag separately               |
| Field is critical and >30% missing     | Document and impute with caution, or exclude from model |

---

## 🧪 4. Flagging Best Practice

```python
# Before filling
df['income_flag'] = df['income'].isnull()
df['income'] = df['income'].fillna(df['income'].median())
```

✔️ Always flag imputed values for auditing and regression testing

---

## ✅ Decision Checklist

* [ ] % missing calculated and pattern explored
* [ ] Cause assessed (MCAR, MAR, MNAR)
* [ ] Column role evaluated (target, input, ID)
* [ ] Chosen imputation/drop method documented
* [ ] Optional: flag column created for auditability

---

## 💡 Tip

> “Not all nulls are noise. Sometimes they’re the most informative signal in the dataset.”
