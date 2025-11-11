# 🔧 Feature Engineering - Quick Reference Guide

## 📚 Complete Cheat Sheet

---

## 1️⃣ Feature Selection

### Comparison Table

| Method | Type | Speed | Accuracy | Use Case |
|--------|------|-------|----------|----------|
| **Variance Threshold** | Filter | ⚡⚡⚡ | ⭐ | Remove constant features |
| **SelectKBest (Chi²)** | Filter | ⚡⚡⚡ | ⭐⭐ | Categorical features |
| **SelectKBest (F-test)** | Filter | ⚡⚡⚡ | ⭐⭐ | Numerical features |
| **Mutual Information** | Filter | ⚡⚡ | ⭐⭐⭐ | Non-linear relationships |
| **RFE** | Wrapper | ⚡ | ⭐⭐⭐⭐ | Model-specific selection |
| **Forward Selection** | Wrapper | ⚡ | ⭐⭐⭐⭐ | Small datasets |
| **L1 Regularization** | Embedded | ⚡⚡ | ⭐⭐⭐ | Linear models |
| **Random Forest Importance** | Embedded | ⚡⚡ | ⭐⭐⭐⭐ | Tree-based models |

### Quick Code

```python
# Filter Method - SelectKBest
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(score_func=f_classif, k=10)
X_selected = selector.fit_transform(X, y)

# Wrapper Method - RFE
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
rfe = RFE(estimator=model, n_features_to_select=10)
X_selected = rfe.fit_transform(X, y)

# Embedded Method - Feature Importance
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
rf = RandomForestClassifier()
rf.fit(X, y)
selector = SelectFromModel(rf, threshold='median', prefit=True)
X_selected = selector.transform(X)
```

---

## 2️⃣ Feature Scaling

### Comparison Table

| Scaler | Formula | Range | Use Case | Outliers? |
|--------|---------|-------|----------|-----------|
| **StandardScaler** | (x - μ) / σ | μ=0, σ=1 | Normal distribution, most common | ❌ Sensitive |
| **MinMaxScaler** | (x - min) / (max - min) | [0, 1] | Bounded range, neural networks | ❌ Very sensitive |
| **RobustScaler** | (x - median) / IQR | Variable | Data with outliers | ✅✅ Robust |
| **MaxAbsScaler** | x / \|max\| | [-1, 1] | Sparse data | ❌ Sensitive |
| **Normalizer** | x / \|\|x\|\| | [0, 1] | Text/NLP data | N/A |

### When to Scale?

```
Algorithm          Need Scaling?    Best Scaler
───────────────────────────────────────────────────
Linear Regression      ✅ Yes       StandardScaler
Logistic Regression    ✅ Yes       StandardScaler
SVM                    ✅ Yes       StandardScaler
KNN                    ✅ Yes       StandardScaler or MinMaxScaler
Neural Networks        ✅ Yes       MinMaxScaler or StandardScaler
Decision Trees         ❌ No        None
Random Forest          ❌ No        None
XGBoost/LightGBM       ❌ No        None
K-Means Clustering     ✅ Yes       StandardScaler
PCA                    ✅ Yes       StandardScaler
```

### Quick Code

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# StandardScaler (Z-score)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# MinMaxScaler
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X_train)

# RobustScaler (for outliers)
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X_train)

# ⚠️ ALWAYS: fit on train, transform on test!
```

---

## 3️⃣ Feature Encoding

### Comparison Table

| Method | Use Case | Cardinality | Creates | Data Leakage Risk |
|--------|----------|-------------|---------|-------------------|
| **Label Encoding** | Ordinal (with order) | Any | 1 feature | ❌ No |
| **One-Hot Encoding** | Nominal (no order) | Low (<15) | n features | ❌ No |
| **Target Encoding** | High cardinality | High (>15) | 1 feature | ⚠️ Yes (use CV!) |
| **Frequency Encoding** | When frequency matters | Any | 1 feature | ❌ No |
| **Binary Encoding** | Memory efficient | High | log₂(n) features | ❌ No |
| **Ordinal Encoding** | Custom order | Any | 1 feature | ❌ No |

### Decision Tree

```
Categorical Feature?
    │
    ├─ Has natural order (Ordinal)?
    │    └─ Yes → Label/Ordinal Encoding
    │
    ├─ No order (Nominal)?
    │    ├─ Low cardinality (<15)?
    │    │    └─ Yes → One-Hot Encoding
    │    │
    │    └─ High cardinality (>15)?
    │         ├─ Target info available?
    │         │    └─ Yes → Target Encoding (with CV!)
    │         │
    │         └─ Memory concern?
    │              ├─ Yes → Binary Encoding
    │              └─ No → Frequency Encoding
