___
## 🎯 Purpose

Use this checklist to verify that a dataset is structurally clean, minimally transformed, and ready for exploratory analysis or early-stage modeling.

---

## 📦 Structural Review

* [ ] Columns match expected schema or dictionary
* [ ] Row and column count is as expected
* [ ] Column names are standardized (no hidden whitespace or case mismatch)

---

## 🔢 Data Type Enforcement

* [ ] All numeric fields are numeric (`int`, `float`)
* [ ] Datetime fields parsed and coerced to datetime type
* [ ] Boolean flags cast from string/object to `bool`
* [ ] Object columns reviewed for misclassification (e.g. encoded numerics)

---

## 🧹 Value Normalization

* [ ] String fields cleaned (whitespace, case, symbols)
* [ ] Currency / % fields converted to numeric
* [ ] Placeholder error values handled (e.g. `-999`, `N/A`, `'missing'`)

---

## ❓ Missing Data Handling

* [ ] Missing value summary created and reviewed
* [ ] Light imputation applied (mean, median, mode, constant)
* [ ] Optional: imputed values flagged (`*_imputed`)

---

## 📏 Outlier Detection

* [ ] Z-score or IQR flags created for numeric features
* [ ] Outliers noted or flagged but not removed unless justified

---

## 📦 Categorical Handling

* [ ] High-cardinality variables reviewed
* [ ] Rare levels grouped (e.g. “Other” if <1–5%)
* [ ] Text categories standardized (case, whitespace, punctuation)

---

## 💾 Dataset Savepoint

* [ ] Cleaned dataset exported or saved as new version
* [ ] Notes taken on changes from original
* [ ] Prepared for use in EDA, transformation, or modeling steps

---

## 🧠 Final Tip

> “Foundational cleaning gets the dataset aligned and safe to explore — without breaking assumptions or burying problems.”
