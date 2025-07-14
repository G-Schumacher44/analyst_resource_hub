___
## 🎯 Purpose

Use this checklist to ensure that datasets meet integrity standards for downstream modeling, publication, or deployment. It supports rule-based validation, field logic enforcement, and audit-driven documentation.

---

## 🔒 Schema Integrity

* [ ] Column set matches schema or data dictionary
* [ ] Dtypes match specification (e.g. `datetime`, `category`, `int64`)
* [ ] Column order (if required) verified
* [ ] Schema snapshot saved before and after cleaning

---

## 🛡 Field-Level Validation

* [ ] All numeric bounds enforced (e.g. `age ∈ [0, 120]`)
* [ ] All categorical values validated against allowed set
* [ ] Text pattern formats enforced (e.g. ZIP, phone, email regex)
* [ ] Validation flags (`*_invalid`) added for each rule type

---

## 🔗 Cross-Field Logic

* [ ] Temporal rules applied (e.g. `start_date < end_date`)
* [ ] Conditional logic verified (e.g. `if status = active → qty > 0`)
* [ ] Multi-column consistency rules flagged and logged
* [ ] Row-level `valid_row` or `row_flag` column created (optional)

---

## 🧪 Imputation QA

* [ ] All imputations explicitly logged
* [ ] Imputed fields flagged with binary indicators (`*_imputed_flag`)
* [ ] Strategy consistent with Part 1 or domain logic
* [ ] Imputation documented in cleaning notes or metadata

---

## 🚨 Outlier & Exception Logging

* [ ] Outliers reviewed per field (z-score, IQR, domain limits)
* [ ] Outlier records exported or logged
* [ ] Manual decisions flagged (`*_override`) if applicable

---

## 🧾 Audit Trail & Logging

* [ ] Cleaning steps documented in JSON/YAML log
* [ ] Rule violations summarized by field
* [ ] All logic flags exported with dataset
* [ ] Version number, timestamp, and hash recorded (if versioning system is in use)

---

## 💾 Final Save + Review

* [ ] Dataset saved in approved format (e.g. `.csv`, `.parquet`)
* [ ] Flags and logs attached or merged
* [ ] Cleaning metadata saved separately if needed

---

## 🧠 Final Tip

> “Advanced cleaning isn’t about removing errors — it’s about proving the dataset can be trusted.”
