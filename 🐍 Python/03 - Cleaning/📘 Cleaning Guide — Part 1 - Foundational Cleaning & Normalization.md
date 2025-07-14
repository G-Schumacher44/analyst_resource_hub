___
## 🎯 Purpose

This guide covers the essential, reusable tasks for turning raw or semi-structured data into an analysis-ready form. It is the first step in building clean, reliable datasets for exploratory analysis, early-stage modeling, and pipeline integration.

---

## 📦 1. Schema + Structure Alignment

### 🔹 Confirm dataset structure

```python
df.shape  # (rows, columns)
df.columns
```

* Validate column count, presence, and order
* Compare against expected schema or dictionary

### 🔹 Data types check

```python
df.dtypes
df.info()
```

✔️ Log non-numeric fields or object types that require conversion

---

## 🔢 2. Data Type Enforcement

### Common fixes:

* `object → string / category`
* `object → datetime`
* Coerce numerics from symbols (`$`, `%`, etc.)

### Example:

```python
df['price'] = pd.to_numeric(df['price'].replace('[\$,]', '', regex=True))
df['date'] = pd.to_datetime(df['date'], errors='coerce')
```

✔️ Explicitly cast booleans, integers, and categories

---

## 🧹 3. Value Normalization

### Text Cleanup

* Strip whitespace, unify case, replace typos/symbols

```python
df['city'] = df['city'].str.strip().str.lower()
```

### Numeric Fixes

* Coerce currency, percentages, bad encodings
* Handle placeholder outliers (e.g. -999)

### Common Tools:

```python
.str.strip(), .str.replace(), pd.to_numeric(), .astype()
```

---

## 🧾 4. Missing Data Handling

### 🔹 Diagnostics

```python
df.isnull().sum()
df.isnull().mean().sort_values(ascending=False)
```

### 🔹 Imputation Strategies

| Type        | Strategy                   |
| ----------- | -------------------------- |
| Numeric     | Mean / Median fill         |
| Categorical | Mode or "Missing" token    |
| Timestamp   | Use time reference or flag |

```python
df['age'] = df['age'].fillna(df['age'].median())
df['gender'] = df['gender'].fillna('Missing')
```

✔️ Track imputed fields with binary flags if needed

---

## 📏 5. Outlier Detection (Light)

### 🔹 Z-score or IQR-based detection

```python
from scipy.stats import zscore
z = np.abs(zscore(df.select_dtypes(include='number')))
```

✔️ Flag (not drop) unless critical

---

## 📊 6. Categorical Grouping

### 🔹 Group rare categories

```python
freq = df['industry'].value_counts(normalize=True)
df['industry'] = df['industry'].where(freq > 0.01, 'Other')
```

✔️ Use before encoding to reduce cardinality
✔️ Review business logic to preserve interpretability

---

## 📋 Analyst Checklist — Part 1

* [ ] Column names and schema matched
* [ ] Dtypes checked and enforced
* [ ] Currency / text normalized
* [ ] Missingness reviewed and imputed
* [ ] Z-score or IQR outliers flagged
* [ ] Categorical levels grouped if needed
* [ ] Dataset exported or copied to validated layer

---

## 💡 Final Tip

> “Part 1 cleaning is your analysis launchpad — focus on clarity, consistency, and low-risk fixes.”

Use this before: EDA, feature engineering, or modeling prep. Pair with: Validation Guide, Transformation Guide, and Cleaning Guide — Part 2.
