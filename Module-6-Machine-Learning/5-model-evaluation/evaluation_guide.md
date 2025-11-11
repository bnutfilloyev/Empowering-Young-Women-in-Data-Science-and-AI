# 📊 Model Evaluation - Tez Yordam Qo'llanmasi

## 🎯 Quick Reference Guide

---

## 1️⃣ Train-Test Split

### Basic Split
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2,      # 20% test, 80% train
    random_state=42,    # Reproducibility
    stratify=y          # Keep class distribution (classification only)
)
```

### Split Ratios
| Dataset Size | Train | Test | Notes |
|--------------|-------|------|-------|
| < 1000 | 70% | 30% | Need more test data |
| 1000-10000 | 75% | 25% | Standard |
| 10000-100000 | 80% | 20% | Most common |
| > 100000 | 85-90% | 10-15% | Large datasets |

### ⚠️ Common Mistakes
```python
# ❌ WRONG: Fit on test data
scaler.fit(X_test)

# ✅ CORRECT: Fit only on train
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## 2️⃣ Cross-Validation

### K-Fold CV
```python
from sklearn.model_selection import cross_val_score, KFold

kfold = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')

print(f"Mean: {scores.mean():.4f} ± {scores.std():.4f}")
```

### Stratified K-Fold (for classification)
```python
from sklearn.model_selection import StratifiedKFold

skfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skfold, scoring='f1')
```

### Multiple Metrics
```python
from sklearn.model_selection import cross_validate

scoring = ['accuracy', 'precision', 'recall', 'f1', 'roc_auc']
results = cross_validate(model, X, y, cv=5, scoring=scoring)

for metric in scoring:
    print(f"{metric}: {results[f'test_{metric}'].mean():.4f}")
```

### K Values Guide
| K | Use Case | Pros | Cons |
|---|----------|------|------|
| 3 | Quick testing | Fast | High variance |
| 5 | Standard | Balanced | - |
| 10 | Robust | Low variance | Slower |
| n | LOO CV | Maximum data usage | Very slow |

---

## 3️⃣ Classification Metrics

### Confusion Matrix
```
                Predicted
              Negative  Positive
Actual Negative  TN       FP
       Positive  FN       TP
```

### Metrics Formulas
| Metric | Formula | Range | Interpretation |
|--------|---------|-------|----------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | 0-1 | Overall correctness |
| **Precision** | TP / (TP + FP) | 0-1 | Positive prediction accuracy |
| **Recall** | TP / (TP + FN) | 0-1 | Actual positive detection |
| **F1-Score** | 2 × (Prec × Rec) / (Prec + Rec) | 0-1 | Harmonic mean |
| **Specificity** | TN / (TN + FP) | 0-1 | Negative detection rate |

### Quick Code
```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, 
    f1_score, confusion_matrix, classification_report
)

# Predictions
y_pred = model.predict(X_test)

# All metrics at once
print(classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Individual metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
```

### Confusion Matrix Visualization
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
```

---

## 4️⃣ ROC Curve & AUC

### ROC Curve
```python
from sklearn.metrics import roc_curve, roc_auc_score

# Get probabilities
y_proba = model.predict_proba(X_test)[:, 1]

# Calculate ROC
fpr, tpr, thresholds = roc_curve(y_test, y_proba)
auc = roc_auc_score(y_test, y_proba)

