## 🎯 Purpose

This checklist outlines the key exploratory data analysis (EDA) steps to perform before fitting a logistic regression model. It focuses on checking class balance, predictor relationships, and key assumptions.

---

## 🧭 Class Variable
- [ ] Target is binary (0/1 or Yes/No)
- [ ] Class imbalance assessed
- [ ] Considered SMOTE / reweighting if imbalanced

## 📊 Categorical Predictors
- [ ] Crosstabs and bar plots created
- [ ] Chi-square tests considered

## 📈 Numeric Predictors
- [ ] Boxplots and KDEs by class
- [ ] Checked for skewness or separation

## 🔁 Linearity of Logit
- [ ] Binned predictor plotted vs outcome rate
- [ ] Curves → applied transformation or engineered feature

## 🧪 Multicollinearity
- [ ] Correlation matrix reviewed
- [ ] **Feature-to-Feature:** Check for high correlation between numeric predictors.
- [ ] VIFs calculated and acted on

## 🧰 Optional Engineering
- [ ] Applied log/sqrt transformation for skewed predictors
- [ ] Created bins with `qcut` if useful

---

## 🧠 Final Tip

> "For logistic regression, EDA is about finding separation. Look for any variable that splits your target class, even slightly."