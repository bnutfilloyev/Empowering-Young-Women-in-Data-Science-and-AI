# Datasets

Bu papkada amaliy mashg'ulotlar uchun sample datasetlar joylashgan.

## Datasetlarni Yaratish

Datasetlarni yaratish uchun:

```bash
# Kerakli kutubxonalarni o'rnating
pip install pandas numpy

# Dataset generator ni ishga tushiring
python generate_datasets.py
```

## Mavjud Datasets

### 1. employees.csv
**Tavsif:** Kompaniya xodimlari haqida ma'lumot

**Ustunlar:**
- `ID` - Xodim IDsi
- `Ism` - Xodim ismi
- `Yosh` - Yosh
- `Jins` - Jinsi (Erkak/Ayol)
- `Bo'lim` - Ishlayotgan bo'limi
- `Lavozim` - Lavozimi
- `Ish_Tajribasi` - Ish tajribasi (yil)
- `Maosh` - Oylik maosh (so'm)
- `Shahar` - Yashaydigan shahar
- `Email` - Email manzil

**Muammolar:**
- Missing values (~15%)
- Takroriy qatorlar (~5%)

### 2. customers.csv
**Tavsif:** Onlayn magazin mijozlari

**Ustunlar:**
- `Customer_ID` - Mijoz IDsi
- `Yosh` - Yosh
- `Jins` - Jinsi
- `Daromad` - Oylik daromad
- `Xarid_Soni` - Xaridlar soni
- `Jami_Xarajat` - Jami xarajat
- `Sodiqlik_Darajasi` - Sodiqlik darajasi (Past/O'rta/Yuqori)
- `Ro'yxatdan_o'tgan` - Ro'yxatdan o'tgan sana

**Muammolar:**
- Missing values (~20%)

### 3. products.csv
**Tavsif:** Mahsulotlar ro'yxati

**Ustunlar:**
- `Product_ID` - Mahsulot IDsi
- `Nomi` - Mahsulot nomi
- `Kategoriya` - Kategoriya
- `Brand` - Brand
- `Narx` - Narx
- `Sotilgan_Soni` - Sotilgan soni
- `Reyting` - Reyting (1-5)
- `Mavjud` - Mavjudligi (Ha/Yo'q)

**Muammolar:**
- Missing values (~10%)

## Foydalanish

```python
import pandas as pd

# Datasetni yuklash
df = pd.read_csv('datasets/employees.csv')

# Ma'lumotlarni ko'rish
print(df.head())
print(df.info())
```

## Eslatma

Barcha datasetlar o'quv maqsadlari uchun yaratilgan va real ma'lumotlar emas.
