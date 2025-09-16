# 🐘 PostgreSQL O'rnatish va Sozlash Qo'llanmasi

## 🎯 Maqsad
PostgreSQL ma'lumotlar bazasini o'rnatish, sozlash va Python bilan ulanishni ta'minlash.

---

## 🖥️ Operatsion Tizimlarga Qarashli O'rnatish

### 🍎 **macOS uchun PostgreSQL**

#### 1-usul: Homebrew orqali (Tavsiya etiladi)
```bash
# Homebrew o'rnatilganini tekshiring
brew --version

# PostgreSQL o'rnatish
brew install postgresql

# PostgreSQL xizmatini ishga tushirish
brew services start postgresql

# PostgreSQL versiyasini tekshiring
psql --version
```

#### 2-usul: Postgres.app orqali
```bash
# https://postgresapp.com saytidan yuklab oling
# .dmg faylni ochib, Applications papkasiga o'tkazing
# Postgres.app ni ishga tushiring
```

#### 3-usul: Rasmiy installer
```bash
# https://www.postgresql.org/download/macosx/ dan yuklab oling
# .pkg faylni ishga tushiring va ko'rsatmalarga amal qiling
```

### 🐧 **Linux (Ubuntu/Debian) uchun PostgreSQL**

```bash
# Paketlar ro'yxatini yangilash
sudo apt update

# PostgreSQL o'rnatish
sudo apt install postgresql postgresql-contrib

# PostgreSQL xizmatini ishga tushirish
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Versiyani tekshiring
psql --version

# postgres foydalanuvchi sifatida kirish
sudo -u postgres psql
```

### 🪟 **Windows uchun PostgreSQL**

```powershell
# 1. https://www.postgresql.org/download/windows/ saytiga kiring
# 2. EnterpriseDB installer yuklab oling
# 3. .exe faylni ishga tushiring
# 4. Installation Wizard ga amal qiling:
#    - Installation directory: C:\Program Files\PostgreSQL\14
#    - Data directory: C:\Program Files\PostgreSQL\14\data
#    - Superuser password: o'zingiz belgilang
#    - Port: 5432 (default)
#    - Locale: [Default locale]

# Command Prompt orqali tekshirish
psql --version
```

---

## ⚙️ Boshlang'ich Sozlash

### 🔐 **PostgreSQL ga Birinchi Ulanish**

#### macOS/Linux:
```bash
# postgres superuser sifatida kirish
sudo -u postgres psql

# yoki to'g'ridan-to'g'ri
psql -U postgres -h localhost
```

#### Windows:
```cmd
# psql ni ishga tushirish
psql -U postgres -h localhost

# yoki pgAdmin 4 dan foydalaning
```

### 👤 **Yangi Foydalanuvchi Yaratish**
```sql
-- PostgreSQL ga kirgandan so'ng
-- Yangi foydalanuvchi yaratish
CREATE USER data_scientist WITH PASSWORD 'secure_password123';

-- Foydalanuvchiga barcha huquqlarni berish
ALTER USER data_scientist CREATEDB;
ALTER USER data_scientist WITH SUPERUSER;

-- Huquqlarni tekshiring
\du
```

### 🗄️ **Yangi Ma'lumotlar Bazasi Yaratish**
```sql
-- Yangi database yaratish
CREATE DATABASE lesson_aggregation 
    OWNER data_scientist
    ENCODING 'UTF8'
    LC_COLLATE 'en_US.UTF-8'
    LC_CTYPE 'en_US.UTF-8';

-- Database ro'yxatini ko'rish
\l

-- Database ga ulanish
\c lesson_aggregation

-- Joriy database va foydalanuvchini ko'rish
SELECT current_database(), current_user;
```

---

## 🐍 Python bilan Ulanish

### 📦 **Kerakli Kutubxonalar O'rnatish**

```bash
# psycopg2 - PostgreSQL adapter
pip install psycopg2-binary

# pandas - ma'lumotlar tahlili uchun
pip install pandas

# sqlalchemy - ORM va database abstraction
pip install sqlalchemy

# jupyter - notebook uchun
pip install jupyter

# matplotlib, seaborn - vizualizatsiya uchun
pip install matplotlib seaborn

# Yoki bitta buyruq bilan hammasi
pip install psycopg2-binary pandas sqlalchemy jupyter matplotlib seaborn
```

### 🔌 **Ulanishni Tekshirish**

