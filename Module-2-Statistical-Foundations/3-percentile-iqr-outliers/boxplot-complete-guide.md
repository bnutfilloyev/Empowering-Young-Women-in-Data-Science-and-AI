# Boxplot Asoslari: To'liq Qo'llanma

## 📊 Boxplot Nima?

**Boxplot (Box-and-Whisker Plot)** - ma'lumotlar taqsimotini vizual ko'rsatuvchi eng kuchli statistik grafik usullaridan biri. U ma'lumotlarning asosiy statistik xususiyatlarini bitta grafikda aks ettiradi.

---

## 🎯 Boxplotning Asosiy Qismlari

### 1. **Box (Quti)** 📦
- **Balandligi**: IQR (Q3 - Q1) ni ifodalaydi
- **Pastki chegarasi**: Q1 (25% kvantil)
- **Yuqori chegarasi**: Q3 (75% kvantil)
- **Ichidagi ma'lumotlar**: O'rta 50% ma'lumotlar

### 2. **Median chiziq** ➖
- Quti ichidagi horizontal chiziq
- Q2 (50% kvantil) ni ko'rsatadi
- Ma'lumotlarning o'rta qiymatini bildiradi

### 3. **Whiskers (Mo'ylovlar)** 📏
- Qutidan chiquvchi vertikal chiziqlar
- **Pastki whisker**: Q1 dan eng kichik qiymatgacha
- **Yuqori whisker**: Q3 dan eng katta qiymatgacha
- **Uzunligi**: Odatda 1.5 × IQR dan oshmasligi kerak

### 4. **Outliers (Chetga chiquvchi qiymatlar)** 🔴
- Whiskers chegarasidan tashqaridagi nuqtalar
- Alohida nuqtalar sifatida ko'rsatiladi
- Noodatiy qiymatlarni bildiradi

---

## 📐 Boxplot Qanday Chiziladi?

### Qadam-baqadam jarayon:

#### 1-qadam: Ma'lumotlarni tartiblash
```
Ma'lumotlar: [2, 5, 7, 8, 10, 12, 15, 18, 20, 25, 30]
Tartibli: [2, 5, 7, 8, 10, 12, 15, 18, 20, 25, 30]
```

#### 2-qadam: Kvartillarni hisoblash
```
Q1 (25%): 7.5
Q2 (50%): 12 (Median)
Q3 (75%): 19
IQR = Q3 - Q1 = 19 - 7.5 = 11.5
```

#### 3-qadam: Whiskers chegaralarini aniqlash
```
Pastki chegara = Q1 - 1.5 × IQR = 7.5 - 1.5 × 11.5 = -9.75
Yuqori chegara = Q3 + 1.5 × IQR = 19 + 1.5 × 11.5 = 36.25
```

#### 4-qadam: Outlierlarni aniqlash
```
Pastki outliers: Ma'lumotlar < -9.75 (yo'q)
Yuqori outliers: Ma'lumotlar > 36.25 (yo'q)
```

#### 5-qadam: Boxplotni chizish
```
- Quti: 7.5 dan 19 gacha
- Median chiziq: 12 da
- Pastki whisker: 7.5 dan 2 gacha
- Yuqori whisker: 19 dan 30 gacha
```

---

## 💻 Python bilan Boxplot Chizish

### 1. Matplotlib bilan

```python
import matplotlib.pyplot as plt
import numpy as np

# Ma'lumotlar
data = [2, 5, 7, 8, 10, 12, 15, 18, 20, 25, 30, 45, 50]

# Boxplot yaratish
plt.figure(figsize=(8, 6))
bp = plt.boxplot(data, patch_artist=True)

# Ranglarni sozlash
bp['boxes'][0].set_facecolor('lightblue')
bp['boxes'][0].set_alpha(0.7)

# Sarlavha va yorliqlar
plt.title('Boxplot Misoli', fontsize=14, fontweight='bold')
plt.ylabel('Qiymatlar')
plt.grid(True, alpha=0.3)

# Kvartillarni ko'rsatish
Q1, Q2, Q3 = np.percentile(data, [25, 50, 75])
plt.text(1.1, Q1, f'Q1: {Q1}', fontsize=10)
plt.text(1.1, Q2, f'Q2: {Q2}', fontsize=10, fontweight='bold')
plt.text(1.1, Q3, f'Q3: {Q3}', fontsize=10)

plt.show()
```

### 2. Seaborn bilan

```python
import seaborn as sns
import pandas as pd

# Ma'lumotlar yaratish
guruh_data = ['A', 'B', 'C'] * 10
qiymat_data = [np.random.normal(50, 10) for _ in range(10)] + \
              [np.random.normal(60, 15) for _ in range(10)] + \
              [np.random.normal(70, 12) for _ in range(10)]

df = pd.DataFrame({'Guruh': guruh_data, 'Qiymat': qiymat_data})


# Boxplot yaratish
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Guruh', y='Qiymat', palette='Set2')
plt.title('Guruhlar bo\'yicha Boxplot', fontsize=14, fontweight='bold')
plt.ylabel('Qiymatlar')
plt.grid(True, alpha=0.3)
plt.show()
```

### 3. Pandas bilan

```python
# DataFrame dan to'g'ridan-to'g'ri
df.boxplot(column='Qiymat', by='Guruh', figsize=(10, 6))
plt.title('Pandas Boxplot')
plt.suptitle('')  # Avtomatik sarlavhani o'chirish
plt.show()
```

---

## 📈 Boxplot Talqin Qilish

