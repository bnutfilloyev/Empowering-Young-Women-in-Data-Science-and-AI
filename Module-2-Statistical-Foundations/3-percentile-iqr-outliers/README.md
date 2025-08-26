# Percentile, IQR va Outlierlar

**Mavzu:** Kvantillar, Interquartile Range (IQR) va Boxplot Asoslari

## Mavzu Haqida

Ushbu bo'limda ma'lumotlar taqsimotining pozitsiya ko'rsatkichlarini o'rganamiz. Percentillar, quartillar, IQR va outlierlarni aniqlash usullarini amaliy misollar orqali o'zlashtirish.

## O'rganish Maqsadlari

Ushbu mavzuni tugatgandan so'ng siz quyidagilarni bilasiz:

1. **Kvantillar va Percentillar:**
   - Kvantil va percentil tushunchalari
   - Turli percentillarni hisoblash usullari
   - Percentillarning talqini va amaliy qo'llanilishi

2. **Quartillar va IQR:**
   - Q1, Q2, Q3 quartillarni hisoblash
   - Interquartile Range (IQR) ning ma'nosi
   - IQR dan foydalanish holatlari

3. **Boxplot va Vizualizatsiya:**
   - Boxplot elementlari va ularning ma'nosi
   - Boxplot yaratish va talqini
   - Taqsimot shaklini vizual baholash

4. **Outlierlarni Aniqlash:**
   - IQR usuli bilan outlierlarni topish
   - Z-score usuli bilan outlierlarni topish
   - Outlierlar bilan ishlash strategiyalari

## Fayl Tuzilishi

```
3-percentile-iqr-outliers/
├── conception.ipynb          # Asosiy nazariy va amaliy dars
├── hometask.ipynb           # Uy vazifasi (2 kunlik) - AQSh shtatlar ma'lumotlari
├── group1_salaries.ipynb    # 1-Guruh: Kompaniya maoshlari tahlili
├── group2_ages.ipynb        # 2-Guruh: Talabalar yoshi tahlili
├── group3_prices.ipynb      # 3-Guruh: Mahsulot narxlari tahlili
├── group4_scores.ipynb      # 4-Guruh: Test natijalari tahlili
├── StudentsPerformance.csv  # Talabalar natijalari (conception uchun)
├── state.csv               # AQSh shtatlar ma'lumotlari (hometask uchun)
└── README.md               # Ushbu fayl
```

## Ma'lumotlar To'plamlari

### 1. StudentsPerformance.csv (Conception uchun)
Talabalarning imtihon natijalarini o'z ichiga oladi:
- **math score**: Matematika bahosi
- **reading score**: O'qish bahosi  
- **writing score**: Yozish bahosi
- **gender**: Jinsi
- **race/ethnicity**: Irqiy tegishlilik
- **parental level of education**: Ota-onalarning ta'lim darajasi
- **lunch**: Tushlik turi (standard/free/reduced)
- **test preparation course**: Test tayyorgarlik kursi

### 2. state.csv (Hometask uchun)
AQSh shtatlarining demografik ma'lumotlari:
- **State**: Shtat nomi
- **Population**: Aholi soni
- **Murder.Rate**: 100,000 aholi uchun qotillik darajasi
- **Abbreviation**: Shtat qisqartmasi

### 3. Class Task Ma'lumotlari (Sintetik)
4 turli ma'lumot to'plami guruh ishi uchun:
- **Company Salaries**: Kompaniya maoshlari (20 ta)
- **Student Ages**: Talabalar yoshi (25 ta)
- **Product Prices**: Mahsulot narxlari (30 ta)
- **Test Scores**: Test natijalari (22 ta)

## Asosiy Tushunchalar

### Kvantillar (Quantiles)
Ma'lumotlar to'plamini ma'lum foizlarga bo'luvchi qiymatlar:
- **0.25-kvantil (Q1)**: Ma'lumotlarning 25% qismi bu qiymatdan kichik
- **0.50-kvantil (Q2)**: Mediana, 50% ajratuvchi
- **0.75-kvantil (Q3)**: Ma'lumotlarning 75% qismi bu qiymatdan kichik

### IQR (Interquartile Range)
```
IQR = Q3 - Q1
```
O'rta 50% ma'lumotlarning tarqalish ko'rsatkichi.

### Outlierlar
**IQR usuli:**
```
Outlier ← x < Q1 - 1.5×IQR  yoki  x > Q3 + 1.5×IQR
```

**Z-score usuli:**
```
Outlier ← |z-score| > 3
```

## Amaliy Qo'llanilish

1. **Ta'lim sohasida:**
   - Talabalar natijalarini baholash
   - O'qitish sifatini tahlil qilish
   - Maxsus e'tibor talab qiluvchi talabalarni aniqlash

2. **Biznes tahlili:**
   - Mijozlar xatti-harakatini o'rganish
   - Narx strategiyasini belgilash
   - Anomaliyalarni aniqlash

3. **Ilmiy tadqiqotlar:**
   - Ma'lumotlar sifatini tekshirish
   - Eksperiment natijalarini tahlil qilish
   - Noaniq qiymatlarni aniqlash

## Ishni Boshlash

1. **Conception notebook** bilan boshlang - nazariy asoslarni o'rganing
2. **Class task** ni darsda guruh bo'lib bajaring (45 daqiqa)
3. **Hometask** ni uyda mustaqil bajaring (2 kun)
4. Real ma'lumotlar bilan tajriba to'plang

## Dars Rejasi

### Nazariya (30 daqiqa)
- Conception notebook bilan asosiy tushunchalar
- Amaliy misollar ko'rish

