# Javoblar Kaliti - Markaziy Tendentsiya va Tarqalish
## Faqat O'qituvchilar Uchun

### Individual Amaliyot Yechimi

**Talaba Baholari:** [85, 92, 78, 96, 88, 74, 91, 83, 87, 95, 79, 89, 93, 82, 86, 90, 77, 94, 81, 88]

```python
import pandas as pd
import numpy as np

scores = [85, 92, 78, 96, 88, 74, 91, 83, 87, 95, 79, 89, 93, 82, 86, 90, 77, 94, 81, 88]
scores_series = pd.Series(scores)

# Markaziy Tendentsiya
mean_score = scores_series.mean()          # 86.45
median_score = scores_series.median()      # 87.5
mode_score = scores_series.mode()          # 88 (ikki marta uchraydi)

# Tarqalish
range_score = scores_series.max() - scores_series.min()  # 22
variance_score = scores_series.var()       # 36.68
std_score = scores_series.std()           # 6.06
```

**Talqin:**
- O'rtacha (86.45) va mediana (87.5) yaqin → taxminan simmetrik taqsimot
- Standart og'ish (6.06) o'rtacha tarqalishni ko'rsatadi
- Ko'pchilik talabalar o'rtachadan 6 ball atrofida baho oladi

---

### A-Guruh Yechimi: Kompaniya Maoshlari

**Maoshlar:** [45000, 52000, 48000, 65000, 58000, 72000, 61000, 55000, 67000, 59000, 63000, 56000, 69000, 120000, 51000, 62000, 57000, 64000, 60000, 68000]

```python
salaries = [45000, 52000, 48000, 65000, 58000, 72000, 61000, 55000, 67000, 59000, 
           63000, 56000, 69000, 120000, 51000, 62000, 57000, 64000, 60000, 68000]
salary_series = pd.Series(salaries)

# Natijalar
mean_salary = salary_series.mean()         # 61,050
median_salary = salary_series.median()     # 60,500
std_salary = salary_series.std()          # 14,356

# Haddan tashqari qiymatlarni tahlil qilish
Q1 = salary_series.quantile(0.25)         # 56,250
Q3 = salary_series.quantile(0.75)         # 66,500
IQR = Q3 - Q1                             # 10,250
upper_bound = Q3 + 1.5 * IQR              # 81,875
# 120,000 > 81,875 → haddan tashqari qiymat aniqlandi
```

**Asosiy Kuzatishlar:**
- 120,000 maosh haddan tashqari qiymat (ehtimol rahbar/yuqori lavozim)
- Mediana (60,500) o'rtachadan (61,050) ko'proq vakillik qiladi
- Haddan tashqari qiymat alohida qilinsa: o'rtacha ≈ 58,947

**Tavsiyalar:**
- **Byudjet:** Oddiy xodim xarajatlari uchun medianadan foydalaning
- **Ishga yollash:** Nomzodlarni jalb qilish uchun medianadan foydalaning
- **Ichki adolat:** Umumiy kompensatsiya byudjetini baholash uchun o'rtachani ishlating

---

### B-Guruh Yechimi: Kunlik Haroratlar

**Haroratlar:** [22, 25, 23, 27, 29, 24, 26, 28, 25, 23, 24, 26, 30, 28, 25, 27, 24, 26, 23, 25, 29, 27, 24, 26, 28, 25, 23, 27, 26, 24]

```python
temps = [22, 25, 23, 27, 29, 24, 26, 28, 25, 23, 24, 26, 30, 28, 25, 27, 24, 26, 
         23, 25, 29, 27, 24, 26, 28, 25, 23, 27, 26, 24]
temp_series = pd.Series(temps)

# Natijalar
mean_temp = temp_series.mean()             # 25.4°C
median_temp = temp_series.median()         # 25.0°C
mode_temp = temp_series.mode()             # 24, 25, 26, 27 (ko'p moda)
std_temp = temp_series.std()              # 2.01°C
range_temp = temp_series.max() - temp_series.min()  # 8°C
```

