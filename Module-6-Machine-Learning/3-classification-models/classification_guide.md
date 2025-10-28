# 🎯 Classification Models - Tezkor Qo'llanma

> Machine Learning Classification algoritmlari bo'yicha to'liq reference guide

---

## 📚 Mundarija

1. [Classification nima?](#classification-nima)
2. [Logistic Regression](#1-logistic-regression)
3. [k-Nearest Neighbors (k-NN)](#2-k-nearest-neighbors-k-nn)
4. [Decision Tree](#3-decision-tree)
5. [Random Forest](#4-random-forest)
6. [Model Selection Guide](#model-selection-guide)
7. [Evaluation Metrics](#evaluation-metrics)
8. [Code Cheat Sheet](#code-cheat-sheet)

---

## Classification nima?

**Classification** - bu supervised learning usuli bo'lib, ma'lumotlarni oldindan belgilangan kategoriyalarga (class) ajratish vazifasi.

### Turlari:
- **Binary Classification**: 2 class (Spam/Not Spam, Yes/No)
- **Multi-class Classification**: 3+ class (Dog/Cat/Bird)
- **Multi-label Classification**: Bir obyekt bir nechta class

---

## 1. Logistic Regression

### 📖 Nazariya

**Ta'rif**: Linear modelni sigmoid funksiyasi bilan o'rab, probability (0 dan 1 gacha) chiqaradi.

**Formula**:
$$P(y=1|x) = \frac{1}{1 + e^{-(wx + b)}}$$

**Decision Boundary**:
- Linear (to'g'ri chiziq, tekislik, gipertekislik)
- Faqat chiziqli ajraladigan ma'lumotlar uchun yaxshi

### ✅ Afzalliklari

- Tez va oddiy
- Interpretable (tushunarli)
- Probability beradi
- Regularization qo'shish oson (L1, L2)
- Scaling kerak

### ❌ Kamchiliklari

- Faqat linear decision boundary
- Non-linear munosabatlarda zaif
- Outlier'larga sezgir
- Feature engineering kerak

### 🔧 Hyperparameters

| Parameter | Default | Tavsiya | Izoh |
|-----------|---------|---------|------|
| `penalty` | `'l2'` | `'l2'` yoki `'l1'` | Regularization turi |
| `C` | `1.0` | `0.01` - `100` | Regularization kuchi (kichik = kuchli) |
| `solver` | `'lbfgs'` | `'liblinear'`, `'saga'` | Optimization algoritmi |
| `max_iter` | `100` | `1000+` | Maksimal iteratsiya |

### 💻 Code Example

```python
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Scaling (muhim!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
log_reg = LogisticRegression(
    penalty='l2',
    C=1.0,
    solver='lbfgs',
    max_iter=1000,
    random_state=42
)

# Training
log_reg.fit(X_train_scaled, y_train)

# Prediction
y_pred = log_reg.predict(X_test_scaled)
y_pred_proba = log_reg.predict_proba(X_test_scaled)

# Coefficients
print("Coefficients:", log_reg.coef_)
print("Intercept:", log_reg.intercept_)
```

### 🎯 Qachon ishlatish?

✅ **Ishlatish:**
- Binary classification
- Linear relationship
- Interpretability muhim
- Tez prediction kerak
- Probability kerak

❌ **Ishlatmaslik:**
- Complex non-linear patterns
- Juda ko'p feature interactions

---

## 2. k-Nearest Neighbors (k-NN)

### 📖 Nazariya

**Ta'rif**: Yangi nuqtani uning eng yaqin k ta qo'shnisining class'iga qarab tasniflaydi.

**Algoritm**:
1. Yangi nuqtadan barcha training nuqtalargacha masofa hisoblash
2. Eng yaqin k ta nuqtani topish
3. Majority voting (ko'pchilik ovozi)

**Distance Metrics**:
- **Euclidean**: $\sqrt{\sum(x_i - y_i)^2}$ (default)
- **Manhattan**: $\sum|x_i - y_i|$
- **Minkowski**: Generalized distance

### ✅ Afzalliklari

- Juda oddiy (no training!)
- Non-linear decision boundaries
- Multi-class uchun yaxshi
- No assumptions about data

### ❌ Kamchiliklari

- Prediction sekin (katta dataset'da)
- High-dimensional data'da zaif (curse of dimensionality)
- Scaling juda muhim
- Memory intensive
- k ni tanlash qiyin

### 🔧 Hyperparameters

| Parameter | Default | Tavsiya | Izoh |
|-----------|---------|---------|------|
| `n_neighbors` | `5` | `3` - `15` (odd) | k qiymati |
| `weights` | `'uniform'` | `'distance'` | Qo'shnilar og'irligi |
| `metric` | `'minkowski'` | `'euclidean'`, `'manhattan'` | Masofa o'lchovi |
| `p` | `2` | `1` (Manhattan), `2` (Euclidean) | Minkowski parameter |

### 💻 Code Example

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

# Scaling (juda muhim!)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Optimal k topish
k_values = range(1, 31)
test_scores = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    test_scores.append(knn.score(X_test_scaled, y_test))

best_k = k_values[np.argmax(test_scores)]
print(f"Best k: {best_k}")

# Final Model
knn = KNeighborsClassifier(
    n_neighbors=best_k,
    weights='distance',  # Yaqinroq nuqtalar ko'proq ta'sir qiladi
    metric='euclidean'
)

knn.fit(X_train_scaled, y_train)
y_pred = knn.predict(X_test_scaled)
```

### 🎯 Qachon ishlatish?

✅ **Ishlatish:**
- Kichik-o'rta dataset
- Non-linear decision boundary
- Multi-class classification
- Training data doimiy o'zgaradi

❌ **Ishlatmaslik:**
- Katta dataset (>10,000 samples)
- High-dimensional data (>20 features)
- Real-time prediction
- Memory limited

---

## 3. Decision Tree

### 📖 Nazariya

**Ta'rif**: Daraxt strukturasida if-else qarorlar zanjiri. Har bir node'da feature bo'yicha split.

**Split Criteria**:

**Gini Impurity**:
$$Gini = 1 - \sum_{i=1}^{C} p_i^2$$

**Entropy (Information Gain)**:
$$Entropy = -\sum_{i=1}^{C} p_i \log_2(p_i)$$

- **Gini**: 0 (pure) - 0.5 (max impurity for binary)
- **Entropy**: 0 (pure) - 1 (max impurity for binary)

### ✅ Afzalliklari

- Juda interpretable (tushunarli)
- No scaling needed!
- Non-linear relationships
- Feature interactions handle
- Mixed data types (numerical + categorical)
- Automatic feature selection

### ❌ Kamchiliklari

- Overfitting (regularization kerak)
- Unstable (data o'zgarsa, tree juda o'zgaradi)
- Biased to dominant classes
- Linear boundaries only (parallel to axes)

### 🔧 Hyperparameters

| Parameter | Default | Tavsiya | Izoh |
|-----------|---------|---------|------|
| `max_depth` | `None` | `3` - `10` | Daraxt chuqurligi |
| `min_samples_split` | `2` | `2` - `20` | Split uchun minimal samples |
| `min_samples_leaf` | `1` | `1` - `10` | Leaf'da minimal samples |
| `criterion` | `'gini'` | `'gini'` yoki `'entropy'` | Split mezonи |
| `max_features` | `None` | `'sqrt'`, `'log2'` | Har bir split'da feature'lar soni |

### 💻 Code Example

```python
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Model (No scaling needed!)
dt = DecisionTreeClassifier(
    criterion='gini',
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
)

# Training
dt.fit(X_train, y_train)

# Prediction
y_pred = dt.predict(X_test)

# Visualization
plt.figure(figsize=(20, 10))
plot_tree(dt, 
          feature_names=feature_names,
          class_names=class_names,
          filled=True,
          rounded=True)
plt.show()

# Feature Importance
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'importance': dt.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance)

# Hyperparameter Tuning
from sklearn.model_selection import GridSearchCV

param_grid = {
    'max_depth': [3, 5, 7, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['gini', 'entropy']
}

grid_search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy'
)

grid_search.fit(X_train, y_train)
print("Best params:", grid_search.best_params_)
```

### 🎯 Qachon ishlatish?

✅ **Ishlatish:**
- Interpretability juda muhim
- Feature interactions
- Mixed data types
- No preprocessing vaqti yo'q
- Feature importance kerak

❌ **Ishlatmaslik:**
- High accuracy kerak (overfitting)
- Unstable model muammo
- Linear relationship (Logistic better)

---

## 4. Random Forest

### 📖 Nazariya

**Ta'rif**: Ko'plab Decision Tree'larni ensemble qiladi (Bagging).

**Algoritm**:
1. **Bootstrap**: Random sample with replacement
2. **Random Feature Selection**: Har bir split'da random feature'lar
3. **Build Trees**: Har bir bootstrap sample'da tree qurish
4. **Voting**: Barcha tree'lar voting (majority)

**Formula**:
$$\hat{y} = mode(\{h_1(x), h_2(x), ..., h_T(x)\})$$

### ✅ Afzalliklari

- High accuracy
- Overfitting'ni kamaytiradi
- Feature importance
- Outlier'larga robust
- No scaling needed
- Missing values handle
- Parallel processing

### ❌ Kamchiliklari

- Less interpretable
- More memory
- Slower prediction
- Hyperparameter tuning qiyin

### 🔧 Hyperparameters

| Parameter | Default | Tavsiya | Izoh |
|-----------|---------|---------|------|
| `n_estimators` | `100` | `100` - `500` | Tree'lar soni |
| `max_depth` | `None` | `10` - `30` | Har bir tree chuqurligi |
| `min_samples_split` | `2` | `2` - `10` | Split uchun minimal samples |
| `min_samples_leaf` | `1` | `1` - `5` | Leaf'da minimal samples |
| `max_features` | `'sqrt'` | `'sqrt'`, `'log2'` | Random feature'lar soni |
| `bootstrap` | `True` | `True` | Bootstrap sampling |

### 💻 Code Example

```python
from sklearn.ensemble import RandomForestClassifier

# Model (No scaling needed!)
rf = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    max_features='sqrt',
    random_state=42,
    n_jobs=-1  # Parallel processing
)

# Training
rf.fit(X_train, y_train)

# Prediction
y_pred = rf.predict(X_test)
y_pred_proba = rf.predict_proba(X_test)

# Feature Importance
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)

print(feature_importance.head(10))

# Hyperparameter Tuning
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'max_features': ['sqrt', 'log2']
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(X_train, y_train)
print("Best params:", grid_search.best_params_)
```

### 🎯 Qachon ishlatish?

✅ **Ishlatish:**
- High accuracy kerak
- Overfitting muammo
- Feature importance kerak
- Complex patterns
- No preprocessing vaqti yo'q

❌ **Ishlatmaslik:**
- Interpretability muhim
- Memory limited
- Real-time prediction (slow)
- Linear relationship (Logistic better)

---

## Model Selection Guide

### Quick Decision Tree 🌳

```
Interpretability juda muhimmi?
├─ Ha → Decision Tree yoki Logistic Regression
└─ Yo'q
    └─ Linear relationshipmi?
        ├─ Ha → Logistic Regression
        └─ Yo'q
            └─ Dataset kattaligi?
                ├─ Kichik (<5000) → k-NN
                └─ Katta (>5000) → Random Forest
```

### Detailed Comparison

| Feature | Logistic | k-NN | Decision Tree | Random Forest |
|---------|----------|------|---------------|---------------|
| **Interpretability** | ✅ ✅ ✅ | ✅ ✅ | ✅ ✅ ✅ | ❌ |
| **Speed (Training)** | ✅ ✅ ✅ | ✅ ✅ ✅ | ✅ ✅ | ❌ |
| **Speed (Prediction)** | ✅ ✅ ✅ | ❌ | ✅ ✅ ✅ | ✅ |
| **Accuracy** | ✅ ✅ | ✅ ✅ | ✅ ✅ | ✅ ✅ ✅ |
| **Overfitting** | ✅ ✅ | ✅ | ❌ | ✅ ✅ |
| **Non-linear** | ❌ | ✅ ✅ ✅ | ✅ ✅ ✅ | ✅ ✅ ✅ |
| **Scaling needed** | ✅ | ✅ | ❌ | ❌ |
| **Feature importance** | ✅ ✅ | ❌ | ✅ ✅ ✅ | ✅ ✅ ✅ |
| **Missing values** | ❌ | ❌ | ✅ | ✅ |
| **Large dataset** | ✅ ✅ ✅ | ❌ | ✅ ✅ | ✅ ✅ |
| **High dimensions** | ✅ | ❌ | ✅ | ✅ |

---

## Evaluation Metrics

### Confusion Matrix

```
                Predicted
                Pos    Neg
Actual  Pos     TP     FN
        Neg     FP     TN
```

- **TP (True Positive)**: To'g'ri positive bashorat
- **TN (True Negative)**: To'g'ri negative bashorat
- **FP (False Positive)**: Noto'g'ri positive (Type I error)
- **FN (False Negative)**: Noto'g'ri negative (Type II error)

### Metrics Formulas

**Accuracy**:
$$Accuracy = \frac{TP + TN}{TP + TN + FP + FN}$$

- **Ishlatish**: Balanced dataset
- **Ishlatmaslik**: Imbalanced dataset

**Precision**:
$$Precision = \frac{TP}{TP + FP}$$

- "Positive deb aytgan narsalarimning nechtasi to'g'ri?"
- **Ishlatish**: False Positive qimmat (email spam detection)

**Recall (Sensitivity)**:
$$Recall = \frac{TP}{TP + FN}$$

- "Haqiqiy positive'larning nechtasini topdim?"
- **Ishlatish**: False Negative qimmat (disease detection)

**F1-Score**:
$$F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}$$

- Precision va Recall'ning harmonic mean
- **Ishlatish**: Imbalanced dataset

**Specificity**:
$$Specificity = \frac{TN}{TN + FP}$$

### ROC Curve va AUC

- **ROC**: True Positive Rate vs False Positive Rate
- **AUC**: Area Under Curve (0.5 - 1.0)
  - 0.5: Random classifier
  - 1.0: Perfect classifier
  - >0.9: Excellent
  - 0.8-0.9: Good
  - 0.7-0.8: Fair

### Code Example

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_curve, auc
)
import seaborn as sns

# Basic Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Classification Report
print(classification_report(y_test, y_pred))

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.plot(fpr, tpr, label=f'AUC = {roc_auc:.3f}')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.show()
```

---

## Code Cheat Sheet

### Complete Pipeline

```python
# 1. Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 2. Load Data
df = pd.read_csv('data.csv')
X = df.drop('target', axis=1)
y = df['target']

# 3. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Scaling (for Logistic and k-NN)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Models
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'k-NN': KNeighborsClassifier(n_neighbors=5),
    'Decision Tree': DecisionTreeClassifier(max_depth=5),
    'Random Forest': RandomForestClassifier(n_estimators=100)
}

# 6. Train and Evaluate
results = {}
for name, model in models.items():
    # Use scaled data for Logistic and k-NN
    if name in ['Logistic Regression', 'k-NN']:
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
    
    results[name] = {
        'Accuracy': accuracy_score(y_test, y_pred),
        'Model': model
    }

# 7. Compare
results_df = pd.DataFrame(results).T
print(results_df.sort_values('Accuracy', ascending=False))
```

### Hyperparameter Tuning Template

```python
# GridSearchCV template
param_grid = {
    'parameter1': [value1, value2, value3],
    'parameter2': [value1, value2]
}

grid_search = GridSearchCV(
    estimator=Model(),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)

print("Best params:", grid_search.best_params_)
print("Best CV score:", grid_search.best_score_)
print("Test score:", grid_search.score(X_test, y_test))

# Best model
best_model = grid_search.best_estimator_
```

---

## 📊 Best Practices

### 1. Data Preprocessing
- ✅ Handle missing values
- ✅ Encode categorical variables
- ✅ Scale features (Logistic, k-NN)
- ✅ Handle outliers
- ✅ Feature engineering

### 2. Model Selection
- ✅ Oddiydan boshlang (Logistic Regression)
- ✅ Baseline model yarating
- ✅ Bir nechta model sinab ko'ring
- ✅ Cross-validation qiling

### 3. Evaluation
- ✅ Train/validation/test split
- ✅ Multiple metrics ishlatang
- ✅ Confusion matrix tahlil qiling
- ✅ ROC curve chizing
- ✅ Feature importance ko'ring

### 4. Optimization
- ✅ Hyperparameter tuning (GridSearchCV)
- ✅ Feature selection
- ✅ Ensemble methods
- ✅ Cross-validation

### 5. Deployment
- ✅ Model save qiling (pickle, joblib)
- ✅ Documentation yozing
- ✅ Error handling
- ✅ Monitoring

---

## 🚀 Quick Start Template

```python
# Minimal working example
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
```

---

## 📚 Resources

### Official Documentation
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [k-NN](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
- [Decision Tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

### Books
- "Hands-On Machine Learning" - Aurélien Géron
- "The Elements of Statistical Learning" - Hastie et al.
- "Pattern Recognition and Machine Learning" - Christopher Bishop

### Online Courses
- Coursera: Machine Learning by Andrew Ng
- Fast.ai: Practical Deep Learning
- Kaggle: Intro to Machine Learning

---

## 💡 Tips & Tricks

### Logistic Regression
```python
# Regularization strength
C_values = [0.001, 0.01, 0.1, 1, 10, 100]
# Kichik C = kuchli regularization = simple model
```

### k-NN
```python
# k ni doim toq son tanlang (binary classification)
k = 5  # ✅ Yaxshi
k = 4  # ❌ Tie bo'lishi mumkin

# Distance weighting
weights='distance'  # Yaqinroq nuqtalar ko'proq muhim
```

### Decision Tree
```python
# Overfitting prevention
dt = DecisionTreeClassifier(
    max_depth=5,          # Tree chuqurligini cheklash
    min_samples_split=20, # Katta node'larnigina split qilish
    min_samples_leaf=10   # Kichik leaf'larga yo'l qo'ymaslik
)
```

### Random Forest
```python
# n_estimators ko'p = yaxshi, lekin sekin
rf = RandomForestClassifier(
    n_estimators=100,  # 100-500 oralig'i yaxshi
    max_features='sqrt',  # Random feature selection
    n_jobs=-1  # Parallel processing
)
```

---

**🎉 Endi siz Classification Models bo'yicha to'liq qo'llanmaga egasiz!**

*Last updated: 2024*
