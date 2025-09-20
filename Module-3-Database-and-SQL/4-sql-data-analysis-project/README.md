# 📊 SQL bilan Ma'lumotlar Tahlili Loyihasi

## 🎯 Loyiha maqsadi
Ushbu loyiha SQL ko'nikmalarini real ma'lumotlar to'plamida qo'llash va to'liq EDA (Exploratory Data Analysis) jarayonini o'rganish uchun mo'ljallangan.

## 📋 Loyiha tarkibi

### 📁 Papkalar tuzilishi:
```
4-sql-data-analysis-project/
├── README.md                    # Ushbu fayl
├── project_analysis.ipynb       # Asosiy loyiha notebook
├── student_template.ipynb       # Talabalar uchun shablon
├── datasets/                    # Ma'lumotlar to'plami
│   ├── ecommerce_data.csv      # Asosiy ma'lumotlar fayli
│   ├── create_database.py      # SQLite bazasi yaratish
│   └── data_dictionary.md      # Ma'lumotlar lug'ati
├── templates/                   # Qo'shimcha shablonlar
│   ├── eda_checklist.md        # EDA ro'yxati
│   └── sql_queries_template.sql # SQL so'rovlar shablon
└── results/                     # Natijalar papkasi
    ├── analysis_report.md      # Tahlil hisoboti
    └── visualizations/         # Grafiklar
```

## 🎓 O'quv maqsadlari

### 1. SQL EDA ko'nikmalarini rivojlantirish:
- **Ma'lumotlarni o'rganish** - COUNT, SUM, AVG, MIN, MAX
- **Guruhlash va agregatsiya** - GROUP BY, HAVING
- **Bog'lanishlar** - JOIN operatorlari
- **Murakkab so'rovlar** - Sub-query, CTE, Window Functions

### 2. Real biznes masalalarini yechish:
- **Savdo ko'rsatkichlari** tahlili
- **Mijozlar segmentatsiyasi**
- **Mahsulot samaradorligi** baholash
- **Mavsumiy trendlar** aniqlash

### 3. Vizualizatsiya va hisobot tayyorlash:
- **Python/pandas** bilan ma'lumotlarni ko'rish
- **Matplotlib/Seaborn** bilan grafiklar
- **Natijalarni sharhlash** va tavsiyalar berish

## 📊 Ma'lumotlar to'plami: E-commerce Sales Data

### Ma'lumotlar haqida:
- **Davr**: 2023-2024 yil
- **Yozuvlar soni**: ~10,000 ta savdo
- **Ustunlar**: 15 ta asosiy maydon
- **Mamlakat**: O'zbekiston (shahar va viloyatlar)

### Asosiy jadvallar:
1. **orders** - buyurtmalar ma'lumotlari
2. **customers** - mijozlar ma'lumotlari  
3. **products** - mahsulotlar katalogi
4. **categories** - mahsulot kategoriyalari
5. **order_items** - buyurtma tarkibi

## 🚀 Loyihani boshlash

### 1. Tayyorgarlik:
```bash
cd Module-3-Database-and-SQL/4-sql-data-analysis-project
pip install pandas matplotlib seaborn sqlite3
```

### 2. Ma'lumotlar bazasini yaratish:
```python
python datasets/create_database.py
```

### 3. Asosiy notebook ni ochish:
```bash
jupyter notebook project_analysis.ipynb
```

## 📝 Loyiha bosqichlari

### 1-bosqich: Ma'lumotlarni o'rganish (30 daqiqa)
- Jadvallar tuzilishini tahlil qilish
- Asosiy statistikalarni hisoblash
- Ma'lumotlar sifatini tekshirish

### 2-bosqich: Biznes savollariga javob topish (45 daqiqa)
- Eng yaxshi mijozlarni aniqlash
- Mashhur mahsulotlarni topish
- Mavsumiy trendlarni o'rganish
- Hudud bo'yicha tahlil

### 3-bosqich: Chuqur tahlil (30 daqiqa)
- Mijozlar segmentatsiyasi (RFM)
- Mahsulot tavsiyalari
- Churn prediction
- Pricing analysis

### 4-bosqich: Natijalar va tavsiyalar (15 daqiqa)
- Asosiy topilmalarni xulosalash
- Biznes tavsiyalari berish
- Keyingi qadamlarni rejalashtirish

## 🎯 Kutilayotgan natijalar

### Talabalar o'rganadi:
- ✅ Real ma'lumotlar bilan ishlash
- ✅ Murakkab SQL so'rovlarni yozish
- ✅ Business Intelligence asoslari
- ✅ Ma'lumotlarni vizualizatsiya qilish
- ✅ Analitik fikrlash ko'nikmasi

### Yakuniy mahsulot:
- 📊 To'liq tahlil hisoboti
- 📈 Infografik va grafiklar
- 💡 Biznes tavsiyalari
- 🔍 SQL so'rovlar to'plami

## 🔗 Qo'shimcha resurslar

### SQL ko'nikmalarini mustahkamlash:
- [SQLite rasmiy hujjatlari](https://sqlite.org/docs.html)
- [SQL exercises](https://sqlbolt.com/)
- [Advanced SQL patterns](https://mode.com/sql-tutorial/)

### Ma'lumotlar tahlili:
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Data visualization with Python](https://python-graph-gallery.com/)
- [Statistical analysis guide](https://scipy-lectures.org/)

---

*🚀 Loyihani boshlash uchun `project_analysis.ipynb` faylini oching!*