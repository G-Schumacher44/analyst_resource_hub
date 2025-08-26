---
## 🎯 Purpose

This QuickRef outlines reusable logic for validating incoming datasets before modeling. Includes type checks, schema alignment, range tests, and conditional rules — suitable for notebooks or production pipelines.

---

## 📦 1. When to Run Validation

| Trigger           | Use Case                                                |
| ----------------- | ------------------------------------------------------- |
| After data load   | Ensure input structure and column names are as expected |
| After cleaning    | Confirm transformations didn’t break expectations       |
| Before modeling   | Catch missingness, bad encodings, or type issues        |
| Before deployment | Validate stability of incoming data feeds               |

---

## 🧪 2. Schema Validation

```python
expected_schema = {
    'age': 'int',
    'gender': 'category',
    'income': 'float',
    'signup_date': 'datetime64[ns]'
}

for col, expected_type in expected_schema.items():
    if col not in df.columns:
        logger.warning(f"Missing column: {col}")
    elif not pd.api.types.is_dtype_equal(df[col].dtype, expected_type):
        logger.warning(f"Type mismatch: {col}")
```

✔️ Log mismatches and optionally halt based on criticality

---

## 📊 3. Range Checks & Allowable Values

```python
# Numeric ranges
assert df['age'].between(0, 120).all(), "Age out of bounds"

# Categorical sets
valid_genders = {'male', 'female', 'other'}
assert set(df['gender'].dropna().unique()).issubset(valid_genders)
```

✔️ Flag out-of-domain entries for audit or cleaning rerun

---

## ⚠️ 4. Null + Duplication Checks

```python
null_report = df.isnull().sum()
if null_report.any():
    logger.info("Missing values detected:")
    print(null_report[null_report > 0])

# Duplicate row check
duplicates = df.duplicated().sum()
if duplicates:
    logger.warning(f"Duplicate rows: {duplicates}")
```

---

## 🔁 5. Cross-field Rules

```python
# Example: signup_date must be before last_activity
assert (df['signup_date'] <= df['last_activity']).all()
```

✔️ Add business logic rules per field pair or group

---

## ✅ Validation Checklist

* [ ] Schema and data types verified
* [ ] Required columns present
* [ ] Value ranges and categories confirmed
* [ ] Nulls and duplicates reviewed
* [ ] Cross-field constraints validated
* [ ] Logger or report generated for each run

---

## 💡 Tip

> “Validation is where silent bugs go to die — before they poison your models.”
