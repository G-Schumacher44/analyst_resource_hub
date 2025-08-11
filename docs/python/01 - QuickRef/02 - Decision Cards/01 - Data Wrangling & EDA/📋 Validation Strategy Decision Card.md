___
## 🎯 Purpose

Use this card to decide how your pipeline should respond to data validation failures — including schema mismatches, range violations, nulls, and business rule failures.

---

## 🚦 1. Strategy Options

| Strategy                    | When to Use                                                                |
| --------------------------- | -------------------------------------------------------------------------- |
| **Log + Continue**          | Non-critical fields, exploratory analysis, or early data access            |
| **Flag + Route for Review** | Potentially important violations where human review is needed before rerun |
| **Auto-Fix + Continue**     | Known, low-risk fixes (e.g., date parsing, inferred types)                 |
| **Abort + Fail**            | Critical fields missing, schema misaligned, unfixable integrity issues     |

---

## 🧪 2. Failure Categories

| Failure Type                     | Typical Action                         |
| -------------------------------- | -------------------------------------- |
| Missing column                   | 🔴 Abort or Flag                       |
| Type mismatch (e.g., str vs int) | 🟡 Auto-fix or Flag                    |
| Range or domain violation        | 🟡 Flag or Log                         |
| Nulls in required field          | 🔴 Abort or 🟡 Flag (if imputable)     |
| Cross-field logic fails          | 🔴 Abort or Flag depending on severity |

---

## 🛠️ 3. Implementing Strategy

```python
if column_missing:
    logger.error("Abort: Required column 'age' missing")
    sys.exit(1)  # Fails hard

elif invalid_category:
    logger.warning("Flag: Unknown gender detected")
    flagged_rows.append(record_id)

elif dtype_fixable:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    logger.info("Autofix: Date parsing applied")
```

---

## ✅ Decision Checklist

* [ ] Severity of violation evaluated
* [ ] Field or rule mapped to strategy (log, flag, abort)
* [ ] Logs or alerts routed to analyst or pipeline monitor
* [ ] Fix logic implemented where safe (type coercion, domain re-mapping)
* [ ] Stop logic enforces critical schema dependencies

---

## 💡 Tip

> “Fail loudly for core fields. Flag gently for edge cases. Always log everything in between.”
