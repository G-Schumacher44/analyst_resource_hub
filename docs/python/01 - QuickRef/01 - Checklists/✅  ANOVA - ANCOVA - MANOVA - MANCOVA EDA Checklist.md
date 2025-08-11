## 🎯 Purpose

This checklist provides targeted visual EDA steps for preparing to run ANOVA-family models. It ensures that key assumptions like normality, homogeneity of variances, and linearity are visually inspected before formal testing.

---

## 🟦 ANOVA (1 DV, categorical group)
- [ ] Outcome distribution checked by group
- [ ] Boxplot or violin plot created
- [ ] Group sizes reviewed for balance
- [ ] Levene’s or Bartlett’s test for equal variances
- [ ] **Normality Check:** QQ plot or histogram of residuals (after a preliminary model fit) reviewed.

## 🟨 ANCOVA (1 DV, 1+ covariate + group)
- [ ] Scatterplot of DV vs covariate, colored by group
- [ ] Group × covariate interaction checked
- [ ] Covariate distributions compared across groups
- [ ] **Linearity:** Ensure the relationship between the covariate and DV is linear across all groups.

## 🟩 MANOVA (2+ DVs, 1 categorical IV)
- [ ] Pairplot or correlation matrix of DVs
- [ ] DVs standardized if scales differ
- [ ] Visual group separation assessed (PCA optional)
- [ ] **Multivariate Normality:** Check histograms for each DV by group.

## 🟥 MANCOVA (2+ DVs, 1+ covariates, 1 group)
- [ ] Scatterplot matrix with grouping/covariates
- [ ] Partial plots or adjusted means reviewed
- [ ] Covariate balance across groups verified
- [ ] **Homogeneity of Slopes:** Visually check that the relationship between covariates and DVs is consistent across groups.

---

## 🧠 Final Tip

> "Visual EDA for these models is about confirming that groups are comparable *before* you test if they are different."