# Z-Score va Modified Z-Score Usuli bilan Outlierlarni Aniqlash

## 📊 Kirish

**Outlier (Chetga chiquvchi qiymat)** - ma'lumotlar to'plamidagi boshqa qiymatlardan sezilarli darajada farq qiluvchi qiymat. Outlierlarni aniqlash statistik tahlilda muhim ahamiyatga ega, chunki ular:

- Natijalarni buzishi mumkin
- Noto'g'ri xulosalarga olib kelishi mumkin
- Ba'zan qiziqarli va muhim ma'lumotlarni o'z ichiga oladi

---

## 🎯 Z-Score Usuli

### Nazariya

**Z-Score** - ma'lumot nuqtasining o'rtachadan necha standart og'ish masofada ekanligini ko'rsatadi.

**Formula:**
```
Z = (x - μ) / σ
```

Bu yerda:
- `x` - ma'lumot nuqtasi
- `μ` - o'rtacha qiymat (mean)
- `σ` - standart og'ish (standard deviation)

### Outlier Mezonlari

**Umumiy qoidalar:**
- `|Z| > 2` - Shubhali outlier
- `|Z| > 2.5` - Outlier
- `|Z| > 3` - Jiddiy outlier

### Afzalliklari ✅
- Sodda va tushunarli
- Keng qo'llaniladi
- Hisoblash oson

### Kamchiliklari ❌
- Normal taqsimot talab qiladi
- Outlierlarning o'zi o'rtacha va standart og'ishga ta'sir qiladi
- Bir nechta outlier bo'lsa, ularni yashirishi mumkin

---

## 🎯 Modified Z-Score Usuli

### Nazariya

**Modified Z-Score** - Z-score usulining muqobil versiyasi bo'lib, o'rtacha va standart og'ish o'rniga **mediana** va **MAD (Median Absolute Deviation)** ishlatadi.

**Formula:**
```
Modified Z = 0.6745 × (x - median) / MAD
```

Bu yerda:
- `MAD = median(|x - median|)`
- `0.6745` - normal taqsimot uchun konversiya koeffitsienti

### Outlier Mezonlari

**Umumiy qoidalar:**
- `|Modified Z| > 3.5` - Outlier

### Afzalliklari ✅
- Outlierlardan kam ta'sirlanadi (robust)
- Normal taqsimot talab qilmaydi
- Ko'p outlier bo'lganda ham ishonchli

### Kamchiliklari ❌
- Biroz murakkab hisoblash
- Kamroq tanilgan
- Ba'zi hollarda haddan tashqari konservativ

---

## 📈 Amaliy Misollar

### 1-Misol: Talabalar Baholarida Outlier Aniqlash

**Ma'lumotlar:** 
```
Baholar: [85, 87, 90, 92, 88, 91, 89, 15, 93, 86, 94, 88, 90]
```

#### Z-Score Usuli:

1. **O'rtacha hisoblash:**
   ```
   μ = (85+87+90+92+88+91+89+15+93+86+94+88+90) / 13 = 83.7
   ```

2. **Standart og'ish hisoblash:**
   ```
   σ = 20.1
   ```

3. **Har bir qiymat uchun Z-score:**
   ```
   15 uchun: Z = (15 - 83.7) / 20.1 = -3.42  ← OUTLIER!
   85 uchun: Z = (85 - 83.7) / 20.1 = 0.06   ← Normal
   90 uchun: Z = (90 - 83.7) / 20.1 = 0.31   ← Normal
   ```

#### Modified Z-Score Usuli:

1. **Mediana hisoblash:**
   ```
   Sorted: [15, 85, 86, 87, 88, 88, 89, 90, 90, 91, 92, 93, 94]
   Mediana = 89
   ```

2. **MAD hisoblash:**
   ```
   |x - 89|: [74, 4, 3, 2, 1, 1, 0, 1, 1, 2, 3, 4, 5]
   MAD = mediana([74, 4, 3, 2, 1, 1, 0, 1, 1, 2, 3, 4, 5]) = 2
   ```

