# 3-dars: Classification Modellar

## Mavzu maqsadi
Bu darsda siz classification (tasniflash) modellarining asosiy turlarini o'rganasiz va real ma'lumotlarda qo'llaysiz.

## O'rganilayotgan mavzular

### 1. Logistic Regression
- Binary Classification
- Sigmoid funksiya
- Decision boundary
- Multiclass classification (One-vs-Rest, Softmax)
- Regularization (L1, L2)

### 2. k-Nearest Neighbors (k-NN)
- Distance metrics (Euclidean, Manhattan, Minkowski)
- k parametrini tanlash
- Weighted k-NN
- Advantages va Disadvantages
- Scaling muhimligi

### 3. Decision Tree
- Entropy va Information Gain
- Gini Impurity
- Tree pruning
- Overfitting muammosi
- Feature importance
- Visualization

### 4. Random Forest
- Ensemble learning
- Bagging
- Out-of-Bag (OOB) error
- Feature importance
- Hyperparameter tuning
- Advantages over single Decision Tree

### 5. Model Evaluation
- Confusion Matrix
- Accuracy, Precision, Recall, F1-Score
- ROC Curve va AUC
- Precision-Recall Curve
- Cross-validation
- Class imbalance handling

## Real-world Applications

### Logistic Regression:
- 🏥 Kasallik diagnostikasi (bor/yo'q)
- 📧 Spam detection
- 💳 Kredit risk baholash
- 🎯 Customer churn prediction

### k-NN:
- 🎵 Recommendation systems
- 🔍 Pattern recognition
- 📝 Handwriting recognition
- 🏷️ Product classification

### Decision Tree:
- 🏦 Loan approval
- 🌡️ Medical diagnosis
- 🎮 Game strategies
- 📊 Business decision making

### Random Forest:
- 💰 Fraud detection
- 🔬 Feature selection
- 📈 Stock market prediction
- 🌾 Agriculture (crop disease detection)

## Fayllar
- `lecture.ipynb` - Nazariy ma'lumotlar va to'liq misollar
- `practical.ipynb` - Amaliy mashg'ulotlar
- `homework.md` - Uy vazifasi
- `classification_guide.md` - Classification bo'yicha to'liq qo'llanma

## Kerakli kutubxonalar
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
    roc_curve, roc_auc_score, precision_recall_curve
)
```

## Prerequisites
- Python basics
- NumPy va Pandas
- Matplotlib/Seaborn
- Statistics asoslari
- Module 6 - Dars 1 (ML Introduction)
- Module 6 - Dars 2 (Regression Models)

## O'rganish vaqti
- Lecture: 3-4 soat
- Practical: 3-4 soat
- Homework: 6-8 soat
- **Jami: ~15 soat**

## Classification vs Regression

| Aspect | Classification | Regression |
|--------|----------------|------------|
| **Output** | Kategorik (Class labels) | Raqamli (Continuous) |
| **Examples** | Spam/Not Spam, Dog/Cat | Narx, Harorat |
| **Metrics** | Accuracy, F1, AUC | R², RMSE, MAE |
| **Algorithms** | Logistic, k-NN, Tree, RF | Linear, Ridge, Lasso |
| **Goal** | Class'ni aniqlash | Qiymatni bashorat qilish |

## Darsning Tuzilishi

### Part 1: Theory (1.5 soat)
- Classification fundamentals
- Logistic Regression matematikasi
- k-NN algoritmi
- Decision Tree tuzilishi
- Random Forest ensembles

### Part 2: Hands-on (2 soat)
- Real dataset'lar bilan ishlash
- Har bir model'ni implement qilish
- Visualization va interpretation
- Model comparison

### Part 3: Evaluation (1 soat)
- Metrics tushunish
- Confusion Matrix tahlili
- ROC va AUC
- Best model selection

## Qo'shimcha manbalar

### Documentation
- [Scikit-learn Classification](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
- [Decision Trees](https://scikit-learn.org/stable/modules/tree.html)
- [Ensemble Methods](https://scikit-learn.org/stable/modules/ensemble.html)

### Video Tutorials
- [StatQuest: Logistic Regression](https://www.youtube.com/watch?v=yIYKR4sgzI8)
- [StatQuest: Decision Trees](https://www.youtube.com/watch?v=7VeUPuFGJHk)
- [StatQuest: Random Forests](https://www.youtube.com/watch?v=J4Wdy0Wc_xQ)

### Books
- "An Introduction to Statistical Learning" - James et al.
- "Hands-On Machine Learning" - Aurélien Géron
- "Pattern Recognition and Machine Learning" - Christopher Bishop

## Learning Path

```
1. Regression Modellar ✅
   ↓
2. Classification Modellar ← Siz shu yerdasiz
   ↓
3. Advanced ML (SVM, Neural Networks)
   ↓
4. Deep Learning
   ↓
5. Real-world Projects
```

---

**Tayyor bo'lsangiz, `lecture.ipynb` ni oching va o'rganishni boshlang! 🚀**