```python
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

# 1-usul: psycopg2 bilan to'g'ridan-to'g'ri ulanish
try:
    conn = psycopg2.connect(
        host="localhost",
        database="lesson_aggregation",
        user="data_scientist",
        password="secure_password123",
        port="5432"
    )
    
    # Cursor yaratish
    cur = conn.cursor()
    
    # PostgreSQL versiyasini olish
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("PostgreSQL versiyasi:", version[0])
    
    # Ulanishni yopish
    cur.close()
    conn.close()
    
    print("✅ Ulanish muvaffaqiyatli!")
    
except Exception as e:
    print("❌ Ulanish xatosi:", e)
```

```python
# 2-usul: SQLAlchemy engine bilan
try:
    # Connection string yaratish
    connection_string = "postgresql://data_scientist:secure_password123@localhost:5432/lesson_aggregation"
    
    # Engine yaratish
    engine = create_engine(connection_string)
    
    # Test query
    df = pd.read_sql("SELECT current_timestamp, current_user", engine)
    print("✅ SQLAlchemy ulanish muvaffaqiyatli!")
    print(df)
    
except Exception as e:
    print("❌ SQLAlchemy ulanish xatosi:", e)
```

---

## 🔧 **psql Command Line Interface**

### 📋 **Asosiy Buyruqlar**

```bash
# PostgreSQL ga ulanish
psql -h localhost -U data_scientist -d lesson_aggregation

# File dan SQL script ishga tushirish
psql -h localhost -U data_scientist -d lesson_aggregation -f script.sql

# Backup yaratish
pg_dump -h localhost -U data_scientist lesson_aggregation > backup.sql

# Backup dan tiklash
psql -h localhost -U data_scientist lesson_aggregation < backup.sql
```

### 🎯 **psql Ichidagi Meta-buyruqlar**

```sql
-- Database va table ma'lumotlari
\l                    -- Barcha databases
\dt                   -- Joriy database dagi tables
\d table_name         -- Table tuzilishi
\du                   -- Foydalanuvchilar ro'yxati

-- Ulanish ma'lumotlari
\conninfo             -- Joriy ulanish ma'lumoti
\c database_name      -- Boshqa database ga o'tish

-- Fayllar bilan ishlash
\i filename.sql       -- SQL file ishga tushirish
\o output.txt         -- Natijani file ga yozish
\copy table TO 'file.csv' CSV HEADER  -- CSV export

-- Yordam va chiqish
\?                    -- Barcha meta-buyruqlar
\h SELECT             -- SQL buyruq uchun yordam
\q                    -- psql dan chiqish
```

---

## 🎨 **pgAdmin 4 - Grafik Interfeys**

### 📥 **pgAdmin O'rnatish**

#### macOS:
```bash
# Homebrew orqali
brew install --cask pgadmin4

# Yoki rasmiy saytdan
# https://www.pgadmin.org/download/pgadmin-4-macos/
```

#### Linux:
```bash
# Ubuntu/Debian uchun
curl -fsSL https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/packages_pgadmin_org.gpg

sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list'

sudo apt update
sudo apt install pgadmin4
```

#### Windows:
```
# https://www.pgadmin.org/download/pgadmin-4-windows/ dan yuklab oling
```

### 🔗 **Server Ulanishini Sozlash**

1. **pgAdmin 4** ni oching
2. **Servers** ga o'ng tugma bosing → **Create** → **Server**
3. **General** tabida:
   - **Name**: `Local PostgreSQL`
4. **Connection** tabida:
   - **Host**: `localhost`
   - **Port**: `5432`
   - **Database**: `lesson_aggregation`
   - **Username**: `data_scientist`
   - **Password**: `secure_password123`
5. **Save** tugmasini bosing

---

## 🛠️ **Konfiguratsiya Fayllar**

### 📝 **postgresql.conf - Asosiy Sozlamalar**

```bash
# Konfiguratsiya fayl manzili topish
SHOW config_file;

# Muhim sozlamalar
listen_addresses = 'localhost'          # Qaysi IP manzillarga tinglash
port = 5432                            # Port raqami
max_connections = 100                  # Maksimal ulanishlar soni
shared_buffers = 128MB                 # Xotira bufferi
effective_cache_size = 4GB             # Sistema keshi hajmi
```

### 🔐 **pg_hba.conf - Autentifikatsiya**

```bash
# Autentifikatsiya faylini topish
SHOW hba_file;

# Masalan:
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             all                                     peer
host    all             all             127.0.0.1/32            md5
host    all             all             ::1/128                 md5
```

