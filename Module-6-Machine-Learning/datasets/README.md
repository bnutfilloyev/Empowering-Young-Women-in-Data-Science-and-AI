# Machine Learning Datasets

Bu papkada turli ML vazifalar uchun datasetlar saqlanadi.

## Dataset Manbalari

### 1. Scikit-learn Built-in Datasets
```python
from sklearn.datasets import (
    load_iris,           # Classification
    load_digits,         # Multi-class classification
    load_wine,           # Classification/Clustering
    load_breast_cancer,  # Binary classification
    fetch_california_housing,  # Regression
    load_diabetes,       # Regression
    make_classification, # Synthetic classification data
    make_regression,     # Synthetic regression data
    make_blobs          # Synthetic clustering data
)
```

### 2. Seaborn Datasets
```python
import seaborn as sns

# Available datasets
sns.load_dataset('titanic')
sns.load_dataset('tips')
sns.load_dataset('iris')
sns.load_dataset('diamonds')
sns.load_dataset('mpg')
```

### 3. Kaggle
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- Download qilish uchun:
  ```bash
  kaggle datasets download -d [dataset-name]
  ```

### 4. UCI Machine Learning Repository
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)

### 5. Google Dataset Search
- [Dataset Search](https://datasetsearch.research.google.com/)

## Dataset Turlari

### Classification
- Iris Dataset - 3 class flower classification
- Breast Cancer - Binary classification
- Digits - Handwritten digit recognition (0-9)
- Wine - Wine quality classification

### Regression
- California Housing - House price prediction
- Diabetes - Disease progression
- Boston Housing - House price (deprecated, use California)

### Clustering
- Mall Customers
- Customer Segmentation
- Synthetic blobs data

## Dataset Yuklash Misollari

### Misol 1: Scikit-learn
```python
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
```

### Misol 2: CSV dan
```python
import pandas as pd
df = pd.read_csv('datasets/your_data.csv')
```

### Misol 3: Kaggle API
```python
# Install: pip install kaggle
# Setup: ~/.kaggle/kaggle.json
import kaggle
kaggle.api.dataset_download_files('dataset-name', path='datasets/', unzip=True)
```

## Dataset Hajmi Bo'yicha Tavsiyalar

- **O'rganish uchun:** 100-10,000 qator
- **Amaliy proyekt:** 10,000-100,000 qator
- **Katta dataset:** 100,000+ qator (Cloud yoki powerful PC kerak)

## Dataset Sifati

Yaxshi dataset:
✅ Yetarli miqdorda ma'lumot
✅ Kam null qiymatlar
✅ Balanced classes (classification uchun)
✅ Relevant features
✅ Clean data

Muammoli dataset:
❌ Juda kam ma'lumot
❌ Ko'p null/missing values
❌ Imbalanced classes
❌ Noisy data
❌ Irrelevant features

## Data Augmentation

Agar ma'lumotlar kam bo'lsa:
- Synthetic data generation
- SMOTE (for imbalanced data)
- Data augmentation techniques
- Web scraping
- API'lardan olish
