# NumPy va Pandas - Uy Vazifasi

## Umumiy ko'rsatmalar
- Barcha topshiriqlarni Jupyter Notebook da yozing
- Har bir topshiriq uchun alohida bo'lim yarating  
- Kodingizni izohlar bilan to'ldiring
- Natijalarni tahlil qiling va xulosa yozing
- Ma'lumotlarni vizual ko'rinishda ham ko'rsating (ixtiyoriy)

---

## Topshiriq 1: NumPy Array Mastery (25 ball)

### 1.1 Array yaratish va manipulatsiya (10 ball)

**Vazifa**: Quyidagi arraylarni yarating va ularga amallar bajaring:

```python
# Yaratish kerak:
# 1. 1 dan 100 gacha bo'lgan juft sonlar arrayi
# 2. 5x5 o'lchamdagi tasodifiy matritsa (0-1 orasida)
# 3. 3x4 o'lchamdagi nollar bilan to'ldirilgan array
# 4. 0 dan 2π gacha 50 ta teng taqsimlangan qiymatlar
```

**Amallar**:
- Har bir arrayning shakli, o'lchami va data tipini chiqaring
- 5x5 matritsani 1x25 arrayga aylantiring
- Juft sonlar arrayidan eng katta va eng kichik 5 tani toping
- Sin va cos qiymatlarini hisoblang trigonometrik array uchun

### 1.2 Advanced indexing va filtering (15 ball)

**Vazifa**: 10x10 tasodifiy matritsa yarating va quyidagilarni bajaring:

```python
# Sizning kodingiz:
import numpy as np
np.random.seed(42)  # Takrorlanuvchi natijalar uchun
matrix = np.random.randint(1, 100, (10, 10))
```

**Topshiriqlar**:
1. Diagonal elementlarni oling
2. 50 dan katta bo'lgan barcha elementlarni toping
3. Har bir qatorning eng katta elementini toping  
4. Matritsaning yuqori uchburchagi elementlarini 0 bilan almashtiring
5. 3x3 submatritsa oling (markaziy qism)
6. Matritsa ustunlarini o'rtacha qiymat bo'yicha tartiblang

---

## Topshiriq 2: Pandas DataFrame Exploration (30 ball)

### 2.1 Dataset tayyorlash (10 ball)

**Vazifa**: Quyidagi tuzilmada 50 ta talaba ma'lumotlari bilan DataFrame yarating:

```python
# Ustunlar:
- talaba_id: 1001 dan boshlab
- ism: Tasodifiy ismlar
- fakultet: ['Informatika', 'Iqtisod', 'Muhandislik', 'Tibbiyot', 'Huquq']
- kurs: 1-4 orasida
- yosh: 18-25 orasida
- gpa: 2.0-4.0 orasida (1 kasr raqam)
- stipendiya: True/False
- shahar: ['Toshkent', 'Samarqand', 'Buxoro', 'Andijon', 'Namangan']
```

**Qo'shimcha talablar**:
- Realistik ma'lumotlar (masalan, 4-kurs talabalar kattaroq)
- Ba'zi missing values qo'shing (5-10 ta)
- DataFrame ni CSV faylga saqlang

### 2.2 Exploratory Data Analysis (20 ball)

**Vazifa**: Yaratilgan dataset bo'yicha to'liq tahlil o'tkazing:

**A. Asosiy statistikalar (5 ball)**:
- DataFrame haqida umumiy ma'lumot
- Har bir ustun uchun statistik ko'rsatkichlar
- Missing values tekshirish va tozalash

**B. Kategorik tahlil (8 ball)**:
- Fakultetlar bo'yicha taqsimot
- Shaharlar bo'yicha talabalar soni
- Stipendiya oluvchilar foizi
- Kurs bo'yicha o'rtacha GPA

