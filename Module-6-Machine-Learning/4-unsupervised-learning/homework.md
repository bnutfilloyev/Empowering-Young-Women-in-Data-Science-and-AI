# 📚 Uyga Vazifa: Unsupervised Learning

## 🎯 Maqsad
Ushbu uyga vazifada siz K-means, Hierarchical Clustering va PCA'ni mustaqil ravishda qo'llaysiz va real datasetlar bilan ishlaysiz.

---

## 📋 Vazifa 1: Customer Retention Analysis (30 ball)

### 📊 Dataset
Bank mijozlari churn dataseti (kimlar bankni tark etgan):
- **Credit Score**: Kredit reytingi
- **Age**: Yosh
- **Tenure**: Bank bilan ishlash muddati (yil)
- **Balance**: Balans
- **NumOfProducts**: Mahsulotlar soni
- **HasCrCard**: Kredit karta bor-yo'qligi
- **IsActiveMember**: Aktiv a'zo
- **EstimatedSalary**: Taxminiy maosh

### ✏️ Sizning vazifangiz:

#### 1. Data Preprocessing (5 ball)
- [ ] Datasetni import qiling yoki synthetic data yarating (200+ mijoz)
- [ ] Missing values'ni tekshiring va to'ldiring
- [ ] Categorical features'ni encode qiling (Gender, Geography)
- [ ] Feature scaling (StandardScaler)

#### 2. K-means Clustering (10 ball)
- [ ] Elbow Method bilan optimal K ni toping (K=2 dan 10 gacha)
- [ ] Silhouette Score hisoblang
- [ ] K-means clustering (optimal K bilan)
- [ ] Har bir klasterning xususiyatlarini tahlil qiling

#### 3. Visualization (10 ball)
- [ ] Income vs Balance scatter plot (klasterlangan)
- [ ] Age distribution per cluster
- [ ] Cluster statistics jadval
- [ ] Elbow plot

#### 4. Interpretation (5 ball)
- [ ] Har bir klasterga nom bering (masalan, "High Value", "At Risk")
- [ ] Qaysi klasterga e'tibor berish kerak?
- [ ] Marketing strategy tavsiya bering

**Deadline**: 1 hafta

---

## 📋 Vazifa 2: World Countries Analysis (35 ball)

### 📊 Dataset
Dunyo mamlakatlari haqida ma'lumot:
- **Population**: Aholi soni
- **GDP**: YaIM (billion $)
- **GDP_per_capita**: Aholi boshiga YaIM
- **Area**: Maydon (km²)
- **Urban_population**: Shahar aholisi (%)
- **Literacy_rate**: Savodxonlik (%)
- **Infant_mortality**: Chaqaloq o'limi (1000 tug'ilishda)
- **Life_expectancy**: O'rtacha umr (yil)
- **CO2_emissions**: CO2 chiqindi (ton/kishi)

### ✏️ Sizning vazifangiz:

#### 1. Data Collection (5 ball)
- [ ] Real dataset topish (Kaggle, World Bank) yoki synthetic yaratish (50+ mamlakat)
- [ ] EDA: Statistika, distribyutsiyalar, correlations

#### 2. Hierarchical Clustering (15 ball)
- [ ] Feature selection (eng muhim 5-6 ta)
- [ ] Standardization
- [ ] Dendrogram chizish (Ward linkage)
- [ ] Optimal klasterlar sonini tanlash
- [ ] 4 xil linkage metodini taqqoslash (Single, Complete, Average, Ward)
- [ ] Eng yaxshi metodini tanlash (Silhouette Score asosida)

#### 3. PCA Analysis (10 ball)
- [ ] PCA: n-D → 2D
- [ ] Scree plot chizish
- [ ] Explained variance tahlil
- [ ] PCA space'da clustering'ni vizualizatsiya qilish

