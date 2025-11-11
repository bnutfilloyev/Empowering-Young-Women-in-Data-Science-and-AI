# 🔧 Feature Engineering va Scaling

## 📚 Modulga Kirish

**Feature Engineering** - Machine Learning dagi eng muhim bosqichlardan biri! Raw data'ni modellar uchun optimal formatga keltirish san'ati.

> *"Applied machine learning is basically feature engineering."* - Andrew Ng

---

## 🎯 O'rganish Maqsadlari

Ushbu modulda siz quyidagilarni o'rganasiz:

1. ✅ **Feature Engineering** asoslari
2. ✅ **Feature Selection** texnikalari
3. ✅ **Feature Scaling** metodlari
4. ✅ **Feature Creation** usullari
5. ✅ **Encoding** texnikalari
6. ✅ **Pipeline** building

---

## 📖 Mavzu Tarkibi

### 1. Feature Engineering Nima?

Feature Engineering - raw data'dan ML modellar uchun optimal features yaratish jarayoni.

**Nega muhim?**
- ✅ Model performance'ni sezilarli yaxshilaydi
- ✅ Training time'ni kamaytiradi
- ✅ Overfitting'ni kamaytiradi
- ✅ Model interpretability'ni oshiradi

**Asosiy Qismlar:**
```
Raw Data
    ↓
Feature Selection (irrelevant features'ni o'chirish)
    ↓
Feature Scaling (range normalization)
    ↓
Feature Creation (yangi features yaratish)
    ↓
Feature Encoding (categorical → numerical)
    ↓
Clean Features → Model Training
```

---

### 2. Feature Selection (Xususiyatlar Tanlash)

Eng muhim va foydali features'ni tanlash.

#### 2.1 Filter Methods
**Statistik testlar orqali features tanlash:**

| Method | Description | Use Case |
|--------|-------------|----------|
| **Variance Threshold** | Past variance'li features'ni o'chirish | Constant yoki near-constant features |
| **Correlation** | Target bilan correlation tekshirish | Linear relationships |
| **Chi-Square Test** | Categorical features uchun | Classification tasks |
| **Mutual Information** | Non-linear dependencies | Complex relationships |
| **ANOVA F-test** | Numerical features uchun | Regression tasks |

**Advantages:**
- ⚡ Tez ishlaydi
- 🔄 Model-independent
- 📊 Interpretable

**Disadvantages:**
- ❌ Feature interactions'ni e'tiborsiz qoldiradi
- ❌ Model-specific optimization yo'q

---

#### 2.2 Wrapper Methods
**Model performance orqali features tanlash:**

| Method | Algorithm | Complexity |
|--------|-----------|------------|
| **Forward Selection** | Start empty, add best feature iteratively | O(n²) |
| **Backward Elimination** | Start full, remove worst feature iteratively | O(n²) |
| **RFE (Recursive Feature Elimination)** | Iteratively remove least important | O(n × m) |
| **Exhaustive Search** | Try all combinations | O(2ⁿ) |

**Advantages:**
- ✅ Model-specific optimization
- ✅ Feature interactions hisoblanadi
- ✅ Best performance

**Disadvantages:**
- ⏰ Sekin (computationally expensive)
- 🎯 Model-dependent
- ⚠️ Overfitting xavfi

---

#### 2.3 Embedded Methods
**Model training paytida features tanlash:**

| Method | Description | Models |
|--------|-------------|--------|
| **L1 Regularization (Lasso)** | Coefficients'ni 0 ga olib boradi | Linear models |
| **Tree-based Feature Importance** | Gini/Entropy importance | Decision Trees, Random Forest |
| **Gradient Boosting Importance** | Gain-based importance | XGBoost, LightGBM, CatBoost |

**Advantages:**
- ⚡ Fast (model training bilan bir vaqtda)
- 🎯 Model-specific
- 🔄 Feature interactions hisobga olinadi

**Disadvantages:**
- 📉 Model-dependent
- 🤔 Less interpretable

---

### 3. Feature Scaling (Masshtablash)

Features'ni bir xil range'ga keltirish.

#### 3.1 Why Scaling?

**Problem:**
```python
# Without scaling
Age: [18, 25, 30, 45, 60]        # Range: 18-60
Income: [20000, 45000, 80000, 120000, 200000]  # Range: 20k-200k

# Income dominates Age in distance calculations!
```

**Need Scaling:**
- 🎯 Distance-based algorithms (KNN, SVM, K-Means)
- 🧮 Gradient Descent optimization (Linear Regression, Neural Networks)
- 🔄 Equal feature importance

