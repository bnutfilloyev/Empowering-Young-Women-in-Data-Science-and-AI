# Python Asoslari - Uy Vazifasi

## Umumiy ko'rsatmalar
- Barcha topshiriqlarni Python da yozing
- Kodingizni izohlar bilan to'ldiring
- Har bir topshiriq uchun alohida fayl yarating yoki bo'limlar ajrating
- Test qilib ko'ring va natijalarni tekshiring

---

## Topshiriq 1: Shaxsiy Ma'lumotlar Bazasi (10 ball)

**Maqsad**: O'zgaruvchilar, satrlar va print funksiyasi bilan ishlash.

**Vazifa**: 
Quyidagi ma'lumotlaringizni o'zgaruvchilarga saqlang va chiroyli formatda ekranga chiqaring:
- Ism va familiya
- Yoshi  
- Tug'ilgan joyi
- Sevimli rang
- Hobby

**Misol chiqish**:
```
=== SHAXSIY MA'LUMOTLAR ===
Ism-familiya: Ahmad Karimov
Yoshi: 20 yosh
Tug'ilgan joyi: Toshkent
Sevimli rang: Ko'k
Hobby: Kitob o'qish
```

---

## Topshiriq 2: Satr Tahlili (15 ball)

**Maqsad**: Satr metodlari va formatlash bilan ishlash.

**Vazifa**: 
Foydalanuvchidan bir jumla kiritishni so'rang va quyidagilarni hisoblang:
- Jami belgilar soni
- So'zlar soni
- Unlilar soni (a, e, i, o, u)
- Katta harflar soni
- Kichik harflar soni

**Qo'shimcha**: Jumlani har xil ko'rinishlarda chiqaring:
- Barchasi katta harf
- Barchasi kichik harf
- Har so'z boshi katta harf

---

## Topshiriq 3: Mevalar Do'koni (20 ball)

**Maqsad**: Ro'yxatlar, metodlar va operatsiyalar bilan ishlash.

**Vazifa**:
Mevalar do'koni uchun dastur yozing:

1. Quyidagi mevalar ro'yxatini yarating:
   ```python
   mevalar = ["olma", "banan", "uzum", "nok", "shaftoli"]
   narxlar = [3000, 2000, 8000, 4000, 12000]  # so'm/kg
   ```

2. Dastur quyidagilarni qilishi kerak:
   - Barcha mevalar va narxlarini ko'rsatish
   - Eng qimmat va eng arzon mevani topish
   - O'rtacha narxni hisoblash
   - Yangi meva qo'shish imkoniyati
   - Ma'lum mevani o'chirish imkoniyati

---

## Topshiriq 4: Baho Hisoblagichi (25 ball)

**Maqsad**: Shartli operatorlar va mantiqiy amallar bilan ishlash.

**Vazifa**:
Talaba bahosini hisoblaydigan dastur yarating:

1. Foydalanuvchidan 5 ta fan bo'yicha baholarni kiriting
2. O'rtacha bahoni hisoblang
3. Harfiy bahoni aniqlang:
   - 90-100: A (A'lo)
   - 80-89: B (Yaxshi) 
   - 70-79: C (Qoniqarli)
   - 60-69: D (Qoniqarsiz)
   - 0-59: F (Yomon)

4. Stipendiya olish huquqini tekshiring:
   - A'lo (90+) - To'liq stipendiya
   - Yaxshi (80+) - Yarim stipendiya  
   - Boshqa - Stipendiya yo'q

5. Qo'shimcha shartlar:
   - Agar birorta fan bo'yicha 60 dan past bo'lsa - "Qayta topshirish kerak"
   - Agar barchasi 95+ bo'lsa - "A'lo talaba" maqomi

---

## Topshiriq 5: Raqamlar O'yini (30 ball)

**Maqsad**: Tsikllar, tasodifiy sonlar va foydalanuvchi bilan o'zaro aloqa.

**Vazifa**:
"Raqamni top" o'yini yarating:

1. Kompyuter 1 dan 100 gacha tasodifiy son tanlaydi
2. Foydalanuvchi raqamni topishga urinadi
3. Har bir urinishdan keyin yo'llanma berish:
   - "Juda katta" - kiritilgan son kattaroq
   - "Juda kichik" - kiritilgan son kichikroq
   - "To'g'ri!" - to'g'ri javob

4. Qo'shimcha funksiyalar:
   - Urinishlar sonini sanash
   - Eng kam urinishda topish rekordini saqlash
   - O'yinni qayta boshlash imkoniyati
   - Qiyinchilik darajasi (oson: 1-50, qiyin: 1-1000)

**Misol o'yin jarayoni**:
```
Raqamni topish o'yini!
Men 1 dan 100 gacha son o'yladim.

1-urinish: 50
Juda katta!

2-urinish: 25  
Juda kichik!

3-urinish: 37
To'g'ri! 3 urinishda topdingiz!
```

---

## Bonus Topshiriq: Parol Yaratuvchi (10 qo'shimcha ball)

**Maqsad**: Barcha o'rgangan tushunchalarni birlashtirib ishlatish.

**Vazifa**:
Xavfsiz parol yaratuvchi dastur yozing:

1. Foydalanuvchi parol parametrlarini tanlaydi:
   - Uzunlik (6-50 orasida)
   - Katta harflar kerakmi?
   - Raqamlar kerakmi?  
   - Maxsus belgilar kerakmi? (!@#$%^&*)

2. Berilgan parametrlar asosida tasodifiy parol yaratish
3. Parol kuchliligini baholash:
   - Zaif (faqat harflar)
   - O'rtacha (harflar + raqamlar)
   - Kuchli (harflar + raqamlar + maxsus belgilar)

4. Bir nechta parol variantini taklif qilish

---

## Topshirish talablari

1. **Deadline**: [Sana ko'rsatilsin]
2. **Format**: Python fayl (.py) yoki Jupyter Notebook (.ipynb)
3. **Fayl nomi**: `ism_familiya_uy_vazifa_4.py`
4. **Kod sifati**: 
   - O'qilishi oson kod
   - Tushunarli o'zgaruvchi nomlari
   - Izohlar va docstring'lar
   - Test qilingan natijalar

## Baholash mezonlari

| Topshiriq | Max ball | Mezon |
|-----------|----------|--------|
| Topshiriq 1 | 10 | To'g'ri kod + formatlash |
| Topshiriq 2 | 15 | String metodlari + hisoblashlar |
| Topshiriq 3 | 20 | List operatsiyalar + funksionallik |
| Topshiriq 4 | 25 | Shartli logika + murakkab hisoblashlar |
| Topshiriq 5 | 30 | Loop + random + user interaction |
| **Jami** | **100** | |
| Bonus | +10 | Qo'shimcha funksiyalar |

**Omad tilaymiz! 🚀**