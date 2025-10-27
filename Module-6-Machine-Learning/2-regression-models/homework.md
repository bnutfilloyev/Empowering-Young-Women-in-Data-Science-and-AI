# Uy Vazifasi: Regression Modellar 🏠

## 📋 Umumiy Ma'lumot

**Muddat**: 1 hafta  
**Ball**: 100  
**Minimal ball**: 70

---

## 🎯 Vazifa 1: Uy Narxini Bashorat Qilish (40 ball)

### Ma'lumotlar
Sizga quyidagi xususiyatlarga ega uylar haqida ma'lumotlar berilgan:

```python
# Ma'lumotlarni yaratish kodi (yoki Kaggle dan yuklab oling)
import numpy as np
import pandas as pd

np.random.seed(42)
n = 1000

house_df = pd.DataFrame({
    'area': np.random.randint(500, 5000, n),           # kvadrat fut
    'bedrooms': np.random.randint(1, 8, n),            # xonalar
    'bathrooms': np.random.randint(1, 6, n),           # hammomlar
    'stories': np.random.randint(1, 5, n),             # qavatlar
    'parking': np.random.randint(0, 4, n),             # parking o'rinlari
    'furnishing': np.random.choice(['furnished', 'semi-furnished', 'unfurnished'], n),
    'age': np.random.randint(0, 50, n),                # bino yoshi
    'basement': np.random.choice([0, 1], n)            # yerto'la bormi
})

# Narxni hisoblash
house_df['price'] = (
    50000 + 
    house_df['area'] * 100 + 
    house_df['bedrooms'] * 20000 + 
    house_df['bathrooms'] * 15000 - 
    house_df['age'] * 2000 + 
    house_df['parking'] * 10000 + 
    house_df['basement'] * 30000 +
    np.random.normal(0, 50000, n)
)
```

### Topshiriqlar:

#### 1.1. Data Exploration (10 ball)
- [ ] Ma'lumotlar haqida umumiy statistika chiqaring
- [ ] Missing values bormi tekshiring
- [ ] Outliers ni aniqlang va visualize qiling (boxplot)
- [ ] Barcha raqamli feature'lar va price o'rtasidagi korrelyatsiyani hisoblang va heatmap chizing
- [ ] Kategorik o'zgaruvchilar (furnishing) va price o'rtasidagi munosabatni ko'rsating (boxplot/barplot)

#### 1.2. Data Preprocessing (5 ball)
- [ ] Kategorik o'zgaruvchilarni encode qiling (One-Hot Encoding)
- [ ] Outliers ni handle qiling (remove yoki transform)
- [ ] Ma'lumotlarni train (70%), validation (15%), test (15%) setlarga ajrating
- [ ] Feature scaling qiling (StandardScaler)

#### 1.3. Model Building (15 ball)
- [ ] **Linear Regression** modelini yarating va o'rgating
  - Train, validation, test setlarda R², RMSE, MAE ni hisoblang
  - Feature importance (coefficients) ni vizualizatsiya qiling
  - Haqiqiy vs bashorat qilingan narxlarni scatter plot qiling

- [ ] **Ridge Regression** modelini yarating
  - Turli alpha qiymatlarini sinab ko'ring: [0.01, 0.1, 1, 10, 100, 1000]
  - Validation set orqali eng yaxshi alpha ni toping
  - Eng yaxshi model bilan test setda baholang

- [ ] **Lasso Regression** modelini yarating
  - Turli alpha qiymatlarini sinab ko'ring
  - Feature selection qobiliyatini ko'rsating (nechta feature 0 koeffitsientga ega?)
  - Eng yaxshi model bilan test setda baholang

