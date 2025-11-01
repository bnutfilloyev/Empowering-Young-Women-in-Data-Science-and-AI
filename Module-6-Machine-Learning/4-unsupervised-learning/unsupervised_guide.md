# 📘 Unsupervised Learning: Quick Reference Guide

## 🎯 Cheat Sheet

Ushbu qo'llanma unsupervised learning algoritmlarini tez eslab qolish va qo'llash uchun.

---

# 1️⃣ K-means Clustering

## 🔑 Asosiy Konsept
Ma'lumotlarni **K ta klasterga** ajratish. Har bir nuqta eng yaqin centroid'ga tegishli.

## 📐 Formula
**Objective (minimize)**:
$$J = \sum_{k=1}^{K} \sum_{x_i \in C_k} ||x_i - \mu_k||^2$$

## 💻 Kod Template

```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# 1. Data Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Optimal K (Elbow Method)
inertias = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertias.append(kmeans.inertia_)

# Plot elbow
plt.plot(range(2, 11), inertias, 'bo-')
plt.xlabel('K')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# 3. K-means Clustering
optimal_k = 3  # elbow'dan tanlang
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

# 4. Evaluation
sil_score = silhouette_score(X_scaled, labels)
print(f"Silhouette Score: {sil_score:.4f}")

# 5. Visualization
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=300, marker='X', c='red', edgecolors='black', linewidths=2)
plt.title(f'K-means (K={optimal_k})')
plt.show()
```

## ✅ Qachon Ishlatish
- ✅ Spherical (dumaloq) klasterlar
- ✅ Tez natija kerak
- ✅ Katta dataset
- ✅ K taxminan ma'lum

## ❌ Qachon Ishlatmaslik
- ❌ Non-spherical shakl (moons, circles)
- ❌ Turli o'lchamdagi klasterlar
- ❌ Ko'p outlier'lar
- ❌ K noma'lum va topish qiyin

## 🎛️ Parameters
- `n_clusters`: K (klasterlar soni)
- `init`: 'k-means++' (default, yaxshi), 'random'
- `n_init`: Random initialization soni (10+ tavsiya)
- `max_iter`: Maksimal iteratsiya (300 default)
- `random_state`: Reproducibility uchun

---

# 2️⃣ Hierarchical Clustering

## 🔑 Asosiy Konsept
**Daraxtsimon klasterlash**. K tanlash shart emas - dendrogram'dan ko'rib tanlanadi.

## 📐 Linkage Methods

| Method | Formula | Xususiyat |
|--------|---------|-----------|
| **Single** | $d(C_1, C_2) = \min_{x \in C_1, y \in C_2} d(x,y)$ | Chaining, har xil shakl |
| **Complete** | $d(C_1, C_2) = \max_{x \in C_1, y \in C_2} d(x,y)$ | Compact, outlier'ga sezgir |
| **Average** | $d(C_1, C_2) = \frac{1}{\|C_1\| \|C_2\|} \sum d(x,y)$ | Balans, hisoblash qimmat |
| **Ward** ⭐ | Inertia minimal oshirish | Eng yaxshi, balanced |

## 💻 Kod Template

```python
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

# 1. Data Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Dendrogram (Ward linkage)
linkage_mat = linkage(X_scaled, method='ward')

plt.figure(figsize=(12, 6))
dendrogram(linkage_mat, labels=labels, leaf_font_size=8)
plt.xlabel('Sample')
plt.ylabel('Distance')
plt.title('Dendrogram (Ward Linkage)')
plt.axhline(y=10, color='red', linestyle='--', label='Cut')
plt.legend()
plt.show()

# 3. Hierarchical Clustering
n_clusters = 3  # dendrogram'dan tanlang
hier = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
labels = hier.fit_predict(X_scaled)

# 4. Evaluation
sil_score = silhouette_score(X_scaled, labels)
print(f"Silhouette Score: {sil_score:.4f}")

# 5. Visualization
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap='viridis')
plt.title(f'Hierarchical Clustering (K={n_clusters})')
plt.show()
```

## ✅ Qachon Ishlatish
- ✅ K noma'lum
- ✅ Hierarchical structure muhim
- ✅ Kichik dataset (< 1000 samples)
- ✅ Har xil shakldagi klasterlar

