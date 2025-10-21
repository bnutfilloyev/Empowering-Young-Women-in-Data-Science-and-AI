# Uy Vazifasi: Machine Learning Asoslari

## Maqsad
Machine Learning turlarini chuqurroq o'rganish va amaliy ko'nikmalarni mustahkamlash.

---

## 📝 Nazariy Qism (30 ball)

### Savol 1 (5 ball)
Machine Learning va an'anaviy dasturlash o'rtasidagi asosiy farqlarni tushuntiring. Har birining qachon ishlatilishi to'g'ri ekanligini misollar bilan ko'rsating.

**Javobingiz:**
```
[Bu yerga javob yozing]
```

### Savol 2 (5 ball)
Supervised Learning va Unsupervised Learning o'rtasidagi farqni tushuntiring. Har biri uchun 3 tadan real hayot misoli keltiring.

**Javobingiz:**
```
[Bu yerga javob yozing]
```

### Savol 3 (5 ball)
Classification va Regression muammolarini qanday farqlash mumkin? Quyidagi vazifalar qaysi turga kiradi?
- Talaba bahosini bashorat qilish (0-100)
- Email spam yoki spam emasligini aniqlash
- Haroratni prognoz qilish
- Rasmda qaysi hayvon borligini aniqlash
- Aksiya narxini bashorat qilish

**Javobingiz:**
```
[Bu yerga javob yozing]
```

### Savol 4 (5 ball)
K-Means clustering algoritmi qanday ishlaydi? Uning afzalliklari va kamchiliklarini sanab bering.

**Javobingiz:**
```
[Bu yerga javob yozing]
```

### Savol 5 (5 ball)
Reinforcement Learning qanday vaziyatlarda qo'llaniladi? AlphaGo yoki avtomobil haydash misolida tushuntiring (agent, environment, state, action, reward).

**Javobingiz:**
```
[Bu yerga javob yozing]
```

### Savol 6 (5 ball)
Overfitting va Underfitting nima? Ularni qanday aniqlash va oldini olish mumkin?

**Javobingiz:**
```
[Bu yerga javob yozing]
```

---

## 💻 Amaliy Qism (70 ball)

### Vazifa 1: Klassifikatsiya - Diabetes Prediction (20 ball)

**Dataset:** Pima Indians Diabetes Dataset (scikit-learn yoki Kaggle)

**Topshiriqlar:**
1. Ma'lumotlarni yuklang va o'rganing (5 ball)
   - Dataset haqida ma'lumot
   - Feature'lar tavsifi
   - Statistik tahlil
   - Null qiymatlarni tekshirish

2. Data Preprocessing (5 ball)
   - Missing value'larni to'ldirish
   - Outlier'larni topish
   - Feature scaling

3. Model O'qitish (5 ball)
   - Train/test split (80/20)
   - Kamida 3 ta turli klassifikatsiya modelini sinab ko'ring:
     * Logistic Regression
     * Decision Tree
     * Random Forest
   - Har birini o'rgating

4. Model Baholash (5 ball)
   - Accuracy, Precision, Recall, F1-score
   - Confusion matrix
   - ROC curve va AUC
   - Eng yaxshi modelni tanlang va sabablari

**Jupyter Notebook:** `diabetes_classification.ipynb`

---

### Vazifa 2: Regressiya - Car Price Prediction (20 ball)

**Dataset:** Auto MPG yoki Car Price Prediction dataset

**Topshiriqlar:**
1. Exploratory Data Analysis (EDA) (5 ball)
   - Ma'lumotlarni vizualizatsiya qiling
   - Feature'lar orasidagi correlation
   - Target variable distribution

2. Feature Engineering (5 ball)
   - Categorical variable'larni encode qiling
   - Yangi feature'lar yarating (masalan, age = current_year - year)
   - Feature selection

3. Multiple Regression Models (5 ball)
   - Linear Regression
   - Polynomial Regression (2-darajali, 3-darajali)
   - Ridge Regression
   - Lasso Regression

4. Model Comparison (5 ball)
   - R² score
   - MSE, RMSE, MAE
   - Residual plots
   - Eng yaxshi modelni tanlang
   - Overfitting bormi? Tekshiring

**Jupyter Notebook:** `car_price_regression.ipynb`

---

### Vazifa 3: Clustering - Customer Segmentation (15 ball)

**Dataset:** Mall Customers dataset yoki o'zingiz yarating