```

### Quick Code

```python
# Label Encoding (Ordinal)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['Education_Encoded'] = le.fit_transform(df['Education'])
# Example: High School=0, Bachelor=1, Master=2, PhD=3

# One-Hot Encoding (Nominal)
df_encoded = pd.get_dummies(df, columns=['Color'], prefix='Color')
# Example: Color_Red, Color_Green, Color_Blue (3 columns)

# Target Encoding (High cardinality)
city_salary_mean = df.groupby('City')['Salary'].mean()
df['City_Encoded'] = df['City'].map(city_salary_mean)
# ⚠️ Use with CV to avoid leakage!

# Frequency Encoding
city_counts = df['City'].value_counts()
df['City_Freq'] = df['City'].map(city_counts)
```

---

## 4️⃣ Feature Creation

### Common Techniques

| Technique | Example | Use Case |
|-----------|---------|----------|
| **Polynomial** | x², x³, x₁×x₂ | Non-linear relationships |
| **Ratios** | Income/Age, Price/SqFt | Relative measures |
| **Binning** | Age → [Young, Middle, Senior] | Categorize continuous |
| **Date/Time** | Year, Month, DayOfWeek | Temporal patterns |
| **Aggregations** | Sum, Mean, Count per group | Summary statistics |
| **Domain-specific** | BMI = Weight/(Height²) | Business logic |
| **Interactions** | Age×Income | Feature combinations |
| **Log Transform** | log(x+1) | Skewed distributions |

### Quick Code

```python
from sklearn.preprocessing import PolynomialFeatures

# Polynomial Features
poly = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly.fit_transform(X)
# [x1, x2] → [x1, x2, x1², x1×x2, x2²]

# Manual Features
df['BMI'] = df['Weight'] / (df['Height']/100)**2
df['Income_per_Year'] = df['Income'] / (df['Experience'] + 1)
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 30, 45, 100], labels=['Young', 'Middle', 'Senior'])

# Date/Time Features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.dayofweek
df['IsWeekend'] = (df['DayOfWeek'] >= 5).astype(int)

# Aggregations
df['Total_Purchases'] = df.groupby('Customer')['Amount'].transform('sum')
df['Avg_Purchase'] = df.groupby('Customer')['Amount'].transform('mean')
```

---

## 5️⃣ Complete Pipeline

### Template

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.ensemble import RandomForestClassifier

# Define columns
numerical_features = ['Age', 'Income', 'Score']
categorical_features = ['Education', 'City']

# Numerical pipeline
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Categorical pipeline
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Combine
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Complete pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('feature_selection', SelectKBest(f_classif, k=10)),
    ('classifier', RandomForestClassifier())
])

# Train
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# ✅ No data leakage!
# ✅ Reproducible!
# ✅ Deployment ready!
```

---

## 6️⃣ Common Pitfalls & Solutions

### ❌ Pitfall 1: Data Leakage
```python
# WRONG
scaler.fit(X)
X_train, X_test = train_test_split(X, ...)

# CORRECT
X_train, X_test = train_test_split(X, ...)
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### ❌ Pitfall 2: Label Encoding for Nominal
```python
# WRONG
le = LabelEncoder()
df['Color_Encoded'] = le.fit_transform(df['Color'])
# Creates false order: Red=0, Green=1, Blue=2