## ❌ Qachon Ishlatmaslik
- ❌ Katta dataset (> 10,000 samples)
- ❌ Real-time clustering
- ❌ Tez natija kerak

## 🎛️ Parameters
- `n_clusters`: Klasterlar soni
- `linkage`: 'ward' (tavsiya), 'complete', 'average', 'single'
- `metric`: 'euclidean' (default), 'manhattan', 'cosine'

---

# 3️⃣ PCA (Principal Component Analysis)

## 🔑 Asosiy Konsept
**Dimensionality Reduction**: n-D → k-D. Maksimal variance saqlab, kamroq feature'larga aylantirish.

## 📐 Asosiy Formulalar

**Standardization**:
$$z = \frac{x - \mu}{\sigma}$$

**Covariance Matrix**:
$$\Sigma = \frac{1}{n-1} X^T X$$

**Eigenvalue/Eigenvector**:
$$\Sigma v = \lambda v$$

**Transform**:
$$X_{new} = X \cdot V$$

## 💻 Kod Template

```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Data Preprocessing (MUHIM!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. PCA: n-D → 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# 3. Explained Variance
print(f"PC1 variance: {pca.explained_variance_ratio_[0]:.2%}")
print(f"PC2 variance: {pca.explained_variance_ratio_[1]:.2%}")
print(f"Total: {pca.explained_variance_ratio_.sum():.2%}")

# 4. Visualization
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.1%})')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.1%})')
plt.title('PCA 2D Projection')
plt.colorbar(label='Target')
plt.show()
```

## 📊 Scree Plot (Optimal n_components)

```python
# Barcha PC'larni hisoblash
pca_all = PCA()
pca_all.fit(X_scaled)

exp_var = pca_all.explained_variance_ratio_
cum_var = np.cumsum(exp_var)

# Plot
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Individual variance
axes[0].bar(range(1, len(exp_var)+1), exp_var, alpha=0.7)
axes[0].plot(range(1, len(exp_var)+1), exp_var, 'ro-')
axes[0].set_xlabel('PC')
axes[0].set_ylabel('Explained Variance')
axes[0].set_title('Scree Plot')

# Cumulative variance
axes[1].plot(range(1, len(cum_var)+1), cum_var, 'bo-')
axes[1].axhline(y=0.95, color='red', linestyle='--', label='95%')
axes[1].set_xlabel('Number of PCs')
axes[1].set_ylabel('Cumulative Variance')
axes[1].set_title('Cumulative Variance')
axes[1].legend()

plt.show()

# Optimal n_components (95% variance)
n_components_95 = np.argmax(cum_var >= 0.95) + 1
print(f"95% variance uchun {n_components_95} PC kerak")
```

## ✅ Qachon Ishlatish
- ✅ Visualization (n-D → 2D/3D)
- ✅ Ko'p feature'lar (curse of dimensionality)
- ✅ Correlated features
- ✅ Noise reduction
- ✅ Storage/speed optimization

## ❌ Qachon Ishlatmaslik
- ❌ Feature interpretation muhim
- ❌ Non-linear relationships (t-SNE ishlatish kerak)
- ❌ Kam feature'lar zaten

## 🎛️ Parameters
- `n_components`: Nechta PC kerak (int yoki 0.95 variance uchun 0.95)
- `whiten`: False (default), True (variance=1 qilish)
- `svd_solver`: 'auto' (default), 'full', 'randomized'

---

# 🔄 Comparison Table

| **Xususiyat** | **K-means** | **Hierarchical** | **PCA** |
|---------------|-------------|------------------|---------|
| **Turi** | Clustering | Clustering | Dim. Reduction |
| **Supervised?** | ❌ | ❌ | ❌ |
| **K tanlash** | ✅ Kerak | ❌ Kerak emas | n_components |
| **Hisoblash** | O(nkt) - Tez ⚡ | O(n²) - Sekin 🐌 | O(min(n³,p³)) - O'rtacha |
| **Scalability** | Katta ✅ | Kichik ⚠️ | Katta ✅ |
| **Shape** | Spherical ⚠️ | Har xil ✅ | - |
| **Outliers** | Sezgir ⚠️ | Kam sezgir ✅ | Kam sezgir ✅ |
| **Visualization** | Scatter | Dendrogram | PC1 vs PC2 |
| **Interpretability** | O'rtacha | Yaxshi ✅ | Qiyin ⚠️ |
| **Best Use** | Customer seg | Taxonomy | Visualization |

