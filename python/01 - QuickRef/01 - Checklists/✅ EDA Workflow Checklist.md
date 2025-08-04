___

_A companion to the [[General EDA Guidebook]], [[📊 Visual EDA Interpretation Guide]], and [[📘 Advanced EDA Guidebook]]
---

## 📦 1. Dataset Structure
- [ ] `.shape`, `.info()` — Dimensions & column types
- [ ] `.describe(include='all')` — Descriptive stats
- [ ] `.duplicated().sum()` — Check for row duplication
- [ ] `.memory_usage()` — Memory optimization

---

## 🔍 2. Variable Exploration

### Numeric
- [ ] Histograms + KDE
- [ ] Skew, kurtosis
- [ ] Outlier detection (boxplot, z-score, IQR)

### Categorical
- [ ] Frequency counts
- [ ] Unique counts / high cardinality flags
- [ ] Encoding strategy (if needed)

---

## 📈 3. Distribution & Relationship Plots
- [ ] Boxplot by category
- [ ] Correlation heatmap (numeric only)
- [ ] Pairplot or scatter matrix
- [ ] Crosstabs (for categorical pairs)

---

## 🧪 4. Missing Values
- [ ] `df.isnull().sum()` summary
- [ ] Heatmap of missingness
- [ ] Consider: drop, fill, predictive imputation

---

## 📉 5. Outliers
- [ ] IQR filtering
- [ ] Z-score filtering
- [ ] Context/domain filtering (caps/floors)

---

## 🔁 6. Scaling & Transformation
- [ ] Log/sqrt transforms for skew
- [ ] StandardScaler, MinMaxScaler, RobustScaler

---

## 🧠 7. Feature Engineering (Optional)
- [ ] Bin continuous vars (if needed)
- [ ] Polynomial or interaction terms
- [ ] Flag rare categories or consolidate groups

---

## 🧹 8. Pre-Model Cleanup
- [ ] Drop ID / index / time features if not useful
- [ ] Recheck all dtypes
- [ ] Align feature set with model goals

---

Ready to export to modeling script or notebook? ✅