# CORRECT
df_encoded = pd.get_dummies(df, columns=['Color'])
# One-Hot: Color_Red, Color_Green, Color_Blue
```

### ❌ Pitfall 3: Forgetting to Scale
```python
# KNN without scaling = Bad performance!
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)  # Features with different scales!

# CORRECT
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
knn.fit(X_train_scaled, y_train)
```

### ❌ Pitfall 4: Target Encoding without CV
```python
# WRONG - Data leakage!
city_mean = df.groupby('City')['Target'].mean()
df['City_Encoded'] = df['City'].map(city_mean)
X_train, X_test = train_test_split(df, ...)

# CORRECT - Use category_encoders
from category_encoders import TargetEncoder
te = TargetEncoder()
te.fit(X_train['City'], y_train)
X_train['City_Encoded'] = te.transform(X_train['City'])
X_test['City_Encoded'] = te.transform(X_test['City'])
```

---

## 7️⃣ Feature Engineering Checklist

### Before Training:
- [ ] **EDA Complete** - Understand data distribution
- [ ] **Missing Values** - Impute or drop
- [ ] **Outliers** - Handle or use RobustScaler
- [ ] **Categorical Encoded** - Label/One-Hot/Target
- [ ] **Numerical Scaled** - If needed (KNN, SVM, NN)
- [ ] **Features Created** - Domain-specific
- [ ] **Features Selected** - Remove redundant
- [ ] **Pipeline Built** - Reproducibility
- [ ] **Train-Test Split** - Before FE to avoid leakage

### During Training:
- [ ] **Fit on Train** - Never on test
- [ ] **Transform Test** - Use fitted transformers
- [ ] **Cross-Validate** - Robust evaluation
- [ ] **Monitor Performance** - Before/after FE

### After Training:
- [ ] **Feature Importance** - Analyze impact
- [ ] **Remove Low Impact** - Simplify model
- [ ] **Document Transformations** - For deployment
- [ ] **Save Pipeline** - `joblib.dump(pipeline, 'pipeline.pkl')`

---

## 8️⃣ Quick Decision Guide

### "Which Feature Selection Method?"
```
Dataset size < 1000?     → Wrapper (RFE)
Dataset size > 100k?     → Filter (SelectKBest) or Embedded
Need model-specific?     → Wrapper (RFE)
Need fast?               → Filter or Embedded
Tree-based model?        → Feature Importance (Embedded)
Linear model?            → L1 Regularization (Embedded)
```

### "Which Scaler?"
```
Normal distribution?     → StandardScaler
Bounded range needed?    → MinMaxScaler
Outliers present?        → RobustScaler
Sparse data?             → MaxAbsScaler
Tree-based model?        → No scaling needed!
```

### "Which Encoding?"
```
Ordinal (with order)?    → Label/Ordinal Encoding
Nominal + Low card?      → One-Hot Encoding
Nominal + High card?     → Target/Frequency Encoding
Binary feature?          → Label Encoding
```

---

## 9️⃣ One-Page Cheat Sheet

```python
# FEATURE SELECTION
from sklearn.feature_selection import SelectKBest, RFE, SelectFromModel
selector = SelectKBest(k=10).fit(X, y)
X_selected = selector.transform(X)

# FEATURE SCALING
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)

# FEATURE ENCODING
df_encoded = pd.get_dummies(df, columns=['Category'])

# FEATURE CREATION
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# PIPELINE
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('selector', SelectKBest(k=10)),
    ('model', RandomForestClassifier())
])
pipeline.fit(X_train, y_train)
```

---

## 🔟 Resources

### Documentation:
- [Scikit-learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
- [Feature Selection Guide](https://scikit-learn.org/stable/modules/feature_selection.html)
- [Category Encoders](https://contrib.scikit-learn.org/category_encoders/)

### Books:
- "Feature Engineering for Machine Learning" - Alice Zheng
- "Hands-On Machine Learning" - Chapter 2

### Courses:
- Kaggle: Feature Engineering course
- Coursera: Applied Machine Learning

---

**Last Updated:** November 2024  
**Version:** 1.0

---

*Keep this guide handy while working on feature engineering! 🚀*
