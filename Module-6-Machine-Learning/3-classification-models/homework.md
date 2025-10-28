# 📚 Classification Models - Uy Vazifasi

---

## 🎯 Maqsad

Bu uy vazifasida siz 4 ta Classification algoritmini real ma'lumotlar to'plamida qo'llash, taqqoslash va natijalarni tahlil qilish ko'nikmalarini rivojlantirasiz.

---

## 📊 Dataset: Titanic Survival Prediction

Siz **Titanic** ma'lumotlar to'plamidan foydalanasiz. Bu dataset Titanic kemasi halokatida qaysi yo'lovchilar omon qolgani haqida ma'lumot beradi.

### Dataset haqida:
- **891** yo'lovchi
- **11** feature (Age, Sex, Pclass, Fare, va boshqalar)
- **Target**: Survived (0 = O'ldi, 1 = Omon qoldi)

### Dataset yuklab olish:

```python
import pandas as pd

# Titanic datasetini yuklash
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
```

---

## 📝 Vazifalar

### **1-Vazifa: Ma'lumotlarni tayyorlash (20 ball)**

#### 1.1. Dataset'ni o'rganing (5 ball)
- Datasetni yuklang va birinchi 10 qatorni ko'ring
- Dataset o'lchamini va feature'larni ko'rsating
- `info()` va `describe()` funksiyalaridan foydalaning
- Target (Survived) class distribution'ni ko'rsating

#### 1.2. Missing Values (5 ball)
- Har bir feature'da nechta missing value borligini aniqlang
- Missing value'larni to'ldiring:
  - `Age`: median bilan
  - `Embarked`: mode bilan
  - `Cabin`: 'Unknown' bilan yoki o'chiring

#### 1.3. Feature Engineering (5 ball)
- `Age` dan age group yarating (Child: <18, Adult: 18-60, Senior: >60)
- `FamilySize` yarating: `SibSp + Parch + 1`
- `IsAlone` yarating: FamilySize == 1 bo'lsa 1, aks holda 0

#### 1.4. Encoding (5 ball)
- `Sex` feature'ni encoding qiling (male=0, female=1)
- `Embarked` feature'ni One-Hot Encoding qiling
- Faqat zarur feature'larni tanlang:
  - `Pclass`, `Sex`, `Age`, `Fare`, `FamilySize`, `IsAlone`, `Embarked_*`

**Topshirish formati:**
```python
# X va y yarating
X = df[selected_features]
y = df['Survived']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
```

---

### **2-Vazifa: Logistic Regression (15 ball)**

#### 2.1. Model yaratish (5 ball)
- Logistic Regression modelini yarating
- Feature'larni scaling qiling (StandardScaler)
- Modelni o'rgating

#### 2.2. Baholash (5 ball)
- Test to'plamida bashorat qiling
- Quyidagi metrikalarni hisoblang:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
- Classification Report chop eting

#### 2.3. Vizualizatsiya (5 ball)
- Confusion Matrix yarating
- ROC Curve chizib, AUC ko'rsating
- Feature coefficients'ni visualize qiling

**Topshirish formati:**
```python
print("="*60)
print("LOGISTIC REGRESSION - NATIJALAR")
print("="*60)
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")
print(f"AUC:       {auc:.4f}")
print("="*60)
```

---

### **3-Vazifa: k-Nearest Neighbors (15 ball)**

#### 3.1. Optimal k topish (8 ball)
- k qiymatini 1 dan 30 gacha test qiling
- Har bir k uchun train va test accuracy ni hisoblang
- Accuracy vs k grafigini chizing
- Eng yaxshi k qiymatini aniqlang

#### 3.2. Model yaratish va baholash (7 ball)
- Eng yaxshi k bilan model yarating
- Barcha metrikalarni hisoblang
- Confusion Matrix yarating
- Logistic Regression bilan taqqoslang

**Topshirish formati:**
```python
print(f"\n🎯 Eng yaxshi k qiymati: {best_k}")
print(f"Test Accuracy: {test_accuracy:.4f}")

# Logistic vs k-NN taqqoslash
comparison = pd.DataFrame({
    'Model': ['Logistic Regression', 'k-NN'],
    'Accuracy': [log_acc, knn_acc],
    'F1-Score': [log_f1, knn_f1]
})
print(comparison)
```

---

### **4-Vazifa: Decision Tree (20 ball)**

#### 4.1. Basic Model (7 ball)
- Decision Tree modelini yarating (max_depth=5)
- Modelni o'rgating va baholang
- Tree'ni visualize qiling (`plot_tree`)

#### 4.2. Feature Importance (6 ball)
- Feature importance'ni hisoblang
- Bar chart bilan ko'rsating
- Top 5 eng muhim feature'larni aniqlang va tushuntiring

#### 4.3. Hyperparameter Tuning (7 ball)
- GridSearchCV yordamida eng yaxshi parametrlarni toping:
  - `max_depth`: [3, 5, 7, 10, None]
  - `min_samples_split`: [2, 5, 10, 20]
  - `min_samples_leaf`: [1, 2, 4]
  - `criterion`: ['gini', 'entropy']
- Best parameters va best score'ni ko'rsating
- Tuned model bilan test accuracy'ni hisoblang

**Topshirish formati:**
```python
print("\n🌳 Decision Tree - Feature Importance:")
print(feature_importance.head(5))

print("\n🎯 Best Hyperparameters:")
print(grid_search.best_params_)
print(f"Best CV Score: {grid_search.best_score_:.4f}")
print(f"Test Score: {grid_search.score(X_test, y_test):.4f}")
```

---

### **5-Vazifa: Random Forest (20 ball)**

#### 5.1. Basic Model (7 ball)
- Random Forest modelini yarating (n_estimators=100)
- Modelni o'rgating va baholang
- Feature importance'ni ko'rsating

#### 5.2. Hyperparameter Tuning (8 ball)
- GridSearchCV qiling:
  - `n_estimators`: [50, 100, 200]
  - `max_depth`: [5, 10, 15, None]
  - `min_samples_split`: [2, 5, 10]
  - `min_samples_leaf`: [1, 2, 4]
- Best model bilan test qiling

#### 5.3. Decision Tree vs Random Forest (5 ball)
- Decision Tree va Random Forest'ni taqqoslang
- Quyidagilarni tahlil qiling:
  - Accuracy farqi
  - Overfitting (train vs test accuracy)
  - Feature importance farqi
  - Prediction time

**Topshirish formati:**
```python
comparison_df = pd.DataFrame({
    'Metric': ['Train Accuracy', 'Test Accuracy', 'Overfitting Gap', 'Time (ms)'],
    'Decision Tree': [dt_train_acc, dt_test_acc, dt_gap, dt_time],
    'Random Forest': [rf_train_acc, rf_test_acc, rf_gap, rf_time]
})
print(comparison_df)
```

---

### **6-Vazifa: Barcha Modellarni Taqqoslash (10 ball)**

#### 6.1. Results Table (5 ball)
- Barcha 4 modelni taqqoshlash jadvalini yarating:
  - Logistic Regression
  - k-NN (best k)
  - Decision Tree (tuned)
  - Random Forest (tuned)
- Metrikalar: Accuracy, Precision, Recall, F1-Score

#### 6.2. Visualization (5 ball)
- 4 ta bar chart yarating (har bir metrika uchun)
- Eng yaxshi modelni aniqlang
- Har bir modelning kuchli va zaif tomonlarini yozing

**Topshirish formati:**
```python
final_results = pd.DataFrame({
    'Model': [...],
    'Accuracy': [...],
    'Precision': [...],
    'Recall': [...],
    'F1-Score': [...]
})

print("\n" + "="*80)
print("YAKUNIY NATIJALAR - BARCHA MODELLAR")
print("="*80)
print(final_results.to_string(index=False))
print("="*80)

print(f"\n🏆 Eng yaxshi model: {best_model_name}")
```

---

## 📊 Bonus Vazifalar (+20 ball)

### Bonus 1: Cross-Validation (10 ball)
- Barcha modellar uchun 5-fold cross-validation qiling
- O'rtacha CV score va standard deviation'ni ko'rsating
- Model stability'ni tahlil qiling

### Bonus 2: Ensemble Voting Classifier (10 ball)
- Barcha 4 modelni birlashtirib Voting Classifier yarating
- Hard voting va soft voting'ni taqqoslang
- Voting Classifier bitta modeldan yaxshiroqmi tekshiring

```python
from sklearn.ensemble import VotingClassifier

voting_clf = VotingClassifier(
    estimators=[
        ('lr', log_reg),
        ('knn', knn),
        ('dt', dt),
        ('rf', rf)
    ],
    voting='soft'  # yoki 'hard'
)
```

---

## 📤 Topshirish talablari

### Format:
1. **Jupyter Notebook** (`.ipynb` format)
2. Barcha kod cell'lar ishga tushishi kerak
3. Har bir vazifa uchun markdown cell bilan tushuntirish
4. Vizualizatsiyalar aniq va o'qilishi oson

### Fayl nomi:
```
classification_homework_<ism>_<familiya>.ipynb
```
Misol: `classification_homework_Ali_Valiyev.ipynb`

### Jupyter Notebook tuzilishi:
```markdown
# Classification Models - Uy Vazifasi
## Talaba: [Ismingiz]
## Sana: [DD/MM/YYYY]

---

## 1-Vazifa: Ma'lumotlarni tayyorlash
[Kod va natijalar]

## 2-Vazifa: Logistic Regression
[Kod va natijalar]

...

## Xulosa
[Qisqacha xulosangiz]
```

---

## ✅ Baholash mezonlari

| Vazifa | Ball | Mezon |
|--------|------|-------|
| 1. Data Preparation | 20 | To'liq va to'g'ri preprocessing |
| 2. Logistic Regression | 15 | Model + Metrics + Visualization |
| 3. k-NN | 15 | Optimal k + Comparison |
| 4. Decision Tree | 20 | Basic + Feature Importance + Tuning |
| 5. Random Forest | 20 | Basic + Tuning + Comparison |
| 6. Model Comparison | 10 | Complete comparison |
| **Jami** | **100** | |
| **Bonus** | **+20** | Extra credit |

### Grading Scale:
- **90-100**: A (Excellent)
- **80-89**: B (Good)
- **70-79**: C (Satisfactory)
- **60-69**: D (Pass)
- **<60**: F (Fail)

---

## 💡 Maslahatlar

1. **Data Exploration muhim**: Ma'lumotlarni yaxshi o'rganing
2. **Visualization qo'shing**: Har bir natijani visualize qiling
3. **Code comments yozing**: Kodingizni tushunarli qiling
4. **Natijalarni tahlil qiling**: Faqat natija emas, sabab ham muhim
5. **Hyperparameter tuning**: GridSearchCV dan foydalaning
6. **Cross-validation**: Model generalization'ni tekshiring

---

## 📚 Qo'shimcha Resurslar

- [Scikit-learn Documentation](https://scikit-learn.org/stable/supervised_learning.html)
- [Kaggle Titanic Tutorial](https://www.kaggle.com/c/titanic)
- [Confusion Matrix Guide](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)
- [GridSearchCV Guide](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

---

## ⏰ Deadline

**Topshirish muddati**: [Muallim tomonidan belgilanadi]

---

## 🆘 Yordam

Agar savol yoki muammo bo'lsa:
1. Lecture va Practical notebook'larni qayta ko'ring
2. Scikit-learn documentation'dan foydalaning
3. Muallim yoki TA dan so'rang

---

## 🎯 Muvaffaqiyat mezonlari

Agar siz quyidagilarni bajarsangiz, uy vazifangiz muvaffaqiyatli hisoblanadi:

✅ Barcha 6 ta vazifani to'liq bajardingiz  
✅ Kod ishlaydi va xatosiz  
✅ Natijalar to'g'ri va tushunarli  
✅ Vizualizatsiyalar aniq va informativ  
✅ Tahlil va xulosalar yozilgan  
✅ O'z vaqtida topshirdingiz  

---

**🎉 Omad tilaymiz! Classification Models bilan ishda muvaffaqiyat!**

---

## 📌 Eslatma

Bu uy vazifasi sizning Classification algorithms bo'yicha bilim va ko'nikmalaringizni baholash uchun mo'ljallangan. Mustaqil ishlashga harakat qiling, lekin tushunmagan joylaringizda yordam so'rashdan tortinmang!

**Plagiarism (nusxa ko'chirish) qat'iyan man etiladi!**
