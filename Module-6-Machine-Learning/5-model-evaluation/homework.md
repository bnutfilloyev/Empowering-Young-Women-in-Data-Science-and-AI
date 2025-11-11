# 📝 Model Baholash - Uyga Vazifa

## 🎯 Maqsad
Model evaluation texnikalarini real dataset'larda mustaqil ravishda qo'llash va tahlil qilish ko'nikmalarini rivojlantirish.

---

## 📋 Vazifalar

### ✅ Task 1: Credit Risk Assessment (40 ball)

**Dataset:** Kaggle Credit Card Fraud Detection yoki shunga o'xshash dataset

**Vazifa:**
1. **Data Preparation (10 ball)**
   - Dataset yuklash va EDA (Exploratory Data Analysis)
   - Missing values va outliers tahlil
   - Train-Test split (80-20)
   - Feature scaling (StandardScaler)

2. **Model Training (15 ball)**
   - Kamida 5 ta classification model train qiling:
     * Logistic Regression
     * Decision Tree
     * Random Forest
     * SVM (SVC)
     * Gradient Boosting (XGBoost yoki LightGBM - bonus!)
   - Har bir model uchun hyperparameter tuning

3. **Evaluation (15 ball)**
   - Confusion Matrix har bir model uchun
   - Classification Report
   - ROC Curve va AUC comparison
   - Stratified 10-Fold Cross-Validation
   - Train vs Test metrics (overfitting check)

**Deliverables:**
- Jupyter Notebook fayli (`task1_credit_risk.ipynb`)
- Har bir modelni taqqoslash jadvali (DataFrame)
- ROC curves bitta plotda (overlay)
- Final report: Qaysi model eng yaxshi va nima uchun? (markdown cell)

**Evaluation Criteria:**
- Code sifati va tushunchasi (10 ball)
- Visualizations (10 ball)
- Analysis va insights (10 ball)
- Best model justification (10 ball)

---

### ✅ Task 2: House Price Prediction with Advanced Evaluation (30 ball)

**Dataset:** Kaggle House Prices dataset yoki California Housing

**Vazifa:**
1. **Feature Engineering (10 ball)**
   - Categorical features encoding
   - Feature creation (polynomial features, interactions)
   - Feature selection (correlation analysis)

2. **Model Training (10 ball)**
   - 4 ta regression model:
     * Linear Regression
     * Ridge Regression (with different alpha values)
     * Decision Tree Regressor
     * Random Forest Regressor
   - K-Fold Cross-Validation (k=5)

3. **Comprehensive Evaluation (10 ball)**
   - MAE, MSE, RMSE, R² barcha modellar uchun
   - Learning curves (train size vs score)
   - Residual plots
   - Actual vs Predicted scatter plots
   - Feature importance analysis (for tree-based models)

**Deliverables:**
- Jupyter Notebook (`task2_house_prices.ipynb`)
- Comprehensive evaluation report
- Best model with justified reasoning

---

### ✅ Task 3: Imbalanced Dataset Challenge (30 ball)

**Dataset:** O'zingiz tanlang (medical diagnosis, fraud detection, churn prediction)

**Vazifa:**
Bu vazifada **imbalanced dataset** bilan ishlashni o'rganasiz!

1. **Problem Analysis (5 ball)**
   - Class imbalance ratio hisoblash
   - Baseline model (Dummy Classifier) natijasi
   - Why accuracy is misleading for imbalanced data?

2. **Handling Imbalance (10 ball)**
   - 3 ta usulni qo'llang:
     * **Method 1:** Class weights adjustment (`class_weight='balanced'`)
     * **Method 2:** Resampling (SMOTE yoki undersampling)
     * **Method 3:** Threshold tuning
   - Har bir usulni taqqoslang

3. **Advanced Metrics (15 ball)**
   - Precision-Recall Curve
   - F1-Score (Macro, Weighted, Binary)
   - ROC-AUC
   - Matthews Correlation Coefficient (MCC) - bonus!
   - Cost-sensitive evaluation (FP vs FN cost)

**Deliverables:**
- Jupyter Notebook (`task3_imbalanced_data.ipynb`)
- Comparison table: 3 methods + metrics
- Recommendation: Qaysi method eng yaxshi va nima uchun?

---

## 🌟 Bonus Tasks (20 ball qo'shimcha)

### Bonus 1: Automated Model Selection Pipeline (10 ball)

**Vazifa:** Python function yozing:
```python
def auto_evaluate_models(X_train, X_test, y_train, y_test, task_type='classification'):
    """
    Automatically train and evaluate multiple models
    
    Args:
        X_train, X_test, y_train, y_test: data
        task_type: 'classification' or 'regression'
    
    Returns:
        pd.DataFrame: Results table with all metrics
        dict: Trained models
        dict: Visualizations (confusion matrix, ROC curve, etc.)
    """
    # TODO: Implement
    pass
```

**Requirements:**
- Kamida 5 ta model avtomatik train qilsin
- Cross-validation
- Barcha metrikalarni hisoblash
- Visualizations avtomatik yaratish
- Best model recommendation

---

### Bonus 2: Custom Evaluation Metric (10 ball)

**Vazifa:** O'zingizning custom metrikangizni yarating!

