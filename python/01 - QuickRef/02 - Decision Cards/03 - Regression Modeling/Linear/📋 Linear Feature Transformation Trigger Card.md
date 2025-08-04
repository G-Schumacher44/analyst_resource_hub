___
## 🎯 Purpose

Use this card to determine when to apply feature transformations (e.g. log, sqrt, power, binning) before running a linear regression model. Helps identify skewed or nonlinear predictors that may violate model assumptions or degrade performance.

---

## 🔍 1. When to Transform Features

| Condition                         | Suggestion                          |
| --------------------------------- | ----------------------------------- |
| Skewness > ±1                     | Use log or sqrt transform           |
| Heteroskedasticity observed       | Log/sqrt to stabilize variance      |
| Long-tailed distribution          | Consider log or Box-Cox/Yeo-Johnson |
| X vs Y non-linear                 | Try polynomial or log(X) variants   |
| Zero-inflated or boundary effects | Apply binning or thresholding       |

```python
from scipy.stats import skew
skew(df['income'])  # > 1 → log candidate
```

---

## 🧪 2. Visual Triggers

| Visual                         | Transformation Cue                     |
| ------------------------------ | -------------------------------------- |
| Histogram with long right tail | Log or sqrt                            |
| Residual plot shows fan shape  | Variance-stabilizing transform         |
| X vs Y: curvature in scatter   | Poly features or log(X)                |
| Extreme outliers (Z > 3)       | Consider robust scale or winsorization |

---

## ⚖️ 3. Transformation Options

| Method              | Use When...                                         |
| ------------------- | --------------------------------------------------- |
| `np.log1p(X)`       | Right-skewed + zero values present                  |
| `np.sqrt(X)`        | Moderate skew, non-negative                         |
| `power_transform()` | General normalizer (Box-Cox or YJ)                  |
| `StandardScaler`    | When model is sensitive to scale (esp. Ridge/Lasso) |

✔️ Scale after transforming, especially if using regularized models

---

## ✅ Transformation Checklist

* [ ] Skew > ±1 or kurtosis > 3 reviewed
* [ ] Visual cues support transformation
* [ ] Chosen method appropriate for data range
* [ ] Post-transform distribution checked
* [ ] Feature scaling applied after transformation

---

## 💡 Tip

> “Linear models love smooth, symmetric input. If your predictors are shouting, transformation helps them whisper.”