---

## 🔍 **Muammolarni Hal Qilish**

### ❌ **Umumiy Xatolar va Yechimlar**

#### 1. "psql: command not found"
```bash
# PATH ga PostgreSQL qo'shish (macOS)
echo 'export PATH="/usr/local/opt/postgresql/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# Linux uchun
sudo apt install postgresql-client
```

#### 2. "FATAL: role does not exist"
```sql
-- PostgreSQL ga postgres sifatida kirib yangi user yarating
sudo -u postgres psql
CREATE USER your_username WITH PASSWORD 'your_password';
ALTER USER your_username CREATEDB;
```

#### 3. "FATAL: database does not exist"
```sql
-- Database yarating
CREATE DATABASE your_database;
```

#### 4. "connection refused"
```bash
# PostgreSQL xizmati ishlab turganini tekshiring
# macOS
brew services list | grep postgresql

# Linux
sudo systemctl status postgresql

# Ishga tushirish
brew services start postgresql  # macOS
sudo systemctl start postgresql # Linux
```

#### 5. Python ulanish xatosi
```python
# To'g'ri parameter nomlari
conn = psycopg2.connect(
    host="localhost",      # hostname
    database="db_name",    # database nomi
    user="username",       # foydalanuvchi
    password="password",   # parol
    port="5432"           # port (string yoki int)
)
```

---

## 📊 **Performance Monitoring**

### 🔍 **Sistem Ma'lumotlari**
```sql
-- Joriy ulanishlar
SELECT count(*) as active_connections 
FROM pg_stat_activity 
WHERE state = 'active';

-- Database hajmi
SELECT 
    datname,
    pg_size_pretty(pg_database_size(datname)) as size
FROM pg_database;

-- Eng ko'p joy olgan jadvallar
SELECT 
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size
FROM pg_tables 
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC 
LIMIT 10;
```

### 📈 **Query Performance**
```sql
-- Sekin ishlayotgan querylar
SELECT 
    query,
    calls,
    total_time,
    mean_time,
    rows
FROM pg_stat_statements 
ORDER BY total_time DESC 
LIMIT 10;

-- Index ishlatilishi
SELECT 
    schemaname,
    tablename,
    indexname,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes;
```

---

## 🔧 **Amaliy Maslahatlar**

### 💡 **Best Practices**

1. **Xavfsizlik:**
   ```sql
   -- Kuchli parol ishlating
   -- Superuser huquqlarini faqat kerak bo'lganda bering
   -- pg_hba.conf ni to'g'ri sozlang
   ```

2. **Performance:**
   ```sql
   -- Index yarating
   CREATE INDEX idx_customer_id ON orders(customer_id);
   
   -- EXPLAIN dan foydalaning
   EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 1;
   ```

3. **Backup:**
   ```bash
   # Kunlik backup
   pg_dump lesson_aggregation > backup_$(date +%Y%m%d).sql
   
   # Siqilgan backup
   pg_dump lesson_aggregation | gzip > backup.sql.gz
   ```

4. **Logging:**
   ```sql
   -- postgresql.conf da
   log_statement = 'all'
   log_duration = on
   log_min_duration_statement = 1000  -- 1 soniya +
   ```

---

## 🎯 **Keyingi Qadamlar**

1. ✅ **PostgreSQL o'rnatildi va sozlandi**
2. ✅ **Python ulanish ishi**
3. ✅ **psql va pgAdmin tayyor**
4. 🔄 **create_postgresql_db.py ni ishga tushiring**
5. 🔄 **lecture.ipynb ni oching**
6. 🔄 **Amaliy mashg'ulotni boshlang**

---

## 📚 **Qo'shimcha Resurslar**

### 🔗 **Foydali Havolalar:**
- [PostgreSQL Official Documentation](https://www.postgresql.org/docs/)
- [psycopg2 Documentation](https://psycopg.org/docs/)
- [pgAdmin Documentation](https://www.pgadmin.org/docs/)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)

### 📖 **Kitoblar:**
- "PostgreSQL: Up and Running" - Regina Obe
- "Mastering PostgreSQL" - Dimitri Fontaine
- "PostgreSQL High Performance" - Gregory Smith

---

*🚀 **Tayyor bo'ldingiz!** Endi PostgreSQL bilan aggregation va grouping mavzusini o'rganishga kirishingiz mumkin!*

