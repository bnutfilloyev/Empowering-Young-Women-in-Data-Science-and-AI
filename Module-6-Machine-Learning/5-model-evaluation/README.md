# 5-dars: Model Baholash (Model Evaluation)

## 📚 Modulning Maqsadi

Ushbu modulda siz machine learning modellarini qanday to'g'ri baholash va test qilishni o'rganasiz. Model yaratish muhim, lekin uni to'g'ri baholash yanada muhimroq!

---

## 🎯 Nima O'rganamiz?

### 1️⃣ Train/Test Split
- **Train set**: Model o'rganish uchun
- **Test set**: Model baholash uchun
- **Validation set**: Hyperparameter tuning uchun
- Optimal split ratio (80/20, 70/30, 60/20/20)

### 2️⃣ Cross-Validation
- **K-Fold Cross-Validation**: Ma'lumotlarni K qismga bo'lish
- **Stratified K-Fold**: Class balance saqlab qolish
- **Leave-One-Out (LOO)**: Kichik dataset uchun
- **Time Series Split**: Vaqt seriyali ma'lumotlar uchun

### 3️⃣ Overfitting va Underfitting
- **Overfitting** (Overlearning): Training data'ga juda ko'p moslashish
- **Underfitting**: Yetarli darajada o'rganmaslik
- **Bias-Variance Trade-off**: Muvozanatni topish
- Overfitting'ni oldini olish (Regularization, Early Stopping, Dropout)

### 4️⃣ Classification Metrics
- **Confusion Matrix**: TP, TN, FP, FN
- **Accuracy**: Umumiy to'g'rilik
- **Precision**: Positive prediction to'g'riligi
- **Recall (Sensitivity)**: Barcha positive'larni topish
- **F1-Score**: Precision va Recall'ning harmonik o'rtachasi
- **Specificity**: True Negative Rate

### 5️⃣ ROC Curve va AUC
- **ROC Curve**: Receiver Operating Characteristic
- **AUC**: Area Under Curve (0-1)
- **Threshold tuning**: Optimal chegarani topish
- Multi-class ROC

### 6️⃣ Regression Metrics
- **MAE** (Mean Absolute Error)
- **MSE** (Mean Squared Error)
- **RMSE** (Root Mean Squared Error)
- **R² Score**: Model qanchalik yaxshi tushuntiradi
- **Adjusted R²**: Feature'lar sonini hisobga olish

---

## 📊 Real-World Dasturlar

