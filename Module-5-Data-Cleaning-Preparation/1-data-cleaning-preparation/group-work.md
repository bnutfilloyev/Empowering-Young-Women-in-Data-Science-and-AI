# Group Work: Data Tozalash Challenge

## 🎯 Maqsad
Guruh bo'lib real ma'lumotlar bilan ishlash va eng yaxshi data cleaning strategiyasini topish.

## 👥 Guruh Tarkibi
3-4 kishi

## ⏱️ Vaqt
60 daqiqa

## 📊 Vazifa
Sizga yangi startup kompaniyasi ma'lumotlari berilgan. Ma'lumotlar juda tartibsiz va noto'liq. Sizning vazifangiz:

1. Ma'lumotlarni tahlil qilish
2. Muammolarni aniqlash
3. Tozalash strategiyasini ishlab chiqish
4. Ma'lumotlarni tozalash
5. Natijalarni taqdim etish

## 🏆 Baholash Mezoni (100 ball)

### 1. Tahlil va Strategiya (30 ball)
- Ma'lumotlar tahlili (10 ball)
- Muammolarni aniqlash (10 ball)
- Strategiya ishlab chiqish (10 ball)

### 2. Amaliy Bajarish (40 ball)
- Missing values (15 ball)
- Duplicates (10 ball)
- Encoding (15 ball)

### 3. Natijalar (20 ball)
- Vizualizatsiya (10 ball)
- Insight'lar (10 ball)

### 4. Taqdimot (10 ball)
- Aniq va tushunarli (5 ball)
- Teamwork (5 ball)

## 📚 Ma'lumotlar

Startup kompaniyasi o'z jamoasi haqida ma'lumot yig'lagan. Lekin ma'lumotlar juda tartibsiz:

```python
import pandas as pd
import numpy as np

np.random.seed(100)

data = {
    'ID': range(1, 61),
    'Ism': ['Ali', 'Vali', 'Sardor', 'Malika', 'Nigora', 'Aziz'] * 10,
    'Yosh': np.random.choice([np.nan, 22, 25, 28, 30, 32, 35, 38, 40], 60),
    'Jins': np.random.choice(['Erkak', 'Ayol', 'E', 'A', np.nan], 60),
    'Pozitsiya': np.random.choice(['Developer', 'Designer', 'Manager', 'dev', 'developer', np.nan], 60),
    'Tajriba_Yil': np.random.choice([np.nan, 0, 1, 2, 3, 5, 7, 10, 15, -1], 60),
    'Maosh_USD': np.random.choice([np.nan, 500, 800, 1000, 1500, 2000, 3000, 5000, 10000], 60),
    'Til': np.random.choice(['Python', 'JavaScript', 'Java', 'python', 'js', np.nan], 60),
    'Remote': np.random.choice(['Ha', 'Yo\'q', 'Yes', 'No', '1', '0', np.nan], 60),
    'Shahar': np.random.choice(['Toshkent', 'Samarqand', 'Buxoro', 'toshkent', np.nan], 60),
    'Email': ['user' + str(i) + '@mail.com' if i % 5 != 0 else np.nan for i in range(1, 61)]
}

df = pd.DataFrame(data)

# Ba'zi takroriy qatorlar qo'shamiz
duplicate_rows = df.iloc[[0, 5, 10, 15, 20, 25]].copy()
df = pd.concat([df, duplicate_rows], ignore_index=True)
```

## 🔍 Muammolar (Aniqlashingiz Kerak!)

Ma'lumotlarda quyidagi muammolar bor:
1. Missing values
2. Takroriy qatorlar
3. Noto'g'ri data types
4. Inconsistent naming (masalan: "Developer" va "dev")
5. Noto'g'ri qiymatlar (masalan: Tajriba_Yil = -1)
6. Case sensitivity (masalan: "Toshkent" va "toshkent")

## 📋 Guruh Vazifalari

### Bosqich 1: Planning (10 daqiqa)
1. Ma'lumotlarni o'rganing
2. Muammolarni yozib oling
3. Har bir muammo uchun strategiya tuzing
4. Vazifalarni taqsimlang

### Bosqich 2: Implementation (35 daqiqa)
1. Ma'lumotlarni tozalang
2. Encoding qiling
3. Vizualizatsiya yarating
4. Insight'lar yozing

### Bosqich 3: Presentation (10 daqiqa)
1. Qanday muammolar topildi?
2. Qanday strategiya ishlatildi?
3. Natijalar qanday?
4. Qanday insight'lar topildi?

### Bosqich 4: Q&A (5 daqiqa)
Savollar va javoblar