**Asosiy Kuzatishlar:**
- Juda barqaror haroratlar (past standart og'ish)
- O'rtacha va mediana juda yaqin → simmetrik taqsimot
- Ko'plab moda umumiy harorat oraliqlarini ko'rsatadi
- Kunlarning 68% 23.4°C va 27.4°C orasida

**Tavsiyalar:**
- **Ob-havo xabarlari:** Vakillik sifatida o'rtachani (25.4°C) ishlating
- **Bashoratlilik:** Yuqori (past o'zgaruvchanlik)
- **Rejalashtirish:** Ko'p kunlarda o'rtachadan 2°C atrofida harorat kutiladi

---

### Uy Vazifasi Yechimlari

#### B-Qism, 1-Masala: O'qish Soatlari
**Ma'lumotlar:** [8, 12, 15, 10, 20, 25, 18, 14, 16, 22, 12, 19, 17, 13, 21]

```python
study_hours = [8, 12, 15, 10, 20, 25, 18, 14, 16, 22, 12, 19, 17, 13, 21]
hours_series = pd.Series(study_hours)

mean = hours_series.mean()                 # 16.13 soat
median = hours_series.median()             # 16.0 soat
mode = hours_series.mode()                 # 12 soat (ikki marta uchraydi)
range_val = hours_series.max() - hours_series.min()  # 17 soat
variance = hours_series.var()              # 24.55
std_dev = hours_series.std()              # 4.95 soat
```

#### B-Qism, 2-Masala: Mahsulot Narxlari
**Ma'lumotlar:** [29.99, 31.50, 28.75, 32.00, 30.25, 29.50, 33.75, 31.00, 28.99, 30.75, 32.50, 29.25, 31.75, 30.00, 28.50, 33.00, 29.75, 32.25, 30.50, 31.25]

```python
prices = [29.99, 31.50, 28.75, 32.00, 30.25, 29.50, 33.75, 31.00, 28.99, 30.75, 
          32.50, 29.25, 31.75, 30.00, 28.50, 33.00, 29.75, 32.25, 30.50, 31.25]
price_series = pd.Series(prices)

mean = price_series.mean()                 # $30.61
median = price_series.median()             # $30.38
std_dev = price_series.std()              # $1.42

# 68% oralig'i (o'rtacha ± 1 standart og'ish)
lower_68 = mean - std_dev                  # $29.19
upper_68 = mean + std_dev                  # $32.03
```

#### C-Qism: Biznes Daromad Tahlili
**Ma'lumotlar:** [45, 52, 48, 61, 58, 67, 71, 69, 63, 55, 49, 73] (ming AQSH dollari)

```python
revenue = [45, 52, 48, 61, 58, 67, 71, 69, 63, 55, 49, 73]
revenue_series = pd.Series(revenue)

mean = revenue_series.mean()               # $59.17K
median = revenue_series.median()           # $59.5K
std_dev = revenue_series.std()            # $9.19K
```

**Biznes Tahlili:**
- **Odatiy daromad:** ~$59K ming (o'rtacha va mediana juda yaqin)
- **Barqarorlik:** O'rtacha o'zgaruvchanlik (standart og'ish = $9.19K ming)
- **G'ayrioddiy oylar:** Dekabr ($73K ming) eng yuqori, Yanvar ($45K ming) eng past

**Tavsiyalar:**
- **Byudjet maqsadlari:** O'rtachani ($59.17K ming) ishlatang - odatiy ishlashni ifodalaydi
- **Investor hisoboti:** Medianani ($59.5K ming) ishlatang - mustahkam ko'rsatkich
- **Cash flow planning:** Consider ±$9K variation around mean

---

### Part D: Creative Dataset Examples

#### Right-skewed Example (Mean > Median):
**Context:** House prices in a neighborhood
**Data:** [150, 160, 170, 180, 190, 200, 210, 450] (thousands)
- Mean: $213.75K
- Median: $185K
- The expensive house pulls the mean up

#### Left-skewed Example (Mean < Median):
**Context:** Test scores (some students performed poorly)
**Data:** [45, 50, 85, 88, 90, 92, 95, 98]
- Mean: 80.4
- Median: 89
- Poor scores pull the mean down

#### Symmetric Example (Mean ≈ Median):
**Context:** Heights of adults
**Data:** [160, 165, 170, 175, 180, 185, 190, 195] (cm)
- Mean: 177.5 cm
- Median: 177.5 cm
- Perfectly symmetric distribution

---

### Common Student Errors and Solutions

#### Error 1: Confusing variance and standard deviation units
**Problem:** "Variance is 25, so spread is 25 points"
**Solution:** Standard deviation (5) is in original units, variance (25) is squared

#### Error 2: Using mean when median is appropriate
**Problem:** Reporting mean salary when CEO outlier present
**Solution:** Identify outliers first, use median for skewed data

#### Error 3: Forgetting to interpret results
**Problem:** Just calculating numbers without context
**Solution:** Always ask "What does this number mean in practice?"

#### Error 4: Mode confusion with continuous data
**Problem:** Expecting unique mode in continuous datasets
**Solution:** Explain that mode is most useful for categorical or discrete data

---

### Ilg'or Talabalar Uchun Qo'shimcha Faoliyatlar

1. **Variatsiya Koeffitsienti:** CV = (standart og'ish / o'rtacha) × 100% ni hisoblang
2. **Haddan Tashqari Qiymatlarni Aniqlash:** IQR usulini sistemali ravishda ishlating
3. **Taqsimot Shakllari:** Qiyalik naqshlarini aniqlanig
4. **Haqiqiy Ma'lumotlar Loyihasi:** Hukumat/biznes manbalaridan haqiqiy ma'lumotlar to'plamini tahlil qiling

---

### Baholash Mezoni Tafsilotlari

#### A'lo (90-100%):
- Barcha hisoblar to'g'ri va aniq tushuntirish bilan
- Har bir ko'rsatkichni qachon ishlatishni chuqur tushunadi
- Haqiqiy dunyodagi chuqur talqinlar beradi
- Kod toza, yaxshi izohli va samarali

#### Yaxshi (80-89%):
- Ko'pchilik hisoblar to'g'ri va yetarli tushuntirish bilan
- Kichik bo'shliqlar bilan yaxshi tushunish ko'rsatadi
- Oqilona talqinlar beradi
- Kod kichik uslub muammolari bilan ishlaydi

#### Qoniqarli (70-79%):
- Asosiy hisoblar to'g'ri lekin cheklangan tushuntirish
- Asosiy tushunishni ko'rsatadi
- Minimal talqin yoki kontekst
- Kod ishlaydi lekin samarasiz bo'lishi mumkin

#### Yaxshilash Kerak (<70%):
- Ko'plab hisob xatolari yoki etishmayotgan ish
- Tushunchalar haqida noto'g'ri tasavvurlar ko'rsatadi
- Kam yoki umuman talqin berilmagan
- Kodda sezilarli xatolar bor yoki ishlamaydi

---

### O'qitish Maslahatlari

1. **Kichik raqamlar bilan boshlang:** Dastlabki namoyishlar uchun [1,2,3,4,5] kabi ma'lumotlar to'plamini ishlating
2. **Vizual yordamchi vositalar:** O'rtacha va medianani ko'rsatish uchun raqam chiziqlarini chizing
3. **Haqiqiy misollar:** Har doim talaba tajribalari bilan bog'lang
4. **Tushunishni tekshiring:** "Bu raqam nimani anglatadi?" tez-tez so'rang
5. **Umumiy xatolar:** Dispersiya birliklari haqida chalkashlikka tayyorlaning
6. **Haddan tashqari qiymatlar ta'kidi:** Turli ko'rsatkichlarga haddan tashqari qiymatlar qanday ta'sir qilishiga ko'proq vaqt ajrating

### Texnologiya Muammolarini Yechish

#### Keng Tarqalgan Muammolar:
1. **Kutubxona import qilish muvaffaqiyatsiz:** O'rnatishni tekshiring, pip install dan foydalaning
2. **Moda seriya qaytaradi:** `.values[0]` bilan qiymatni ajratib oling
3. **Bo'sh moda:** Barcha qiymatlar noyob bo'lgan holatni ko'rib chiqing
4. **Aniqlik xatolari:** Ko'rsatish uchun `.round(2)` dan foydalaning

#### Zaxira Usullari:
1. **Qo'lda hisoblash:** Bosqichma-bosqich arifmetikani ko'rsating
2. **Excel muqobili:** Elektron jadval shablonlarini taqdim eting
3. **Onlayn kalkulyatorlar:** Veb-ga asoslangan vositalarni tayyor qiling
4. **Oldindan hisoblangan misollar:** Kod ishlamasa natijalarni tayyor qiling
