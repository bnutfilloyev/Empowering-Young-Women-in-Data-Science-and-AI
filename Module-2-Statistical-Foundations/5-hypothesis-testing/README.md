# 5-dars: Hipoteza testi va p-qiymat

## Maqsad
Bu darsda talabalar hipoteza testlari asoslari va turli xil testlar (t-test, chi-square, z-test) bilan tanishadi.

## O'rganiluvchi mavzular

### 1. Hipoteza testi asoslari
- Null va alternative hipotezalar
- I va II tur xatolar
- Ahamiyat darajasi (α)
- p-qiymat tushunchasi

### 2. Z-test
- Bir tanlovli z-test
- Ikki tanlovli z-test
- Qo'llanish shartlari
- Katta tanlov hajmi (n > 30)

### 3. T-test
- Bir tanlovli t-test
- Ikki tanlovli t-test (independent va paired)
- Kichik tanlov hajmi uchun
- Student's t-distribution

### 4. Chi-square test
- Goodness of fit test
- Independence test
- Kategorik ma'lumotlar uchun

### 5. Amaliy misollar
- Real ma'lumotlar bilan ishlash
- Natijalari talqin qilish
- Xulosa chiqarish

## Dars tuzilishi

1. **Leksiya** (`lecture.ipynb`) - nazariy qism
2. **Amaliy mashq** - 2 ta guruh uchun:
   - `group1_practice.ipynb` - 1-guruh (asosiy)
   - `group2_practice.ipynb` - 2-guruh (ilg'or)
3. **Uy vazifasi** (`hometask.ipynb`)

## Talablardan kutilayotgan natijalar
- Hipoteza testi jarayonini tushunish
- p-qiymatni talqin qilish
- Turli testlarni to'g'ri qo'llash
- Real ma'lumotlarga testlarni tatbiq etish

## Kerakli kutubxonalar
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm, t, chi2
import warnings
warnings.filterwarnings('ignore')
```
