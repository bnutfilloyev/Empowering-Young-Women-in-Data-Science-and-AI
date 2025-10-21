# 1-dars: Machine Learningga Kirish

## Mavzu maqsadi
Bu darsda siz Machine Learning asoslari, uning turlari va real hayotdagi qo'llanilishi bilan tanishasiz.

## O'rganilayotgan mavzular

### 1. Machine Learning nima?
- Aniq ta'rif va tushuncha
- An'anaviy dasturlash vs Machine Learning
- ML nima uchun muhim?

### 2. Machine Learning turlari

#### Supervised Learning (Nazorat ostida o'qitish)
- Ma'lumotlar belgilangan (labeled data)
- Kiruvchi va chiquvchi o'rtasida bog'liqlik o'rganiladi
- Klassifikatsiya va Regressiya

#### Unsupervised Learning (Nazorat-siz o'qitish)
- Ma'lumotlar belgisiz (unlabeled data)
- Ma'lumotlardagi naqsh va tuzilmalarni topish
- Clustering va Dimensionality Reduction

#### Reinforcement Learning (Mustahkamlovchi o'qitish)
- Agent muhitda harakatlar qiladi
- Mukofot va jazo orqali o'rganadi
- O'yin, robotika, avtomatlashtirishda qo'llaniladi

### 3. ML Workflow
1. Problem aniqlash
2. Ma'lumotlarni to'plash
3. Ma'lumotlarni tayyorlash
4. Model tanlash
5. Model o'qitish
6. Model baholash
7. Model sozlash
8. Deployment

## Fayllar
- `lecture.ipynb` - Nazariy ma'lumotlar va misollar
- `practical.ipynb` - Amaliy mashg'ulotlar
- `homework.md` - Uy vazifasi

## Kerakli kutubxonalar
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
```

## Qo'shimcha manbalar
- [Scikit-learn Tutorial](https://scikit-learn.org/stable/tutorial/index.html)
- [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
- [Andrew Ng's Machine Learning Course](https://www.coursera.org/learn/machine-learning)