#### 1.4. Model Comparison va Analysis (10 ball)
- [ ] Barcha modellarni taqqoslang (jadval ko'rinishida)
- [ ] Eng yaxshi modelni tanlang va tanlovingizni asoslang
- [ ] Learning curves chizing (training set size vs performance)
- [ ] Residual analysis qiling:
  - Residual plot (predicted vs residuals)
  - Histogram of residuals
  - QQ-plot (agar bilsangiz)

---

## 🎯 Vazifa 2: Maosh Bashorati (30 ball)

### Kontekst
Siz HR департamentida ishlaysiz va xodimlarning maoshini bashorat qiluvchi model yaratishingiz kerak.

### Ma'lumotlar
Kaggle dan "Data Science Salaries" yoki o'xshash dataset yuklab oling.  
Yoki quyidagi ma'lumotlardan foydalaning:

```python
salary_df = pd.DataFrame({
    'experience': np.random.uniform(0, 20, 800),       # yillar
    'education_level': np.random.choice(['Bachelor', 'Master', 'PhD'], 800),
    'job_title': np.random.choice(['Junior', 'Mid', 'Senior', 'Lead'], 800),
    'company_size': np.random.choice(['Small', 'Medium', 'Large'], 800),
    'location': np.random.choice(['Tashkent', 'Samarkand', 'Bukhara', 'Others'], 800),
    'skills_count': np.random.randint(1, 15, 800),     # bilgan texnologiyalar soni
    'certifications': np.random.randint(0, 5, 800)     # sertifikatlar
})

# Maosh formulasi (murakkab, nochiziqli)
base_salary = 5000000  # UZS
salary_df['salary'] = ...  # Sizning formulangiz
```

### Topshiriqlar:

#### 2.1. EDA va Feature Engineering (10 ball)
- [ ] To'liq EDA qiling (distributions, correlations, relationships)
- [ ] Yangi feature'lar yarating:
  - `experience_category`: 0-2: Junior, 2-5: Mid, 5-10: Senior, 10+: Lead
  - `total_qualifications`: education_level + certifications (weighted)
  - `experience_squared`: experience^2 (polynomial feature)
  - Sizning o'z feature'laringiz

#### 2.2. Multiple Linear Regression (10 ball)
- [ ] Barcha feature'lar bilan Multiple Linear Regression modeli yarating
- [ ] Multicollinearity tekshiring (VIF - Variance Inflation Factor)
- [ ] P-values ga qarang, qaysi feature'lar statistik significant?
- [ ] Model performance ni baholang

#### 2.3. Polynomial Regression (10 ball)
- [ ] `experience` feature uchun polynomial features (degree 2, 3, 4) yarating
- [ ] Har bir degree uchun model yarating va baholang
- [ ] Overfitting bormi? Train vs Test performance ni taqqoslang
- [ ] Polynomial + Ridge/Lasso ni sinab ko'ring
- [ ] Eng yaxshi kombinatsiyani tanlang

---

## 🎯 Vazifa 3: Real Dataset Analysis - Kaggle Competition (30 ball)

### Vazifa
Kaggle dan regression dataset tanlang va to'liq tahlil qiling.

**Tavsiya etiladigan datasetlar:**
1. House Prices - Advanced Regression Techniques
2. Bike Sharing Demand
3. Restaurant Revenue Prediction
4. Store Sales Forecasting
5. Flight Price Prediction

### Topshiriqlar:

#### 3.1. Dataset Selection va Understanding (5 ball)
- [ ] Dataset tanlash va yuklab olish
- [ ] Dataset description yozing (nima haqida, nechta feature, target nima)
- [ ] Business understanding (bu ma'lumotlar nimaga kerak?)

#### 3.2. Complete EDA (10 ball)
- [ ] Missing values analysis va handling strategy
- [ ] Outliers detection va handling
- [ ] Feature distributions (histograms, boxplots)
- [ ] Correlation analysis
- [ ] Target variable analysis
- [ ] Kategorik va raqamli feature'lar analysis
- [ ] Kamida 10 ta visualization (informative va professional)

#### 3.3. Feature Engineering (5 ball)
- [ ] Missing values ni to'ldirish (mean, median, mode, yoki advanced methods)
- [ ] Outliers ni handle qilish
- [ ] Kategorik encoding (One-Hot, Label, Target encoding)
- [ ] Feature scaling/normalization
- [ ] Yangi feature'lar yaratish (kamida 3 ta meaningful feature)
- [ ] Feature selection (correlation, feature importance)

#### 3.4. Modeling va Tuning (10 ball)
- [ ] Baseline model (Linear Regression)
- [ ] Regularization models (Ridge, Lasso, ElasticNet)
- [ ] Polynomial features (agar mos bo'lsa)
- [ ] Hyperparameter tuning:
  - GridSearchCV yoki RandomizedSearchCV
  - K-Fold Cross-Validation
- [ ] Ensemble Methods (bonus: agar bilsangiz - Random Forest, XGBoost)
- [ ] Final model selection va evaluation
- [ ] Test set da yakuniy natija

---

## 🎯 Bonus Vazifa (20 ball)

Quyidagi topshiriqlardan kamida 2 tasini bajarsangiz bonus ball olasiz:

### Option 1: Advanced Feature Engineering (10 ball)
- [ ] Polynomial Interaction features
- [ ] Target encoding for categorical variables
- [ ] Feature selection using:
  - Recursive Feature Elimination (RFE)
  - Feature importance from tree-based models
  - Statistical tests (chi-square, ANOVA)

### Option 2: Model Interpretation (10 ball)
- [ ] Partial Dependence Plots
- [ ] Feature importance visualization
- [ ] Coefficient analysis (positive/negative impact)
- [ ] SHAP values (agar bilsangiz)

### Option 3: Deployment Simulation (10 ball)
- [ ] Modelni save qiling (pickle yoki joblib)
- [ ] Load qiling va yangi ma'lumotlarda bashorat qiling
- [ ] Simple prediction function yozing
- [ ] Model performance report yarating (PDF yoki HTML)

### Option 4: Custom Metric (5 ball)
- [ ] O'zingizning custom evaluation metric yarating
- [ ] Business context ga mos kelsin
- [ ] Nima uchun bu metric muhimligini tushuntiring

### Option 5: Ensemble Methods (10 ball)
- [ ] Voting Regressor (Linear, Ridge, Lasso kombinatsiyasi)
- [ ] Stacking Regressor
- [ ] Performanceni oddiy modellar bilan taqqoslang

---

## 📤 Topshirish Talablari

### Fayl Strukturasi
```
homework_regression/
│
├── data/
│   ├── raw/                    # Original datasets
│   └── processed/              # Cleaned datasets
│
├── notebooks/
│   ├── 01_task1_house_price.ipynb
│   ├── 02_task2_salary_prediction.ipynb
│   ├── 03_task3_kaggle_analysis.ipynb
│   └── 04_bonus_tasks.ipynb (agar bor bo'lsa)
│
├── models/                     # Saved models (bonus)
│
├── reports/
│   ├── figures/                # Visualizations
│   └── summary.md              # Executive summary
│
└── README.md                   # Loyiha haqida
```

### README.md da bo'lishi kerak:
- Loyiha tavsifi
- Har bir vazifa uchun qisqacha xulosa
- Natijalar (eng yaxshi modellar va ularning metrikalari)
- Qanday ishlatish (installation, run instructions)
- Muammolar va yechimlar

### Notebook Talablari:
- ✅ Kod toza va o'qilishi oson
- ✅ Markdown cells bilan izohlar
- ✅ Visualizations professional ko'rinishda
- ✅ Barcha cell'lar run qilingan
- ✅ Output'lar ko'rinib turadigan

---

## 📊 Baholash Mezonlari

### Vazifa 1: Uy narxi (40 ball)
- EDA: 10 ball
- Preprocessing: 5 ball
- Modeling: 15 ball
- Analysis: 10 ball

### Vazifa 2: Maosh bashorati (30 ball)
- EDA va Feature Engineering: 10 ball
- Multiple Linear Regression: 10 ball
- Polynomial Regression: 10 ball

### Vazifa 3: Kaggle Dataset (30 ball)
- Dataset Understanding: 5 ball
- EDA: 10 ball
- Feature Engineering: 5 ball
- Modeling va Tuning: 10 ball

### Bonus (20 ball)
- Har bir bonus task: 5-10 ball

### Kod Sifati va Presentation (10 ball deduction agar yomon bo'lsa)
- Kod toza va o'qilishi oson
- Markdown/comments yetarli
- Visualizations professional
- README to'liq va tushunarli

---

## 💡 Maslahatlar

1. **EDA ga vaqt ajrating**: Yaxshi EDA yaxshi model uchun asos
2. **Oddiydan boshlang**: Linear Regression → Regularization → Polynomial
3. **Overfitting'ga e'tibor bering**: Train vs Test performance
4. **Visualize qiling**: Har bir muhim topilma uchun grafik
5. **Document qiling**: Nima qildingiz, nima uchun, natija nima
6. **Git ishlatish**: Har bir vazifani alohida commit qiling (bonus)
7. **Vaqtni rejalashtiring**:
   - Vazifa 1: 2-3 kun
   - Vazifa 2: 2-3 kun  
   - Vazifa 3: 3-4 kun
   - Bonus: 1-2 kun

---

## 🚫 Qilmaslik Kerak

- ❌ Copy-paste qilish (internet/do'stdan)
- ❌ Kod izohsiz
- ❌ Test set'ni training'da ishlatish
- ❌ Data leakage (target info feature'larda)
- ❌ Overfitting'ga e'tibor bermaslik
- ❌ Faqat bitta metric bilan baholash
- ❌ Visualizations'siz taqdimot

---

## 📅 Deadline

**Topshirish sanasi**: [Instrukton tomonidan belgilanadi]

**Topshirish formati**: 
- GitHub repository link (public yoki private + access)
- yoki ZIP file (Google Drive/Dropbox link)

---

## ❓ Savollar

Agar savol tug'ilsa:
- Telegram/Slack guruhda so'rang
- Office hours'da keling
- Email yuboring: [instructor_email]

---

## ✅ Self-Assessment Checklist

Topshirishdan oldin tekshiring:

- [ ] Barcha 3 vazifa bajarilgan
- [ ] Kod ishlamoqda (xatosiz run bo'ladi)
- [ ] Barcha vizualizatsiyalar professional
- [ ] README to'liq va tushunarli
- [ ] Fayl strukturasi to'g'ri
- [ ] Notebook'lar toza va tartibli
- [ ] Natijalar yaxshi dokumentlangan
- [ ] (Bonus) Qo'shimcha vazifalar bajarilgan

---

**Omad! 🚀 Savol bo'lsa so'rang!**