#### 4. Report (5 ball)
- [ ] Mamlakatlarni guruhlash (Developed, Developing, Underdeveloped)
- [ ] Har bir guruhning xususiyatlari
- [ ] Policy recommendations

**Deadline**: 1.5 hafta

---

## 📋 Vazifa 3: Image Compression with PCA (20 ball)

### 📊 Dataset
Rasmlarni PCA bilan siqish (compression).

### ✏️ Sizning vazifangiz:

#### 1. Image Loading (3 ball)
- [ ] Rang rasmi yuklash (misol: 256x256 RGB yoki dataset'dan)
- [ ] Matplotlib bilan vizualizatsiya

#### 2. PCA Compression (10 ball)
- [ ] Rasm pixellarini 2D matrix'ga aylantirish
- [ ] Har bir rang kanali (R, G, B) uchun alohida PCA
- [ ] Turli n_components bilan siqish: 
  - 10, 20, 50, 100, 200 components
- [ ] Har bir variant uchun compressed rasmi ko'rsatish

#### 3. Quality vs Compression (5 ball)
- [ ] Explained variance vs n_components grafigi
- [ ] Original va compressed rasmlarni taqqoslash (side-by-side)
- [ ] Compression ratio hisoblash:
  ```
  Compression ratio = Original size / Compressed size
  ```

#### 4. Analysis (2 ball)
- [ ] Qancha components yetarli? (90%+ variance)
- [ ] Quality vs Storage trade-off

**Bonus (+5 ball)**: Grayscale rasm bilan ham test qiling va natijalarni taqqoslang.

**Deadline**: 1 hafta

---

## 📋 Vazifa 4: Advanced Clustering (15 ball)

### 📊 Task
Turli clustering algoritmlarini taqqoslash.

### ✏️ Sizning vazifangiz:

#### 1. Dataset Preparation (3 ball)
- [ ] `sklearn.datasets.make_moons` yoki `make_circles` ishlatish
- [ ] Yoki real dataset (Kaggle)

#### 2. Clustering Algorithms (9 ball)
Quyidagi algoritmlarn qo'llash:
- [ ] K-means
- [ ] Hierarchical Clustering (Ward, Average, Single)
- [ ] DBSCAN (bonus algorithm - o'rganib qo'llash kerak)

Har biri uchun:
- [ ] Clustering natijasini vizualizatsiya qilish
- [ ] Silhouette Score hisoblash
- [ ] Ustunliklari va kamchiliklari

#### 3. Comparison Table (3 ball)
Jadval yaratish:

| Algorithm | Silhouette | Speed | Best For | Worst For |
|-----------|------------|-------|----------|-----------|
| K-means   | ...        | ...   | ...      | ...       |
| Hierarchical | ...     | ...   | ...      | ...       |
| DBSCAN    | ...        | ...   | ...      | ...       |

**Deadline**: 1 hafta

---

## 🎁 Bonus Vazifalar (Qo'shimcha 20 ball)

### Bonus 1: t-SNE vs PCA (10 ball)
- [ ] t-SNE algoritmi haqida o'qing
- [ ] MNIST yoki Fashion-MNIST'da PCA vs t-SNE taqqoslang
- [ ] Visualization quality'ni baholang

### Bonus 2: Real Business Case (10 ball)
- [ ] Kaggle'dan real business dataset topish
- [ ] Complete end-to-end clustering project:
  - EDA
  - Feature engineering
  - Clustering (K-means yoki Hierarchical)
  - Business insights
  - Recommendations
- [ ] Jupyter Notebook yoki report tayyorlash

---

## 📤 Topshirish Ko'rsatmalari

### Format:
1. **Jupyter Notebook** (.ipynb) - barcha kod va visualization
2. **PDF Report** - natijalar, tahlil, xulosalar
3. **README.md** - qisqacha qo'llanma

### Folder Structure:
```
homework_unsupervised_learning/
├── task1_customer_retention/
│   ├── task1.ipynb
│   ├── report.pdf
│   └── data/ (agar kerak bo'lsa)
├── task2_countries/
│   ├── task2.ipynb
│   ├── report.pdf
│   └── data/
├── task3_image_compression/
│   ├── task3.ipynb
│   ├── images/
│   └── report.pdf
└── task4_advanced_clustering/
    ├── task4.ipynb
    └── report.pdf
```

### Submission:
- GitHub repository link yoki
- ZIP file

---

## 📊 Baholash Mezonlari

| Mezon | Ball |
|-------|------|
| **Vazifa 1**: Customer Retention | 30 |
| **Vazifa 2**: Countries Analysis | 35 |
| **Vazifa 3**: Image Compression | 20 |
| **Vazifa 4**: Advanced Clustering | 15 |
| **Bonus 1**: t-SNE vs PCA | +10 |
| **Bonus 2**: Real Business Case | +10 |
| **Jami** | **100 (+20 bonus)** |

### Baholash Tizimi:
- **90-100**: A (Excellent) - Barcha vazifalar to'liq, bonus qilgan
- **80-89**: B (Good) - Barcha vazifalar yaxshi ishlangan
- **70-79**: C (Satisfactory) - Ko'pgina vazifalar to'liq
- **60-69**: D (Pass) - Asosiy vazifalar bajarilgan
- **< 60**: F (Fail) - Yetarli emas

---

## 💡 Hints va Maslahatlar

### K-means:
```python
# Elbow Method
inertias = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

plt.plot(range(2, 11), inertias, 'bo-')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()
```

### Hierarchical:
```python
from scipy.cluster.hierarchy import dendrogram, linkage

linkage_mat = linkage(X_scaled, method='ward')
dendrogram(linkage_mat)
plt.show()
```

### PCA:
```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Explained variance: {pca.explained_variance_ratio_.sum():.2%}")
```

### Image Compression:
```python
from sklearn.decomposition import PCA
import matplotlib.image as mpimg

# Load image
img = mpimg.imread('image.jpg')

# Separate channels
R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]

# PCA per channel
pca_r = PCA(n_components=50)
R_compressed = pca_r.inverse_transform(pca_r.fit_transform(R))

# Combine
img_compressed = np.stack([R_compressed, G_compressed, B_compressed], axis=2)

# Clip values [0, 255]
img_compressed = np.clip(img_compressed, 0, 255).astype(np.uint8)
```

---

## 📚 Qo'shimcha Resurslar

### Documentation:
- [Scikit-learn Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [Scikit-learn PCA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- [Scipy Hierarchical](https://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html)

### Tutorials:
- [K-means Clustering Tutorial](https://realpython.com/k-means-clustering-python/)
- [Hierarchical Clustering](https://stackabuse.com/hierarchical-clustering-with-python-and-scikit-learn/)
- [PCA in Python](https://towardsdatascience.com/pca-using-python-scikit-learn-e653f8989e60)

### Datasets:
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [World Bank Data](https://data.worldbank.org/)

---

## ❓ Savollar?

Agar savollar bo'lsa:
- Email: instructor@example.com
- Office Hours: Har kuni 14:00-16:00
- Forum: [course-forum.com](https://example.com)

---

## ⚠️ Muhim Eslatmalar

1. **Plagiarism (ko'chirish)** - qat'iyan man etilgan! Boshqadan ko'chirsangiz 0 ball.
2. **Deadline** - Kechiksa har kun uchun -5 ball.
3. **Code quality** - Yaxshi yozilgan, izohli kod (comments) muhim.
4. **Visualization** - Grafiklar professional bo'lishi kerak.
5. **Interpretation** - Faqat kod emas, tahlil va xulosa ham kerak!

---

# ✅ Omad tilaymiz!

Bu vazifa murakkab, lekin juda foydali. Real loyihalarda unsupervised learning ko'p ishlatiladi. Diqqat bilan ishlang va o'rganing!

**Good luck! 🚀🎯**
