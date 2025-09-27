# Funksiyalar va Modullar - Uy Vazifasi

## Umumiy ko'rsatmalar
- Barcha topshiriqlarni Python da yozing  
- Funksiyalar uchun docstring yozing
- Kodni testlang va natijalarni tekshiring
- Modullar yarating va import qiling

---

## Topshiriq 1: Matematik Kalkulyator (20 ball)

**Maqsad**: Funksiyalar yaratish va parametrlar bilan ishlash.

**Vazifa**:
Matematik amallar uchun funksiyalar yarating:

```python
def qoshish(a, b):
    """Ikki sonni qo'shish"""
    # Kodi yozing

def ayirish(a, b):
    """Ikki sonni ayirish"""
    # Kodi yozing

def kopaytirish(a, b):
    """Ikki sonni ko'paytirish"""
    # Kodi yozing

def bolish(a, b):
    """Ikki sonni bo'lish (nolga bo'lishni tekshirish)"""
    # Kodi yozing

def daraja(a, b):
    """a ning b-darajasini hisoblash"""
    # Kodi yozing

def kalkulyator():
    """Asosiy kalkulyator funksiyasi"""
    # Foydalanuvchi bilan o'zaro aloqa
    # Amallarni tanlab, natijani ko'rsatish
```

**Qo'shimcha talablar**:
- Noto'g'ri kiritilgan ma'lumotlarni boshqarish
- Kalkulyatorni davom ettirish yoki chiqish imkoniyati
- Tarixni saqlash (oxirgi 5 ta amal)

---

## Topshiriq 2: Matn Tahlilchisi (25 ball)

