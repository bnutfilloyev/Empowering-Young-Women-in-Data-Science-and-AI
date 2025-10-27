# 2-dars: Regression Modellar

## Mavzu maqsadi
Bu darsda siz regressiya modellarining barcha asosiy turlarini o'rganasiz va amalda qo'llaysiz.

## O'rganilayotgan mavzular

### 1. Linear Regression (Chiziqli Regressiya)
- Simple Linear Regression (1 feature)
- Multiple Linear Regression (ko'p feature'lar)
- Model coefficients va interpretation
- R² score va model baholash

### 2. Polynomial Regression
- Nima uchun kerak?
- Polynomial features yaratish
- Degree tanlash
- Overfitting muammosi

### 3. Regularization Techniques
- Overfitting muammosi
- Ridge Regression (L2 regularization)
- Lasso Regression (L1 regularization)
- ElasticNet (L1 + L2)
- Hyperparameter tuning

### 4. Model Comparison
- Turli modellarni taqqoslash
- Cross-validation
- Learning curves
- Bias-Variance tradeoff

## Real-world Applications

### Linear Regression:
- 💰 Uy/mashina narxini bashorat qilish
- 📈 Sotuvni prognoz qilish
- 🌡️ Harorat bashorati
- 💹 Stock price prediction

### Polynomial Regression:
- 📊 Nochiziqli munosabatlar
- 🔬 Fizik jarayonlar modellashtirish
- 📉 Growth curves

### Regularization:
- 🎯 Feature'lar ko'p bo'lganda
- 🛡️ Overfitting oldini olish
- 🔍 Feature selection (Lasso)

## Fayllar
- `lecture.ipynb` - Nazariy ma'lumotlar va to'liq misollar
- `practical.ipynb` - Amaliy mashg'ulotlar
- `homework.md` - Uy vazifasi
- `regression_guide.md` - Regression bo'yicha to'liq qo'llanma

## Kerakli kutubxonalar
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
```

## Prerequisites
- Python basics
- NumPy va Pandas
- Matplotlib/Seaborn
- Statistics asoslari
- Module 6 - Dars 1 (ML Introduction)

## O'rganish vaqti
- Lecture: 2-3 soat
- Practical: 2-3 soat
- Homework: 4-6 soat
- **Jami: ~10 soat**

## Qo'shimcha manbalar
- [Scikit-learn Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)
- [StatQuest: Linear Regression](https://www.youtube.com/watch?v=nk2CQITm_eo)
- [3Blue1Brown: Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