**Topshiriqlar:**
1. Dataset yaratish/yuklash (3 ball)
   - Agar yaratilsa: 200+ mijoz, 3+ feature
   - Feature'lar: Age, Income, Spending Score, va boshqalar

2. Data Preprocessing (3 ball)
   - Scaling (StandardScaler yoki MinMaxScaler)
   - Dimensionality reduction (ixtiyoriy, PCA)

3. K-Means Clustering (5 ball)
   - Elbow method bilan optimal K ni toping
   - K-Means qo'llang
   - Cluster markazlarini tahlil qiling

4. Results Analysis (4 ball)
   - Har bir cluster'ning xususiyatlari
   - Cluster profiling (masalan: "Premium customers", "Budget shoppers")
   - 2D visualization (PCA yoki birinchi 2 feature)
   - Business insights: Har bir segment uchun marketing tavsiyalari

**Jupyter Notebook:** `customer_segmentation.ipynb`

---

### Vazifa 4: ML Pipeline - Complete Project (15 ball)

**Dataset:** O'zingiz tanlang (Kaggle, UCI ML Repository)

**Topshiriqlar:**
To'liq ML workflow'ni amalga oshiring:

1. Problem Definition (2 ball)
   - Muammo tavsifi
   - Qanday ML turi ishlatiladi?
   - Success metric nima?

2. Data Collection & EDA (3 ball)
   - Dataset haqida ma'lumot
   - Visualizations
   - Statistical analysis

3. Data Preprocessing (3 ball)
   - Cleaning
   - Feature engineering
   - Transformation

4. Model Development (4 ball)
   - Kamida 3 ta model
   - Hyperparameter tuning
   - Cross-validation

5. Model Evaluation & Deployment Plan (3 ball)
   - Best model selection
   - Final evaluation metrics
   - Qanday deploy qilish mumkin?
   - Limitations va future improvements

**Jupyter Notebook:** `ml_project.ipynb`

---

## 📊 Bonus Vazifalar (20 ball)

### Bonus 1: Ensemble Methods (10 ball)
Voting Classifier yoki Stacking classifier yarating va oddiy modellar bilan taqqoslang.

### Bonus 2: Deep Dive into Reinforcement Learning (10 ball)
Q-Learning algoritmini boshqa muhitda (masalan, CartPole, Mountain Car) qo'llang va natijalarni tahlil qiling.

---

## 📤 Topshirish

### Format:
1. Barcha Jupyter notebook'lar
2. Ma'lumotlar (agar kichik bo'lsa)
3. README.md fayli bilan:
   - Ishni qanday run qilish
   - Requirements (pip install -r requirements.txt)
   - Asosiy natijalar
   - Qiyinchiliklar va yechimlar

### Baholash Mezonlari:

**Nazariy qism (30 ball):**
- To'liq va aniq javoblar
- Real misollar
- Chuqur tushuncha

**Amaliy qism (70 ball):**
- Kod sifati va o'qilishi
- Vizualizatsiyalar
- Tahlil va xulosalar
- Natijalarni tushuntirish
- Originallik

**Bonus (20 ball):**
- Qo'shimcha tadqiqotlar
- Advanced techniques
- Creative approach

### Deadline: [O'qituvchi tomonidan belgilanadi]

---

## 💡 Maslahatlar

1. **Kod yozishdan oldin plan tuzing**
2. **Vizualizatsiya qiling** - grafiklar tushunishni osonlashtiradi
3. **Comentariy yozing** - kodingizni tushuntiring
4. **Natijalarni tahlil qiling** - faqat kod yozish yetarli emas
5. **Xatolardan o'rganing** - model yomon ishlasa, nima uchun ekanligini tushunishga harakat qiling
6. **Kaggle Notebooks** ga qarang - inspiratsiya uchun

---

## 📚 Qo'shimcha Manbalar

### Datasets:
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

### O'qish:
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Hands-On Machine Learning (book)](https://github.com/ageron/handson-ml2)
- [Machine Learning Mastery](https://machinelearningmastery.com/)

### Practice:
- [Kaggle Competitions](https://www.kaggle.com/competitions)
- [DataCamp](https://www.datacamp.com/)
- [Google Colab](https://colab.research.google.com/) - bepul GPU

---

## ❓ Savollar?

Agar biror narsa tushunarsiz bo'lsa, o'qituvchidan so'rang yoki guruh chatida muhokama qiling.

**Omad! 🚀**
