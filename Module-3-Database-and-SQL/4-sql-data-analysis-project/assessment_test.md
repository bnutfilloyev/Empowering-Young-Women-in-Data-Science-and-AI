# Module 3 - Final Lesson Test

**Kurs**: AI va Data Science Foundation  
**Module**: 3 - Database va SQL  
**Dars**: 4 - SQL bilan Data Analysis Project  
**Vaqt**: 90 daqiqa  

---

## 📋 Test Ko'rsatmalari

- **Jami savollar**: 25 ta
- **Umumiy ball**: 100 ball
- **O'tish balli**: 70 ball
- **Vaqt**: 90 daqiqa
- **Resurslar**: Computer, SQLite database, SQL environment

---

## 🎯 Qism 1: Nazariy Savollar (25 ball)

### 1. SQL asoslari (5 ball)
**Savol**: Quyidagi SQL so'rovni tushuntiring:
```sql
SELECT c.name, COUNT(p.id) as product_count
FROM categories c
LEFT JOIN products p ON c.id = p.category_id
GROUP BY c.id, c.name
HAVING COUNT(p.id) > 5;
```

**Javob variantlari:**
- A) Barcha kategoriyalarni va ularning mahsulotlar sonini ko'rsatadi
- B) 5 tadan ko'p mahsuloti bo'lgan kategoriyalarni ko'rsatadi
- C) Mahsuloti bo'lmagan kategoriyalarni ham qo'shib ko'rsatadi
- D) B va C javoblar to'g'ri

### 2. Window Functions (5 ball)
**Savol**: `ROW_NUMBER()` va `RANK()` funksiyalari orasidagi farq nima?

### 3. JOIN turlari (5 ball)
**Savol**: Qaysi JOIN turi chapda bo'lgan barcha yozuvlarni va o'ngda mos keluvchilarini qaytaradi?
- A) INNER JOIN
- B) LEFT JOIN  
- C) RIGHT JOIN
- D) FULL OUTER JOIN

### 4. Agregatsiya (5 ball)
**Savol**: `GROUP BY` bo'limida qaysi ustunlar ko'rsatilishi kerak?

### 5. SQL Optimizatsiya (5 ball)
**Savol**: SQL so'rovlarni tezlashtirish uchun qanday usullar mavjud? Kamida 3 ta usulni ayting.

---

## 💻 Qism 2: Amaliy Vazifalar (75 ball)

**Ma'lumotlar bazasi**: `ecommerce_data.db`

### Vazifa 1: Ma'lumotlarni O'rganish (10 ball)

**1.1** (3 ball) Quyidagi so'rovni yozing:
"Har bir jadvalda nechta yozuv borligini aniqlang"

**1.2** (3 ball) Quyidagi so'rovni yozing:
"`products` jadvalidagi eng qimmat 5 ta mahsulotni ko'rsating"

**1.3** (4 ball) Quyidagi so'rovni yozing:
"NULL qiymatli email'ga ega mijozlar sonini aniqlang"

---

### Vazifa 2: Agregatsiya va Statistika (15 ball)

**2.1** (5 ball) Quyidagi hisobotni yarating:
```
Kategoriya | Mahsulotlar_soni | O'rtacha_narx | Jami_stock
```

**2.2** (5 ball) Oylik sotuvlar statistikasini chiqaring:
```
Oy | Buyurtmalar_soni | Jami_daromad | O'rtacha_buyurtma_qiymati
```

**2.3** (5 ball) Shaharlar bo'yicha mijozlar taqsimotini ko'rsating (TOP 10):
```
Shahar | Mijozlar_soni | Foiz
```

---

### Vazifa 3: JOIN va Murakkab So'rovlar (20 ball)

**3.1** (7 ball) Eng ko'p xarid qilgan 10 ta mijozni ko'rsating:
```sql
-- Quyidagilarni ko'rsating:
-- Mijoz ismi, Shahar, Buyurtmalar_soni, Jami_sarflagan_pul
```

**3.2** (6 ball) Har bir kategoriyada eng ko'p sotilgan mahsulotni toping:
```sql
-- Window function yoki subquery ishlatishingiz mumkin
```

