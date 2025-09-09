# 🗄️ 3-Modul, 1-Dars: SQLga kirish va SELECT asoslari

## 📚 Dars maqsadi
SQL (Structured Query Language) asoslarini o'rganish va SELECT buyrug'i yordamida ma'lumotlar bazasidan ma'lumotlarni olish ko'nikmalarini rivojlantirish.

## 🎯 O'rganish natijalar

Ushbu darsdan so'ng talabalar quyidagilarni bilishi va qila olishi kerak:

### 📖 Nazariy bilimlar:
- ✅ SQL nima va nima uchun kerakligini tushunish
- ✅ Relatsion ma'lumotlar bazasi tushunchasi
- ✅ SQL sintaksisi asoslari
- ✅ SELECT operatori strukturasi
- ✅ WHERE, ORDER BY, LIMIT buyruqlarining maqsadi

### 💻 Amaliy ko'nikmalar:
- ✅ Oddiy SELECT so'rovlarini yozish
- ✅ Ma'lumotlarni filtrlash (WHERE)
- ✅ Natijalarni tartiblash (ORDER BY)
- ✅ Chiqarish hajmini cheklash (LIMIT)
- ✅ Turli ma'lumot turlari bilan ishlash
- ✅ Murakkab shart operatorlaridan foydalanish

## 📋 Dars tarkibi

### 1. 📖 Nazariy qism (45 daqiqa)
- **1.1** SQL ga kirish va tarixi
- **1.2** Relatsion ma'lumotlar bazasi modeli
- **1.3** SQL sintaksisi va konventsiyalari
- **1.4** SELECT operatori asoslari
- **1.5** WHERE buyrug'i va filtrlash
- **1.6** ORDER BY bilan tartiblash
- **1.7** LIMIT va ma'lumot cheklash

### 2. 🔬 Amaliy mashg'ulot (60 daqiqa)
- **2.1** SQLite bilan ishlash
- **2.2** Oddiy SELECT so'rovlari
- **2.3** Filtrlash amaliyoti
- **2.4** Tartiblash mashqlari
- **2.5** Murakkab so'rovlar yaratish

### 3. 👥 Guruh ishi (45 daqiqa)
- **3.1** 1-guruh: Xodimlar ma'lumotlari tahlili
- **3.2** 2-guruh: Mahsulotlar katalogi boshqaruvi
- **3.3** Natijalar taqdimoti

### 4. 📝 Mustaqil ish (30 daqiqa)
- **4.1** Amaliy vazifalar yechish
- **4.2** SQL so'rovlari optimizatsiyasi
- **4.3** Qo'shimcha topshiriqlar

## 💾 Amaliy ma'lumotlar to'plami

### 📊 **employees.db** - Xodimlar ma'lumotlari
- `employees` jadvali (100 yozuv)
- Ustunlar: id, name, position, department, salary, hire_date, age

### 🛍️ **products.db** - Mahsulotlar katalogi  
- `products` jadvali (150 yozuv)
- Ustunlar: id, name, category, price, stock, supplier, rating

### 🎓 **students.db** - Talabalar reytingi
- `students` jadvali (80 yozuv)  
- Ustunlar: id, name, faculty, course, gpa, city, age

## 🛠️ Texnologiyalar va vositalar

### Asosiy:
- **SQLite** - Engil ma'lumotlar bazasi
- **Python sqlite3** - Ma'lumotlar bazasi bilan ishlash
- **Jupyter Notebook** - Interaktiv muhit
- **pandas** - Ma'lumotlarni ko'rish uchun

### Qo'shimcha:
- **DB Browser for SQLite** - Vizual interfeys
- **SQLite Online** - Brauzer versiyasi

## 📚 Dars materiallari

| 📁 Fayl | 📖 Tavsif | ⏱️ Vaqt |
|---------|-----------|--------|
| `lecture.ipynb` | Asosiy nazariy material | 45 min |
| `practical.ipynb` | Amaliy mashg'ulotlar | 60 min |
| `group1_practice.ipynb` | 1-guruh: Xodimlar tahlili | 45 min |
| `group2_practice.ipynb` | 2-guruh: Mahsulotlar katalogi | 45 min |
| `homework.ipynb` | Uy vazifasi | - |
| `datasets/` | Ma'lumotlar to'plami | - |

## 🎯 Baholash mezonlari (100 ball)

### 📝 Nazariy bilim (25 ball)
- SQL asoslari tushunchasi: **10 ball**
- SELECT sintaksisi: **8 ball**  
- Operatorlar bilimi: **7 ball**

### 💻 Amaliy ko'nikmalar (45 ball)
- Oddiy SELECT so'rovlari: **15 ball**
- WHERE filtrlash: **15 ball**
- ORDER BY va LIMIT: **15 ball**

### 👥 Guruh ishi (20 ball)
- Muammoni tahlil qilish: **8 ball**
- SQL so'rovlarini yozish: **8 ball**
- Taqdimot: **4 ball**

### 📋 Mustaqil ish (10 ball)
- Vazifalarni to'g'ri bajarish: **6 ball**
- Kodni optimallash: **4 ball**

## 📖 Qo'shimcha manbalar

### 📚 Kitoblar:
- "Learning SQL" - Alan Beaulieu
- "SQL in 10 Minutes" - Ben Forta
- "The Practical SQL Handbook" - Judith Bowman

### 🌐 Online manbalar:
- [W3Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [SQLBolt](https://sqlbolt.com/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

### 🎥 Video darslar:
- [SQL Basics - Khan Academy](https://www.khanacademy.org/computing/computer-programming/sql)
- [Codecademy SQL Course](https://www.codecademy.com/learn/learn-sql)

## 🚀 Keyingi darsga tayyorgarlik

### O'rganish kerak:
- SQL JOIN operatori
- Ma'lumotlarni guruhlash (GROUP BY)
- Agregat funksiyalar (COUNT, SUM, AVG)
- Ichki so'rovlar (Subqueries)

### Amaliy vazifalar:
- Murakkab so'rovlar yozish
- Ko'p jadvalli so'rovlar
- Ma'lumotlarni export/import qilish

---

## 👨‍🏫 O'qituvchi uchun eslatmalar

### ⏰ Vaqt boshqaruvi:
- Nazariy qism: maksimal 45 daqiqa
- Har bir misol uchun: 5-7 daqiqa
- Savol-javob: 10 daqiqa
- Guruh ishi: aniq vaqt chegarasi

### 🎯 Muhim nuqtalar:
- SQL sintaksisi asoslariga e'tibor qarating
- Amaliy misollar ko'proq bo'lsin
- Talabalar amaliyotda ishtirok etishini ta'minlang
- Guruh ishida hamkorlikni rag'batlantiring

### 💡 Maslahatlar:
- Oddiy misollardan boshlang
- Har bir operatorni alohida tushuntiring  
- Xatolar bilan ishlashni o'rgating
- Real ma'lumotlar bilan ishlang

---

**📅 Yaratilgan:** 2025-yil 9-sentyabr  
**👨‍💻 Muallif:** AI Data Science o'qituvchisi  
**🔄 Versiya:** 1.0