Bu yerda:
- n = samples soni
- p = features soni
- k = clusters soni
- t = iterations

---

# 📊 Metrics Cheat Sheet

## 1. Inertia (Within-Cluster Sum of Squares - WCSS)
**Formula**:
$$WCSS = \sum_{k=1}^{K} \sum_{x_i \in C_k} ||x_i - \mu_k||^2$$

**Qachon**: K-means uchun, Elbow Method

**Qiymati**: Kichik = yaxshi

```python
inertia = kmeans.inertia_
```

## 2. Silhouette Score
**Formula**:
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$$

Bu yerda:
- $a(i)$ - o'z klasteridagi o'rtacha masofa
- $b(i)$ - eng yaqin boshqa klasterdagi o'rtacha masofa

**Qiymati**:
- **1**: Perfect
- **0**: Klaster chegarasida
- **-1**: Noto'g'ri klaster

```python
from sklearn.metrics import silhouette_score
sil_score = silhouette_score(X, labels)
```

## 3. Explained Variance Ratio (PCA)
**Formula**:
$$\text{Explained Variance Ratio} = \frac{\lambda_i}{\sum_{j=1}^{p} \lambda_j}$$

**Qiymati**: 0.8-0.95 (80-95%) yaxshi

```python
exp_var = pca.explained_variance_ratio_
cum_var = np.cumsum(exp_var)
```

---

# 🛠️ Common Workflows

## Workflow 1: Customer Segmentation

```python
# 1. Load Data
df = pd.read_csv('customers.csv')

# 2. Feature Selection
X = df[['age', 'income', 'spending']].values

# 3. Preprocessing
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Optimal K (Elbow + Silhouette)
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

inertias, silhouettes = [], []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    inertias.append(kmeans.inertia_)
    silhouettes.append(silhouette_score(X_scaled, labels))

# Plot
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(K_range, inertias, 'bo-')
axes[0].set_title('Elbow Method')
axes[1].plot(K_range, silhouettes, 'ro-')
axes[1].set_title('Silhouette Score')
plt.show()

# 5. Final Clustering
optimal_k = 4  # elbow'dan
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# 6. Analysis
cluster_stats = df.groupby('Cluster').mean()
print(cluster_stats)
```

---

## Workflow 2: High-Dimensional Data Visualization

```python
# 1. Load Data
from sklearn.datasets import load_digits
digits = load_digits()
X = digits.data  # 64 features
y = digits.target  # labels

# 2. Standardization
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. PCA: 64D → 2D
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Explained variance: {pca.explained_variance_ratio_.sum():.2%}")

# 4. Visualization
plt.figure(figsize=(10, 7))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='tab10')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Digits Dataset - PCA 2D')
plt.colorbar(scatter, label='Digit')
plt.show()

# 5. Clustering (optional)
kmeans = KMeans(n_clusters=10, random_state=42)
clusters = kmeans.fit_predict(X_pca)

# Compare
from sklearn.metrics import adjusted_rand_score
ari = adjusted_rand_score(y, clusters)
print(f"Adjusted Rand Index: {ari:.4f}")
```

---

## Workflow 3: Hierarchical Clustering with Dendrogram

```python
# 1. Load & Preprocess
X_scaled = StandardScaler().fit_transform(X)

# 2. Linkage Matrix
from scipy.cluster.hierarchy import dendrogram, linkage
linkage_mat = linkage(X_scaled, method='ward')

# 3. Dendrogram
plt.figure(figsize=(12, 6))
dendrogram(linkage_mat, labels=sample_labels)
plt.xlabel('Sample')
plt.ylabel('Distance')
plt.title('Hierarchical Clustering - Dendrogram')
plt.axhline(y=threshold, color='red', linestyle='--')
plt.show()

# 4. Clustering
from sklearn.cluster import AgglomerativeClustering
n_clusters = 3  # dendrogram'dan
hier = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
labels = hier.fit_predict(X_scaled)

# 5. Visualization (PCA 2D)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis')
plt.title(f'Hierarchical Clustering (K={n_clusters})')
plt.show()
```

