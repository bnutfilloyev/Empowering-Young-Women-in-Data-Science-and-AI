## Empowering Young Women in Data Science and AI

📚 Sun'iy Intellekt va Ma'lumotlar Tahlili Bo‘yicha To‘liq O‘quv Kursi ✨

Ushbu kurs sun'iy intellekt, amaliy statistika, ma'lumotlar bazasi, Python dasturlash, ma'lumotlar tahlili, matematik asoslar va mashinaviy o‘qitish bo‘yicha 48 ta darsdan iborat bo‘lib, nazariya va amaliy mashqlarni o‘z ichiga oladi. 🎯

---

## 🧭 Mundarija
- [📋 Darslar Ro‘yxati](#-darslar-roʻyxati)
- [🗂️ Repozitoriy tuzilmasi](#-repozitoriy-tuzilmasi)
- [⚙️ O‘rnatish (Installation)](#-oʻrnatish-installation)
- [▶️ Foydalanish (Usage)](#️-foydalanish-usage)
- [🎓 O‘rganish natijalari](#-oʻrganish-natijalari-learning-outcomes)
- [📄 Litsenziya](#-litsenziya)
- [👤 Muallif va sana](#-muallif-va-sana)
- [🔗 Foydali resurslar](#-foydali-resurslar)

---

## 📋 Darslar Ro‘yxati

### 1️⃣ Introduction to AI
1. Introduction to AI

### 2️⃣ Practical Statistics
2. Exploratory Data Analysis  
3. Estimates of Location  
4. Estimates of Variability I  
5. Estimates of Variability II  
6. Exploring the Data Distribution  
7. Exploring Binary and Categorical Data  
8. Correlation  
9. Exploring Two Variables  
10. Exploring Two or More Variables  
11. End-to-End Data Analysis Project  

### 3️⃣ SQL for Data Science
12. Introduction to Databases and SQL  
13. Basic SELECT Queries  
14. Filtering and Sorting Data  
15. JOINs and Relationships  
16. GROUP BY and Aggregations  
17. Subqueries and CTEs  

### 4️⃣ Python Crash Course
18. Python Basics  
19. Python Data Structures  
20. Python Control Flow and Functions  
21. Python Object Oriented Programming  

### 5️⃣ Exploratory Data Analysis (EDA)
22. Data Gathering I  
23. Data Gathering II  
24. Data Assessment  
25. Data Cleaning  
26. Data Visualization  

### 6️⃣ Essential Math for AI
27. Linear Algebra Basics  
28. Discrete Math Basics  
29. Differential Calculus  
30. Partial Derivatives and Gradients  

### 7️⃣ Machine Learning
31. Introduction to Machine Learning  
32. End-to-End Machine Learning Project  
33. Linear Regression  
34. Polynomial Regression and Regularization  
35. Logistic and Softmax Regression  
36. Evaluating Classification Models I  
37. Evaluating Classification Models II  
38. Naive Bayes  
39. K-Nearest Neighbors  
40. Support Vector Machine  
41. Decision Tree: Classification  
42. Decision Tree: Regression  
43. Ensemble Learning: Random Forests  
44. Ensemble Learning: Boosting and Stacking  
45. K-Means Clustering  
46. Dimensionality Reduction  

### 8️⃣ Software Engineering for AI
47. Software Engineering Principles for AI Systems  
48. Software Design Concepts and Web Development

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

Kelgusida bo‘limlar bo‘yicha yangi papkalar va notebooklar qo‘shilib boradi (AI Intro, SQL, Python Crash Course, EDA amaliy bo‘limlari, Math, ML va boshqalar).

---

## ⚙️ O‘rnatish (Installation)

Tavsiya etiladigan muhit:
- Python 3.9 yoki undan yuqori
- MacOS (brew bilan ixtiyoriy DB o‘rnatish), Windows yoki Linux

1) Virtual muhit yaratish va faollashtirish

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Python kutubxonalarini o‘rnatish

```bash
pip install --upgrade pip
pip install -r requirements.txt
# Notebook muhitlari uchun qo‘shimcha:
pip install jupyter ipykernel
python -m ipykernel install --user --name dsai-course
```

3) Ma’lumotlar bazasi (ixtiyoriy)
- Asosan EDA va Python bo‘limlari uchun DB shartsiz ishlaydi.
- SQL bo‘limlari uchun eng osoni — SQLite (macOS’da oldindan mavjud bo‘ladi).
- Agar PostgreSQL ishlatmoqchi bo‘lsangiz (macOS):

```bash
brew install postgresql@16
brew services start postgresql@16
createdb dsai_course
```

> Eslatma: PostgreSQL o‘rnatish ixtiyoriy. SQL darslari SQLite yoki mavjud DBMS’da ham bajarilishi mumkin.

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

### Ma’lumotlar
- `Titanic-Dataset.csv` — EDA uchun namuna dataset.
- Qo‘shimcha fayllar har bir modul papkasiga joylanadi.

### 🧰 SQL bo‘limlari
- SQLite bilan ishlash uchun Python’dan `sqlite3` yoki `SQLAlchemy` kutubxonasidan foydalanishingiz mumkin.
- PostgreSQL ishlatilsa, bog‘lanish parametrlari va credential’lar `.env` yoki muhit o‘zgaruvchilarida saqlanishi tavsiya etiladi.
	- 📘 SQLite: https://www.sqlite.org/docs.html
	- 🐘 PostgreSQL: https://www.postgresql.org/docs/
	- 🍺 Homebrew: https://brew.sh/
  
### 🧪 Notebook/IDE tavsiyalari
- Jupyter hujjatlar: https://jupyter.org/
- VS Code uchun Jupyter va Python kengaytmalari (Marketplace):
	- Jupyter: https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter
	- Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python

---

## 🎓 O‘rganish natijalari (Learning Outcomes)

Kurs yakunida siz:
- AI asoslari, etik masalalar va amaliy qo‘llanmalardan xabardor bo‘lasiz.
- Statistik tahlil: EDA, taqsimotlar, baholashlar, bog‘liqlik va o‘zgaruvchilar bilan ishlashni bilasiz.
- SQL orqali ma’lumotlarni so‘rash: SELECT, FILTER, JOIN, GROUP BY, Subquery, CTE kabi konseptlarni qo‘llaysiz.
- Python asoslari: sintaksis, ma’lumot tuzilmalar, boshqaruv oqimi, OOP konseptlarini amalda qo‘llaysiz.
- Matematik asoslar: chiziqli algebra, differensial hisob, gradientlar va diskret matematika bo‘yicha poydevor hosil qilasiz.
- Mashinaviy o‘qitish: regressiya/klassifikatsiya/klasterlash, model baholash (accuracy, precision/recall, ROC-AUC), regulatsiya va o‘lchamni qisqartirish usullarini qo‘llaysiz.
- E2E (end-to-end) yondashuv: ma’lumot yig‘ish, tozalash, baholash va tahlil qilish bosqichlarini boshidan oxirigacha bajarish ko‘nikmasiga ega bo‘lasiz.
- Notebooklar, grafik kutubxonalar (Matplotlib, Seaborn) va Numpy/Pandas bilan samarali ishlaysiz.

Qo‘shimcha foydali havolalar:
- 🐍 Python: https://docs.python.org/3/
- 📊 Pandas: https://pandas.pydata.org/docs/
- 🔢 NumPy: https://numpy.org/doc/
- 📈 Matplotlib: https://matplotlib.org/stable/
- 🖼️ Seaborn: https://seaborn.pydata.org/
- 🤖 Scikit-learn (ML): https://scikit-learn.org/stable/

---

## 📄 Litsenziya

Ushbu repozitoriy MIT License asosida tarqatiladi. Batafsil: `LICENSE` (agar mavjud bo‘lsa) yoki MIT litsenziyasi matnini GitHub sahifalaridan ko‘rishingiz mumkin.

---

## 👤 Muallif va sana

- Muallif: @bnutfilloyev
- Yaratilgan sana: 2025-08-12

Yordam, taklif va fikrlar uchun Issues bo‘limidan foydalaning yoki Pull Request yuboring.

