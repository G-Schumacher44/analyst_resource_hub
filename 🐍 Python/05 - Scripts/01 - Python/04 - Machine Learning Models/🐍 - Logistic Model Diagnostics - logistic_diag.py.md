___

📲 - Function Calls and Imports
```python
# --------------------------------------------------
# 📦 Core Classification Metrics & Visuals
# --------------------------------------------------
from diagnostics.logistic_classification_metrics import (
    print_classification_metrics,
    plot_confusion_matrix
)

# --------------------------------------------------
# 📊 Probability-Based Diagnostics
# --------------------------------------------------
from diagnostics.logistic_probability_diagnostics import (
    print_auc_score,
    plot_roc_curve,
    plot_calibration_curve,
    calculate_brier_score
)

# --------------------------------------------------
# 🧮 Summary Runners
# --------------------------------------------------
from diagnostics.logistic_diag_runner import summarize_classification_diagnostics
from diagnostics.logistic_fit_summary import summarize_logistic_fit
```

# **🧪 Typical Notebook Usage**
```python
# Assuming you’ve already run:
# model, y_pred, y_proba = logistic_regression_runner(...)

# 🔹 1. Quick summary of model performance
summarize_classification_diagnostics(y_test, y_pred, y_proba)

# 🔹 2. Statsmodels-specific model fit summary (optional)
summarize_logistic_fit(model)

# 🔹 3. Probability calibration tools (optional)
plot_calibration_curve(y_test, y_proba)
calculate_brier_score(y_test, y_proba)
```

# **⚡ One-Click Diagnostic Cell (Copy-Paste Ready)**
```python
# 🔍 Full Logistic Diagnostic Block

summarize_classification_diagnostics(y_test, y_pred, y_proba)
summarize_logistic_fit(model)                  # For statsmodels only
plot_calibration_curve(y_test, y_proba)        # Optional calibration tool
calculate_brier_score(y_test, y_proba)         # Optional score for probability accuracy
```




# **📂** **Logistic Model Diagnostics**
```python
# model_diag_logistic.py

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, roc_auc_score, ConfusionMatrixDisplay

def plot_confusion_matrix(y_true, y_pred, labels=None):
    """
    Plot confusion matrix with optional custom class labels.
    """
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap='Blues')
    plt.title("Confusion Matrix")
    plt.show()

def print_classification_metrics(y_true, y_pred):
    """
    Print accuracy, precision, recall, F1 score.
    """
    print("📊 Classification Report:")
    print(classification_report(y_true, y_pred))

def plot_roc_curve(y_true, y_proba):
    """
    Plot ROC curve and compute AUC.
    """
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    auc_score = roc_auc_score(y_true, y_proba)

    plt.plot(fpr, tpr, label=f"AUC = {auc_score:.2f}")
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend(loc="lower right")
    plt.grid(True)
    plt.show()
```

### **📄 logistic classification metrics**
```python
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

def print_classification_metrics(y_true, y_pred):
    print("📊 Classification Report:")
    print(classification_report(y_true, y_pred))

def plot_confusion_matrix(y_true, y_pred, labels=None):
    cm = confusion_matrix(y_true, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
    disp.plot(cmap='Blues')
    return cm
```

___

### **📄** **logistic probability diagnostics**
```python
from sklearn.metrics import roc_auc_score, roc_curve
import matplotlib.pyplot as plt

def print_auc_score(y_true, y_proba):
    auc = roc_auc_score(y_true, y_proba)
    print(f"🔹 ROC AUC Score: {auc:.3f}")
    return auc

def plot_roc_curve(y_true, y_proba):
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    auc = roc_auc_score(y_true, y_proba)
    plt.plot(fpr, tpr, label=f"AUC = {auc:.2f}")
    plt.plot([0, 1], [0, 1], 'k--')
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()
    plt.grid(True)
    plt.show()
```

___
### **📄** **logistic_fit_summary.py(for statsmodels only)**
```python
def summarize_logistic_fit(model):
    try:
        print("🧾 Model Fit Summary:")
        print(f"🔹 Log-Likelihood: {model.llf:.2f}")
        print(f"🔹 AIC: {model.aic:.2f}")
        print(f"🔹 BIC: {model.bic:.2f}")
        null_ll = getattr(model, 'llnull', None)
        if null_ll is not None:
            pseudo_r2 = 1 - (model.llf / null_ll)
            print(f"🔹 McFadden's Pseudo R²: {pseudo_r2:.3f}")
    except AttributeError:
        print("⚠️ Not a statsmodels model — skipping fit summary.")
```

___