3. **Modified Z-score hisoblash:**
   ```
   15 uchun: Modified Z = 0.6745 × (15 - 89) / 2 = -24.9  ← OUTLIER!
   85 uchun: Modified Z = 0.6745 × (85 - 89) / 2 = -1.35  ← Normal
   ```

---

## 💻 Python Implementatsiyasi

### Z-Score Usuli

```python
import numpy as np
from scipy import stats

def find_outliers_zscore(data, threshold=3):
    """
    Z-score usuli bilan outlierlarni topish
    
    Parameters:
    data: array-like, ma'lumotlar
    threshold: float, outlier chegarasi (odatda 2, 2.5 yoki 3)
    
    Returns:
    outliers: outlier qiymatlar
    z_scores: barcha Z-score qiymatlari
    """
    # Z-score hisoblash
    z_scores = np.abs(stats.zscore(data))
    
    # Outlierlarni aniqlash
    outlier_mask = z_scores > threshold
    outliers = data[outlier_mask]
    
    return outliers, z_scores

# Misol:
data = np.array([85, 87, 90, 92, 88, 91, 89, 15, 93, 86, 94, 88, 90])
outliers, z_scores = find_outliers_zscore(data, threshold=3)

print(f"Outlierlar: {outliers}")
print(f"Z-scores: {z_scores}")
```

### Modified Z-Score Usuli

```python
def find_outliers_modified_zscore(data, threshold=3.5):
    """
    Modified Z-score usuli bilan outlierlarni topish
    
    Parameters:
    data: array-like, ma'lumotlar
    threshold: float, outlier chegarasi (odatda 3.5)
    
    Returns:
    outliers: outlier qiymatlar
    modified_z_scores: barcha Modified Z-score qiymatlari
    """
    # Mediana hisoblash
    median = np.median(data)
    
    # MAD (Median Absolute Deviation) hisoblash
    mad = np.median(np.abs(data - median))
    
    # MAD = 0 bo'lsa, standart og'ishdan foydalanish
    if mad == 0:
        mad = np.std(data)
    
    # Modified Z-score hisoblash
    modified_z_scores = 0.6745 * (data - median) / mad
    
    # Outlierlarni aniqlash
    outlier_mask = np.abs(modified_z_scores) > threshold
    outliers = data[outlier_mask]
    
    return outliers, modified_z_scores

# Misol:
outliers_mod, mod_z_scores = find_outliers_modified_zscore(data, threshold=3.5)

print(f"Modified Z-score Outlierlar: {outliers_mod}")
print(f"Modified Z-scores: {mod_z_scores}")
```

---

## 📊 Taqqoslash Jadvali

| Xususiyat | Z-Score | Modified Z-Score |
|-----------|---------|------------------|
| **Asosi** | O'rtacha, Standart og'ish | Mediana, MAD |
| **Robustlik** | Past | Yuqori |
| **Normal taqsimot** | Talab qiladi | Talab qilmaydi |
| **Outlier ta'siri** | Yuqori | Past |
| **Hisoblash** | Oson | O'rtacha |
| **Threshold** | 2-3 | 3.5 |

---

## 🎯 Qachon Qaysi Usulni Ishlatish

### Z-Score Usuli:
- Ma'lumotlar normal taqsimotga yaqin
- Outlierlar kam
- Tez va sodda tahlil kerak
- Kichik ma'lumotlar to'plami

### Modified Z-Score Usuli:
- Ma'lumotlar normal taqsimotga ega emas
- Ko'p outlier kutilmoqda
- Robust tahlil kerak
- Katta ma'lumotlar to'plami

---

## ⚠️ Muhim Eslatmalar

1. **Outlierlarni avtomatik o'chirmang** - ularning sababini tekshiring
2. **Kontekstni hisobga oling** - ba'zi outlierlar qimmatli ma'lumot bo'lishi mumkin
3. **Bir nechta usulni taqqoslang** - turli usullar turli natijalar berishi mumkin
4. **Threshold qiymatini maqsadga qarab sozlang**
5. **Vizualizatsiya qiling** - grafik ko'rinish ko'pincha aniqroq

