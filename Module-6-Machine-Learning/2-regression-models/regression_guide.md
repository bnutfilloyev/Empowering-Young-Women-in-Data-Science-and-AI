# Regression Complete Guide 📊

## Table of Contents
1. [Introduction](#introduction)
2. [Linear Regression](#linear-regression)
3. [Polynomial Regression](#polynomial-regression)
4. [Regularization](#regularization)
5. [Model Evaluation](#model-evaluation)
6. [Best Practices](#best-practices)
7. [Quick Reference](#quick-reference)

---

## Introduction

### Regression nima?
Regression - bu supervised learning algoritmi bo'lib, **raqamli qiymatlarni** bashorat qilish uchun ishlatiladi.

### Regression turlari:
- **Linear Regression**: Chiziqli munosabat
- **Polynomial Regression**: Nochiziqli munosabat
- **Ridge Regression**: L2 regularization
- **Lasso Regression**: L1 regularization
- **ElasticNet**: L1 + L2 regularization

### Qachon ishlatish?
✅ **Regression**:
- Continuous output (narx, harorat, maosh)
- Munosabat borligini bilasiz
- Bashorat qilish kerak

❌ **Regression emas**:
- Categorical output (ha/yo'q, spam/not spam) → Classification

---

## Linear Regression

### 📐 Mathematical Formula

**Simple Linear Regression**:
```
y = β₀ + β₁x + ε
```

**Multiple Linear Regression**:
```
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε
```

Bu yerda:
- `y` - target (bashorat qilinadigan)
- `x₁, x₂, ..., xₙ` - features
- `β₀` - intercept (y-kesim)
- `β₁, ..., βₙ` - coefficients (og'irliklar)
- `ε` - error (xatolik)

### 🎯 Cost Function

**Mean Squared Error (MSE)**:
```
MSE = (1/n) Σ(yᵢ - ŷᵢ)²
```

**Goal**: MSE ni minimallashtirish

### 💻 Python Implementation

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Ma'lumotlarni ajratish
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model yaratish
model = LinearRegression()

# O'rgatish
model.fit(X_train, y_train)

# Bashorat
y_pred = model.predict(X_test)

# Baholash
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"R² Score: {r2:.4f}")
print(f"RMSE: {rmse:.4f}")
```

### 📊 Assumptions (Taxminlar)

Linear Regression quyidagi taxminlarga tayanadi:

1. **Linearity**: X va y o'rtasida chiziqli munosabat
2. **Independence**: Observations mustaqil
3. **Homoscedasticity**: Residuals ning variansiyasi doimiy
4. **Normality**: Residuals normal taqsimlangan
5. **No Multicollinearity**: Feature'lar o'rtasida yuqori korrelyatsiya yo'q

**Tekshirish usullari**:
```python
# 1. Linearity - Scatter plots
plt.scatter(X, y)

# 2. Homoscedasticity - Residual plot
plt.scatter(y_pred, y_test - y_pred)
plt.axhline(y=0, color='r', linestyle='--')

# 3. Normality - QQ plot
import scipy.stats as stats
stats.probplot(y_test - y_pred, dist="norm", plot=plt)

# 4. Multicollinearity - VIF
from statsmodels.stats.outliers_influence import variance_inflation_factor
vif = pd.DataFrame()
vif["Feature"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
```

### ✅ Pros
- Tez va sodda
- Interpretable (tushunish oson)
- Kam overfitting
- Feature importance ni beradi

### ❌ Cons
- Faqat chiziqli munosabatlar
- Outliers'ga sezgir
- Multicollinearity muammosi
- Katta dataset'larda ba'zan yetarli emas

---

## Polynomial Regression

### 📐 Mathematical Formula

**2nd Degree (Quadratic)**:
```
y = β₀ + β₁x + β₂x² + ε
```

**3rd Degree (Cubic)**:
```
y = β₀ + β₁x + β₂x² + β₃x³ + ε
```

**nth Degree**:
```
y = β₀ + β₁x + β₂x² + ... + βₙxⁿ + ε
```

### 💻 Python Implementation

```python
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Method 1: Manual
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)

model = LinearRegression()
model.fit(X_poly, y)

# Method 2: Pipeline (recommended)
poly_model = Pipeline([
    ('poly', PolynomialFeatures(degree=2)),
    ('linear', LinearRegression())
])

poly_model.fit(X_train, y_train)
y_pred = poly_model.predict(X_test)
```

### 🔍 Degree Selection

```python
# Turli degree'larni sinab ko'rish
degrees = range(1, 11)
train_scores = []
test_scores = []

for degree in degrees:
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)
    
    model = LinearRegression()
    model.fit(X_train_poly, y_train)
    
    train_scores.append(model.score(X_train_poly, y_train))
    test_scores.append(model.score(X_test_poly, y_test))

# Vizualizatsiya
plt.plot(degrees, train_scores, label='Train')
plt.plot(degrees, test_scores, label='Test')
plt.xlabel('Polynomial Degree')
plt.ylabel('R² Score')
plt.legend()
```

### ⚠️ Overfitting Warning

**Signs of Overfitting**:
- Train R² >> Test R²
- Very high degree polynomial
- Wild predictions outside data range

**Solutions**:
- Lower degree
- More data
- Regularization (Ridge/Lasso)
- Cross-validation

### ✅ Pros
- Nochiziqli munosabatlarni model qiladi
- Flexible
- Simple implementation

### ❌ Cons
- Overfitting risk
- Extrapolation da yomon
- Feature'lar soni exponential oshadi
- Interpretability pasayadi

---

## Regularization

### Nima uchun kerak?

**Muammolar**:
1. **Overfitting**: Model train data'ni juda yaxshi o'rganadi
2. **High variance**: Kichik o'zgarishlarga juda sezgir
3. **Too many features**: Keraksiz feature'lar
4. **Multicollinearity**: Feature'lar o'rtasida yuqori korrelyatsiya

**Yechim**: Regularization - model koeffitsientlarini "jazolash"

---

### Ridge Regression (L2)

#### 📐 Formula
```
Cost = MSE + α Σβᵢ²
```

Bu yerda:
- `α` (alpha) - regularization strength
- Higher α → smaller coefficients

#### 💻 Python Implementation

```python
from sklearn.linear_model import Ridge

# Model
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)
y_pred = ridge.predict(X_test)

# Alpha tuning
alphas = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
scores = []

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    scores.append(ridge.score(X_test, y_test))

best_alpha = alphas[np.argmax(scores)]
print(f"Best alpha: {best_alpha}")

# GridSearchCV (recommended)
from sklearn.model_selection import GridSearchCV

param_grid = {'alpha': np.logspace(-3, 3, 50)}
grid = GridSearchCV(Ridge(), param_grid, cv=5, scoring='r2')
grid.fit(X_train, y_train)

print(f"Best alpha: {grid.best_params_['alpha']:.4f}")
print(f"Best score: {grid.best_score_:.4f}")
```

#### ✅ When to use
- Ko'p feature'lar
- Multicollinearity
- Overfitting muammosi
- Barcha feature'lar muhim

#### ❌ When not to use
- Feature selection kerak
- Sparse model kerak

---

### Lasso Regression (L1)

#### 📐 Formula
```
Cost = MSE + α Σ|βᵢ|
```

#### 💻 Python Implementation

```python
from sklearn.linear_model import Lasso

# Model
lasso = Lasso(alpha=1.0, max_iter=10000)
lasso.fit(X_train, y_train)
y_pred = lasso.predict(X_test)

# Feature selection
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'coefficient': lasso.coef_
})
feature_importance = feature_importance[feature_importance['coefficient'] != 0]
print(f"Selected features: {len(feature_importance)}/{len(X.columns)}")

# Alpha tuning
from sklearn.linear_model import LassoCV

lasso_cv = LassoCV(alphas=np.logspace(-3, 1, 50), cv=5)
lasso_cv.fit(X_train, y_train)

print(f"Best alpha: {lasso_cv.alpha_:.4f}")
print(f"Number of features: {np.sum(lasso_cv.coef_ != 0)}")
```

#### ✅ When to use
- Feature selection kerak
- Ko'p feature'lar, ayrimlari keraksiz
- Sparse model kerak
- Interpretability muhim

#### ❌ When not to use
- Barcha feature'lar muhim
- Yuqori multicollinearity (Ridge yaxshiroq)

---

### ElasticNet (L1 + L2)

#### 📐 Formula
```
Cost = MSE + α₁ Σ|βᵢ| + α₂ Σβᵢ²
```

#### 💻 Python Implementation

```python
from sklearn.linear_model import ElasticNet, ElasticNetCV

# Model
elastic = ElasticNet(alpha=1.0, l1_ratio=0.5)  # l1_ratio: L1 weight (0-1)
elastic.fit(X_train, y_train)

# Tuning both parameters
from sklearn.model_selection import GridSearchCV

param_grid = {
    'alpha': [0.001, 0.01, 0.1, 1, 10],
    'l1_ratio': [0.1, 0.3, 0.5, 0.7, 0.9]
}

grid = GridSearchCV(ElasticNet(), param_grid, cv=5, scoring='r2')
grid.fit(X_train, y_train)

print(f"Best params: {grid.best_params_}")
```

#### ✅ When to use
- Ridge va Lasso o'rtasi kerak
- Ko'p correlated features
- Feature selection + regularization

---

### Regularization Comparison

| Aspect | Ridge (L2) | Lasso (L1) | ElasticNet |
|--------|------------|------------|------------|
| **Penalty** | Σβᵢ² | Σ\|βᵢ\| | Both |
| **Coefficients** | Small, non-zero | Can be zero | Mixed |
| **Feature Selection** | ❌ | ✅ | ✅ |
| **Multicollinearity** | ✅ Good | ⚠️ OK | ✅ Good |
| **Interpretability** | Medium | High | Medium |
| **Computation** | Fast | Medium | Medium |

**Visual Comparison**:
```python
# Koeffitsientlarni taqqoslash
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

models = [
    ('Ridge', Ridge(alpha=1.0)),
    ('Lasso', Lasso(alpha=0.1)),
    ('ElasticNet', ElasticNet(alpha=0.1, l1_ratio=0.5))
]

for idx, (name, model) in enumerate(models):
    model.fit(X_train_scaled, y_train)
    axes[idx].bar(range(len(model.coef_)), model.coef_)
    axes[idx].set_title(f'{name} Coefficients')
    axes[idx].axhline(y=0, color='r', linestyle='--')
    axes[idx].set_xlabel('Feature Index')
    axes[idx].set_ylabel('Coefficient Value')

plt.tight_layout()
```

---

## Model Evaluation

### Metrics

#### 1. R² Score (Coefficient of Determination)
```
R² = 1 - (SS_res / SS_tot)
```

**Range**: 0 to 1 (higher is better)
- R² = 1: Perfect prediction
- R² = 0: No better than mean
- R² < 0: Worse than mean (very bad!)

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print(f"R² Score: {r2:.4f}")
print(f"Model explains {r2*100:.2f}% of variance")
```

#### 2. Mean Squared Error (MSE)
```
MSE = (1/n) Σ(yᵢ - ŷᵢ)²
```

**Lower is better**
- Punishes large errors more
- Same units as y²

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mse:.4f}")
```

#### 3. Root Mean Squared Error (RMSE)
```
RMSE = √MSE
```

**Lower is better**
- Same units as y
- Interpretable
- Most common metric

```python
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.4f}")
```

#### 4. Mean Absolute Error (MAE)
```
MAE = (1/n) Σ|yᵢ - ŷᵢ|
```

**Lower is better**
- Same units as y
- Less sensitive to outliers than RMSE
- Linear penalty

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
print(f"MAE: {mae:.4f}")
```

#### 5. Mean Absolute Percentage Error (MAPE)
```
MAPE = (100/n) Σ|(yᵢ - ŷᵢ)/yᵢ|
```

**Percentage**
- Easy to understand
- Scale-independent

```python
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100
print(f"MAPE: {mape:.2f}%")
```

### Metrics Comparison

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def evaluate_model(y_true, y_pred, model_name="Model"):
    """To'liq model baholash"""
    print(f"\n{'='*50}")
    print(f"{model_name} Evaluation")
    print(f"{'='*50}")
    
    r2 = r2_score(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    print(f"R² Score:  {r2:.4f}")
    print(f"MSE:       {mse:.4f}")
    print(f"RMSE:      {rmse:.4f}")
    print(f"MAE:       {mae:.4f}")
    print(f"MAPE:      {mape:.2f}%")
    
    return {'R²': r2, 'MSE': mse, 'RMSE': rmse, 'MAE': mae, 'MAPE': mape}

# Ishlatish
results = evaluate_model(y_test, y_pred, "Linear Regression")
```

---

### Cross-Validation

**Why?**: Bitta train-test split yetarli emas

```python
from sklearn.model_selection import cross_val_score

# K-Fold CV
scores = cross_val_score(model, X, y, cv=5, scoring='r2')

print(f"CV Scores: {scores}")
print(f"Mean: {scores.mean():.4f}")
print(f"Std: {scores.std():.4f}")

# Turli metrics
from sklearn.model_selection import cross_validate

scoring = ['r2', 'neg_mean_squared_error', 'neg_mean_absolute_error']
cv_results = cross_validate(model, X, y, cv=5, scoring=scoring)

print(f"R² Score: {cv_results['test_r2'].mean():.4f} (+/- {cv_results['test_r2'].std():.4f})")
print(f"MSE: {-cv_results['test_neg_mean_squared_error'].mean():.4f}")
print(f"MAE: {-cv_results['test_neg_mean_absolute_error'].mean():.4f}")
```

---

### Learning Curves

```python
from sklearn.model_selection import learning_curve

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y, cv=5, 
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='r2'
)

train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)
val_mean = np.mean(val_scores, axis=1)
val_std = np.std(val_scores, axis=1)

plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, label='Train score')
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.2)
plt.plot(train_sizes, val_mean, label='Validation score')
plt.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, alpha=0.2)
plt.xlabel('Training Set Size')
plt.ylabel('R² Score')
plt.title('Learning Curves')
plt.legend()
plt.grid(True)
```

**Interpretation**:
- **High bias**: Both curves low, converging → Underfitting
- **High variance**: Large gap between curves → Overfitting
- **Good fit**: Both curves high, small gap

---

### Residual Analysis

```python
# Residuals
residuals = y_test - y_pred