# Plot
plt.plot(fpr, tpr, label=f'AUC = {auc:.3f}')
plt.plot([0, 1], [0, 1], 'k--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

### AUC Interpretation
| AUC Score | Model Quality |
|-----------|---------------|
| 0.90 - 1.00 | Excellent |
| 0.80 - 0.90 | Very Good |
| 0.70 - 0.80 | Good |
| 0.60 - 0.70 | Fair |
| 0.50 - 0.60 | Poor |
| < 0.50 | Worse than random |

### Threshold Tuning
```python
# Test different thresholds
thresholds_to_test = [0.3, 0.5, 0.7, 0.9]

for thresh in thresholds_to_test:
    y_pred_thresh = (y_proba >= thresh).astype(int)
    prec = precision_score(y_test, y_pred_thresh)
    rec = recall_score(y_test, y_pred_thresh)
    print(f"Threshold {thresh}: Prec={prec:.3f}, Rec={rec:.3f}")
```

---

## 5️⃣ Regression Metrics

### Metrics Formulas
| Metric | Formula | Range | Lower is Better |
|--------|---------|-------|-----------------|
| **MAE** | (1/n) Σ \|y - ŷ\| | [0, ∞) | ✅ |
| **MSE** | (1/n) Σ (y - ŷ)² | [0, ∞) | ✅ |
| **RMSE** | √MSE | [0, ∞) | ✅ |
| **R²** | 1 - (SS_res / SS_tot) | (-∞, 1] | ❌ (higher better) |

### Quick Code
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Predictions
y_pred = model.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE:  {mae:.4f}")
print(f"MSE:  {mse:.4f}")
print(f"RMSE: {rmse:.4f}")
print(f"R²:   {r2:.4f}")
```

### R² Interpretation
| R² Score | Model Quality |
|----------|---------------|
| 0.90 - 1.00 | Excellent |
| 0.80 - 0.90 | Very Good |
| 0.70 - 0.80 | Good |
| 0.60 - 0.70 | Fair |
| < 0.60 | Poor |

### Actual vs Predicted Plot
```python
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], 
         [y_test.min(), y_test.max()], 'r--')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')
plt.show()
```

### Residual Plot
```python
residuals = y_test - y_pred

plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()
```

---

## 6️⃣ Overfitting Detection

### Train vs Test Comparison
```python
# Train predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# For classification
train_acc = accuracy_score(y_train, y_train_pred)
test_acc = accuracy_score(y_test, y_test_pred)

# For regression
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train: {train_r2:.4f}, Test: {test_r2:.4f}")
print(f"Gap: {train_r2 - test_r2:.4f}")
```

### Overfitting Indicators
| Indicator | Overfitting? |
|-----------|--------------|
| Train >> Test (gap > 0.1) | ✅ Yes |
| Train ≈ Test (gap < 0.05) | ❌ No |
| Train < Test | ❌ No (but suspicious) |
| Both low | Underfitting |

### Learning Curves
```python
from sklearn.model_selection import learning_curve

train_sizes, train_scores, test_scores = learning_curve(
    model, X, y, cv=5, train_sizes=np.linspace(0.1, 1.0, 10)
)

plt.plot(train_sizes, train_scores.mean(axis=1), label='Train')
plt.plot(train_sizes, test_scores.mean(axis=1), label='Test')
plt.xlabel('Training Size')
plt.ylabel('Score')
plt.legend()
plt.title('Learning Curves')
plt.show()
```

---

## 7️⃣ Model Comparison Template

### Complete Evaluation Function
```python
def evaluate_model(model, X_train, X_test, y_train, y_test, task='classification'):
    """Complete model evaluation"""
    
    # Train
    model.fit(X_train, y_train)
    
    # Predict
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)
    
    if task == 'classification':
        # Metrics
        train_acc = accuracy_score(y_train, y_train_pred)
        test_acc = accuracy_score(y_test, y_test_pred)
        
        prec = precision_score(y_test, y_test_pred)
        rec = recall_score(y_test, y_test_pred)
        f1 = f1_score(y_test, y_test_pred)
        
        # ROC AUC
        y_proba = model.predict_proba(X_test)[:, 1]
        auc = roc_auc_score(y_test, y_proba)
        
        # Confusion Matrix
        cm = confusion_matrix(y_test, y_test_pred)
        
        return {
            'train_acc': train_acc,
            'test_acc': test_acc,
            'precision': prec,
            'recall': rec,
            'f1': f1,
            'auc': auc,
            'confusion_matrix': cm,
            'overfit_gap': train_acc - test_acc
        }
    
    elif task == 'regression':
        # Metrics
        train_r2 = r2_score(y_train, y_train_pred)
        test_r2 = r2_score(y_test, y_test_pred)
        
        mae = mean_absolute_error(y_test, y_test_pred)
        mse = mean_squared_error(y_test, y_test_pred)
        rmse = np.sqrt(mse)
        
        return {
            'train_r2': train_r2,
            'test_r2': test_r2,
            'mae': mae,
            'mse': mse,
            'rmse': rmse,
            'overfit_gap': train_r2 - test_r2
        }
