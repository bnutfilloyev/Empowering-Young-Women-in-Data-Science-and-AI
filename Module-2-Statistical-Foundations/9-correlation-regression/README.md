# 9-dars: Korrelyatsiya va Regressiya Asoslari

## 📚 Dars maqsadi
Talabalar korrelyatsiya va regressiya asoslarini o'rganib, o'zgaruvchilar orasidagi bog'lanishni tahlil qilish usullarini o'rganadilar.

## 🎯 O'rganish natijalari
Dars oxirida talabalar quyidagilarni bila oladilar:

### Korrelyatsiya
- 📊 Korrelyatsiya tushunchasini tushunish
- 🔢 Pearson korrelyatsiya koeffitsiyentini hisoblash va talqin qilish
- 📈 Spearman korrelyatsiya koeffitsiyentini hisoblash va talqin qilish
- 🎯 Qachon qaysi korrelyatsiya turidan foydalanishni bilish
- ⚠️ Korrelyatsiya va sabab-oqibat farqini anglash

### Regressiya
- 📉 Oddiy chiziqli regressiya tushunchasini tushunish
- 🧮 Regressiya tenglamasini tuzish (y = ax + b)
- 📊 R² (aniqlash koeffitsiyenti) ni hisoblash va talqin qilish
- 🎯 Bashorat qilish uchun regressiya modelidan foydalanish
- ✅ Model sifatini baholash usullari

## 📖 Dars tarkibi

### 1. Korrelyatsiya asoslari (45 daqiqa)
- **Nazariy qism** (15 daqiqa)
  - Korrelyatsiya nima?
  - Korrelyatsiya koeffitsiyentining ma'nosi (-1 dan +1 gacha)
  - Ijobiy, salbiy va nol korrelyatsiya
  
- **Pearson korrelyatsiyasi** (15 daqiqa)
  - Formula va hisoblash
  - Chiziqli bog'lanishni o'lchash
  - Amaliy misollar
  
- **Spearman korrelyatsiyasi** (15 daqiqa)
  - Rang korrelyatsiyasi tushunchasi
  - Noparametrik usul
  - Qachon ishlatish kerak

### 2. Oddiy chiziqli regressiya (60 daqiqa)
- **Nazariy qism** (20 daqiqa)
  - Regressiya maqsadi
  - Eng kichik kvadratlar usuli
  - Regressiya chizig'i
  
- **Amaliy qism** (25 daqiqa)
  - Python'da regressiya
  - Grafik tasvir
  - Bashorat qilish
  
- **Model baholash** (15 daqiqa)
  - R² koeffitsiyenti
  - Xatoliklar tahlili
  - Model sifatini oshirish

### 3. Amaliy mashg'ulot (30 daqiqa)
- Real ma'lumotlar bilan ishlash
- Korrelyatsiya va regressiya tahlili
- Natijalarni talqin qilish

## 📁 Fayl tarkibi
- `lecture.ipynb` - Asosiy ma'ruza materiali
- `practical.ipynb` - Amaliy mashg'ulotlar
- `homework.ipynb` - Uy vazifasi
- `group1_practice.ipynb` - 1-guruh amaliyoti
- `group2_practice.ipynb` - 2-guruh amaliyoti
- `datasets/` - Ma'lumotlar to'plami
  - `students_math.csv` - Talabalar matematika balilar
  - `house_prices.csv` - Uy narxlari ma'lumotlari
  - `sales_data.csv` - Sotuv ma'lumotlari

## 🛠 Talab qilinadigan kutubxonalar
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
```

## 📊 Asosiy formulalar

### Pearson korrelyatsiya koeffitsiyenti:
```
r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)² × Σ(yi - ȳ)²]
```

### Spearman korrelyatsiya koeffitsiyenti:
```
ρ = 1 - (6 × Σdi²) / (n(n² - 1))
```

### Oddiy chiziqli regressiya:
```
y = ax + b
a = Σ[(xi - x̄)(yi - ȳ)] / Σ(xi - x̄)²
b = ȳ - ax̄
```

### Aniqlash koeffitsiyenti:
```
R² = 1 - (SSres / SStot)
```

## 🎯 Baholash mezonlari
- Nazariy bilim: 30%
- Amaliy ko'nikmalar: 40%
- Loyiha ishi: 30%

## 📚 Qo'shimcha manbalar
- "Statistics for Data Science" - 9-bob
- Python documentation: scipy.stats
- Real ma'lumotlar: Kaggle datasets
- Video darslar: Khan Academy Statistics