# 1. Residual Plot
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')

# 2. Histogram of Residuals
plt.subplot(1, 3, 2)
plt.hist(residuals, bins=30, edgecolor='black')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Histogram of Residuals')

# 3. QQ Plot
plt.subplot(1, 3, 3)
from scipy import stats
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('QQ Plot')

plt.tight_layout()
```

**Good Residuals**:
- Random scatter around 0
- Constant variance (homoscedasticity)
- Normally distributed

---

## Best Practices

### 1. Data Preparation

```python
# Missing values
X.isnull().sum()  # Check
X.fillna(X.mean(), inplace=True)  # Fill

# Outliers
from scipy import stats
z_scores = np.abs(stats.zscore(X))
X = X[(z_scores < 3).all(axis=1)]

# Scaling (IMPORTANT for regularization!)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### 2. Feature Engineering

```python
# Polynomial features
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)

# Interaction features
X['feature1_x_feature2'] = X['feature1'] * X['feature2']

# Log transformation (skewed data)
X['log_feature'] = np.log1p(X['feature'])

# Binning
X['age_group'] = pd.cut(X['age'], bins=[0, 18, 35, 60, 100], labels=['Young', 'Adult', 'Middle', 'Senior'])
```

### 3. Feature Selection

```python
# Correlation-based
corr_matrix = X.corr()
high_corr = np.where(np.abs(corr_matrix) > 0.8)

# Lasso-based
from sklearn.linear_model import LassoCV
lasso = LassoCV(cv=5)
lasso.fit(X, y)
important_features = X.columns[lasso.coef_ != 0]

# RFE (Recursive Feature Elimination)
from sklearn.feature_selection import RFE
selector = RFE(LinearRegression(), n_features_to_select=10)
selector.fit(X, y)
selected_features = X.columns[selector.support_]
```

