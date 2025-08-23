# Empowering Young Women in Data Science and AI

📚 Sun'iy Intellekt va Ma'lumotlar Tahlili Bo'yicha To'liq O'quv Kursi ✨

Ushbu kurs sun'iy intellekt, amaliy statistika, ma'lumotlar bazasi, Python dasturlash, ma'lumotlar tahlili, matematik asoslar va mashinaviy o'qitish bo'yicha 30 ta darsdan iborat bo'lib, nazariya va amaliy mashqlarni o'z ichiga oladi. 🎯

---

## 🧭 Mundarija
- [📋 Darslar Ro'yxati](#-darslar-roʻyxati)
- [🗂️ Repozitoriy tuzilmasi](#️-repozitoriy-tuzilmasi)
- [⚙️ O'rnatish (Installation)](#️-oʻrnatish-installation)
- [▶️ Foydalanish (Usage)](#️-foydalanish-usage)
- [🎓 O'rganish natijalari](#-oʻrganish-natijalari-learning-outcomes)
- [📄 Litsenziya](#-litsenziya)
- [👤 Muallif va sana](#-muallif-va-sana)
- [🔗 Foydali resurslar](#-foydali-resurslar)

---

## 📋 Darslar Ro'yxati

### 🤖 Modul 1: AI va Data Sciencega Kirish (3 dars)
1. **Sun'iy intellekt va Data Sciencega kirish** — AI tarihi, Data Science jarayoni, amaliy sohalar
2. **Ma'lumotlar turlari va yig'ish usullari** — sonli, kategoriyaviy, matnli, tasvirli ma'lumotlar  
3. **Data Science ish jarayoni** — ma'lumot yig'ish → tozalash → tahlil → model → deployment

### 📊 Modul 2: Amaliy Statistika (6 dars)
4. **Statistik asoslar** — populyatsiya, sample, parametr, statistik o'lchovlar
5. **Markaziy tendensiya va tarqalish** — mean, median, mode, variance, standard deviation
6. **Percentile, IQR va outlierlar** — kvantillar, IQR, boxplot asoslari
7. **Ehtimollik va taqsimotlar** — normal, binomial, uniform, exponential
8. **Hipoteza testi va p-qiymat** — t-test, chi-square, z-test
9. **Korrelyatsiya va regressiya asoslari** — Pearson/Spearman, oddiy chiziqli regressiya

### 🗄️ Modul 3: SQL Data Science uchun (4 dars)
10. **SQLga kirish va SELECT** — asosiy querylar, filter, sort, limit
11. **Agregatsiya va guruhlash** — COUNT, SUM, AVG, GROUP BY, HAVING
12. **Joins va subquerylar** — INNER, LEFT, RIGHT, FULL, nested queries
13. **SQL bilan data tahlil loyihasi** — real dataset bilan EDA SQL orqali

### 🐍 Modul 4: Python Crash Course (3 dars)
14. **Python asoslari** — satrlar, ro'yxatlar, shartlar, looplar
15. **Funksiyalar va modullar** — function, scope, import, kutubxonalar
16. **Numpy va Pandas bilan data ishlash** — arraylar, DataFrame, indexing, filtering, aggregation

### 🔍 Modul 5: Exploratory Data Analysis (3 dars)
17. **Data tozalash va tayyorlash** — missing values, duplicates, categorical encoding
18. **Vizualizatsiya asoslari** — matplotlib, seaborn, histogram, scatterplot
19. **Case Study: Real Dataset EDA** — Titanic / Penguins / real datasetda EDA

### 🧮 Modul 6: Essential Math for AI (3 dars)
20. **Linear Algebra asoslari** — vector, matrix, dot product, transpose
21. **Calculus va optimizatsiya** — derivative, gradient descent intuitively
22. **Statistika va ehtimollik matematik poydevori** — conditional probability, Bayes teoremasi

### 🤖 Modul 7: Machine Learning (8 dars)
23. **Machine Learningga kirish** — ML turlari: supervised, unsupervised, reinforcement
24. **Regression modellar** — Linear, Polynomial, Regularization: Ridge/Lasso
25. **Classification modellar** — Logistic Regression, k-NN, Decision Tree, Random Forest
26. **Unsupervised Learning** — Clustering: K-means, Hierarchical, PCA
27. **Model baholash** — train/test split, cross-validation, overfitting, metrics: accuracy, precision, recall, F1, AUC
28. **Feature Engineering va Scaling** — feature selection, normalization, standardization
29. **Deep Learning asoslari** — neural networks, perceptron, forward/backpropagation, keras/pytorch intro
30. **AI Loyiha Case Study** — bosqichma-bosqich ML loyihasi: data → model → natija → prezentatsiya

---

## 🗂️ Repozitoriy tuzilmasi

Joriy tuzilma:

```text
Empowering-Young-Women-in-Data-Science-and-AI/
├── Practical-Statistics/
│   └── 1-exploratory-data-analysis/
│       ├── Assignment.pdf
│       ├── Titanic-Dataset.csv
│       └── conception.ipynb
├── requirements.txt          # Asosiy Python kutubxonalari
├── README.md
└── venv/                     # (ixtiyoriy) Lokal virtual muhit
```

Tez havolalar:
- 📓 Notebook: [`conception.ipynb`](Practical-Statistics/1-exploratory-data-analysis/conception.ipynb)
- 📄 Vazifa: [`Assignment.pdf`](Practical-Statistics/1-exploratory-data-analysis/Assignment.pdf)
- 🧾 Dataset: [`Titanic-Dataset.csv`](Practical-Statistics/1-exploratory-data-analysis/Titanic-Dataset.csv)
- 📦 Asosiy talablari: [`requirements.txt`](requirements.txt)

Kelgusida bo'limlar bo'yicha yangi papkalar va notebooklar qo'shilib boradi (AI Intro, SQL, Python Crash Course, EDA amaliy bo'limlari, Math, ML va boshqalar).

---

## ⚙️ O'rnatish (Installation)

Tavsiya etiladigan muhit:
- Python 3.9 yoki undan yuqori
- MacOS (brew bilan ixtiyoriy DB o'rnatish), Windows yoki Linux

1) Virtual muhit yaratish va faollashtirish

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Python kutubxonalarini o'rnatish

```bash
pip install --upgrade pip
pip install -r requirements.txt
# Notebook muhitlari uchun qo'shimcha:
pip install jupyter ipykernel
python -m ipykernel install --user --name dsai-course
```

3) Ma'lumotlar bazasi (ixtiyoriy)
- Asosan EDA va Python bo'limlari uchun DB shartsiz ishlaydi.
- SQL bo'limlari uchun eng osoni — SQLite (macOS'da oldindan mavjud bo'ladi).
- Agar PostgreSQL ishlatmoqchi bo'lsangiz (macOS):

```bash
brew install postgresql@16
brew services start postgresql@16
createdb dsai_course
```

> Eslatma: PostgreSQL o'rnatish ixtiyoriy. SQL darslari SQLite yoki mavjud DBMS'da ham bajarilishi mumkin.

---

## ▶️ Foydalanish (Usage)

### Notebooklarni ishga tushirish
1) Virtual muhitni faollashtiring: `source .venv/bin/activate`
2) Jupyter muhitini ishga tushiring:

```bash
jupyter lab
# yoki
jupyter notebook
```

3) [`conception.ipynb`](Practical-Statistics/1-exploratory-data-analysis/conception.ipynb) faylini oching.
4) Kernel sifatida `dsai-course` ni tanlang va ketma-ket barcha hujayralarni ishga tushiring.

### Ma'lumotlar
- `Titanic-Dataset.csv` — EDA uchun namuna dataset.
- Qo'shimcha fayllar har bir modul papkasiga joylanadi.

### 🧰 SQL bo'limlari
- SQLite bilan ishlash uchun Python'dan `sqlite3` yoki `SQLAlchemy` kutubxonasidan foydalanishingiz mumkin.
- PostgreSQL ishlatilsa, bog'lanish parametrlari va credential'lar `.env` yoki muhit o'zgaruvchilarida saqlanishi tavsiya etiladi.
  - 📘 SQLite: https://www.sqlite.org/docs.html
  - 🐘 PostgreSQL: https://www.postgresql.org/docs/
  - 🍺 Homebrew: https://brew.sh/
  
### 🧪 Notebook/IDE tavsiyalari
- Jupyter hujjatlar: https://jupyter.org/
- VS Code uchun Jupyter va Python kengaytmalari (Marketplace):
  - Jupyter: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
  - Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python

---

## 🎓 O'rganish natijalari (Learning Outcomes)

Kurs yakunida siz:
- AI asoslari, etik masalalar va amaliy qo'llanmalardan xabardor bo'lasiz.
- Statistik tahlil: EDA, taqsimotlar, baholashlar, bog'liqlik va o'zgaruvchilar bilan ishlashni bilasiz.
- SQL orqali ma'lumotlarni so'rash: SELECT, FILTER, JOIN, GROUP BY, Subquery, CTE kabi konseptlarni qo'llaysiz.
- Python asoslari: sintaksis, ma'lumot tuzilmalar, boshqaruv oqimi, OOP konseptlarini amalda qo'llaysiz.
- Matematik asoslar: chiziqli algebra, differensial hisob, gradientlar va diskret matematika bo'yicha poydevor hosil qilasiz.
- Mashinaviy o'qitish: regressiya/klassifikatsiya/klasterlash, model baholash (accuracy, precision/recall, ROC-AUC), regulatsiya va o'lchamni qisqartirish usullarini qo'llaysiz.
- E2E (end-to-end) yondashuv: ma'lumot yig'ish, tozalash, baholash va tahlil qilish bosqichlarini boshidan oxirigacha bajarish ko'nikmasiga ega bo'lasiz.
- Notebooklar, grafik kutubxonalar (Matplotlib, Seaborn) va Numpy/Pandas bilan samarali ishlaysiz.

Qo'shimcha foydali havolalar:
- 🐍 Python: https://docs.python.org/3/
- 📊 Pandas: https://pandas.pydata.org/docs/
- 🔢 NumPy: https://numpy.org/doc/
- 📈 Matplotlib: https://matplotlib.org/stable/
- 🖼️ Seaborn: https://seaborn.pydata.org/
- 🤖 Scikit-learn (ML): https://scikit-learn.org/stable/

---

## 📄 Litsenziya

Ushbu repozitoriy MIT License asosida tarqatiladi. Batafsil: `LICENSE` (agar mavjud bo'lsa) yoki MIT litsenziyasi matnini GitHub sahifalaridan ko'rishingiz mumkin.

---

## 👤 Muallif va sana

- Muallif: @bnutfilloyev
- Yaratilgan sana: 2025-08-23

Yordam, taklif va fikrlar uchun Issues bo'limidan foydalaning yoki Pull Request yuboring.

## 🔗 Foydali resurslar

### 📚 O'rganish materiallari
- 🤖 AI Ethics: https://ethics.fast.ai/
- 📊 Statistics: https://www.khanacademy.org/math/statistics-probability
- 💾 SQL Tutorial: https://www.w3schools.com/sql/
- 🐍 Python Tutorial: https://docs.python.org/3/tutorial/
- 🧮 Math for ML: https://mml-book.github.io/

### 🛠️ Vositalar
- 🔗 Anaconda: https://www.anaconda.com/products/distribution
- 🌐 Google Colab: https://colab.research.google.com/
- 💻 VS Code: https://code.visualstudio.com/
- 📊 Kaggle: https://www.kaggle.com/

### 🏆 Amaliyot platformalari
- 💡 LeetCode: https://leetcode.com/
- 🧠 HackerRank: https://www.hackerrank.com/
- 🎯 DataCamp: https://www.datacamp.com/
- 📈 Coursera: https://www.coursera.org/