### Medical Diagnosis (Tibbiy Diagnostika)
- **Masala**: Kasallikni aniqlash (cancer detection)
- **Muhim metric**: **Recall** - barcha kasallarni topish kerak!
- **Xavf**: False Negative (kasalni o'tkazib yuborish) juda xavfli

### Spam Detection (Spam Filtrlash)
- **Masala**: Email spam yoki yo'qligi
- **Muhim metric**: **Precision** - yaxshi emailni spam deb belgilamaslik
- **Xavf**: False Positive (yaxshi emailni spam qilish) yomon

### Credit Scoring (Kredit Reytingi)
- **Masala**: Kredit berish yoki bermaslik
- **Muhim metric**: **F1-Score** - Precision va Recall balans
- **Xavf**: Yaxshi mijozga kredit bermaslik yoki yomon mijozga berish

### Customer Churn Prediction
- **Masala**: Mijoz ketadimi?
- **Muhim metric**: **ROC-AUC** - threshold'ni sozlash
- **Xavf**: Mijozlarni yo'qotish

---

## 🔑 Asosiy Kontseptsiyalar

### Confusion Matrix (Classification uchun)

```
                    Predicted
                Positive  Negative
Actual Positive    TP        FN
       Negative    FP        TN
```

- **TP (True Positive)**: To'g'ri positive deb aniqlangan
- **TN (True Negative)**: To'g'ri negative deb aniqlangan
- **FP (False Positive)**: Noto'g'ri positive (Type I Error)
- **FN (False Negative)**: Noto'g'ri negative (Type II Error)

### Metrics Formulalari

**Accuracy** (To'g'rilik):
$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

**Precision** (Aniqlik):
$$\text{Precision} = \frac{TP}{TP + FP}$$

**Recall/Sensitivity** (Sezgirlik):
$$\text{Recall} = \frac{TP}{TP + FN}$$

**F1-Score** (Harmonik o'rtacha):
$$F1 = 2 \cdot \frac{\text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$

**Specificity** (True Negative Rate):
$$\text{Specificity} = \frac{TN}{TN + FP}$$

---

## 📈 Overfitting vs Underfitting

| **Xususiyat** | **Underfitting** | **Good Fit** | **Overfitting** |
|---------------|------------------|--------------|-----------------|
| **Training Error** | Yuqori 📈 | Past ✅ | Juda past 📉 |
| **Test Error** | Yuqori 📈 | Past ✅ | Yuqori 📈 |
| **Model Complexity** | Juda oddiy | Optimal ✅ | Juda murakkab |
| **Sabab** | Kam feature, oddiy model | Balans ✅ | Ko'p feature, murakkab |
| **Yechim** | Ko'proq feature, murakkab model | - | Regularization, ko'proq data |

---

## 🎯 Qaysi Metric Qachon?

### Balanced Dataset (50-50)
- **Accuracy** ✅ - sodda va tushunarli

### Imbalanced Dataset (95-5)
- **Precision, Recall, F1** ✅ - accuracy misleading
- **ROC-AUC** ✅ - threshold-independent

### Medical/Critical
- **Recall** ✅ - barcha kasallarni topish muhim
- High Recall, Low Precision OK (False Alarm yaxshi, Missed Detection yomon)

### Spam/Fraud Detection
- **Precision** ✅ - yaxshi emailni spam qilmaslik
- High Precision, Low Recall OK (Ba'zi spam o'tib ketsin, lekin yaxshi email spam bo'lmasin)

### Multi-class Classification
- **Macro-F1** ✅ - har bir class uchun F1 o'rtachasi
- **Weighted-F1** ✅ - class balance hisobga olinadi

---

## 🛠️ Kutubxonalar

```python
# Scikit-learn
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report,
    roc_curve, roc_auc_score, auc
)

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 📝 Darslar

### [lecture.ipynb](lecture.ipynb)
To'liq nazariy va amaliy dars:
- Train/Test/Validation Split
- Cross-Validation (K-Fold, Stratified, LOO)
- Overfitting/Underfitting visualizations
- Confusion Matrix va barcha metrics
- ROC Curve va AUC
- Real datasets bilan misollar

### [practical.ipynb](practical.ipynb)
Amaliy mashqlar:
- Medical diagnosis dataset
- Spam detection
- Credit scoring
- Model comparison

### [homework.md](homework.md)
Uyga vazifa:
- Train/test split va evaluation
- Cross-validation implementation
- Metrics calculation va interpretation
- Overfitting detection va fixing

### [evaluation_guide.md](evaluation_guide.md)
Tez qo'llanma:
- Metrics cheat sheet
- Kod templates
- Common mistakes
- Best practices

---

## 🎓 O'rganish Natijalari

Ushbu modulni tugatgandan so'ng siz:

✅ Train/Test/Validation split'ni to'g'ri qo'llay olasiz  
✅ Cross-validation'dan foydalanib modelni baholaysiz  
✅ Overfitting va Underfitting'ni aniqlay olasiz  
✅ Confusion Matrix'ni tushunasiz va qo'llaysiz  
✅ Accuracy, Precision, Recall, F1 farqini bilasiz  
✅ ROC Curve va AUC'ni interpretatsiya qilasiz  
✅ Har xil vazifa uchun to'g'ri metric tanlaysiz  
✅ Model performance'ni yaxshilaysiz  

---

## 📚 Qo'shimcha Resurslar

### Documentation:
- [Scikit-learn Model Selection](https://scikit-learn.org/stable/model_selection.html)
- [Scikit-learn Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html)

### Tutorials:
- [Cross-Validation Tutorial](https://machinelearningmastery.com/k-fold-cross-validation/)
- [ROC and AUC Explained](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)
- [Confusion Matrix Guide](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)

### Videos:
- [StatQuest: Cross-Validation](https://www.youtube.com/watch?v=fSytzGwwBVw)
- [StatQuest: ROC and AUC](https://www.youtube.com/watch?v=4jRBRDbJemM)

---

## ⚡ Quick Start

```python
# Basic train/test split va evaluation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
```

---

**Keyingi qadam**: [lecture.ipynb](lecture.ipynb) dan boshlang! 🚀

---

## 👨‍🏫 Muallif

**AI & Data Science Course**  
📧 Email: instructor@example.com  
📅 Sana: 2024

---

**Good luck with Model Evaluation! 🎯📊**