**Don't Need Scaling:**
- 🌲 Tree-based algorithms (Decision Trees, Random Forest, XGBoost)

---

#### 3.2 Scaling Methods

| Method | Formula | Range | Use Case | Outliers? |
|--------|---------|-------|----------|-----------|
| **Normalization (Min-Max)** | (x - min) / (max - min) | [0, 1] | Bounded distribution, Neural Networks | ❌ Sensitive |
| **Standardization (Z-score)** | (x - μ) / σ | μ=0, σ=1 | Normal distribution, Linear models | ✅ Robust |
| **Robust Scaling** | (x - median) / IQR | Variable | Data with outliers | ✅✅ Very robust |
| **Max Abs Scaling** | x / \|x_max\| | [-1, 1] | Sparse data | ❌ Sensitive |
| **Log Transformation** | log(x + 1) | [0, ∞) | Skewed distribution | ✅ Handles skewness |

---

#### 3.3 When to Use Which Scaler?

**Decision Tree:**
```
Start
  │
  ├─ Outliers present?
  │    ├─ Yes → RobustScaler
  │    └─ No → Continue
  │
  ├─ Normal distribution?
  │    ├─ Yes → StandardScaler
  │    └─ No → Continue
  │
  ├─ Bounded range needed?
  │    ├─ Yes → MinMaxScaler
  │    └─ No → StandardScaler
  │
  ├─ Sparse data?
  │    └─ Yes → MaxAbsScaler
  │
  └─ Skewed distribution?
       └─ Yes → Log Transform → StandardScaler
```

**Algorithm-based Guide:**

| Algorithm | Best Scaler | Why? |
|-----------|-------------|------|
| **Linear Regression** | StandardScaler | Gradient descent optimization |
| **Logistic Regression** | StandardScaler | Regularization works better |
| **SVM** | StandardScaler | Distance-based |
| **KNN** | StandardScaler or MinMaxScaler | Distance calculations |
| **Neural Networks** | MinMaxScaler or StandardScaler | Activation functions |
| **Decision Trees** | None | Split-based, scale-invariant |
| **Random Forest** | None | Ensemble of trees |
| **XGBoost/LightGBM** | None | Tree-based |
| **K-Means Clustering** | StandardScaler | Distance-based |
| **PCA** | StandardScaler | Variance-based |

---

### 4. Feature Creation (Yangi Features Yaratish)

#### 4.1 Polynomial Features
Higher-order interactions:
```python
# Original: [x1, x2]
# Polynomial (degree=2): [1, x1, x2, x1², x1·x2, x2²]
```

**Use Cases:**
- Non-linear relationships
- Complex patterns
- Underfitting'ni bartaraf etish

**⚠️ Warning:** Overfitting xavfi!

---

#### 4.2 Interaction Features
Manual feature combinations:
```python
# E-commerce example
Total_Spent = Quantity × Price
BMI = Weight / (Height²)
Age_Income_Interaction = Age × Income
```

**Domain Knowledge Required!**

---

#### 4.3 Date/Time Features
Datetime'dan multiple features:
```python
# From: 2024-03-15 14:30:00
Year = 2024
Month = 3
Day = 15
DayOfWeek = Friday (4)
Hour = 14
IsWeekend = False
Quarter = Q1
```

---

#### 4.4 Aggregation Features
Group statistics:
```python
# Customer transactions
Total_Purchases = COUNT(transactions)
Average_Amount = MEAN(amount)
Max_Purchase = MAX(amount)
Days_Since_Last = TODAY - MAX(date)
```

---

### 5. Feature Encoding (Kategorik → Numerical)

#### 5.1 Label Encoding
Ordinal categories:
```python
# Education: ['High School', 'Bachelor', 'Master', 'PhD']
# Encoded:   [0, 1, 2, 3]
```

**✅ Use when:** Ordinal relationship exists  
**❌ Don't use when:** Nominal categories (no order)

---

#### 5.2 One-Hot Encoding
Nominal categories:
```python
# Color: ['Red', 'Green', 'Blue']
# Encoded:
#   Color_Red  Color_Green  Color_Blue
#      1           0            0
#      0           1            0
#      0           0            1
```

**✅ Use when:** Nominal categories  
**❌ Don't use when:** High cardinality (>10-15 categories)

---