### 4. Model Selection Workflow

```python
# 1. Start simple
lr_model = LinearRegression()

# 2. Check for overfitting
# Train vs Test R²

# 3. Try regularization if needed
ridge_model = Ridge(alpha=1.0)
lasso_model = Lasso(alpha=0.1)

# 4. Polynomial if non-linear
poly_model = Pipeline([
    ('poly', PolynomialFeatures(degree=2)),
    ('ridge', Ridge(alpha=1.0))
])

# 5. Hyperparameter tuning
from sklearn.model_selection import GridSearchCV

param_grid = {'alpha': np.logspace(-3, 3, 20)}
grid = GridSearchCV(Ridge(), param_grid, cv=5)
grid.fit(X_train, y_train)

# 6. Final evaluation
best_model = grid.best_estimator_
test_score = best_model.score(X_test, y_test)
```

### 5. Avoiding Common Mistakes

❌ **DON'T**:
- Use test data in training
- Forget to scale for regularization
- Ignore assumptions
- Use only one metric
- Choose high polynomial degree blindly
- Fit scaler on test data

✅ **DO**:
- Split data properly
- Scale features (especially for regularization)
- Check assumptions (linearity, normality, etc.)
- Use multiple metrics
- Use cross-validation
- Analyze residuals
- Document your process