**Misol:** Medical diagnosis uchun:
- False Negative (missed disease) = 10x worse than False Positive
- Custom score = Precision + 10 * Recall

```python
def custom_medical_score(y_true, y_pred, fn_cost=10, fp_cost=1):
    """
    Custom metric for medical diagnosis
    """
    # TODO: Implement
    pass
```

Test qiling va qanday holatda foydali ekanini tushuntiring!

---

## 📊 Submission Format

### Folder Structure:
```
5-model-evaluation-homework/
│
├── task1_credit_risk.ipynb
├── task2_house_prices.ipynb
├── task3_imbalanced_data.ipynb
├── bonus_tasks.ipynb (optional)
│
├── datasets/
│   ├── credit_data.csv
│   ├── house_prices.csv
│   └── imbalanced_data.csv
│
├── results/
│   ├── model_comparison_task1.csv
│   ├── model_comparison_task2.csv
│   └── model_comparison_task3.csv
│
└── README.md (summary of your work)
```

### README.md qanday bo'lishi kerak:
```markdown
# Model Evaluation - Homework Report

## Task 1: Credit Risk Assessment
- Dataset: [name and source]
- Best Model: [model name]
- Best F1-Score: [score]
- Key Insights: [your analysis]

## Task 2: House Price Prediction
- Dataset: [name]
- Best Model: [model name]
- Best R²: [score]
- Key Insights: [your analysis]

## Task 3: Imbalanced Data
- Dataset: [name]
- Imbalance Ratio: [ratio]
- Best Method: [method]
- Key Insights: [your analysis]

## Bonus Tasks (if completed)
- [Description of what you did]

## What I Learned
- [Key takeaways from homework]
```

---

## ⏰ Deadline va Submission

**Deadline:** [Instructor sets deadline]

**Submission:**
1. GitHub repository link yuboring
2. Yoki ZIP file ko'rinishida
3. Barcha code'lar run qilinishi kerak (no errors!)

---

## 🎓 Grading Rubric

| Criteria | Points | Description |
|----------|--------|-------------|
| **Code Quality** | 20 | Clean, commented, reproducible |
| **Task 1** | 40 | Credit risk assessment |
| **Task 2** | 30 | House price prediction |
| **Task 3** | 30 | Imbalanced data handling |
| **Visualizations** | 20 | Clear, professional plots |
| **Analysis** | 20 | Insightful interpretations |
| **Documentation** | 10 | README and comments |
| **Bonus Tasks** | +20 | Extra credit |
| **Total** | **150** | (170 with bonus) |

**Grading Scale:**
- **A+:** 140+ (93%+)
- **A:** 130-139 (87-92%)
- **B+:** 120-129 (80-86%)
- **B:** 110-119 (73-79%)
- **C+:** 100-109 (67-72%)
- **C:** 90-99 (60-66%)

---

## 💡 Hints va Resources

### Foydali Libraries:
```python
# Imbalanced data uchun
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

# Hyperparameter tuning
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Advanced metrics
from sklearn.metrics import matthews_corrcoef, precision_recall_curve

# Gradient Boosting
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
```

### Datasets Resources:
- **Kaggle:** https://www.kaggle.com/datasets
- **UCI ML Repository:** https://archive.ics.uci.edu/ml/
- **Scikit-learn Datasets:** `from sklearn.datasets import load_*`

### Useful Links:
- [Scikit-learn Metrics Documentation](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [Imbalanced-learn Tutorial](https://imbalanced-learn.org/stable/)
- [ROC Curve Explanation](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)

---

## ❓ FAQ

**Q1: Dataset qayerdan topish mumkin?**
- A: Kaggle, UCI ML Repository, yoki workspace'dagi mavjud datasetlardan foydalaning.

**Q2: Hyperparameter tuning qilish kerakmi?**
- A: Task 1 da kerak, boshqa tasklarda bonus.

**Q3: Notebook'lar run qilinmasa qanday qilaman?**
- A: Notebook ustida "Restart Kernel and Run All Cells" qiling va xatoliklarni to'g'rilang.

**Q4: Bonus tasklar majburiyatmi?**
- A: Yo'q, lekin qo'shimcha ball olasiz (+20 ball).

**Q5: Cross-validation qaysi taskda kerak?**
- A: Barcha tasklarda tavsiya etiladi, Task 1 da majburiy.

---

## ✅ Self-Check Before Submission

- [ ] Barcha notebooks run qilinadi (no errors)
- [ ] Har bir cell natijasi ko'rsatilgan
- [ ] Visualizations chizilgan va labels bor
- [ ] Code commented (kamida key steps)
- [ ] README.md yozilgan
- [ ] Results fayllar saqlangan
- [ ] Dataset'lar yoki linklar qo'shilgan
- [ ] Best model justification yozilgan
- [ ] GitHub/ZIP ready for submission

---

## 🚀 Good Luck!

**Esda tuting:**
> *"The goal is not just to complete the tasks, but to deeply understand model evaluation and develop critical thinking skills for real-world ML projects!"*

Savollaringiz bo'lsa, bemalol so'rang! 💪

---

**Instructor:** [Your Name]  
**Contact:** [Your Email/Telegram]  
**Office Hours:** [Time]
