___
🎯 Purpose

This QuickRef provides a compact checklist and syntax guide for identifying structural and content issues during early data wrangling. It is ideal for validating schema alignment, type consistency, and common integrity flags before cleaning or transformation.

---

## 📦 1. Schema Snapshot & Type Review

```python
# Compare expected vs actual columns
expected_cols = ['id', 'age', 'date', 'gender']
assert set(df.columns) == set(expected_cols)

# Check types
schema = df.dtypes.to_dict()
```

✔️ Export `.dtypes` or save as YAML/JSON for schema audit
✔️ Use column order enforcement only if required

---

## 🔢 2. Type Coercion Checks

```python
# Numeric type coercion with fallback
pd.to_numeric(df['price'], errors='coerce')

# Convert to datetime
pd.to_datetime(df['start_date'], errors='coerce')

# Boolean flags
(df['flag_col'].astype('bool'))
```

✔️ Avoid silent failures — check for nulls after coercion
✔️ Always log column conversions for reproducibility

---

## ❓ 3. Unexpected Values & Format Checks

```python
# Unique and frequent values
for col in df.columns:
    print(df[col].value_counts(dropna=False).head())

# Regex pattern match
import re
df['zipcode'].str.match(r'^\d{5}$')
```

✔️ Use this to detect rogue entries, typos, and mixed formats (e.g. '12.5%', 'N/A', '-')

---

## 🧪 4. Logical Rule Violations (Cross-field)

```python
# Start date should be before end date
invalid_date_rows = df[df['start_date'] > df['end_date']]

# Quantity must be > 0 if order status = 'active'
df['invalid_qty'] = (df['status'] == 'active') & (df['qty'] <= 0)
```

✔️ Always create a Boolean flag for downstream QA or filtering
✔️ Use to catch high-risk row-level inconsistencies

---

## 🚧 5. Dirty Data Red Flags

* [ ] Unexpected nulls in primary keys or required fields
* [ ] Placeholder values like `-999`, `'N/A'`, `'?'`
* [ ] Columns with only 1 unique value (constant)
* [ ] Columns with unique values for every row (likely IDs)
* [ ] Duplicate rows or near-duplicates

---

## 🧾 6. Output & Logging Strategy

```python
# Save schema snapshot
schema = df.dtypes.to_dict()

# Save validation results
violations = df[['start_date', 'end_date', 'invalid_qty']]
violations.to_csv("validation_violations.csv", index=False)
```

✔️ Use structured logs for reproducibility + deployment readiness

---

## ✅ Mini Wrangling QA Checklist

* [ ] Schema matches expected columns and dtypes
* [ ] All coercions reviewed and logged
* [ ] Outlier values or typos detected
* [ ] Format rules enforced (e.g., date, ID, pattern)
* [ ] Logical rules applied (cross-field)
* [ ] Cleaning/export logs updated or saved

---

## 💡 Tip

> “Wrangling is not just about fixing — it’s about proving the data is ready to be trusted.”
