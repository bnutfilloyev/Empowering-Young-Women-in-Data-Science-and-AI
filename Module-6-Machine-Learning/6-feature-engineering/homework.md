# 📝 Feature Engineering - Uyga Vazifa

## 🎯 Maqsad
Feature engineering texnikalarini real-world dataset'larda mustaqil ravishda qo'llash va model performance'ni yaxshilash.

---

## 📋 Vazifalar

### ✅ Task 1: Feature Selection Championship (30 ball)

**Dataset:** Your choice (Kaggle, UCI, workspace'dagi diabetes.csv)

**Requirements:**
1. High-dimensional dataset tanlang (20+ features)
2. 3 ta selection usulini qo'llang:
   - Filter: SelectKBest, Variance Threshold, Correlation
   - Wrapper: RFE with 2 different models
   - Embedded: L1 (Lasso), Random Forest importance
3. Har bir usul uchun:
   - Selected features list
   - Model accuracy (5-fold CV)
   - Training time
4. Comparison table yarating
5. Best method justification yozing

**Deliverables:**
- `task1_feature_selection.ipynb`
- Results DataFrame
- Visualization (bar chart, heatmap)
- 200-word analysis

**Grading:**
- Code quality (10)
- All 3 methods implemented (10)
- Comparison & analysis (10)

---

### ✅ Task 2: Scaling Deep Dive (25 ball)

**Dataset:** California Housing or similar regression dataset

**Requirements:**
1. Test 5 scalers:
   - StandardScaler
   - MinMaxScaler
   - RobustScaler
   - MaxAbsScaler
   - Log Transform + StandardScaler
2. Test on 4 algorithms:
   - Linear Regression
   - KNN Regressor
   - SVR
   - Decision Tree Regressor
3. Create 4x5 heatmap (model vs scaler)
4. Analyze:
   - Which model benefits most from scaling?
   - Best scaler for outliers?
   - Performance difference quantification

**Deliverables:**
- `task2_scaling_analysis.ipynb`
- Heatmap visualization
- Insights document (150 words)

**Grading:**
- Implementation (12)
- Visualization (8)
- Analysis (5)

---

### ✅ Task 3: Feature Creation Mastery (25 ball)

**Dataset:** Create your own or use E-commerce/Finance dataset

**Requirements:**
1. Create 10+ new features:
   - **Polynomial**: x², x³, x₁×x₂
   - **Ratios**: Income/Age, Spending/Income
   - **Binning**: Age groups, Income brackets
   - **Date/Time**: Year, Month, DayOfWeek, IsWeekend
   - **Aggregations**: Total, Mean, Count per group
   - **Domain-specific**: BMI, Density, etc.
2. Compare models:
   - Before FE
   - After FE
3. Feature importance analysis
4. Document which features helped most

**Deliverables:**
- `task3_feature_creation.ipynb`
- Feature engineering functions
- Before/After comparison
- Feature importance plot

**Grading:**
- Creativity (10)
- Implementation (10)
- Impact analysis (5)

---

### ✅ Task 4: Encoding Showdown (20 ball)

**Dataset:** Mixed data with categorical variables

**Requirements:**
1. Apply ALL encoding methods:
   - Label Encoding
   - One-Hot Encoding
   - Target Encoding (with proper CV!)
   - Frequency Encoding
   - Binary Encoding (bonus)
2. Test each encoding with:
   - Logistic Regression
   - Random Forest
3. Handle high-cardinality feature (15+ categories)
4. Compare memory usage

**Deliverables:**
- `task4_encoding.ipynb`
- Encoding comparison table
- Memory usage analysis

**Grading:**
- All encodings (12)
- High-cardinality handling (5)
- Analysis (3)

---

## 🌟 Bonus Tasks (20 ball qo'shimcha)

### Bonus 1: AutoFE - Automated Feature Engineering (10 ball)

Create Python function:
```python
def auto_feature_engineer(df, target_col, task='classification'):
    """
    Automatically apply best FE practices
    
    Returns:
        - Engineered DataFrame
        - Feature importance
        - Performance improvement report
    """
    pass
```

**Requirements:**
- Auto-detect numerical/categorical
- Auto-create features (polynomial, ratios)
- Auto-select best features
- Auto-scale
- Return complete pipeline

---

### Bonus 2: Complete ML Pipeline with FE (10 ball)

**Requirements:**
1. Real dataset (Kaggle competition)
2. Complete pipeline:
   ```
   Raw Data → EDA → FE → Selection → Scaling → Model → Evaluation
   ```
3. Compare 5+ pipelines
4. Hyperparameter tuning
5. Final test set evaluation
6. Deployment-ready code

---

## 📊 Submission Format

### Folder Structure:
```
6-feature-engineering-homework/
│
├── task1_feature_selection.ipynb
├── task2_scaling_analysis.ipynb
├── task3_feature_creation.ipynb
├── task4_encoding.ipynb
├── bonus_tasks.ipynb (optional)
│
├── datasets/
│   └── (your datasets)
│
├── results/
│   ├── comparison_tables.csv
│   └── visualizations/
│
└── README.md
```

### README.md Template:
```markdown
# Feature Engineering Homework

## Task 1: Feature Selection
- Dataset: [name]
- Best Method: [method]
- Performance: [metric]
- Key Insight: [...]

## Task 2: Scaling
- Best Scaler: [scaler]
- Most Impacted Model: [model]
- Key Insight: [...]

## Task 3: Feature Creation
- Features Created: [count]
- Performance Improvement: [%]
- Most Important Feature: [name]

## Task 4: Encoding
- Best Encoding: [method]
- High-Cardinality Strategy: [...]

## What I Learned
- [Key takeaway 1]
- [Key takeaway 2]
- [Key takeaway 3]
```

---

## 🎓 Grading Rubric

| Task | Points | Criteria |
|------|--------|----------|
| **Task 1** | 30 | Feature selection methods, comparison, analysis |
| **Task 2** | 25 | Scaling experiments, heatmap, insights |
| **Task 3** | 25 | Feature creation creativity, impact |
| **Task 4** | 20 | Encoding methods, high-cardinality handling |
| **Code Quality** | 10 | Clean, commented, reproducible |
| **Visualizations** | 10 | Clear, professional plots |
| **Documentation** | 10 | README, comments, explanations |
| **Bonus Tasks** | +20 | Extra credit |
| **Total** | **130** | (150 with bonus) |

**Grading Scale:**
- **A+:** 120+ (92%+)
- **A:** 110-119 (85-91%)
- **B+:** 100-109 (77-84%)
- **B:** 90-99 (69-76%)
- **C:** 80-89 (62-68%)

---

## 💡 Tips & Resources

### Foydali Libraries:
```python
# Feature selection
from sklearn.feature_selection import SelectKBest, RFE, SelectFromModel, VarianceThreshold

# Scaling
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Encoding
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import category_encoders as ce  # pip install category-encoders

# Polynomial features
from sklearn.preprocessing import PolynomialFeatures
```

### Dataset Sources:
- **Kaggle:** https://www.kaggle.com/datasets
- **UCI:** https://archive.ics.uci.edu/ml/
- **Workspace:** diabetes.csv, california_housing

### Best Practices:
1. Always split data BEFORE feature engineering
2. Fit scalers only on train set
3. Use pipelines for reproducibility
4. Cross-validate to avoid overfitting
5. Document every transformation

---

## ❓ FAQ

**Q: Qaysi dataset tanlash kerak?**
A: Task requirement'ga mos: high-dimensional (Task1), regression (Task2), categorical bor (Task4)

**Q: Target encoding qanday to'g'ri qilish kerak?**
A: Cross-validation bilan! Leave-one-out yoki K-Fold ichida encode qiling.

**Q: Polynomial features overfitting qilsa?**
A: Regularization (L1/L2) yoki feature selection qo'llang.

**Q: Pipelines qanday ishlaydi?**
A: `lecture.ipynb` Section 5'ga qarang - complete example.

---

## ⏰ Deadline

**Deadline:** [Instructor sets]

**Submission:** GitHub link or ZIP file

---

## ✅ Self-Check Before Submission

- [ ] All notebooks run without errors
- [ ] All tasks completed
- [ ] Visualizations present
- [ ] Code commented
- [ ] README.md filled
- [ ] Results saved
- [ ] Datasets included or linked
- [ ] Analysis written

---

**Good luck! Feature engineering is where ML magic happens! 🎩✨**