### Guruh Ishi (45 daqiqa)  
- 4 guruhga bo'linish
- Har guruh o'z ma'lumoti bilan ishlash
- Natijalarni taqdim etish (12 daqiqa)

### Uy Vazifasi Tushuntirish (15 daqiqa)
- Hometask talablarini tushuntirish
- AQSh shtatlar ma'lumotlari bilan tanishish

## Texnik Talablar

### Kerakli Kutubxonalar:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
```

### Python Versiyasi:
- Python 3.7+
- Jupyter Notebook yoki JupyterLab

## Yordam va Qo'shimcha Resurslar

### Foydali Funksiyalar:
- `numpy.percentile()` - percentillarni hisoblash
- `pandas.DataFrame.quantile()` - kvantillarni hisoblash
- `matplotlib.pyplot.boxplot()` - boxplot yaratish
- `seaborn.boxplot()` - kengaytirilgan boxplot
- `scipy.stats.zscore()` - z-score hisoblash

### Qo'shimcha O'qish:
- Descriptive Statistics
- Data Visualization
- Exploratory Data Analysis
- Robust Statistics

## Nazariy Asoslar

### Kvantillar va Percentillar: Chuqur Tushuncha

**Kvantil** - ma'lumotlar to'plamini ma'lum foizlarga bo'luvchi nuqta. Bu tushuncha statistikada ma'lumotlar taqsimotining pozitsion xarakteristikalarini tavsiflash uchun ishlatiladi.

#### Kvantillarning matematik ta'rifi:
Agar X tasodifiy o'zgaruvchi bo'lsa, p-kvantil (0 < p < 1) quyidagi shartni qanoatlantiruvchi x_p qiymatidir:
```
P(X ≤ x_p) ≥ p va P(X ≥ x_p) ≥ 1-p
```

#### Asosiy kvantil turlari:
- **Mediana (Q2)**: 0.5-kvantil, ma'lumotlarni teng ikkiga bo'ladi
- **Quartillar**: Ma'lumotlarni 4 teng qismga bo'ladi (Q1, Q2, Q3)
- **Desillar**: Ma'lumotlarni 10 teng qismga bo'ladi (D1, D2, ..., D9)
- **Percentillar**: Ma'lumotlarni 100 teng qismga bo'ladi (P1, P2, ..., P99)

### IQR (Interquartile Range): Mustahkam Tarqalish O'lchovi

**IQR = Q3 - Q1** - bu o'rta 50% ma'lumotlarning tarqalish darajasini ko'rsatadi.

#### IQR ning afzalliklari:
1. **Mustahkamlik**: Outlierlardan kam ta'sirlanadi
2. **Interpretatsiya**: O'rta yarmi ma'lumotlarning tarqalishini ko'rsatadi
3. **Outlier aniqlash**: IQR asosida outlierlarni topish mumkin

#### Outlierlarni aniqlash qoidasi:
```
Outlier ← x < Q1 - 1.5×IQR  yoki  x > Q3 + 1.5×IQR
```

Bu qoida Jon Tukey tomonidan taklif qilingan va boxplot vizualizatsiyasida keng qo'llaniladi.

### Boxplot: Vizual Tahlil Vositasi

Boxplot (quti diagrammasi) ma'lumotlar taqsimotini 5 asosiy ko'rsatkich orqali tasvirlaydi:

1. **Minimum**: Eng kichik outlier bo'lmagan qiymat
2. **Q1**: Birinchi quartil (25% chegarasi)
3. **Mediana (Q2)**: Ikkinchi quartil (50% chegarasi)  
4. **Q3**: Uchinchi quartil (75% chegarasi)
5. **Maksimum**: Eng katta outlier bo'lmagan qiymat

#### Boxplotdan olinadigan ma'lumotlar:
- **Markaziy tendentsiya**: Mediana orqali
- **Tarqalish**: IQR orqali
- **Asimmetriya**: Mediananing Q1 va Q3 ga nisbatan joylashuvi
- **Outlierlar**: Alohida nuqtalar sifatida

### Outlierlar: Sabablari va Hal Qilish Usullari

#### Outlierlarning turlari:
1. **Tabiiy outlierlar**: Ma'lumotlar tabiatiga xos
2. **Xato outlierlar**: O'lchash yoki kiritish xatolari natijasida
3. **Qiziqarli outlierlar**: Maxsus hodisalar yoki noyob holatlar

#### Outlierlar bilan ishlash strategiyalari:
1. **Tekshirish**: Outlier haqiqiy yoki xato ekanligini aniqlash
2. **Saqlash**: Tabiiy outlierlarni tahlilda qoldirish
3. **O'zgartirish**: Winsorization yoki log transformatsiya
4. **Olib tashlash**: Faqat xato ma'lumotlar uchun
5. **Alohida tahlil**: Outlierlarni mustaqil o'rganish

### Amaliy Qo'llanish Sohalari

#### 1. Ta'lim sohasida:
- Talabalar natijalarini baholash
- O'qitish sifatini monitoring qilish
- Maxsus e'tibor talab qiluvchi talabalarni aniqlash

#### 2. Biznes tahlili:
- Mijozlar xatti-harakatini segmentatsiya qilish
- Narx strategiyasini ishlab chiqish
- Risk management va anomaliya detection

#### 3. Tibbiyot sohasida:
- Normal va patologik holatlarni ajratish
- Dori ta'sirini baholash
- Epidemiologik tadqiqotlar

#### 4. Iqtisodiyot va moliya:
- Daromad taqsimotini o'rganish
- Bozor anomaliyalarini aniqlash
- Kredit risklarini baholash
---

**Muvaffaqiyat tilaymiz!** 🎯📊
