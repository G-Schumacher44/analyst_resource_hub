___
## 🎯 Purpose

This guide consolidates all critical tasks for cleaning, validating, and preparing structured and semi-structured data before analysis or modeling. It supports pipeline-ready workflows and schema-compliant data management across EDA, ML, and deployment.

---

## 📦 1. Initial Structural Review

### 🔹 Shape and Schema Alignment

```python
df.shape  # (rows, columns)
df.columns
df.info()
```

* Confirm row/column counts against expectations
* Check column presence, order, and spelling

### 🔹 Basic Summary Overview

```python
df.describe(include='all').T
```

* Detect constant fields, unexpected types, empty categories

✔️ Save schema snapshot or comparison log for pipeline consistency

---

## 🔢 2. Data Type and Conversion Review

| Type         | Action Needed                                  |
| ------------ | ---------------------------------------------- |
| `object`     | Detect true type (category, date, ID)          |
| `float64`    | Check for rounding issues, missingness         |
| `int64`      | Watch for encoding, special flags (e.g., -999) |
| `bool`       | Confirm logic vs stringified booleans          |
| `datetime64` | Parse formats, detect tz-aware timestamps      |

### Snippet:

```python
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['flag'] = df['flag'].astype('bool')
```

✔️ Log all casting and dtype overrides

---

## 🧹 3. Value Normalization and Cleaning

### 🔹 Standard Cleaning Tasks

* Strip whitespace
* Lowercase strings / apply title case
* Remove symbols (`$`, `%`, `#`, etc.)
* Parse mixed-format numerics (e.g., `$1,200.00` → 1200.0)

```python
df['name'] = df['name'].str.strip().str.lower()
df['cost'] = df['cost'].replace('[\$,]', '', regex=True).astype(float)
```

✔️ Ensure consistent formatting across columns and rows

---

## 🧪 4. Missing Data Review

### 🔹 Diagnostics

```python
df.isnull().sum()
df.isnull().mean().sort_values(ascending=False)
```

### 🔹 Strategy Options

| Case                              | Suggested Strategy               |
| --------------------------------- | -------------------------------- |
| < 5% missing                      | Drop or fill with median/mode    |
| > 30% missing                     | Consider column drop             |
| Patterned missingness (MNAR, MAR) | Flag + model-based imputation    |
| Isolated categorical gaps         | Fill with "Missing" or new label |

✔️ Always report imputation logic in data dictionary or logs

---

## 📏 5. Validation Rule Checks

| Rule Type          | Example                                           |
| ------------------ | ------------------------------------------------- |
| Allowed values     | `state ∈ ['CA', 'NY', 'TX']`                      |
| Value range bounds | `age ∈ [0, 120]`, `revenue >= 0`                  |
| Format constraints | Regex for emails, phone, postal codes             |
| Cross-field logic  | `start_date < end_date`, `qty > 0 if ordered = 1` |

### Snippet:

```python
df['valid_age'] = df['age'].between(0, 120)
df['flag_invalid_state'] = ~df['state'].isin(valid_states)
```

✔️ Build reusable validation functions and triggers for logging

---

## 🔁 6. Categorical Review and Encoding Prep

### 🔹 Cardinality and Balance

```python
df['category'].value_counts(normalize=True)
df['category'].nunique()
```

✔️ Group rare levels as "Other" when frequency < 1–5%
✔️ Use ordinal vs one-hot vs target encoding as appropriate

---

## 📐 7. Outlier Handling and Flagging

### 🔹 Visual and Statistical Detection

* Boxplots, histograms, scatterplots
* Z-score, IQR range check, MAD (robust)

```python
from scipy.stats import zscore
outliers = (np.abs(zscore(df['feature'])) > 3)
```

✔️ Create outlier flag column for traceability
✔️ Avoid automatic deletion without business logic

---

## 🧾 8. Schema and Audit Logging

| Task                        | Tool / Method                    |
| --------------------------- | -------------------------------- |
| Capture schema snapshot     | `df.dtypes.to_dict()`            |
| Save pre/post cleaning diff | Use `deepdiff`, `pandas-diff`    |
| Add processing metadata     | Log source, date, imputer, notes |

✔️ Use structured metadata tracking per versioned dataset

---

## 📋 Master Wrangling + Validation Checklist

* [ ] Column names + schema confirmed
* [ ] Dtypes explicitly validated and cast
* [ ] Missingness reviewed + handling strategy applied
* [ ] Strings/numbers parsed + normalized
* [ ] Outliers flagged and/or handled
* [ ] Categorical levels grouped and encoded
* [ ] Validation rules checked (range, format, logic)
* [ ] Schema snapshot or cleaning log saved

---

## 💡 Final Tip

> “Wrangling is not just cleanup — it’s structure, strategy, and traceability. Build once, validate always.”

Use before: Feature engineering, EDA, ML pipelines, or schema release.