---

# ⚠️ Common Mistakes

## 1. Standardization Unutish
```python
# ❌ NOTO'G'RI
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)  # Scaled emas!

# ✅ TO'G'RI
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X_scaled)
```

## 2. Random State Bermaslik
```python
# ❌ NOTO'G'RI (har safar turli natija)
kmeans = KMeans(n_clusters=3)

# ✅ TO'G'RI (reproducible)
kmeans = KMeans(n_clusters=3, random_state=42)
```

## 3. Elbow Method'siz K Tanlash
```python
# ❌ NOTO'G'RI (K random)
kmeans = KMeans(n_clusters=5)  # Nega 5?

# ✅ TO'G'RI (Elbow Method bilan)
# ... elbow method code ...
optimal_k = 3  # elbow'dan
kmeans = KMeans(n_clusters=optimal_k)
```

## 4. PCA'da Standardization Unutish
```python
# ❌ NOTO'G'RI (katta scale feature dominate qiladi)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# ✅ TO'G'RI
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

## 5. Low Explained Variance (PCA)
```python
# ❌ NOTO'G'RI (faqat 40% variance)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
# Explained variance: 0.40 (kam!)

# ✅ TO'G'RI (80%+ variance)
pca = PCA(n_components=10)  # ko'proq PC
# yoki
pca = PCA(n_components=0.95)  # 95% variance
```

---

# 🧪 Testing & Debugging

## Tekshirish Ro'yxati (Checklist)

### K-means:
- [ ] Data standardized?
- [ ] Elbow Method qildingizmi?
- [ ] Silhouette Score yaxshimi? (>0.5)
- [ ] Klasterlar ma'noli?
- [ ] Outlier'lar bor-mi?

### Hierarchical:
- [ ] Data standardized?
- [ ] Dendrogram chizilganmi?
- [ ] Linkage method to'g'rimi?
- [ ] Dataset kichikmi? (<1000)
- [ ] Silhouette Score yaxshimi?

### PCA:
- [ ] Data standardized? (MUHIM!)
- [ ] Explained variance yetarlimi? (>80%)
- [ ] Scree plot ko'rilganmi?
- [ ] n_components optimal?
- [ ] Interpretation qiyin emas-mi?

---

# 📚 Quick Reference Commands

## Import Statements
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import dendrogram, linkage
```

## Standardization
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

## K-means (One-liner)
```python
labels = KMeans(n_clusters=3, random_state=42, n_init=10).fit_predict(X_scaled)
```

## Hierarchical (One-liner)
```python
labels = AgglomerativeClustering(n_clusters=3, linkage='ward').fit_predict(X_scaled)
```

## PCA (One-liner)
```python
X_pca = PCA(n_components=2).fit_transform(X_scaled)
```

## Silhouette Score (One-liner)
```python
sil = silhouette_score(X_scaled, labels)
```

---

# 🎓 Final Tips

## Do's ✅
1. **DOIM standardize qiling** - StandardScaler
2. **Elbow Method** - optimal K uchun
3. **Silhouette Score** - evaluation uchun
4. **Visualization** - natijalarni ko'ring
5. **Interpretation** - klasterlar ma'noli bo'lishi kerak
6. **Multiple runs** - random_state turli bo'lsin
7. **Domain knowledge** - feature selection uchun

## Don'ts ❌
1. **Standardization'siz** - clustering/PCA qilmaslik
2. **Random K** - Elbow Method'siz tanlash
3. **Outliers ignore** - outlier'larni e'tiborsiz qoldirish
4. **Low variance PCA** - <80% variance bilan ishlash
5. **Overfit** - juda ko'p klaster
6. **No validation** - silhouette score tekshirmaslik
7. **Blindly trust** - natijalarni tahlil qilmaslik

---

# 📖 Further Reading

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Towards Data Science - Clustering](https://towardsdatascience.com/tagged/clustering)
- [StatQuest - PCA](https://www.youtube.com/watch?v=FgakZw6K1QQ)
- [K-means Visualization](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/)

---

# ✅ End of Guide

Bu qo'llanma unsupervised learning'ning asosiy qismlarini qamrab oladi. Real loyihalarda qo'llang va tajriba orttiring!

**Good luck! 🚀**
