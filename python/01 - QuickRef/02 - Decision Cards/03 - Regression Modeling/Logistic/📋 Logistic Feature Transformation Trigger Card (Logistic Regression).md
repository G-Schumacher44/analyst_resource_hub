#GAD #Coursera #dataAnalytics #regression 
Regression Analysis
**Course:** [[Google Advanced Data Analytics Certificate]]  
**Module:** 
___

## 🎯 Should You Transform a Feature?

✅ Check these conditions:

| Symptom | Suggested Action |
|---------|------------------|
| Strong right-skew in a numeric predictor | Log-transform or Square Root the predictor |
| Predictor has strong non-linear relationship with log-odds | Try binning or adding polynomial features |
| Heavy-tailed distribution (extreme outliers) | Log-transform to compress outliers |
| Large scale differences across features | Standardize (Z-score) or Min-Max scale predictors |

---

## 🧠 Key Reminders

- Logistic regression needs **linear relationship between X and log-odds**, NOT X and Y directly.
- Target variable (Y) must stay binary (0 or 1) ➔ **NEVER transform Y**.
- Always **check distribution plots** and **log-odds plots** if possible.

✅ Transform messy predictors — NOT the binary outcome!

---

___

### 🔗 **Related Notes**

- [[Links]]