**C. Advanced queries (7 ball)**:
- Eng yuqori GPA ga ega 10 ta talaba
- Informatika fakultetida stipendiya olmaydigan talabalar
- Har bir shahardan eng yaxshi talaba (GPA bo'yicha)
- 3.5+ GPA va 4-kurs talabalar
- Fakultet va kurs bo'yicha pivot table

---

## Topshiriq 3: Real Dataset Analysis (35 ball)

### 3.1 E-commerce ma'lumotlari tahlili (35 ball)

**Vazifa**: Quyidagi tuzilmada 200 ta sotish ma'lumotlari yarating va tahlil qiling:

```python
# Dataset tuzilmasi:
- order_id: Unique identifikator
- customer_id: Mijoz ID (100 xil mijoz)
- product_category: ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
- product_name: Mahsulot nomi
- quantity: Miqdor (1-10)
- price: Narx (10,000 - 500,000 so'm)
- discount: Chegirma (0-30%)
- order_date: Sana (2024 yil davomida)
- customer_city: Mijoz shahri
- delivery_status: ['Delivered', 'Pending', 'Cancelled']
```

**Tahlil topshiriqlari**:

**A. Sales Performance (12 ball)**:
1. Umumiy sotuv hajmi va daromad
2. Oylik sotuv trendi  
3. Eng ko'p sotilgan mahsulot kategoriyalari
4. O'rtacha buyurtma qiymati (AOV)

**B. Customer Analysis (12 ball)**:
1. Eng faol mijozlar (ko'p xarid qilganlar)
2. Shaharlar bo'yicha sotuv taqsimoti
3. Mijozlarning o'rtacha xarid miqdori
4. Takroriy mijozlar foizi

**C. Product Insights (11 ball)**:
1. Kategoriya bo'yicha profitability
2. Chegirma ta'sirini tahlil qilish
3. Seasonal trends (fasllik o'zgarishlar)
4. Delivery status tahlili
5. Inventory management insights

**Natija**: Har bir tahlil uchun qisqacha xulosalar yozing.

---

## Topshiriq 4: Advanced Operations (20 ball)

### 4.1 Multi-dataset analysis (20 ball)

**Vazifa**: Uch xil dataset yarating va ularni birlashtiring:

**Dataset 1 - Mijozlar**:
```python
- customer_id
- customer_name  
- age
- gender
- registration_date
- city
```

**Dataset 2 - Mahsulotlar**:
```python
- product_id
- product_name
- category
- supplier
- cost_price
- selling_price
- stock_quantity
```

**Dataset 3 - Orders**:
```python
- order_id
- customer_id
- product_id
- quantity
- order_date
- status
```

**Birlashtirish va tahlil**:
1. Barcha datasetlarni to'g'ri birlashtiring
2. Customer lifetime value hisoblang
3. Product profitability tahlili
4. Supplier performance
5. Customer segmentation (RFM analysis asosida)
6. Inventory optimization recommendations

---

## Bonus Topshiriq: Data Visualization (10 qo'shimcha ball)

**Vazifa**: Yuqoridagi tahlillar uchun vizualizatsiya yarating:

1. **Matplotlib** yoki **Seaborn** ishlatib:
   - Bar charts - kategorik ma'lumotlar uchun
   - Line plots - trend tahlili uchun  
   - Heatmaps - korrelyatsiya uchun
   - Scatter plots - bog'lanishlar uchun
   - Histograms - taqsimot uchun

2. **Interaktiv grafiklar** (ixtiyoriy):
   - Plotly ishlatib dashboard yarating

---

## Topshirish talablari

### Format:
- **Fayl nomi**: `ism_familiya_numpy_pandas.ipynb`
- **Qo'shimcha fayllar**: CSV datasets, agar kerak bo'lsa

### Kod sifati:
- ✅ O'qilishi oson kod
- ✅ Tushunarli o'zgaruvchi nomlari  
- ✅ Har bo'lim uchun izohlar
- ✅ Markdown hujjatlari bilan tushuntirish
- ✅ Natijalarni tahlil qilish

### Taqdimot:
- ✅ Har topshiriq uchun qisqacha xulosalar
- ✅ Business insights
- ✅ Recommendations

---

## Baholash mezonlari

| Topshiriq | Max Ball | Asosiy mezonlar |
|-----------|----------|-----------------|
| NumPy Arrays | 25 | Array manipulations, indexing |
| Pandas DataFrame | 30 | EDA, filtering, grouping |
| Real Dataset | 35 | Advanced analysis, insights |
| Multi-dataset | 20 | Merging, complex queries |
| **Jami** | **110** | |
| Bonus Visualization | +10 | Chart quality, insights |

### Bal taqsimoti:
- **A** (90-110 ball): Excellent work
- **B** (80-89 ball): Good analysis  
- **C** (70-79 ball): Satisfactory
- **D** (60-69 ball): Needs improvement
- **F** (<60 ball): Insufficient

---

## Qo'shimcha maslahatlar

### 🔧 Technical tips:
- `pd.set_option('display.max_columns', None)` - barcha ustunlarni ko'rsatish
- `df.info(memory_usage='deep')` - xotira ishlatilishini tekshirish
- `df.describe(include='all')` - barcha ustunlar statistikasi

### 📊 Analysis tips:
- Har doim ma'lumotlar sifatini tekshiring
- Outlier'larni aniqlang va boshqaring
- Business context ni hisobga oling
- Actionable insights bering

### 💡 Bonus points uchun:
- Performance optimization
- Error handling
- Code reusability
- Creative insights

---

**Omad tilaymiz! Ma'lumotlar olamini kashf qiling! 🚀📊**