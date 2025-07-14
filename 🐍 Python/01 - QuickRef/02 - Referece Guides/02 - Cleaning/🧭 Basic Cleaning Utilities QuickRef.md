___
🎯 Purpose

This QuickRef provides fast, reusable Pandas patterns for common cleaning operations — including whitespace fixes, missing value handling, value replacement, type coercion, and row filtering.

---

## 🧹 1. Column Cleaning

```python
# Strip whitespace from strings
df['name'] = df['name'].str.strip()

# Standardize case
df['email'] = df['email'].str.lower()

# Remove special characters
df['id_clean'] = df['id'].str.replace(r'[^A-Za-z0-9]', '', regex=True)

# Rename columns to lowercase
cols = [c.lower().strip().replace(' ', '_') for c in df.columns]
df.columns = cols
```

---

## 🔄 2. Value Replacement

```python
# Replace known bad entries
df['gender'] = df['gender'].replace({'M': 'male', 'F': 'female', '': np.nan})

# Replace multiple values in one go
df.replace(['?', 'NA', 'n/a'], np.nan, inplace=True)

# Map values
df['state_code'] = df['state'].map({'IL': 1, 'WI': 2, 'MI': 3})
```

---

## 🧪 3. Type Coercion

```python
# Convert to datetime
df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')

# Force numeric (invalid = NaN)
df['income'] = pd.to_numeric(df['income'], errors='coerce')

# Change categorical dtype
df['category'] = df['category'].astype('category')
```

---

## 🧼 4. Missing Value Handling

```python
# Count nulls
df.isnull().sum()

# Drop rows with nulls in any column
df.dropna()

# Drop rows with nulls in specific columns
df.dropna(subset=['email', 'age'])

# Fill nulls with median or constant
df['age'] = df['age'].fillna(df['age'].median())
df['city'] = df['city'].fillna('unknown')
```

---

## 📏 5. Row Filtering + Outlier Removal

```python
# Remove negative ages
df = df[df['age'] >= 0]

# Remove duplicates
df.drop_duplicates(inplace=True)

# Clip values to range
df['score'] = df['score'].clip(lower=0, upper=100)
```

---

## ✅ Cleaning Checklist

* [ ] Whitespace + case normalized
* [ ] Known bad strings replaced or mapped
* [ ] Types coerced safely with fallback
* [ ] Nulls filled, flagged, or dropped
* [ ] Outliers, negatives, and duplicates removed

---

## 💡 Tip

> “Start with a strip, replace, map, fillna, and you’ll already be ahead of 80% of dirty datasets.”
