___
## 🎯 Purpose

Use this decision card to determine whether a column should be kept, cleaned, dropped, or flagged — based on its uniqueness, value patterns, format consistency, and downstream importance.

---

## 🔍 1. Uniqueness Checks

| Column Type                           | Action                                                    |
| ------------------------------------- | --------------------------------------------------------- |
| Only 1 unique value                   | Drop — provides no variance                               |
| Mostly unique values (e.g. 1 per row) | Likely an ID — exclude from modeling, retain as reference |
| Very few unique values (<10)          | Review for categorical encoding                           |

```python
df.nunique().sort_values()
```

---

## 🔍 2. Format Problems

| Symptom                                             | Action                                         |
| --------------------------------------------------- | ---------------------------------------------- |
| Contains mix of `%`, `$`, or strings                | Normalize to numeric (use regex or `.replace`) |
| Long tail of weird strings (e.g. ‘N/A’, ‘–’, empty) | Coerce to `NaN`, flag for cleaning             |
| Case and whitespace mismatches                      | `.str.lower().str.strip()` fixable             |

---

## ⚠️ 3. Dirty Data Patterns

| Pattern                                         | Suggestion                              |
| ----------------------------------------------- | --------------------------------------- |
| Placeholders like `-999`, `'missing'`, `'na'`   | Convert to `np.nan` and document in log |
| Repeating junk (e.g. `'unknown', 'error', '—'`) | Clean or tag; consider drop if >50%     |
| Broken date formats                             | Try coercion, else flag or drop         |

```python
# Coerce and flag
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['bad_date_flag'] = df['date'].isnull()
```

---

## ⚖️ 4. Drop vs Clean Decision Rules

| If...                                                           | Then...                      |
| --------------------------------------------------------------- | ---------------------------- |
| Column has no variance                                          | Drop it                      |
| >50% missing AND not critical                                   | Drop OR document removal     |
| Values are repairable and used in model                         | Clean + log                  |
| Mixed types with no clear pattern                               | Drop, or flag for SME review |
| Derived from another field (e.g. duplicate of `price_per_unit`) | Drop or document as proxy    |

---

## ✅ Column Review Checklist

* [ ] Uniqueness profile reviewed
* [ ] Placeholders and bad entries standardized
* [ ] Mixed types normalized or removed
* [ ] Date/ID fields coerced or excluded from model
* [ ] Low-value or noisy columns dropped or documented

---

## 💡 Tip

> “A dirty column might be an error — or the most important red flag in the dataset. Always check before you drop.”
