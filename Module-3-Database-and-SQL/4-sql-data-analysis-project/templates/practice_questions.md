# SQL Mashq Savollari

Bu faylda SQL bilan ma'lumotlar tahlili bo'yicha amaliy mashq savollari berilgan.

## 📚 Boshlang'ich Darajasi

### 1. Ma'lumotlar Bazasini O'rganish
1. Mavjud jadvallar ro'yxatini chiqaring
2. `customers` jadvalidagi ustunlar nomini ko'rsating
3. `products` jadvalida nechta mahsulot borligini aniqlang
4. `orders` jadvalidagi eng katta buyurtma miqdorini toping

### 2. Oddiy SELECT so'rovlari
1. Barcha kategoriyalarni ko'rsating
2. Narxi 100,000 so'mdan yuqori bo'lgan mahsulotlarni toping
3. Toshkent shahrida yashovchi mijozlarni ko'rsating
4. "pending" holatidagi buyurtmalarni toping

### 3. Agregatsiya Funksiyalari
1. Jami mijozlar sonini hisoblang
2. O'rtacha mahsulot narxini toping
3. Eng qimmat va eng arzon mahsulot narxini ko'rsating
4. Jami buyurtmalar miqdorini hisoblang

## 📊 O'rta Daraja

### 4. GROUP BY bilan Ishlash
1. Har bir kategoriyada nechta mahsulot borligini aniqlang
2. Har bir shaharda nechta mijoz yashashipti?
3. Har bir buyurtma holatida nechta buyurtma bor?
4. Har bir mijoz necha marta buyurtma bergan?

### 5. JOIN Operatsiyalari
1. Mijoz ismi va ularning buyurtmalari miqdorini ko'rsating
2. Mahsulot nomi va kategoriya nomini birga ko'rsating
3. Eng ko'p xarid qilgan 10 ta mijozni toping
4. Har bir kategoriyada eng qimmat mahsulotni ko'rsating

### 6. Vaqt bilan Ishlash
1. Oxirgi 30 kun ichida qilingan buyurtmalarni ko'rsating
2. Har oy necha buyurtma qilinganini aniqlang
3. Hafta kunlari bo'yicha buyurtmalar statistikasini chiqaring
4. 2024-yil boshidagi buyurtmalarni ko'rsating

## 🎯 Ilg'or Daraja

### 7. Window Functions
1. Har bir mijozni umumiy xarajlari bo'yicha tartiblang (RANK)
2. Har bir kategoriyada mahsulotlarni narx bo'yicha raqamlang (ROW_NUMBER)
3. Oylik daromadning yugurib boruvchi jamini hisoblang
4. Har bir mahsulotning o'z kategoriyasidagi o'rnini aniqlang

### 8. Murakkab Subquery'lar
1. O'rtachadan yuqori narxga ega mahsulotlarni toping
2. Eng ko'p buyurtma qilgan mijozning barcha buyurtmalarini ko'rsating
3. Har bir kategoriyada eng arzon mahsulotni toping
4. Hech qanday buyurtma qilmagan mijozlarni aniqlang

### 9. CTE (Common Table Expressions)
1. Mijozlarni xarajlari bo'yicha segmentlarga ajrating
2. Mavsumiy trendlarni tahlil qiling
3. Mahsulot performance'ini baholang
4. Qayta xarid qiluvchi mijozlarni aniqlang

## 🔥 Expert Daraja

### 10. Biznes Tahlili Savollari
1. **RFM Tahlili**: Mijozlarni Recency, Frequency, Monetary qiymatlar bo'yicha tahlil qiling
2. **Cohort Tahlili**: Bir oyda ro'yxatdan o'tgan mijozlarning keyingi oylardagi faolligini kuzating
3. **Market Basket Analysis**: Qaysi mahsulotlar ko'pincha birga sotiladi?
4. **Customer Lifetime Value**: Har bir mijozning potentsial qiymatini hisoblang

### 11. Performance Optimizatsiya
1. Sekin ishlovchi so'rovlarni optimallashtiring
2. Index strategiyasini ishlab chiqing
3. Query execution plan'ni tahlil qiling
4. Memory va CPU samaradorligini oshiring

### 12. Real Biznes Savollari
1. Qaysi mahsulotlar inventarizatsiyadan chiqarilishi kerak?
2. Eng samarali marketing kanallari qaysilar?
3. Mavsumiy trendlar asosida zaxira rejasini tuzing
4. Mijozlar churn prediction uchun ma'lumotlarni tayyorlang

## 📁 Qo'shimcha Vazifalar

### 13. Data Quality Check
```sql
-- NULL qiymatlarni tekshirish
-- Dublikatlarni topish  
-- Ma'lumotlar turi validatsiyasi
-- Business rule validation
```

### 14. Reporting Queries
```sql
-- Kunlik hisobot
-- Haftalik performance dashboard
-- Oylik biznes ko'rsatkichlar
-- Yillik trend tahlili
```

### 15. Automation Scripts
```sql
-- Ma'lumotlarni tozalash
-- Avtomatik hisobotlar
-- Alert sistemasi
-- Backup va maintenance
```

## 🎖️ Bonus Challenges

1. **Real-time Dashboard**: Jonli dashboard uchun so'rovlar yozing
2. **Predictive Analytics**: ML uchun feature engineering
3. **Geographic Analysis**: Location-based insights
4. **Social Network Analysis**: Customer relationship mapping
5. **Time Series Forecasting**: Ma'lumotlarni vaqt qatorlari uchun tayyorlang

---

**Eslatma**: Har bir savol uchun:
- Avval o'zingiz yechishga harakat qiling
- SQL so'rovingizni yozing va test qiling
- Natijalarni tahlil qiling va xulosalar chiqaring
- Qiyin bo'lsa, `project_analysis.ipynb` dan yordam oling