### 1. **Markaziy Tendensiya**
```python
# Median pozitsiyasi
if median_quti_ortada:
    print("Simmetrik taqsimot")
elif median_quti_pastida:
    print("Chapga qiyshaygan")
else:
    print("O'ngga qiyshaygan")
```

### 2. **Tarqalish Tahlili**
```python
# IQR tahlili
if IQR < ma_lumotlar_range * 0.2:
    print("Past tarqalish - ma'lumotlar to'plangan")
elif IQR > ma_lumotlar_range * 0.6:
    print("Yuqori tarqalish - ma'lumotlar sochilgan")
else:
    print("O'rtacha tarqalish")
```

### 3. **Outlierlar Baholash**
```python
# Outlierlar soni
outlier_count = len(outliers)
total_count = len(data)
outlier_percentage = (outlier_count / total_count) * 100

if outlier_percentage < 5:
    print("Normal outlier miqdori")
elif outlier_percentage > 10:
    print("Ko'p outlier - ma'lumotlarni tekshiring")
```

---

## 🔧 Boxplot Turlari

### 1. **Oddiy Boxplot**
- Bitta o'zgaruvchi uchun
- Asosiy statistikalarni ko'rsatadi

### 2. **Guruhli Boxplot**
- Bir nechta guruhni taqqoslash
- Kategorik o'zgaruvchi bo'yicha

### 3. **Violin Plot**
- Boxplot + zichlik egri chizig'i
- Taqsimot shaklini batafsil ko'rsatadi

### 4. **Notched Boxplot**
- Median atrofida ishonch oralig'i
- Medianlarni statistik taqqoslash uchun

---

## 🎨 Boxplot Sozlash

### 1. **Ranglar va Uslub**

```python
# Ranglarni sozlash
colors = ['lightblue', 'lightgreen', 'lightcoral']
bp = plt.boxplot(data, patch_artist=True)

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Chiziqlar uslubi
bp['medians'][0].set_color('red')
bp['medians'][0].set_linewidth(2)
```

### 2. **Outlier Belgisini O'zgartirish**

```python
# Outlier shakli va rangi
plt.boxplot(data, 
           flierprops=dict(marker='o', markerfacecolor='red', 
                          markersize=8, alpha=0.7))
```

### 3. **Whiskers Uzunligini Sozlash**

```python
# Whiskers koeffitsienti (standart: 1.5)
plt.boxplot(data, whis=2.0)  # 2 × IQR
plt.boxplot(data, whis=[10, 90])  # 10% va 90% percentillar
```

---

## 📊 Amaliy Misollar

### Misol 1: Talabalar Baholarini Tahlil

```python
import pandas as pd
import matplotlib.pyplot as plt

# Ma'lumotlar
baholar = {
    'Matematika': [85, 90, 78, 92, 88, 95, 76, 89, 91, 45],
    'Fizika': [82, 87, 90, 85, 88, 92, 79, 86, 94, 77],
    'Kimyo': [90, 85, 88, 91, 87, 89, 93, 86, 84, 92]
}

df = pd.DataFrame(baholar)

# Boxplot yaratish
plt.figure(figsize=(10, 6))
bp = plt.boxplot([df['Matematika'], df['Fizika'], df['Kimyo']], 
                 labels=['Matematika', 'Fizika', 'Kimyo'],
                 patch_artist=True)

# Ranglar
colors = ['lightblue', 'lightgreen', 'lightcoral']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Fanlar bo\'yicha Talabalar Baholari', fontweight='bold')
plt.ylabel('Baholar')
plt.grid(True, alpha=0.3)
plt.show()

# Statistik tahlil
for fan, baholar_list in baholar.items():
    data = pd.Series(baholar_list)
    Q1, Q2, Q3 = data.quantile([0.25, 0.5, 0.75])
    print(f"\n{fan}:")
    print(f"  Q1: {Q1:.1f}, Q2: {Q2:.1f}, Q3: {Q3:.1f}")
    print(f"  IQR: {Q3-Q1:.1f}")
```

### Misol 2: Oylik Maosh Taqsimoti

```python
# Turli lavozimlar bo'yicha maosh
maoshlar = {
    'Junior': [3000, 3200, 3500, 3100, 3400, 3300, 3600],
    'Middle': [5000, 5200, 5500, 5100, 5400, 5300, 5800, 4800],
    'Senior': [8000, 8500, 9000, 8200, 8800, 9200, 8600, 12000]
}

# Boxplot bilan tahlil
plt.figure(figsize=(12, 6))
data_list = list(maoshlar.values())
labels = list(maoshlar.keys())

bp = plt.boxplot(data_list, labels=labels, patch_artist=True)

# Gradient ranglar
colors = plt.cm.viridis(np.linspace(0, 1, len(labels)))
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.title('Lavozimlar bo\'yicha Maosh Taqsimoti', fontweight='bold')
plt.ylabel('Maosh (USD)')
plt.grid(True, alpha=0.3)
plt.show()
```


---

## 💡 Amaliy Tavsiyalar

### 1. **Qachon Ishlatish**
- ✅ Bir nechta guruhni taqqoslashda
- ✅ Outlierlarni aniqlashda
- ✅ Tez statistik ko'rinish olishda
- ✅ Ma'lumotlar sifatini baholashda

### 2. **Qachon Ishlatmaslik**
- ❌ Aniq taqsimot shakli kerakda
- ❌ Kichik ma'lumotlar to'plamida
- ❌ Bimodal taqsimotlarni tahlil qilishda

### 3. **Yaxshilash Usullari**
- Violin plot bilan birlashtrish
- Ranglarni ma'noli qilish
- Statistik testlar bilan qo'shish
- Kontekst ma'lumoti qo'shish