**3.3** (7 ball) Bir oydan ortiq buyurtma bermagan mijozlarni aniqlang:
```sql
-- So'nggi buyurtma sanasi ham ko'rsatilsin
```

---

### Vazifa 4: Vaqt bilan Ishlash (15 ball)

**4.1** (5 ball) Hafta kunlari bo'yicha sotuvlar faolligini aniqlang:
```sql
-- Qaysi kunlarda ko'proq sotuvlar bo'lishi
-- Kun_nomi, Buyurtmalar_soni, Jami_daromad
```

**4.2** (5 ball) Oxirgi 30 kun ichidagi kunlik sotuvlar trendini ko'rsating:
```sql
-- Kun, Buyurtmalar_soni, Daromad
-- Faqat buyurtma bo'lgan kunlar
```

**4.3** (5 ball) Har oy nechta yangi mijoz qo'shilganini aniqlang:
```sql
-- Registration date asosida
```

---

### Vazifa 5: Ilg'or Tahlil (15 ball)

**5.1** (8 ball) Mijozlarni RFM (Recency, Frequency, Monetary) asosida segmentlarga ajrating:
```sql
-- Segments: VIP, Loyal, New, At_Risk, Lost
-- Har bir segment uchun criteria o'zingiz belgilang
```

**5.2** (7 ball) Running total (yugurib boruvchi jami) hisobini yarating:
```sql
-- Oylik daromadlarning yugurib boruvchi jamini hisoblang
-- Window function ishlatish kerak
```

---

## 🎯 Qism 3: Bonus Vazifa (15 ball)

### Vazifa 6: Biznes Tahlili
**6.1** (15 ball) Kompleks biznes hisobotini yarating:

Quyidagi ma'lumotlarni bir so'rovda chiqaring:
- Jami mijozlar soni
- Qayta xarid qiluvchi mijozlar foizi
- Eng yuqori daromadli kategoriya
- O'rtacha buyurtma qiymati
- So'nggi 30 kun ichidagi o'sish foizi (buyurtmalar soni bo'yicha)

---

## 📊 Baholash Mezonlari

### SQL So'rovlar (60 ball)
- **Syntax to'g'riligi**: 20 ball
- **Mantiqiy to'g'rilik**: 25 ball  
- **Optimizatsiya**: 10 ball
- **Formatlashtirish**: 5 ball

### Natijalar (15 ball)
- **Ma'lumotlar aniqligi**: 10 ball
- **Tushuntirish**: 5 ball

### Nazariy bilim (25 ball)
- **SQL tushunchalari**: 15 ball
- **Best practices**: 10 ball

---

## ⚠️ Muhim Qoidalar

1. **Plagiatsim**: Boshqa talabalardan nusxa ko'chirish ta'qiqlanadi
2. **Internet**: Dokumentatsiyaga murojaat qilish ruxsat etiladi
3. **Vaqt**: 90 daqiqa qattiq cheklangan
4. **Formatlash**: SQL so'rovlar aniq va o'qilishi oson bo'lishi kerak
5. **Test case**: Har bir so'rovni test qilib ko'ring

---

## 🏆 Baholash Shkalasi

- **90-100 ball**: A (Excellent) - Mukammal
- **80-89 ball**: B (Good) - Yaxshi  
- **70-79 ball**: C (Satisfactory) - Qoniqarli
- **60-69 ball**: D (Poor) - Yomon
- **0-59 ball**: F (Fail) - Muvaffaqiyatsiz

---

## 📝 Topshirish Formati

1. **SQL fayllar**: Har bir vazifa uchun alohida `.sql` fayl
2. **Natijalar**: Screenshot yoki tekst formatida
3. **Tushuntirishlar**: Qisqacha izoh yozing
4. **Fayl nomlari**: `task_1_1.sql`, `task_1_2.sql` formatida

**Topshirish muddati**: Test yakunlangandan keyin darhol

---

**Omad tilaymiz!** 🍀

Eslatma: Bu test sizning SQL va ma'lumotlar tahlili bo'yicha bilimlaringizni baholaydi. Diqqat bilan o'qing va puxta ishlang.