# 🚀 Netflix Tavsiya Tizimi - Deployment Qo'llanmasi

Bu qo'llanma loyihani lokal va cloudda ishga tushirish uchun.

---

## 📋 Talablar

### Python kutubxonalari:
```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy streamlit
```

Yoki:
```bash
pip install -r requirements.txt
```

---

## 🏃 Lokal ishga tushirish

### 1. Ma'lumotlarni tayyorlash

Avval datasetlarni yuklab oling:
```bash
cd Module-6-Machine-Learning/8-ml-project-case-study/datasets
bash download_data.sh
```

### 2. Modelni o'qitish

Jupyter notebookni ishga tushiring:
```bash
cd ../notebooks
jupyter notebook netflix_recommendation_system.ipynb
```

Yoki:
```bash
jupyter lab netflix_recommendation_system.ipynb
```

**Muhim:** Barcha celllarni ketma-ket ishga tushiring (Cell → Run All)

### 3. Streamlit ilovasini ishga tushirish

Terminal ochib quyidagini yozing:
```bash
cd notebooks
streamlit run streamlit_app.py
```

Brauzerda avtomatik ochiladi: `http://localhost:8501`

---

## 🌐 Cloud Deployment

### A) Streamlit Cloud (Eng oson)

1. **GitHub repositoriyaga yuklash:**
```bash
git add .
git commit -m "Netflix recommendation system"
git push origin main
```

2. **Streamlit Cloud:**
   - https://streamlit.io/cloud ga kiring
   - "New app" bosing
   - Repository tanlang
   - File path: `notebooks/streamlit_app.py`
   - Deploy!

**Vaqt:** 5 daqiqa

---

### B) Heroku Deployment

1. **Heroku account yaratish:**
   - https://heroku.com
   - Bepul account

2. **Heroku CLI o'rnatish:**
```bash
# macOS
brew tap heroku/brew && brew install heroku

# Linux
curl https://cli-assets.heroku.com/install.sh | sh
```

3. **Fayllarni tayyorlash:**

`Procfile` yaratish:
```
web: streamlit run notebooks/streamlit_app.py --server.port=$PORT
```

`runtime.txt` yaratish:
```
python-3.9.16
```

`requirements.txt` yaratish:
```
numpy==1.24.3
pandas==2.0.3
matplotlib==3.7.2
seaborn==0.12.2
scikit-learn==1.3.0
scipy==1.11.1
streamlit==1.25.0
```

4. **Deploy:**
```bash
heroku login
heroku create netflix-recommender-app
git push heroku main
heroku open
```

**Vaqt:** 10-15 daqiqa

---

### C) Docker Container

1. **Dockerfile yaratish:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "notebooks/streamlit_app.py", "--server.port=8501"]
```

2. **Build va Run:**
```bash
# Build
docker build -t netflix-recommender .

# Run
docker run -p 8501:8501 netflix-recommender
```

3. **Docker Hub ga yuklash:**
```bash
docker tag netflix-recommender yourusername/netflix-recommender
docker push yourusername/netflix-recommender
```

**Vaqt:** 15-20 daqiqa

---

### D) AWS EC2 Deployment

1. **EC2 instance yaratish:**
   - AWS Console → EC2
   - Launch Instance
   - Ubuntu 22.04 LTS
   - t2.micro (bepul tier)
   - Security Group: Port 8501 ochiq

2. **SSH orqali kirish:**
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

3. **Server sozlash:**
```bash
# Python o'rnatish
sudo apt update
sudo apt install python3-pip git

# Loyihani klonlash
git clone your-repo-url
cd your-repo

# Kutubxonalar
pip3 install -r requirements.txt

# Streamlit ishga tushirish (background)
nohup streamlit run notebooks/streamlit_app.py --server.port=8501 &
```

4. **Kirish:**
```
http://your-ec2-ip:8501
```

**Vaqt:** 20-30 daqiqa

---

## 🔧 Muammolarni Bartaraf Etish

### 1. Model yuklanmadi
```
⚠️ Modellar yuklanmadi!
```

**Yechim:**
- `netflix_recommendation_system.ipynb` ni to'liq ishga tushiring
- `../models/` papkasida `.pkl` fayllar borligini tekshiring

### 2. Dataset topilmadi
```
FileNotFoundError: ml-1m/movies.dat
```

**Yechim:**
```bash
cd datasets
bash download_data.sh
```

### 3. Memory xatosi
```
MemoryError
```

**Yechim:**
- Notebookda `MIN_RATINGS = 100` qiling (filmlar sonini kamaytiradi)
- SVD'da `k = 20` qiling (latent faktorlar)

### 4. Streamlit port band
```
Address already in use
```

**Yechim:**
```bash
streamlit run streamlit_app.py --server.port=8502
```

---

## 📊 Performance Optimization

### 1. Caching
Streamlit `@st.cache_resource` ishlatilgan - modellar faqat 1 marta yuklanadi.

### 2. Model Size
Agar modellar katta bo'lsa:
```python
# Faqat kerakli qismini saqlash
pickle.dump(cosine_sim[:1000, :1000], f)
```

### 3. Dataset
Katta datasetda:
- Faqat mashgur filmlarni oling
- Chunking ishlatib qismma-qism yuklang

---

## 🎨 Customization

### Logo qo'shish:
```python
st.image("logo.png", width=200)
```

### Theme:
`.streamlit/config.toml` yaratish:
```toml
[theme]
primaryColor="#E50914"
backgroundColor="#141414"
secondaryBackgroundColor="#1f1f1f"
textColor="#ffffff"
```

### Domain:
Streamlit Cloud/Heroku'da custom domain qo'shish mumkin.

---

## 📈 Monitoring

### Streamlit Analytics:
- Streamlit Cloud dashboard'da built-in analytics

### Custom:
```python
import logging
logging.info(f"User {user_id} requested recommendations")
```

---

## 🔐 Security

### 1. API Key (agar kerak bo'lsa):
```python
API_KEY = st.secrets["api_key"]
```

### 2. User authentication:
```python
import streamlit_authenticator as stauth
```

### 3. Rate limiting:
```python
from streamlit_server_state import server_state
```

---

## 📝 Production Checklist

- [ ] Dataset yuklab olingan
- [ ] Model o'qitilgan (`.pkl` fayllar mavjud)
- [ ] `requirements.txt` to'liq
- [ ] Error handling qo'shilgan
- [ ] Loading indicators mavjud
- [ ] README.md yozilgan
- [ ] GitHub'ga yuklangan
- [ ] Cloud platformada test qilingan
- [ ] Custom domain sozlangan (optional)
- [ ] Analytics sozlangan (optional)

---

## 🎉 Tayyor!

Sizning Netflix tavsiya tizimingiz endi ishlaydi!

**Demo:** http://your-app-url.streamlit.app

---

## 🆘 Yordam

Muammo bo'lsa:
1. GitHub Issues
2. Streamlit Community Forum
3. Stack Overflow

---

**Muvaffaqiyatlar!** 🚀