```

### Compare Multiple Models
```python
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier()
}

results = []
for name, model in models.items():
    res = evaluate_model(model, X_train, X_test, y_train, y_test)
    res['model'] = name
    results.append(res)

df_results = pd.DataFrame(results)
print(df_results)
```

---

## 8️⃣ Metric Selection Guide

### Classification

#### When to use which metric?

| Scenario | Best Metric | Why? |
|----------|-------------|------|
| **Balanced dataset** | Accuracy | All classes equal |
| **Imbalanced dataset** | F1-Score, ROC-AUC | Handles class imbalance |
| **Medical diagnosis** | Recall | Don't miss diseases (low FN) |
| **Spam detection** | Precision | Avoid false positives |
| **Model selection** | ROC-AUC | Threshold-independent |
| **Multi-class** | Macro/Weighted F1 | All classes considered |

#### Decision Tree
```
Start
  │
  ├─ Balanced dataset? 
  │    ├─ Yes → Accuracy
  │    └─ No → F1 or AUC
  │
  ├─ False Negative costly?
  │    └─ Yes → Recall
  │
  ├─ False Positive costly?
  │    └─ Yes → Precision
  │
  └─ Need threshold tuning?
       └─ Yes → ROC-AUC
```

### Regression

| Scenario | Best Metric | Why? |
|----------|-------------|------|
| **Outliers present** | MAE | Robust to outliers |
| **Outliers important** | RMSE | Penalizes large errors |
| **Interpretability** | MAE | Same units as y |
| **Optimization** | MSE | Differentiable |
| **Model comparison** | R² | Percentage variance |
| **Standard reporting** | RMSE | Most common |

---

## 9️⃣ Common Pitfalls & Solutions

### ❌ Pitfall 1: Data Leakage
```python
# WRONG
scaler.fit(X)  # Fit on entire dataset
X_scaled = scaler.transform(X)
X_train, X_test = train_test_split(X_scaled, ...)

# CORRECT
X_train, X_test = train_test_split(X, ...)
scaler.fit(X_train)  # Fit only on train
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### ❌ Pitfall 2: Imbalanced Data Accuracy
```python
# WRONG: Only looking at accuracy for imbalanced data
acc = accuracy_score(y_test, y_pred)  # Can be misleading!

# CORRECT: Use F1, Precision, Recall, AUC
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_proba)
```

### ❌ Pitfall 3: No Cross-Validation
```python
# WRONG: Single train-test split
score = model.score(X_test, y_test)

# CORRECT: Cross-validation
scores = cross_val_score(model, X, y, cv=5)
print(f"Mean: {scores.mean():.4f} ± {scores.std():.4f}")
```

### ❌ Pitfall 4: Ignoring Overfitting
```python
# WRONG: Only checking test metrics
test_score = model.score(X_test, y_test)

# CORRECT: Compare train vs test
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
gap = train_score - test_score
if gap > 0.1:
    print("⚠️ Overfitting detected!")
```

---

## 🔟 Cheat Sheet: One-Page Summary

### Classification Quick Commands
```python
# Basic evaluation
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")
print(f"F1-Score: {f1_score(y_test, y_pred):.3f}")
print(f"ROC-AUC: {roc_auc_score(y_test, y_proba):.3f}")

# Full report
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
```

### Regression Quick Commands
```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

y_pred = model.predict(X_test)

print(f"MAE: {mean_absolute_error(y_test, y_pred):.3f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.3f}")
print(f"R²: {r2_score(y_test, y_pred):.3f}")
```

### Cross-Validation Quick Command
```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X, y, cv=5, scoring='f1')
print(f"CV F1: {scores.mean():.3f} ± {scores.std():.3f}")
```

---

## 📚 Additional Resources

### Documentation
- [Scikit-learn Metrics Guide](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Cross-Validation Strategies](https://scikit-learn.org/stable/modules/cross_validation.html)

### Tutorials
- Google ML Crash Course: Classification
- Towards Data Science: Model Evaluation Articles

### Books
- "Hands-On Machine Learning" - Chapter 2 & 3
- "Python Machine Learning" - Chapter 6

---

**Last Updated:** 2024  
**Version:** 1.0

---

*Keep this guide handy when evaluating your models! 🚀*