### **📄** **logistic diag runner**
```python
from .logistic_classification_metrics import print_classification_metrics, plot_confusion_matrix
from .logistic_probability_diagnostics import print_auc_score

def summarize_classification_diagnostics(y_true, y_pred, y_proba=None, labels=None):
    """
    One-call diagnostic runner.
    """
    print("📌 Summary of Classification Performance")
    plot_confusion_matrix(y_true, y_pred, labels=labels)
    print_classification_metrics(y_true, y_pred)
    if y_proba is not None:
        print_auc_score(y_true, y_proba)
```

___
### **✅**  **plot_calibration_curve()**
```python
from sklearn.calibration import calibration_curve
import matplotlib.pyplot as plt

def plot_calibration_curve(y_true, y_proba, n_bins=10):
    """
    Plot a calibration curve to assess probability reliability.
    """
    prob_true, prob_pred = calibration_curve(y_true, y_proba, n_bins=n_bins, strategy='uniform')
    
    plt.plot(prob_pred, prob_true, marker='o', label='Model')
    plt.plot([0, 1], [0, 1], 'k--', label='Perfectly Calibrated')
    plt.xlabel('Mean Predicted Probability')
    plt.ylabel('Fraction of Positives')
    plt.title('Calibration Curve')
    plt.legend()
    plt.grid(True)
    plt.show()
```

____

### **✅** **calculate_brier_score()**
```python
from sklearn.metrics import brier_score_loss

def calculate_brier_score(y_true, y_proba):
    """
    Compute the Brier score: mean squared difference between predicted probability and actual outcome.
    Lower = better.
    """
    score = brier_score_loss(y_true, y_proba)
    print(f"🔹 Brier Score: {score:.4f}")
    return score
```

____

# **📂 model_diag_counts.py**(For Poisson and Negative Binomial model diagnostics)

📲 - Function calls and imports
```python
# 📦 Import diagnostic functions
from diagnostics.model_diag_counts import (
    plot_actual_vs_pred_nb_p,     # actual vs predicted counts (y_true, y_pred)
    plot_deviance_residuals,      # deviance residuals (model)
    summarize_poisson_fit,        # fit summary stats (model)
    check_overdispersion          # check variance vs mean (y_true, y_pred)
)

# Assume model is a statsmodels Poisson or NB GLM
# And you've run the modeling runner:
# model, y_pred = poisson_regression_runner(...)

plot_actual_vs_pred_nb_p(y_test, y_pred)
plot_deviance_residuals(model)
summarize_poisson_fit(model)
check_overdispersion(y_test, y_pred)

```

### **✅ 1.plot_actual_vs_pred_nb_p()**
```python
import matplotlib.pyplot as plt
import seaborn as sns

def plot_actual_vs_predicted(y_true, y_pred, title="Actual vs Predicted Counts"):
    """
    Scatterplot comparing actual and predicted count outcomes.
    """
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=y_true, y=y_pred, alpha=0.7)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
    plt.xlabel("Actual Counts")
    plt.ylabel("Predicted Counts")
    plt.title(title)
    plt.grid(True)
    plt.show()
```

### **✅ 2.** **plot_deviance_residuals()**
```python
def plot_deviance_residuals(model):
    """
    Plot deviance residuals from a statsmodels GLM Poisson or NB model.
    """
    try:
        residuals = model.resid_deviance
        fitted = model.fittedvalues

        plt.figure(figsize=(7, 4))
        sns.scatterplot(x=fitted, y=residuals, alpha=0.6)
        plt.axhline(0, color='red', linestyle='--')
        plt.xlabel("Fitted Values")
        plt.ylabel("Deviance Residuals")
        plt.title("Deviance Residuals vs Fitted")
        plt.grid(True)
        plt.show()
    except AttributeError:
        print("⚠️ model.resid_deviance not available — is this a statsmodels GLM model?")
```

### **✅ 3.**summarize_poisson_fit()**
```python
def summarize_poisson_fit(model):
    """
    Print GLM Poisson/NB model summary stats.
    """
    print("📊 Poisson/NB Fit Summary:")
    print(f"🔹 Log-Likelihood: {model.llf:.2f}")
    print(f"🔹 AIC: {model.aic:.2f}")
    print(f"🔹 BIC: {model.bic:.2f}")

    null_ll = getattr(model, "llnull", None)
    if null_ll is not None:
        pseudo_r2 = 1 - (model.llf / null_ll)
        print(f"🔹 Pseudo R² (McFadden): {pseudo_r2:.3f}")
```

### **✅ 4.check_overdispersion()**
```python
def check_overdispersion(y_true, y_pred):
    """
    Quick check: if variance >> mean → overdispersion likely (suggests NB instead of Poisson).
    """
    residuals = y_true - y_pred
    mean = y_pred.mean()
    variance = residuals.var()

    print(f"🔍 Mean: {mean:.2f}, Residual Variance: {variance:.2f}")
    if variance > mean * 2:
        print("⚠️ Possible overdispersion detected. Consider using Negative Binomial.")
    else:
        print("✅ Dispersion looks reasonable for Poisson.")
```