**Maqsad**: String bilan ishlaydigan funksiyalar va *args/*kwargs.

**Vazifa**:
Matn tahlili uchun funksiyalar yozing:

```python
def sozlar_soni(matn):
    """Matndagi so'zlar sonini hisoblash"""
    pass

def unlilar_soni(matn):
    """Matndagi unlilar sonini hisoblash"""
    pass

def belgilar_statistikasi(matn):
    """Har xil belgilar statistikasi"""
    # Dict qaytarsin: {'harflar': 10, 'raqamlar': 3, ...}
    pass

def matn_tozalash(matn, **parametrlar):
    """Matnni tozalash va formatlash"""
    # katta_harf=True, bo'sh_joylar_olib_tashla=False, va h.k.
    pass

def matnlarni_solishitirish(*matnlar):
    """Bir nechta matnni solishtirish"""
    # Uzunlik, so'zlar soni va boshqa statistikalarni solishtirish
    pass
```

**Test uchun**:
```python
matn1 = "Python dasturlash tili juda qiziq!"
matn2 = "Men Python o'rganmoqdaman."

# Funksiyalaringizni test qiling
```

---

## Topshiriq 3: Talabalar Boshqaruv Tizimi (30 ball)

**Maqsad**: Murakkab funksiyalar va ma'lumotlar tuzilmasi.

**Vazifa**:
Talabalar va ularning baholarini boshqarish tizimi yarating:

```python
# Global o'zgaruvchilar
talabalar = {}  # {ism: {'fanlar': {'matematika': [90, 85]}, 'orta_ball': 87.5}}

def talaba_qoshish(ism, **fanlar):
    """Yangi talaba qo'shish"""
    pass

def baho_qoshish(ism, fan, baho):
    """Talabaga yangi baho qo'shish"""
    pass

def orta_ball_hisoblash(ism, fan=None):
    """Talabaning o'rtacha ballini hisoblash"""
    # fan=None bo'lsa, barcha fanlar bo'yicha
    pass

def eng_yaxshi_talaba():
    """Eng yuqori o'rtacha ballga ega talabani topish"""
    pass

def fanlar_statistikasi():
    """Har bir fan bo'yicha statistika"""
    # {'matematika': {'orta': 85.5, 'eng_yuqori': 95, 'eng_past': 70}}
    pass

def hisobot_yaratish():
    """To'liq hisobot yaratish va saqlash"""
    pass
```

**Test ma'lumotlari**:
```python
# Testlar
talaba_qoshish("Ali", matematika=[90, 85], fizika=[88, 92])
talaba_qoshish("Zara", matematika=[95, 90], kimyo=[85, 88])
baho_qoshish("Ali", "matematika", 93)
```

---

## Topshiriq 4: Maxsus Modullar Yaratish (25 ball)

**Maqsad**: O'z modullaringizni yaratish va import qilish.

**Vazifa 4.1**: `matematik_amallar.py` moduli yarating:
```python
# matematik_amallar.py

import math
import random

PI = math.pi
E = math.e

def faktorial_hisoblash(n):
    """n! ni hisoblash"""
    pass

def fibonacci_ketma_ketlik(n):
    """Fibonachchi ketma-ketligining n ta elementini qaytarish"""
    pass

def tub_son_tekshirish(n):
    """Sonning tub son ekanligini tekshirish"""
    pass

def tasodifiy_sonlar(count, min_val=1, max_val=100):
    """Tasodifiy sonlar ro'yxatini yaratish"""
    pass

def statistika_hisoblash(sonlar):
    """Sonlar ro'yxati uchun statistika"""
    # {'orta': 50, 'median': 55, 'max': 100, 'min': 10}
    pass
```

**Vazifa 4.2**: `fayl_ishlari.py` moduli yarating:
```python
# fayl_ishlari.py

def matn_saqlash(fayl_nomi, matn):
    """Matnni faylga saqlash"""
    pass

def matn_oqish(fayl_nomi):
    """Fayldan matn o'qish"""
    pass

def csv_yaratish(fayl_nomi, ma_lumotlar):
    """CSV fayl yaratish"""
    pass

def json_saqlash(fayl_nomi, ma_lumot):
    """Ma'lumotni JSON formatda saqlash"""
    pass
```

**Vazifa 4.3**: `asosiy.py` faylida modullarni ishlatish:
```python
# asosiy.py

# Barcha yaratgan modullaringizni import qiling
# Modullar funksiyalarini test qiling
# Natijalarni konsolda va faylda ko'rsating
```

---

## Bonus Topshiriq: Mini Loyiha - "Kitoblar Kutubxonasi" (15 qo'shimcha ball)

**Maqsad**: Barcha o'rgangan bilimlarni birlashtirib loyiha yaratish.

**Vazifa**:
Kutubxona boshqaruv tizimi yarating:

**Fayl tuzilmasi**:
```
kutubxona/
├── models.py          # Kitob va Foydalanuvchi classlari
├── database.py        # Ma'lumotlar bilan ishlash
├── utils.py          # Yordamchi funksiyalar  
├── main.py           # Asosiy dastur
└── data/
    ├── kitoblar.json
    └── foydalanuvchilar.json
```

**Funksionallik**:
1. Kitob qo'shish, o'chirish, tahrirlash
2. Kitob qidirish (nom, muallif, janr bo'yicha)
3. Foydalanuvchi ro'yxatdan o'tish
4. Kitob ijarasi berish/qaytarish
5. Hisobotlar (eng mashhur kitoblar, qarzdorlar)
6. Ma'lumotlarni JSON faylda saqlash

**models.py**:
```python
def kitob_yaratish(id, nom, muallif, janr, yil):
    """Kitob ma'lumotlari strukturasini yaratish"""
    pass

def foydalanuvchi_yaratish(id, ism, email, telefon):
    """Foydalanuvchi ma'lumotlari strukturasini yaratish"""  
    pass
```

---

## Topshirish talablari

1. **Deadline**: [Sana]
2. **Format**: 
   - Har bir topshiriq uchun alohida fayl
   - Modullar uchun alohida katalog
3. **Fayl nomlari**:
   - `1_kalkulyator.py`
   - `2_matn_tahlilchi.py`
   - `3_talabalar_tizimi.py`
   - `4_modullar/` katalogi
   - `bonus_kutubxona/` katalogi (ixtiyoriy)

4. **Kod talablari**:
   - Har funksiya uchun docstring
   - Test kodlari
   - Error handling
   - Izohlar

## Baholash mezonlari

| Topshiriq | Max ball | Asosiy mezon |
|-----------|----------|---------------|
| Kalkulyator | 20 | Funksiyalar + UI |
| Matn tahlilchisi | 25 | *args/**kwargs + string methods |
| Talabalar tizimi | 30 | Murakkab data structure + functions |
| Modullar | 25 | Import/export + modularity |
| **Jami** | **100** | |
| Bonus loyiha | +15 | To'liq tizim + file operations |

---

## Qo'shimcha maslahatlar

1. **Kod yozishdan oldin**:
   - Har topshiriq uchun rejalashtiring
   - Qaysi funksiyalar kerakligini ro'yxatlang
   - Ma'lumotlar strukturasini o'ylang

2. **Dasturlash jarayonida**:
   - Kichik qismlar bo'lib yozing
   - Har funksiyani alohida test qiling
   - Docstring va izohlar qo'shing

3. **Tugagandan keyin**:
   - Barcha funksiyalarni test qiling
   - Error case'larni tekshiring
   - Kodni qayta ko'rib chiqing va optimallashtiring

**Omad tilaymiz! Happy Coding! 🐍✨**