---

## Quick Reference

### Complete Pipeline Example

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# 1. Load Data
X = ...  # features
y = ...  # target

# 2. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Model Training
models = {
    'Linear': LinearRegression(),
    'Ridge': Ridge(),
    'Lasso': Lasso()
}

results = {}
for name, model in models.items():
    # Hyperparameter tuning (Ridge/Lasso)
    if name != 'Linear':
        param_grid = {'alpha': np.logspace(-3, 3, 20)}
        grid = GridSearchCV(model, param_grid, cv=5, scoring='r2')
        grid.fit(X_train_scaled, y_train)
        model = grid.best_estimator_
        print(f"{name} best alpha: {grid.best_params_['alpha']:.4f}")
    else:
        model.fit(X_train_scaled, y_train)
    
    # Predictions
    y_pred_train = model.predict(X_train_scaled)
    y_pred_test = model.predict(X_test_scaled)
    
    # Evaluation
    results[name] = {
        'Train R²': r2_score(y_train, y_pred_train),
        'Test R²': r2_score(y_test, y_pred_test),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_test)),
        'MAE': mean_absolute_error(y_test, y_pred_test)
    }

# 5. Results
results_df = pd.DataFrame(results).T
print("\nModel Comparison:")
print(results_df)

# 6. Visualization
best_model_name = results_df['Test R²'].idxmax()
print(f"\nBest Model: {best_model_name}")
```

### Cheat Sheet

#### Model Selection Decision Tree

```
Start
  |
  ├─ Linear relationship? 
  │   ├─ Yes → Linear Regression
  │   │   ├─ Overfitting? → Ridge
  │   │   └─ Need feature selection? → Lasso
  │   │
  │   └─ No → Polynomial Regression
  │       ├─ Overfitting? → Polynomial + Ridge/Lasso
  │       └─ Still bad? → Try other models (Tree-based, etc.)
