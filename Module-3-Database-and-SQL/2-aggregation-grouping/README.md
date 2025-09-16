# 📊 Module 3 - Lesson 2: Agregatsiya va Guruhlash (PostgreSQL)

## 🎯 Dars Maqsadi
PostgreSQL ma'lumotlar bazasida agregatsiya funksiyalari va guruhlash operatorlari yordamida ma'lumotlarni tahlil qilish va xulosalar chiqarishni o'rganish.

---

## 📚 O'quv Materiallar

### 🗂️ Fayllar Tuzilishi
```
2-aggregation-grouping/
├── README.md                    # Dars rejasi va ko'rsatmalar
├── postgresql_setup.md          # PostgreSQL o'rnatish va sozlash
├── lecture.ipynb               # Nazariy dars materiallari
├── practical.ipynb             # Amaliy mashg'ulot
├── group1_practice.ipynb       # 1-guruh amaliyoti
├── group2_practice.ipynb       # 2-guruh amaliyoti
├── homework.ipynb              # Uy vazifasi
└── datasets/
    ├── create_postgresql_db.py # PostgreSQL bazalarini yaratish
    ├── connect_postgresql.py   # PostgreSQL ulanish namunalari
    └── sample_data.sql         # Namuna ma'lumotlar
```

---

## 🎓 O'quv Natijalari

### 📋 Bilimlar:
- [x] **PostgreSQL** ma'lumotlar bazasi bilan ishlash
- [x] **Agregatsiya funksiyalari**: COUNT, SUM, AVG, MIN, MAX
- [x] **GROUP BY** operatori va guruhlash tamoyillari
- [x] **HAVING** operatori va guruh filtrlash
- [x] **Murakkab agregatsiya** so'rovlari yaratish
- [x] **PostgreSQL** o'ziga xos funksiyalari

### 🛠️ Ko'nikmalar:
- [x] PostgreSQL serveriga ulanish va sozlash
- [x] Ma'lumotlarni guruh bo'yicha tahlil qilish
- [x] Statistik ko'rsatkichlarni hisoblash
- [x] Shartli guruhlash va filtrlash
- [x] Murakkab hisobotlar yaratish
- [x] PostgreSQL CLI va GUI vositalaridan foydalanish

---

## ⏰ Dars Rejasi (120 daqiqa)

### 📖 1-qism: PostgreSQL Kirish (30 daqiqa)
- **PostgreSQL** haqida umumiy ma'lumot
- O'rnatish va sozlash jarayoni
- **psql** buyruq satri interfeysi
- **pgAdmin** grafik interfeysi
- Ma'lumotlar bazasiga ulanish

### 📊 2-qism: Agregatsiya Funksiyalari (35 daqiqa)
- **COUNT()** - yozuvlar sonini hisoblash
- **SUM()** - yig'indini hisoblash
- **AVG()** - o'rtacha qiymatni hisoblash
- **MIN()/MAX()** - eng kichik/katta qiymatlar
- **DISTINCT** bilan ishlatish

### 🔗 3-qism: GROUP BY Operatori (30 daqiqa)
- Guruhlash tamoyillari va sintaksis
- Bir va ko'p ustun bo'yicha guruhlash
- Agregatsiya bilan birga ishlatish
- **ORDER BY** bilan kombinatsiya

### 🎯 4-qism: HAVING Operatori (25 daqiqa)
- **WHERE** va **HAVING** farqi
- Guruh natijalarini filtrlash
- Murakkab shartlar yaratish
- Amaliy misollar va vazifalar

---

## 📊 Baholash Tizimi (100 ball)

### 🎯 Ball Taqsimoti:
| Faoliyat | Ball | Tavsif |
|----------|------|---------|
| **Darsda ishtirok** | 15 | Faol qatnashish va savollar |
| **Amaliy mashg'ulot** | 25 | Vazifalarni to'g'ri bajarish |
| **Guruh ishi** | 20 | Hamkorlikda ishlash ko'nikmalari |
| **Uy vazifasi** | 40 | Mustaqil bajarish va tahlil |
| **JAMI** | **100** | **Umumiy baho** |

### 📏 Baho Mezonlari:
- **90-100 ball**: A'lo (5) - PostgreSQL va agregatsiyani mukammal biladi
- **80-89 ball**: Yaxshi (4) - Asosiy tushunchalarni yaxshi tushunadi
- **70-79 ball**: Qoniqarli (3) - O'rtacha daraja, qo'shimcha mashq kerak
- **60-69 ball**: Qoniqarsiz (2) - Asosiy bilimlar yetishmaydi
- **0-59 ball**: Yomon (1) - Qayta o'rganish talab etiladi

---

## 🗄️ Ma'lumotlar Bazalari

### 📈 Ishlatilayotgan Jadvallar:
1. **sales** - Savdo ma'lumotlari (10,000+ yozuv)
2. **employees** - Xodimlar va bo'limlar (500+ yozuv)
3. **products** - Mahsulotlar va kategoriyalar (1,000+ yozuv)
4. **customers** - Mijozlar va demografik ma'lumotlar (2,000+ yozuv)
5. **orders** - Buyurtmalar va to'lovlar (5,000+ yozuv)

