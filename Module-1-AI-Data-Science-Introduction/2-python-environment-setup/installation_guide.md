# 🔧 Python va Data Science Muhitini O'rnatish

**Maqsad:** Barcha zarur dasturlarni o'rnatib, to'liq ishga tayyor muhit yaratish

---

## 🖥️ Tizim Talablari

### Minimal talablar:
- **RAM:** 4GB (8GB tavsiya etiladi)
- **Storage:** 5GB bo'sh joy
- **OS:** Windows 10+, macOS 10.12+, Ubuntu 18.04+
- **Internet:** O'rnatish uchun turg'un ulanish

---

## 📥 1. Python O'rnatish

### Variant 1: Anaconda (Tavsiya etiladi) 🌟

**Nima uchun Anaconda?**
- Python + 250+ data science paketi
- Jupyter Notebook built-in
- Package management oson
- Cross-platform

#### Windows uchun:
```bash
# 1. https://anaconda.com/products/distribution ga o'ting
# 2. "Download" tugmasini bosing
# 3. Windows 64-bit installer yuklab oling
# 4. .exe faylni ishga tushiring
# 5. "Add Anaconda to PATH" ni belgilang
# 6. O'rnatish tugaganidan keyin Command Prompt ochib test qiling:

conda --version
python --version
```

#### macOS uchun:
```bash
# 1. https://anaconda.com/products/distribution ga o'ting
# 2. macOS installer yuklab oling  
# 3. .pkg faylni ishga tushiring
# 4. Terminal ochib test qiling:

conda --version
python --version
```

#### Linux (Ubuntu) uchun:
```bash
# 1. Terminal oching
# 2. Wget bilan installer yuklab oling:
wget https://repo.anaconda.com/archive/Anaconda3-2023.07-Linux-x86_64.sh

# 3. O'rnatishni boshlang:
bash Anaconda3-2023.07-Linux-x86_64.sh

# 4. Terminal'ni qayta oching va test qiling:
conda --version
python --version
```

### Variant 2: Python.org dan oddiy o'rnatish

Agar Anaconda'da muammo bo'lsa:

1. https://python.org/downloads ga o'ting
2. Eng yangi versiyani yuklab oling (Python 3.9+)
3. O'rnatish jarayonida "Add to PATH" ni belgilang
4. Pip orqali qo'shimcha paketlar o'rnating

---

## 🔧 2. Code Editor O'rnatish

### Variant 1: VS Code (Tavsiya etiladi) 🌟

```bash
# 1. https://code.visualstudio.com ga o'ting
# 2. OS'ingizga mos versiyani yuklab oling
# 3. O'rnating va oching
# 4. Quyidagi extension'larni o'rnating:

# Zarur extension'lar:
- Python (Microsoft)
- Jupyter (Microsoft)  
- Python Docstring Generator
- GitLens
- Bracket Pair Colorizer
```

**VS Code Python sozlash:**
```json
// settings.json ga qo'shing:
{
    "python.defaultInterpreterPath": "/path/to/anaconda/python",
    "jupyter.askForKernelRestart": false,
    "python.formatting.provider": "black"
}
```

### Variant 2: PyCharm Community

```bash
# 1. https://jetbrains.com/pycharm ga o'ting
# 2. Community Edition (bepul) yuklab oling
# 3. O'rnating va Python interpreter'ni sozlang
```

---

## 📓 3. Jupyter Notebook Sozlash

### Anaconda bilan (avtomatik):
```bash
# Terminal/Command Prompt da:
jupyter notebook

# Yoki Jupyter Lab (zamonaviyroq):
jupyter lab
```

### Oddiy Python bilan:
```bash
# Pip orqali o'rnating:
pip install jupyter notebook

# Ishga tushiring:
jupyter notebook
```

### Jupyter Extensions o'rnatish:
```bash
# Foydali extension'lar:
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user

# Variable inspector:
pip install lckr-jupyterlab-variableinspector
```

---

## 📦 4. Data Science Kutubxonalari

### Asosiy paketlar ro'yxati:

```bash
# Anaconda bilan (ko'pchiligi allaqachon o'rnatilgan):
conda install numpy pandas matplotlib seaborn scikit-learn

# Pip bilan:
pip install numpy pandas matplotlib seaborn scikit-learn
```

### To'liq ro'yxat:
```bash
# Ma'lumotlar bilan ishlash:
numpy>=1.21.0          # Numerical computing
pandas>=1.3.0          # Data manipulation
scipy>=1.7.0           # Scientific computing

# Vizualizatsiya:
matplotlib>=3.4.0      # Basic plotting
seaborn>=0.11.0        # Statistical plotting
plotly>=5.0.0          # Interactive plots

# Machine Learning:
scikit-learn>=1.0.0    # ML algorithms
tensorflow>=2.6.0      # Deep learning
torch>=1.9.0          # PyTorch (optional)

# Jupyter:
jupyter>=1.0.0         # Notebook environment
ipywidgets>=7.6.0      # Interactive widgets

# Utilities:
requests>=2.25.0       # HTTP library
beautifulsoup4>=4.9.0  # Web scraping
openpyxl>=3.0.0        # Excel files
```