## 🎯 Topshiriqlar

### Guruh 1: Missing Values Specialists
**Fokus:** Missing values ni eng yaxshi usulda to'ldirish

Vazifalar:
1. Har bir ustundagi missing values ni tahlil qiling
2. Har biri uchun to'ldirish strategiyasini asoslang
3. Turli usullarni taqqoslang (mean vs median vs mode)
4. Qaysi usul eng yaxshi ekanligini ko'rsating

### Guruh 2: Data Consistency Experts
**Fokus:** Inconsistent data ni tozalash

Vazifalar:
1. Barcha inconsistency'larni toping
2. Standardization strategiyasini ishlab chiqing
3. Case sensitivity muammolarini hal qiling
4. Naming conventions yarating

### Guruh 3: Encoding Masters
**Fokus:** Eng yaxshi encoding strategiyasini topish

Vazifalar:
1. Har bir kategorik ustun uchun encoding usulini tanlang
2. Turli usullarni taqqoslang (Label vs One-Hot)
3. Encoding'dan keyin dimensionality ni tahlil qiling
4. Qaysi usul model uchun yaxshiroq ekanligini ko'rsating

### Guruh 4: Quality Assurance Team
**Fokus:** Data quality va validation

Vazifalar:
1. Data quality metrics yarating
2. Outlier'larni aniqlang
3. Validation rules yarating
4. Final quality report tayyorlang

## 📊 Taqdimot Template

```markdown
# Guruh [Raqam]: [Nom]

## 1. Topilgan Muammolar
- Muammo 1: ...
- Muammo 2: ...
- Muammo 3: ...

## 2. Strategiya
- Yondashuv: ...
- Sabab: ...
- Kutilgan natija: ...

## 3. Natijalar
- Boshlang'ich vs Yakuniy
- Vizualizatsiya
- Statistika

## 4. Insight'lar
- Insight 1: ...
- Insight 2: ...
- Insight 3: ...

## 5. Tavsiyalar
- Kompaniyaga tavsiya 1: ...
- Tavsiya 2: ...
```

## 💡 Tips

1. **Planning:** Yaxshi reja - ishning yarmi
2. **Communication:** Guruhda doimiy muloqot
3. **Documentation:** Har bir qaror uchun izoh yozing
4. **Visualization:** Grafik 1000 so'zdan ko'ra
5. **Time Management:** Vaqtni to'g'ri taqsimlang

## 🏅 Bonus Topshiriqlar (+10 ball har biri)

1. **Automation:** Butun jarayonni function qilib yozing
2. **Feature Engineering:** Yangi feature'lar yarating
3. **Advanced Analysis:** Machine learning uchun feature importance
4. **Documentation:** Professional README yozing

## 📈 Success Metrics

Sizning ishingiz quyidagi mezonlar bo'yicha baholanadi:

1. **Correctness:** To'g'ri yechim
2. **Efficiency:** Optimal kod
3. **Clarity:** Tushunarli tushuntirish
4. **Creativity:** Yangicha yondashuv
5. **Teamwork:** Jamoaviy ish

## ⚠️ Common Mistakes

1. ❌ Planning qilmasdan boshlash
2. ❌ Vizualizatsiya qilmaslik
3. ❌ Strategiya asoslamaslik
4. ❌ Teamwork'ga e'tibor bermaslik
5. ❌ Time management yo'qligi

## 🎓 O'rganish Natijalari

Ushbu group work'dan keyin siz:
- ✅ Guruhda ishlashni o'rganasiz
- ✅ Real muammolarni hal qilasiz
- ✅ Strategiya ishlab chiqishni bilasiz
- ✅ O'z fikringizni himoya qilishni o'rganasiz
- ✅ Boshqalardan o'rganasiz

## 🚀 Boshlash

1. Guruh bo'ling (3-4 kishi)
2. Ma'lumotlarni yuklang
3. Planning qiling
4. Ishlashni boshlang!

**Omad tilaymiz! 🎉**

---

## 📝 Hisobot Template (Topshirish uchun)

```python
# GURUH HISOBOTI

## Guruh A'zolari
- Ism 1: Vazifa
- Ism 2: Vazifa
- Ism 3: Vazifa

## Tahlil
# Sizning tahlil kodingiz

## Strategiya
"""
Bizning strategiyamiz:
1. ...
2. ...
3. ...
"""

## Implementation
# Sizning data cleaning kodingiz

## Natijalar
# Vizualizatsiya va statistika

## Insight'lar
"""
1. ...
2. ...
3. ...
"""

## Tavsiyalar
"""
1. ...
2. ...
"""
```
