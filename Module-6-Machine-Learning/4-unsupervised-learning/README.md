# 4-dars: Unsupervised Learning (Clustering va Dimensionality Reduction)

## 📚 Mavzu maqsadi
Bu darsda siz unsupervised learning algoritmlarini o'rganasiz - bu algoritmlarda label (javob) bo'lmaydi, faqat pattern'larni topish kerak.

---

## 🎯 O'rganilayotgan mavzular

### 1. Clustering (Klasterlash)

#### K-means Clustering
- Algoritm ishlashi
- Centroid kontseptsiyasi
- Elbow method (optimal K topish)
- Silhouette Score
- Inertia (within-cluster sum of squares)
- Limitations va best practices

#### Hierarchical Clustering
- Agglomerative (bottom-up) clustering
- Dendrogram vizualizatsiyasi
- Linkage methods:
  - Single linkage
  - Complete linkage
  - Average linkage
  - Ward linkage
- Distance metrics
- K-means vs Hierarchical taqqoslash

### 2. Dimensionality Reduction

#### Principal Component Analysis (PCA)
- High-dimensional data muammosi
- Variance va covariance
- Eigenvectors va eigenvalues
- Principal components tushunchasi
- Explained variance ratio
- Scree plot
- Data compression
- Visualization (3D → 2D)

---

## 🌍 Real-world Applications

### Clustering:
- 🛒 **Customer Segmentation** - Mijozlarni guruhlash (marketing)
- 📰 **Document Clustering** - Xabarlarni kategoriyalash
- 🧬 **Gene Expression Analysis** - Genlarni guruhlash (biologiya)
- 🏙️ **City Planning** - Shahar hududlarini guruhlash
- 🎵 **Music Recommendation** - Musiqa janrlarini aniqlash
- 📸 **Image Segmentation** - Rasm qismlarini ajratish

### PCA:
- 👤 **Face Recognition** - Yuz tanish (eigenfaces)
- 📊 **Data Visualization** - High-dim data'ni 2D/3D'da ko'rsatish
- 🎬 **Recommendation Systems** - Feature reduction
- 📈 **Stock Market Analysis** - Ko'p o'zgaruvchilarni kamaytirish
- 🧪 **Genomics** - DNA data compression
- 🖼️ **Image Compression** - Rasm hajmini kamaytirish

---

## 🔍 Supervised vs Unsupervised Learning

| Aspect | Supervised | Unsupervised |
|--------|-----------|--------------|
| **Label (Y)** | ✅ Bor | ❌ Yo'q |
| **Maqsad** | Prediction | Pattern discovery |
| **Misollar** | Classification, Regression | Clustering, PCA |
| **Evaluation** | Accuracy, RMSE | Silhouette, Inertia |
| **Qiyinchilik** | Label kerak | Natijani baholash qiyin |

---

## 📊 Dataset'lar

Bu darsda ishlatadigan dataset'lar:
1. **Iris Dataset** - Gul turlarini klasterlash
2. **Mall Customers** - Mijozlarni segmentatsiya qilish
3. **Wine Dataset** - Vino turlarini guruhlash
4. **Synthetic Data** - Clustering algoritmlarini tushunish uchun

---

## 📂 Dars tuzilishi

```
4-unsupervised-learning/
├── README.md                    # Bu fayl
├── lecture.ipynb                # To'liq nazariy material
├── practical.ipynb              # Amaliy mashg'ulotlar
├── homework.md                  # Uy vazifasi
└── unsupervised_guide.md        # Quick reference guide
```

---

## 🎓 Darsdan keyin siz:

✅ K-means clustering algoritmini tushunasiz va qo'llaysiz  
✅ Optimal K qiymatini topishni bilasiz (Elbow method)  
✅ Hierarchical clustering va dendrogram'ni tushunarli o'qiysiz  
✅ PCA yordamida dimensionality reduction qilasiz  
✅ High-dimensional data'ni 2D/3D'da visualize qilasiz  
✅ Real dataset'larda customer segmentation qilasiz  
✅ Clustering natijalarini baholashni bilasiz  

---

## 📖 Zarur bilimlar

Ushbu darsdan oldin bilishingiz kerak:
- ✅ Python (NumPy, Pandas, Matplotlib)
- ✅ Basic statistics (mean, variance)
- ✅ Linear algebra basics (vector, matrix)
- ✅ Distance metrics (Euclidean, Manhattan)
- ✅ Supervised learning concepts (Classification)

---

## 🚀 Keyingi qadamlar

Ushbu darsdan keyin o'rganishingiz mumkin:
- DBSCAN clustering
- Gaussian Mixture Models (GMM)
- t-SNE (dimensionality reduction)
- Anomaly Detection
- Association Rules (Market Basket Analysis)

---

## 💻 Amaliyot

1. **lecture.ipynb** - Nazariyani o'rganing
2. **practical.ipynb** - Amaliy mashqlarni bajaring
3. **homework.md** - Uy vazifasini bajaring
4. **unsupervised_guide.md** - Reference sifatida foydalaning

---

## 📚 Qo'shimcha resurslar

- [Scikit-learn Clustering Documentation](https://scikit-learn.org/stable/modules/clustering.html)
- [PCA Explained Visually](http://setosa.io/ev/principal-component-analysis/)
- [Clustering Algorithms Comparison](https://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_comparison.html)

---

**🎯 Tayyor bo'lsangiz, `lecture.ipynb` ga o'ting!**
