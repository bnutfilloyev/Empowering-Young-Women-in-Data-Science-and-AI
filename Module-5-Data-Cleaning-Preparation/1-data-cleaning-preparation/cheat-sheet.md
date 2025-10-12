# Data Tozalash va Tayyorlash - Cheat Sheet

## 🔍 Missing Values

### Aniqlash
```python
# Missing values borligini tekshirish
df.isnull()  # yoki df.isna()
df.isnull().sum()  # har bir ustunda
df.isnull().sum().sum()  # jami

# Missing values foizi
(df.isnull().sum() / len(df)) * 100

# Vizualizatsiya
import seaborn as sns
sns.heatmap(df.isnull(), cbar=True)
```

### O'chirish
```python
# Barcha missing values bo'lgan qatorlarni o'chirish
df.dropna()

# Ma'lum ustundagi missing values bo'yicha
df.dropna(subset=['ustun_nomi'])

# Ustunlarni o'chirish
df.dropna(axis=1)

# Threshold: kamida 3 ta non-null bo'lishi kerak
df.dropna(thresh=3)
```

### To'ldirish
```python
# Ma'lum qiymat bilan
df.fillna(0)
df['ustun'].fillna('Unknown')

# Statistik qiymatlar bilan
df['ustun'].fillna(df['ustun'].mean())    # o'rtacha
df['ustun'].fillna(df['ustun'].median())  # median
df['ustun'].fillna(df['ustun'].mode()[0]) # mode

# Forward/Backward fill
df.fillna(method='ffill')  # oldingisini nusxalash
df.fillna(method='bfill')  # keyingisini nusxalash

# Interpolation
df['ustun'].interpolate()
```

### SimpleImputer (Scikit-learn)
```python
from sklearn.impute import SimpleImputer

# Mean imputer
imputer = SimpleImputer(strategy='mean')
df[['ustun1', 'ustun2']] = imputer.fit_transform(df[['ustun1', 'ustun2']])

# Strategiyalar: 'mean', 'median', 'most_frequent', 'constant'
```

---

## 🔄 Duplicates

### Aniqlash
```python
# Takroriy qatorlar
df.duplicated()
df.duplicated().sum()  # soni

# Barcha takrorlarni ko'rsatish
df[df.duplicated(keep=False)]

# Ma'lum ustunlar bo'yicha
df.duplicated(subset=['ustun1', 'ustun2'])
```

### O'chirish
```python
# Birinchisini saqlash (default)
df.drop_duplicates()

# Oxirgisini saqlash
df.drop_duplicates(keep='last')

# Hammasini o'chirish
df.drop_duplicates(keep=False)

# Ma'lum ustunlar bo'yicha
df.drop_duplicates(subset=['ustun1', 'ustun2'])
```

---

## 🔢 Categorical Encoding

### Label Encoding
```python
# Manual mapping
mapping = {'Past': 0, "O'rta": 1, 'Yuqori': 2}
df['daraja'] = df['daraja'].map(mapping)

# LabelEncoder
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['ustun_encoded'] = le.fit_transform(df['ustun'])

# Kategoriyalarni ko'rish
le.classes_
```

### Ordinal Encoding
```python
from sklearn.preprocessing import OrdinalEncoder

categories = [['Past', "O'rta", 'Yuqori']]
encoder = OrdinalEncoder(categories=categories)
df['ustun_encoded'] = encoder.fit_transform(df[['ustun']])
```

### One-Hot Encoding
```python
# Pandas get_dummies
df_encoded = pd.get_dummies(df, columns=['ustun'])
df_encoded = pd.get_dummies(df, columns=['ustun'], drop_first=True)
df_encoded = pd.get_dummies(df, columns=['ustun'], prefix='prefix')

# OneHotEncoder
from sklearn.preprocessing import OneHotEncoder

ohe = OneHotEncoder(sparse_output=False, drop='first')
encoded = ohe.fit_transform(df[['ustun']])
```

---

## 🎯 Qaysi Usulni Tanlash?

### Missing Values
| Holat | Usul | Sabab |
|-------|------|-------|
| Missing < 5% | dropna() | Ma'lumot kam yo'qoladi |
| Numerical data | mean/median | Statistik to'g'ri |
| Outlier bor | median | Mean noto'g'ri |
| Categorical | mode | Eng ko'p uchraydigan |
| Time series | ffill/bfill | Vaqt bo'yicha mantiqiy |
| Missing > 50% | Ustunni o'chirish | Juda ko'p missing |

### Encoding
| Ma'lumot Turi | Usul | Misol |
|---------------|------|-------|
| Binary (2 kategoriya) | Label Encoding | Jins: Erkak/Ayol |
| Ordinal (tartibli) | Ordinal Encoding | Daraja: Past < O'rta < Yuqori |
| Nominal (tartiбsiz) | One-Hot Encoding | Rang: Qizil, Ko'k, Yashil |
| Ko'p kategoriya (>10) | Target Encoding | Shahar (100+ shahar) |

### Model bo'yicha
| Model | Encoding | Sabab |
|-------|----------|-------|
| Tree-based (RF, XGBoost) | Label Encoding | Daraxtlar tartibni hal qiladi |
| Linear models | One-Hot | Tartib yaratilmasligi kerak |
| Neural Networks | One-Hot yoki Embedding | Kategoriyalar o'rtasida masofa yo'q |

---