### 🔧 Texnik Talablar:
- **PostgreSQL 12+** (tavsiya etiladi 14+)
- **Python 3.8+** psycopg2 kutubxonasi bilan
- **pgAdmin 4** yoki boshqa GUI vosita
- **Jupyter Notebook** amaliy ishlar uchun

---

## 📖 Dars Bosqichlari

### 🚀 Boshlash:
1. **PostgreSQL Setup** - postgresql_setup.md faylini o'qing
2. **Database Creation** - create_postgresql_db.py ishga tushiring
3. **Connection Test** - connect_postgresql.py orqali ulanishni tekshiring

### 📚 Nazariy Qism:
4. **lecture.ipynb** - Nazariy materiallarni o'rganish
5. **Interaktiv misollar** - Har bir mavzu bo'yicha amaliyot

### 🔧 Amaliy Qism:
6. **practical.ipynb** - Mustaqil vazifalar
7. **Guruh ishi** - group1_practice.ipynb yoki group2_practice.ipynb
8. **Yakuniy baholash** - homework.ipynb

---

## 💡 PostgreSQL Afzalliklari

### 🌟 Nima uchun PostgreSQL?
- **🔓 Open Source** - Bepul va ochiq kodli
- **⚡ Yuqori unumdorlik** - Katta ma'lumotlar bilan ishlash
- **🛡️ Xavfsizlik** - Kuchli autentifikatsiya va shifrlash
- **🔧 Kengaytirilganlik** - Ko'plab kengaytmalar va funksiyalar
- **📊 Analitik quvvat** - Window functions, CTE, JSON qo'llab-quvvatlash
- **🌐 Standartlar** - SQL standartlariga to'liq muvofiqlik

### 🎯 Real Loyihalarda Qo'llanilishi:
- **Veb ilovalar** - Django, Rails, Node.js bilan
- **Analitika** - Business Intelligence va reporting
- **GIS** - PostGIS kengaytmasi bilan geografik ma'lumotlar
- **JSON ma'lumotlar** - NoSQL xususiyatlari
- **Time series** - Vaqt bo'yicha ma'lumotlar tahlili

---

## 📚 Qo'shimcha Resurslar

### 🔗 Foydali Havolalar:
- [PostgreSQL Rasmiy Sayt](https://postgresql.org)
- [pgAdmin Download](https://pgadmin.org)
- [PostgreSQL Tutorial](https://postgresqltutorial.com)
- [Psycopg2 Documentation](https://psycopg.org)

### 📖 Tavsiya Etiladigan Kitoblar:
- "PostgreSQL: Up and Running" - Regina Obe
- "The Art of PostgreSQL" - Dimitri Fontaine
- "PostgreSQL 13 Administration Cookbook" - Simon Riggs

### 🎥 Video Kurslar:
- PostgreSQL for Beginners (YouTube)
- Advanced PostgreSQL Features (Coursera)
- Data Analysis with PostgreSQL (Udemy)

---

## ❓ Tez-tez So'raladigan Savollar

### **S: PostgreSQL va MySQL o'rtasidagi farq nima?**
**J:** PostgreSQL ko'proq analitik funksiyalarga ega, JSON qo'llab-quvvatlaydi va SQL standartlariga ko'proq mos keladi. MySQL tezroq lekin funksionalligi cheklangan.

### **S: psql commandalari haqida qayerdan o'rganish mumkin?**
**J:** `\?` buyrug'i barcha commandlarni ko'rsatadi. `\h SELECT` kabi buyruqlar SQL syntax haqida ma'lumot beradi.

### **S: Python bilan PostgreSQL ulanishida xato chiqsa nima qilish kerak?**
**J:** Avval psycopg2 o'rnatilganini, database yaratilganini va ulanish parametrlarini tekshiring.

### **S: GROUP BY ishlatmasdan agregatsiya mumkinmi?**
**J:** Ha, lekin faqat barcha jadval uchun umumiy natija beradi. Guruh bo'yicha tahlil uchun GROUP BY shart.

---

## 📅 Muhim Sanalar

- **📚 Nazariy materiallar**: Darsdan oldin o'rganish
- **💻 Amaliy ish**: Dars davomida bajarish  
- **👥 Guruh loyihasi**: Dars oxirida bajarish
- **📝 Uy vazifasi**: Keyingi darsdan oldin topshirish

---

## 👨‍🏫 O'qituvchi Ma'lumotlari

**📧 Aloqa:** AI Data Science Mentor  
**⏰ Dars vaqti:** Jadval bo'yicha  
**🆘 Yordam:** Dars vaqtida yoki alohida konsultatsiya  

---

*🎯 **Muvaffaqiyat kaliti:** Doimiy amaliyot va PostgreSQL bilan tajriba to'plash!*

📊 **Eslatma:** Ushbu dars AI va Data Science yo'nalishida PostgreSQL dan foydalanishga qaratilgan. Real loyihalar uchun zarur bo'lgan barcha asosiy bilimlar beriladi.