#### 5.3 Target Encoding
Mean target per category:
```python
# City: ['NY', 'LA', 'SF']
# Target (Salary):
# NY → mean(salary for NY) = 85000
# LA → mean(salary for LA) = 78000
# SF → mean(salary for SF) = 95000
```

**✅ Use when:** High cardinality categories  
**⚠️ Warning:** Data leakage risk! Use cross-validation.

---

#### 5.4 Frequency Encoding
Count per category:
```python
# Category: ['A', 'B', 'A', 'C', 'A', 'B']
# Encoded:  [3,   2,   3,   1,   3,   2]
```

**✅ Use when:** Frequency is informative

---

#### 5.5 Binary Encoding
Combination of Label + One-Hot:
```python
# For high cardinality (memory efficient)
# Category: [0, 1, 2, 3, 4, 5, 6, 7]
# Binary:
#   Bit_0  Bit_1  Bit_2
#     0      0      0    (0)
#     0      0      1    (1)
#     0      1      0    (2)
#     ...
```

---

### 6. Complete Feature Engineering Pipeline

```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Define transformers
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Full pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('feature_selection', SelectKBest(k=10)),
    ('classifier', RandomForestClassifier())
])
```

---

## 📊 Feature Engineering Impact

### Before vs After Example:

| Scenario | Without FE | With FE | Improvement |
|----------|-----------|---------|-------------|
| Customer Churn | Accuracy: 75% | Accuracy: 88% | **+13%** |
| House Prices | R²: 0.65 | R²: 0.82 | **+26%** |
| Credit Risk | F1: 0.62 | F1: 0.79 | **+27%** |

**Key Insight:** Good feature engineering >> Complex model!

---

## 🎯 Best Practices

### ✅ DO:
1. **Start with EDA** - Understand your data first
2. **Domain knowledge** - Leverage subject matter expertise
3. **Iterative process** - Test, measure, improve
4. **Document everything** - Track transformations
5. **Validate on test set** - Avoid data leakage
6. **Use pipelines** - Reproducibility and deployment
7. **Feature selection early** - Reduce dimensionality
8. **Cross-validate** - Robust evaluation

### ❌ DON'T:
1. **Data leakage** - Never fit on test data
2. **Blind transformation** - Understand why you transform
3. **Over-engineer** - Simple is better
4. **Ignore outliers** - Handle them properly
5. **Forget scaling** - Critical for many algorithms
6. **One-size-fits-all** - Different problems need different approaches
7. **Skip validation** - Always check impact
8. **Ignore domain** - Features should make business sense

---

## 🗂️ Module Resources

### Files:
1. **README.md** - Ushbu file (overview)
2. **lecture.ipynb** - Detailed lecture with code examples
3. **practical.ipynb** - Hands-on exercises
4. **homework.md** - Assignments
5. **feature_engineering_guide.md** - Quick reference cheat sheet

---

## 📚 Learning Path

```
1. Read README.md (30 min) ← You are here
       ↓
2. Study lecture.ipynb (2-3 hours)
       ↓
3. Practice practical.ipynb (2-3 hours)
       ↓
4. Complete homework.md (5-7 hours)
       ↓
5. Keep feature_engineering_guide.md handy!
```

---

## 🔗 Key Takeaways

1. **Feature Engineering** is often more important than model choice
2. **Feature Selection** reduces dimensionality and improves performance
3. **Feature Scaling** is critical for distance-based and gradient-based algorithms
4. **Feature Creation** requires domain knowledge and creativity
5. **Feature Encoding** converts categorical data to numerical
6. **Pipelines** ensure reproducibility and prevent data leakage
7. **Validation** is crucial - always measure impact on test set

---

## 📈 Impact on Model Performance

```
Raw Data → [Feature Engineering] → Better Data → [Model Training] → Better Model

Where Feature Engineering includes:
- Selection (remove noise)
- Scaling (normalize ranges)
- Creation (add information)
- Encoding (proper format)
```

**Remember:** 
> *"Garbage in, garbage out. Better features in, better predictions out!"* 🚀

---

## 🎓 Next Steps

After completing this module, you will be able to:
- ✅ Select most relevant features using various techniques
- ✅ Scale features appropriately for different algorithms
- ✅ Create new features from existing data
- ✅ Encode categorical variables correctly
- ✅ Build complete preprocessing pipelines
- ✅ Avoid common pitfalls (data leakage, over-fitting)
- ✅ Improve model performance significantly

**Ready to start?** Open `lecture.ipynb`! 📖

---

**Version:** 1.0  
**Last Updated:** November 2024  
**Module:** 6 - Machine Learning Foundations
