___
## 🎯 Purpose

This QuickRef helps you design and maintain structured logs for your cleaning and wrangling steps. Use these logs to track changes, support audits, or build reproducible pipelines.

---

## 🗂 1. What to Log

| Item                | Example                                   |
| ------------------- | ----------------------------------------- |
| Schema snapshot     | `df.dtypes.to_dict()` or YAML structure   |
| Missing value logic | "filled 'age' with median + created flag" |
| Coercions           | "'price' → float, 'date' → datetime"      |
| Outlier flags       | "Z-score > 3 → flagged, not dropped"      |
| Column drops        | "Dropped 'temp\_id' due to >60% nulls"    |
| Cross-field rules   | "start\_date < end\_date enforced"        |
| Validation fails    | Export of row-level flags                 |

---

## 📄 2. YAML Format Template

```yaml
dataset: customer_q2.csv
date_cleaned: 2025-05-14
cleaning_steps:
  - schema_snapshot:
      id: int64
      age: float64
      signup_date: datetime64[ns]
  - imputation:
      age: median_fill
      gender: filled with 'Missing'
  - dropped:
      - temp_id
  - type_coercion:
      price: string → float
      signup_date: object → datetime
  - outliers:
      z_score_threshold: 3
      flagged_fields: ['income', 'quantity']
  - cross_field_rules:
      - rule: start_date < end_date
        violations_flagged: 82 rows
```

✔️ Use this format for Git-tracked datasets or ML pipelines

---

## 📊 3. Markdown Log Template (Notebook-Friendly)

```markdown
### 🧼 Cleaning Log — customer_q2.csv
**Date:** 2025-05-14  
**Analyst:** Garrett

#### ✅ Schema
- `id`: int → OK  
- `price`: object → float ✅

#### 🔄 Coercions
- `'price'` converted using regex clean → float
- `'signup_date'` parsed as datetime

#### ❓ Missingness
- `age`: 12% null → filled with median + `age_imputed` flag
- `gender`: 6% null → filled with 'Missing'

#### 🚧 Outliers
- `income`, `duration` → Z-score > 3 flagged

#### 🧪 Cross-Field Rules
- `start_date < end_date`: 82 violations → flagged in `date_flag`

#### ❌ Dropped Columns
- `temp_id` dropped (>60% nulls)
```

---

## 💾 4. Export + Versioning

| Format  | Use Case                               |
| ------- | -------------------------------------- |
| `.yaml` | Structured logs in pipeline repos      |
| `.json` | API or automation integrations         |
| `.md`   | Notebook reports / versioned snapshots |
| `.csv`  | Row-level QA exports                   |

---

## ✅ Logging Checklist

* [ ] Schema snapshot saved
* [ ] All coercions documented
* [ ] Null fill methods + flags recorded
* [ ] Outliers flagged and noted (not just removed)
* [ ] Cross-field rules logged
* [ ] Export format versioned and saved

---

## 💡 Tip

> “If your cleaning logic isn’t logged, your dataset isn’t trustworthy.”