## 📊 Data Quality Checks

```python
# Asosiy ma'lumot
df.info()
df.describe()
df.shape

# Missing values
df.isnull().sum()

# Duplicates
df.duplicated().sum()

# Data types
df.dtypes

# Unique qiymatlar
df.nunique()
df['ustun'].unique()
df['ustun'].value_counts()

# Outliers (IQR usuli)
Q1 = df['ustun'].quantile(0.25)
Q3 = df['ustun'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['ustun'] < Q1 - 1.5*IQR) | (df['ustun'] > Q3 + 1.5*IQR)]
```

---

## 🔧 To'liq Pipeline

```python
def clean_data(df):
    """Data cleaning pipeline"""
    
    # 1. Nusxa yaratish
    df_cleaned = df.copy()
    
    # 2. Missing values
    numeric_cols = df_cleaned.select_dtypes(include=[np.number]).columns
    categorical_cols = df_cleaned.select_dtypes(include=['object']).columns
    
    # Raqamli ustunlar - median
    for col in numeric_cols:
        df_cleaned[col].fillna(df_cleaned[col].median(), inplace=True)
    
    # Kategorik ustunlar - mode
    for col in categorical_cols:
        df_cleaned[col].fillna(df_cleaned[col].mode()[0], inplace=True)
    
    # 3. Duplicates
    df_cleaned.drop_duplicates(inplace=True)
    
    # 4. Encoding
    # Binary
    if 'jins' in df_cleaned.columns:
        df_cleaned['jins'] = df_cleaned['jins'].map({'Erkak': 0, 'Ayol': 1})
    
    # Ordinal
    if 'daraja' in df_cleaned.columns:
        daraja_map = {'Past': 0, "O'rta": 1, 'Yuqori': 2}
        df_cleaned['daraja'] = df_cleaned['daraja'].map(daraja_map)
    
    # One-Hot
    nominal_cols = ['shahar', 'bo\'lim']  # misol
    for col in nominal_cols:
        if col in df_cleaned.columns:
            df_cleaned = pd.get_dummies(df_cleaned, columns=[col], drop_first=True)
    
    return df_cleaned
```

---

## 💡 Best Practices

1. **Har doim nusxa yarating**
   ```python
   df_cleaned = df.copy()
   ```

2. **Missing values ni tushunib to'ldiring**
   - Nima uchun missing?
   - Random yoki pattern bormi?
   - Qanday to'ldirish to'g'ri?

3. **Visualize edin**
   ```python
   # Missing values
   sns.heatmap(df.isnull())
   
   # Distributions
   df.hist(figsize=(12, 10))
   
   # Boxplots (outliers)
   df.boxplot()
   ```

4. **Dokumentatsiya qiling**
   - Qanday o'zgarishlar qilindingiz
   - Nima uchun o'sha usulni tanladingiz
   - Qancha ma'lumot o'chirildi

5. **Validate qiling**
   ```python
   # Missing values yo'qligini tekshirish
   assert df.isnull().sum().sum() == 0
   
   # Barcha ustunlar raqamli ekanligini tekshirish
   assert df.select_dtypes(include=['object']).shape[1] == 0
   ```

---

## 🎯 Common Pitfalls

1. ❌ **Missing values ni 0 bilan to'ldirish**
   - 0 ham ma'lumot! Mean/median ishlatish yaxshiroq

2. ❌ **Barcha kategoriyalarni one-hot encoding qilish**
   - Ko'p ustun yaratadi
   - Memory muammolari
   - Multicollinearity

3. ❌ **Takrorlarni tekshirmaslik**
   - Model overfitting
   - Noto'g'ri statistika

4. ❌ **Strategiya tanlamaslik**
   - Har bir ustun uchun individual yondashuv kerak

5. ❌ **Outlier tekshirmaslik**
   - Model performance past bo'ladi

---

## 📚 Foydali Funksiyalar

```python
# Ma'lumotlar haqida to'liq hisobot
def data_report(df):
    print("="*60)
    print("DATA REPORT")
    print("="*60)
    print(f"\nShape: {df.shape}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nDuplicates: {df.duplicated().sum()}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMemory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# Missing values foizi
def missing_percentage(df):
    missing = pd.DataFrame({
        'Column': df.columns,
        'Missing': df.isnull().sum(),
        'Percentage': (df.isnull().sum() / len(df)) * 100
    })
    return missing.sort_values('Percentage', ascending=False)

# Kategorik ustunlar haqida ma'lumot
def categorical_info(df):
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        print(f"\n{col}:")
        print(df[col].value_counts())
```

---

## 🚀 Quick Reference

```python
# Missing values
df.isnull().sum()                      # aniqlash
df.dropna()                            # o'chirish
df.fillna(df.mean())                   # to'ldirish

# Duplicates
df.duplicated().sum()                  # aniqlash
df.drop_duplicates()                   # o'chirish

# Encoding
df['col'].map({'A': 0, 'B': 1})       # label
pd.get_dummies(df, columns=['col'])    # one-hot

# Data types
df.dtypes                              # ko'rish
df['col'].astype('int')               # o'zgartirish

# Selection
df.select_dtypes(include=['object'])   # kategorik
df.select_dtypes(include=[np.number])  # raqamli
```

---

**Eslatma:** Bu cheat sheet asosiy usullarni o'z ichiga oladi. Har bir vazifa uchun context muhim! 🎯