### requirements.txt yaratish:
```bash
# Loyiha papkasida requirements.txt yarating:
numpy==1.21.0
pandas==1.3.3
matplotlib==3.4.3
seaborn==0.11.2
scikit-learn==1.0.2
jupyter==1.0.0

# O'rnatish:
pip install -r requirements.txt
```

---

## 🔄 5. Git va GitHub

### Git o'rnatish:

#### Windows:
```bash
# https://git-scm.com/download/win dan yuklab oling
# Git Bash ham o'rnatiladi
```

#### macOS:
```bash
# Homebrew bilan:
brew install git

# Yoki Xcode command line tools:
xcode-select --install
```

#### Linux:
```bash
# Ubuntu/Debian:
sudo apt-get install git

# CentOS/RHEL:
sudo yum install git
```

### Git sozlash:
```bash
# Global settings:
git config --global user.name "Ismingiz"
git config --global user.email "email@example.com"

# VS Code'ni default editor qilish:
git config --global core.editor "code --wait"
```

### GitHub account:
1. https://github.com ga o'ting
2. Account yarating (bepul)
3. Personal Access Token yarating
4. SSH key sozlang (optional, lekin tavsiya etiladi)

---

## ✅ 6. Muhit Test Qilish

### Test script (test_environment.py):
```python
print("🔄 Python muhitini tekshirish...")

# Python version
import sys
print(f"Python version: {sys.version}")

# Asosiy kutubxonalar
try:
    import numpy as np
    print(f"✅ NumPy {np.__version__}")
except ImportError:
    print("❌ NumPy topilmadi")

try:
    import pandas as pd
    print(f"✅ Pandas {pd.__version__}")
except ImportError:
    print("❌ Pandas topilmadi")

try:
    import matplotlib.pyplot as plt
    print("✅ Matplotlib topildi")
except ImportError:
    print("❌ Matplotlib topilmadi")

try:
    import seaborn as sns
    print(f"✅ Seaborn {sns.__version__}")
except ImportError:
    print("❌ Seaborn topilmadi")

try:
    import sklearn
    print(f"✅ Scikit-learn {sklearn.__version__}")
except ImportError:
    print("❌ Scikit-learn topilmadi")

try:
    import jupyter
    print("✅ Jupyter topildi")
except ImportError:
    print("❌ Jupyter topilmadi")

print("\\n🎉 Muhit tayyor!" if all([
    'numpy' in sys.modules,
    'pandas' in sys.modules, 
    'matplotlib' in sys.modules
]) else "\\n⚠️ Ba'zi kutubxonalar etishmayapti")
```

### Terminal'da test:
```bash
# Python ishlayaptimi?
python --version

# Pip ishlayaptimi?
pip --version

# Jupyter ishlayaptimi?
jupyter --version

# Git ishlayaptimi?
git --version
```

---

## 🆘 Muammolarni Hal Qilish

### Tez-tez uchraydigan muammolar:

#### 1. "Python not found" xatosi:
```bash
# Windows'da PATH'ga qo'shing:
# Control Panel > System > Advanced > Environment Variables
# PATH ga Python papkasini qo'shing

# macOS/Linux'da:
echo 'export PATH="/path/to/python:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

#### 2. "Permission denied" pip da:
```bash
# --user flag ishlating:
pip install --user package_name

# Yoki virtual environment yarating:
python -m venv myenv
source myenv/bin/activate  # Linux/macOS
myenv\\Scripts\\activate     # Windows
```

#### 3. Jupyter ochilmayapti:
```bash
# Browser'ni manual ko'rsating:
jupyter notebook --browser=chrome

# Port o'zgartiring:
jupyter notebook --port=8889
```

#### 4. Package install qilishda xato:
```bash
# Pip'ni yangilang:
pip install --upgrade pip

# Alternative repository:
pip install -i https://pypi.org/simple/ package_name

# Conda bilan sinab ko'ring:
conda install package_name
```

---

## 📱 Qo'shimcha Tools (Optional)

### Data Science uchun foydali tools:

#### 1. Anaconda Navigator:
- GUI orqali package management
- Jupyter, Spyder, VS Code launch

#### 2. Google Colab:
- Cloud-based Jupyter notebooks
- Free GPU access
- No installation required

#### 3. Docker:
- Consistent environment
- Easy deployment
- Version control

#### 4. Postman:
- API testing
- Data source testing

---

## 🎯 Keyingi Qadamlar

### Muhit tayyor bo'lgandan keyin:

1. **test_environment.py** ni ishga tushiring
2. **environment_test.ipynb** ni oching
3. Birinchi Jupyter notebook yarating
4. GitHub repository yarating
5. **python_basics.ipynb** bilan ishlashni boshlang

---

## 📞 Yordam

### Muammo bo'lsa:
- **Class Telegram group**'ga yozing
- **Office hours**'da keling
- **StackOverflow**'da qidiring
- **Documentation**'lar o'qing

### Foydali linklar:
- [Python.org documentation](https://docs.python.org)
- [Anaconda documentation](https://docs.anaconda.com)
- [Jupyter documentation](https://jupyter.org/documentation)
- [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)

---

**🎉 Tabriklaymiz! Python muhitingiz tayyor!**
