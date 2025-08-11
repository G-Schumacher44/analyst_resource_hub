___
🎯 Purpose

This guide deepens the visual analysis of linear regression models by incorporating diagnostics for assumption testing, robustness, and model complexity. It extends the standard visual evaluation companion and supports high-quality model QA and reporting.

---

## 📊 1. Actual vs Predicted (Model Fit Check)

**Goal:** Evaluate prediction accuracy and potential bias.

✔️ Look for tight clustering around the 45° line.
⚠️ Curvature or separation suggests underfitting or omitted variables.

```python
sns.scatterplot(x=y_test, y=y_pred)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
```

---

## 📉 2. Residuals vs Fitted (Homoscedasticity)

**Goal:** Validate constant variance and check for patterning.

✔️ Cloud-like spread = good.
⚠️ Funnel shape = heteroscedasticity.
⚠️ Curve = nonlinear trend not captured.

```python
sns.scatterplot(x=y_pred, y=residuals)
plt.axhline(0, color='red', linestyle='--')
```

---

## 📁 3. Histogram of Residuals (Normality Check)

**Goal:** Test if residuals are bell-shaped (assumption for inference).

✔️ Smooth bell curve = OK.
⚠️ Skew, multiple peaks = assumption violated.

```python
sns.histplot(residuals, kde=True)
```

---

## 📋 4. QQ Plot (Normality Diagnostic)

**Goal:** Quantify deviation from normal distribution.

✔️ Points on line = good.
⚠️ S-curve = skewed; tails = outliers or heavy-tailed errors.

```python
sm.qqplot(residuals, line='45')
```

---

## 🧪 5. Scale-Location Plot

**Goal:** Detect non-constant variance (more sensitive than residuals plot).

✔️ Flat horizontal band = homoscedastic.
⚠️ Upward curve = residuals increasing with fitted value.

```python
sns.scatterplot(x=y_pred, y=np.sqrt(np.abs(residuals)))
plt.axhline(y=np.mean(np.sqrt(np.abs(residuals))), color='red', linestyle='--')
```

---

## 🧭 6. Influence & Leverage Diagnostics

**Goal:** Identify influential points or high-leverage outliers.

| Plot                 | What to Look For            |
| -------------------- | --------------------------- |
| Cook’s Distance      | Large spikes = influence    |
| Leverage vs Residual | Far top right = danger zone |

```python
influence = model.get_influence()
(c, p) = influence.cooks_distance
plt.stem(c)
```

---

## 🔁 7. Visualizing Model Extensions

### 📐 Regularization (Ridge/Lasso)

* Plot coefficients vs alpha (log scale)
* Use `RidgeCV`, `LassoCV` with grid of `alphas`

### 📈 Polynomial Regression

* Overlay predicted vs actual with fitted line
* Visual residual pattern vs degree of polynomial

```python
from sklearn.preprocessing import PolynomialFeatures
```

---

## 🧪 8. Visual Summary Table

| Visual                 | Diagnosis Target           |
| ---------------------- | -------------------------- |
| Actual vs Predicted    | General fit & bias         |
| Residuals vs Fitted    | Homoscedasticity           |
| Histogram of Residuals | Normality                  |
| QQ Plot                | Normality (tail behavior)  |
| Scale-Location Plot    | Variance diagnostics       |
| Leverage vs Residual   | Influential obs / outliers |

---

## 📋 Analyst Visual Review Checklist

* [ ] Actual vs Predicted: Tight line fit?
* [ ] Residuals: Random cloud?
* [ ] Histogram: Bell-shaped?
* [ ] QQ Plot: Aligned with diagonal?
* [ ] Scale-location: Flat trend?
* [ ] Influential point plots reviewed?
* [ ] If using Ridge/Lasso, coefficient paths reviewed?

---

## 💡 Final Tip

> Always blend **residual visuals**, **fit diagnostics**, and **robustness checks** for trustworthy regression results.

Use this with: Advanced Linear Regression Guidebook, Statistical Summary Sheet, and Evaluation Checklist.