```

#### Quick Commands

```python
# Linear Regression
LinearRegression().fit(X_train, y_train)

# Ridge (with CV)
from sklearn.linear_model import RidgeCV
RidgeCV(alphas=[0.1, 1, 10]).fit(X_train, y_train)

# Lasso (with CV)
from sklearn.linear_model import LassoCV
LassoCV(cv=5).fit(X_train, y_train)

# Polynomial
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
Pipeline([
    ('poly', PolynomialFeatures(degree=2)),
    ('linear', LinearRegression())
]).fit(X_train, y_train)

# ElasticNet
from sklearn.linear_model import ElasticNetCV
ElasticNetCV(cv=5, l1_ratio=[0.1, 0.5, 0.9]).fit(X_train, y_train)
```

#### Evaluation Template

```python
def quick_evaluate(model, X_train, X_test, y_train, y_test):
    """Quick model evaluation"""
    model.fit(X_train, y_train)
    
    print(f"Train R²: {model.score(X_train, y_train):.4f}")
    print(f"Test R²:  {model.score(X_test, y_test):.4f}")
    
    y_pred = model.predict(X_test)
    print(f"RMSE:     {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
    print(f"MAE:      {mean_absolute_error(y_test, y_pred):.4f}")
    
    return model
```

---

## Common Issues & Solutions

### Issue 1: Low R² Score
**Solutions**:
- More features
- Feature engineering
- Polynomial features
- Different model (non-linear)
- More data

### Issue 2: High Train R², Low Test R² (Overfitting)
**Solutions**:
- Regularization (Ridge/Lasso)
- Lower polynomial degree
- More data
- Feature selection
- Cross-validation

### Issue 3: Both Train and Test R² Low (Underfitting)
**Solutions**:
- More features
- Higher polynomial degree
- Feature engineering
- Different model

### Issue 4: Multicollinearity
**Solutions**:
- Remove correlated features
- PCA (Principal Component Analysis)
- Ridge regression

### Issue 5: Non-normal Residuals
**Solutions**:
- Transform target (log, sqrt)
- Remove outliers
- Try different model

---

## Resources

### Documentation
- [Scikit-learn Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)

### Tutorials
- [StatQuest: Linear Regression](https://www.youtube.com/watch?v=nk2CQITm_eo)
- [3Blue1Brown: Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

### Books
- "An Introduction to Statistical Learning" - James, Witten, Hastie, Tibshirani
- "The Elements of Statistical Learning" - Hastie, Tibshirani, Friedman

---

**Good luck with your regression projects! 🚀**
