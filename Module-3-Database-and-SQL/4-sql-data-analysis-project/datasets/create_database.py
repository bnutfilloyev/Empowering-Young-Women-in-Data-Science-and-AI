import sqlite3
import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# Date adapter warning'ni bartaraf etish uchun
def adapt_date(date):
    return date.isoformat()

def convert_date(date_string):
    return datetime.fromisoformat(date_string.decode()).date()

# SQLite date adapter'larni o'rnatish
sqlite3.register_adapter(datetime.date, adapt_date)
sqlite3.register_converter("date", convert_date)

# O'zbek nomlari va shaharlar uchun Faker
fake = Faker('en_US')
Faker.seed(42)
np.random.seed(42)
random.seed(42)

print("🚀 E-commerce ma'lumotlar bazasini yaratish boshlandi...")
print("="*60)

# SQLite ma'lumotlar bazasi yaratish
conn = sqlite3.connect('ecommerce_analysis.db', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()

# Jadvallarni yaratish
print("📋 Jadvallar yaratilmoqda...")

# 1. Categories jadvali
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# 2. Products jadvali
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category_id INTEGER,
    price REAL NOT NULL,
    cost REAL NOT NULL,
    stock_quantity INTEGER DEFAULT 0,
    rating REAL DEFAULT 0,
    reviews_count INTEGER DEFAULT 0,
    weight_kg REAL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
)
''')

# 3. Customers jadvali
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    birth_date DATE,
    gender TEXT,
    city TEXT,
    region TEXT,
    registration_date DATE,
    customer_segment TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# 4. Orders jadvali
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date DATE,
    order_status TEXT,
    total_amount REAL,
    discount_amount REAL DEFAULT 0,
    shipping_cost REAL DEFAULT 0,
    payment_method TEXT,
    delivery_city TEXT,
    delivery_region TEXT,
    delivery_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
''')

# 5. Order_items jadvali
cursor.execute('''
CREATE TABLE IF NOT EXISTS order_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    total_price REAL,
    discount_percent REAL DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
''')

print("✅ Jadvallar muvaffaqiyatli yaratildi")

# Ma'lumotlarni kiritish
print("\n📊 Test ma'lumotlari kiritilmoqda...")

# O'zbekiston shaharlari va viloyatlari
uzbek_regions = [
    ('Toshkent', 'Toshkent shahri'),
    ('Samarqand', 'Samarqand viloyati'),
    ('Buxoro', 'Buxoro viloyati'),
    ('Andijon', 'Andijon viloyati'),
    ('Namangan', 'Namangan viloyati'),
    ('Farg\'ona', 'Farg\'ona viloyati'),
    ('Qashqadaryo', 'Qashqadaryo viloyati'),
    ('Surxondaryo', 'Surxondaryo viloyati'),
    ('Xorazm', 'Xorazm viloyati'),
    ('Navoiy', 'Navoiy viloyati'),
    ('Jizzax', 'Jizzax viloyati'),
    ('Sirdaryo', 'Sirdaryo viloyati'),
    ('Qoraqalpog\'iston', 'Qoraqalpog\'iston Respublikasi')
]

# 1. Kategoriyalar
categories = [
    ('Elektronika', 'Telefonlar, kompyuterlar va boshqa elektronika'),
    ('Kiyim va Poyafzal', 'Erkaklar va ayollar kiyimlari'),
    ('Uy va Bog\'', 'Uy uchun buyumlar va bog\' anjomlari'),
    ('Kitoblar', 'Badiiy va o\'quv adabiyotlari'),
    ('Sport va Faollik', 'Sport anjomlari va faollik buyumlari'),
    ('Salomatlik va Go\'zallik', 'Kosmetika va salomatlik mahsulotlari'),
    ('Oziq-ovqat', 'Oziq-ovqat mahsulotlari va ichimliklar'),
    ('Avtomobil', 'Avtomobil ehtiyot qismlari va aksessuarlar'),
    ('Bolalar', 'Bolalar uchun o\'yinchoqlar va kiyimlar'),
    ('Hobbi va San\'at', 'San\'at buyumlari va hobbi aksessuarlari')
]

cursor.executemany('INSERT INTO categories (category_name, description) VALUES (?, ?)', categories)
print(f"📝 {len(categories)} ta kategoriya qo'shildi")

# 2. Mahsulotlar
products_data = []
product_names = {
    1: ['iPhone 15 Pro', 'Samsung Galaxy S24', 'MacBook Air M2', 'iPad Pro', 'AirPods Pro', 'Gaming Laptop', 'Smart Watch', 'Bluetooth Speaker', 'Wireless Charger', 'USB-C Cable'],
    2: ['Cotton T-Shirt', 'Jeans Pants', 'Dress Shirt', 'Sneakers', 'Winter Jacket', 'Summer Dress', 'Formal Shoes', 'Casual Pants', 'Sweater', 'Athletic Wear'],
    3: ['Sofa Set', 'Dining Table', 'Coffee Maker', 'Vacuum Cleaner', 'Bed Frame', 'Kitchen Knife Set', 'Curtains', 'Floor Lamp', 'Storage Box', 'Garden Tools'],
    4: ['Python Programming', 'Data Science Guide', 'History Book', 'Novel Collection', 'Children Story', 'Cookbook', 'Travel Guide', 'Biography', 'Science Fiction', 'Self-Help'],
    5: ['Football', 'Basketball', 'Tennis Racket', 'Yoga Mat', 'Dumbbells', 'Running Shoes', 'Gym Bag', 'Water Bottle', 'Exercise Bike', 'Swimming Goggles'],
    6: ['Face Cream', 'Shampoo', 'Vitamin C', 'Sunscreen', 'Perfume', 'Moisturizer', 'Body Wash', 'Hair Oil', 'Face Mask', 'Supplement'],
    7: ['Organic Rice', 'Premium Tea', 'Olive Oil', 'Honey', 'Dark Chocolate', 'Nuts Mix', 'Fresh Juice', 'Protein Bar', 'Spices Set', 'Coffee Beans'],
    8: ['Car Battery', 'Engine Oil', 'Brake Pads', 'Air Filter', 'Spark Plugs', 'Car Charger', 'Seat Cover', 'Floor Mats', 'Dash Cam', 'Car Polish'],
    9: ['Educational Toy', 'Plush Bear', 'Building Blocks', 'Kids Bicycle', 'Puzzle Game', 'Coloring Books', 'Baby Clothes', 'School Bag', 'Toy Car', 'Board Game'],
    10: ['Art Supplies', 'Craft Kit', 'Musical Instrument', 'Photography Camera', 'Paint Set', 'Knitting Yarn', 'Model Kit', 'Sewing Machine', 'Canvas Board', 'Sketch Pad']
}

for category_id in range(1, 11):
    for i, name in enumerate(product_names[category_id]):
        # Narx va tannarxni kategoriyaga qarab belgilash
        if category_id == 1:  # Elektronika
            price = random.uniform(500000, 25000000)
        elif category_id in [3, 8]:  # Uy-joy, Avtomobil
            price = random.uniform(100000, 15000000)
        elif category_id == 2:  # Kiyim
            price = random.uniform(50000, 1500000)
        else:  # Boshqa kategoriyalar
            price = random.uniform(25000, 1000000)
        
        cost = price * random.uniform(0.4, 0.7)  # 40-70% tannarx
        stock = random.randint(0, 500)
        rating = round(random.uniform(3.0, 5.0), 1)
        reviews = random.randint(0, 2000)
        weight = round(random.uniform(0.1, 50.0), 2)
        
        products_data.append((name, category_id, round(price, 0), round(cost, 0), stock, rating, reviews, weight))

cursor.executemany('''
    INSERT INTO products (product_name, category_id, price, cost, stock_quantity, rating, reviews_count, weight_kg) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', products_data)
print(f"🛍️ {len(products_data)} ta mahsulot qo'shildi")

# 3. Mijozlar
customers_data = []
used_emails = set()  # Email unikalligi uchun
uzbek_first_names_male = ['Akmal', 'Bobur', 'Dilshod', 'Eldor', 'Farrux', 'Gulomjon', 'Humoyun', 'Islom', 'Jasur', 'Karim', 'Laziz', 'Muhsin', 'Nodir', 'Otabek', 'Pulat', 'Qodirjon', 'Rustam', 'Sardor', 'Tulkin', 'Umid']
uzbek_first_names_female = ['Adolat', 'Barno', 'Dilfuza', 'Elnora', 'Feruza', 'Gulnora', 'Hilola', 'Iroda', 'Jasmin', 'Kamila', 'Laylo', 'Madina', 'Nilufar', 'Oygul', 'Parichehr', 'Qizlarxon', 'Robiya', 'Sevaroxon', 'Toshbonu', 'Umida']
uzbek_last_names = ['Abdullayev', 'Karimov', 'Toshev', 'Rahimov', 'Yunusov', 'Hakimov', 'Salimov', 'Umarov', 'Nazarov', 'Ismoilov', 'Mahmudov', 'Aliyev', 'Ergashev', 'Yusupov', 'Qodirov', 'Mirzayev', 'Shokirov', 'Rustamov', 'Sultonov', 'Boboev']

customer_segments = ['Bronze', 'Silver', 'Gold', 'Platinum', 'VIP']

for i in range(2000):
    gender = random.choice(['Male', 'Female'])
    if gender == 'Male':
        first_name = random.choice(uzbek_first_names_male)
    else:
        first_name = random.choice(uzbek_first_names_female)
    
    last_name = random.choice(uzbek_last_names)
    
    # Unikal email yaratish
    while True:
        email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 9999)}@email.uz"
        if email not in used_emails:
            used_emails.add(email)
            break
    
    phone = f"+99890{random.randint(1000000, 9999999)}"
    birth_date = fake.date_between(start_date='-60y', end_date='-18y')
    city, region = random.choice(uzbek_regions)
    registration_date = fake.date_between(start_date='-2y', end_date='today')
    segment = random.choice(customer_segments)
    
    customers_data.append((first_name, last_name, email, phone, birth_date, gender, city, region, registration_date, segment))

cursor.executemany('''
    INSERT INTO customers (first_name, last_name, email, phone, birth_date, gender, city, region, registration_date, customer_segment) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', customers_data)
print(f"👥 {len(customers_data)} ta mijoz qo'shildi")

# 4. Buyurtmalar va buyurtma elementlari
orders_data = []
order_items_data = []
order_statuses = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled', 'Returned']
payment_methods = ['Credit Card', 'Debit Card', 'UzCard', 'Humo', 'Click', 'PayMe', 'Cash', 'Bank Transfer']

# 2023-2024 yillar uchun buyurtmalar
start_date = datetime(2023, 1, 1)
end_date = datetime(2024, 12, 31)
order_id = 1

for i in range(10000):  # 10,000 ta buyurtma
    customer_id = random.randint(1, 2000)
    order_date = fake.date_between(start_date=start_date, end_date=end_date)
    
    # Mavsumiy ta'sir (qish va yozda ko'proq savdo)
    month = order_date.month
    if month in [12, 1, 2, 6, 7, 8]:  # Qish va yoz
        order_probability = 1.3
    else:
        order_probability = 1.0
    
    if random.random() > order_probability * 0.7:
        continue
    
    status = random.choices(order_statuses, weights=[5, 10, 15, 60, 8, 2])[0]
    payment_method = random.choice(payment_methods)
    city, region = random.choice(uzbek_regions)
    
    # Buyurtma elementlarini yaratish
    num_items = random.choices([1, 2, 3, 4, 5], weights=[40, 30, 20, 8, 2])[0]
    total_amount = 0
    discount_amount = 0
    shipping_cost = random.uniform(15000, 50000)
    
    delivery_date = None
    if status in ['Delivered', 'Returned']:
        delivery_date = order_date + timedelta(days=random.randint(1, 14))
    
    # Har bir buyurtma uchun mahsulotlar
    selected_products = random.sample(range(1, 101), num_items)
    
    for product_id in selected_products:
        # Mahsulot narxini olish
        cursor.execute('SELECT price FROM products WHERE product_id = ?', (product_id,))
        product_price = cursor.fetchone()[0]
        
        quantity = random.choices([1, 2, 3, 4], weights=[70, 20, 8, 2])[0]
        unit_price = product_price
        discount_percent = random.choices([0, 5, 10, 15, 20], weights=[60, 20, 10, 7, 3])[0]
        
        discounted_price = unit_price * (1 - discount_percent / 100)
        item_total = discounted_price * quantity
        total_amount += item_total
        
        order_items_data.append((order_id, product_id, quantity, unit_price, item_total, discount_percent))
    
    # Umumiy chegirma
    if total_amount > 1000000:  # 1 million so'mdan ko'p bo'lsa
        discount_amount = total_amount * random.uniform(0.02, 0.10)
    
    total_amount = total_amount - discount_amount + shipping_cost
    
    orders_data.append((customer_id, order_date, status, round(total_amount, 0), 
                       round(discount_amount, 0), round(shipping_cost, 0), 
                       payment_method, city, region, delivery_date))
    order_id += 1

cursor.executemany('''
    INSERT INTO orders (customer_id, order_date, order_status, total_amount, discount_amount, 
                       shipping_cost, payment_method, delivery_city, delivery_region, delivery_date) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', orders_data)

cursor.executemany('''
    INSERT INTO order_items (order_id, product_id, quantity, unit_price, total_price, discount_percent) 
    VALUES (?, ?, ?, ?, ?, ?)
''', order_items_data)

print(f"🛒 {len(orders_data)} ta buyurtma qo'shildi")
print(f"📦 {len(order_items_data)} ta buyurtma elementi qo'shildi")

# Indexlar yaratish
print("\n🔍 Indexlar yaratilmoqda...")
indexes = [
    'CREATE INDEX idx_products_category ON products(category_id)',
    'CREATE INDEX idx_products_price ON products(price)',
    'CREATE INDEX idx_customers_region ON customers(region)',
    'CREATE INDEX idx_customers_segment ON customers(customer_segment)',
    'CREATE INDEX idx_orders_customer ON orders(customer_id)',
    'CREATE INDEX idx_orders_date ON orders(order_date)',
    'CREATE INDEX idx_orders_status ON orders(order_status)',
    'CREATE INDEX idx_order_items_order ON order_items(order_id)',
    'CREATE INDEX idx_order_items_product ON order_items(product_id)'
]

for index in indexes:
    cursor.execute(index)

print("✅ Indexlar yaratildi")

# Foydali views yaratish
print("\n👁️ Views yaratilmoqda...")

# 1. Order summary view
cursor.execute('''
CREATE VIEW order_summary AS
SELECT 
    o.order_id,
    o.customer_id,
    c.first_name || ' ' || c.last_name as customer_name,
    c.customer_segment,
    o.order_date,
    o.order_status,
    o.total_amount,
    o.discount_amount,
    o.payment_method,
    o.delivery_region,
    COUNT(oi.item_id) as items_count,
    SUM(oi.quantity) as total_quantity
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
LEFT JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, o.customer_id, c.first_name, c.last_name, c.customer_segment,
         o.order_date, o.order_status, o.total_amount, o.discount_amount, 
         o.payment_method, o.delivery_region
''')

# 2. Product performance view
cursor.execute('''
CREATE VIEW product_performance AS
SELECT 
    p.product_id,
    p.product_name,
    cat.category_name,
    p.price,
    p.rating,
    p.reviews_count,
    COUNT(oi.item_id) as times_ordered,
    SUM(oi.quantity) as total_sold,
    SUM(oi.total_price) as total_revenue,
    AVG(oi.total_price / oi.quantity) as avg_selling_price
FROM products p
JOIN categories cat ON p.category_id = cat.category_id
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name, cat.category_name, p.price, p.rating, p.reviews_count
''')

# 3. Customer analytics view
cursor.execute('''
CREATE VIEW customer_analytics AS
SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name as full_name,
    c.customer_segment,
    c.region,
    c.registration_date,
    COUNT(o.order_id) as total_orders,
    SUM(o.total_amount) as total_spent,
    AVG(o.total_amount) as avg_order_value,
    MAX(o.order_date) as last_order_date,
    MIN(o.order_date) as first_order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.customer_segment, 
         c.region, c.registration_date
''')

print("✅ Views yaratildi")

# Bazani saqlash va yopish
conn.commit()
conn.close()

print("\n" + "="*60)
print("🎉 E-commerce ma'lumotlar bazasi muvaffaqiyatli yaratildi!")
print("\n📊 Yaratilgan jadvallar:")
print("   • categories (10 ta)")
print("   • products (100 ta)")
print("   • customers (2000 ta)")
print(f"   • orders ({len(orders_data)} ta)")
print(f"   • order_items ({len(order_items_data)} ta)")
print("\n👁️ Yaratilgan views:")
print("   • order_summary")
print("   • product_performance") 
print("   • customer_analytics")
print("\n🔗 Ma'lumotlar bazasi fayli:")
print("   ecommerce_analysis.db")
print("\n✅ Endi loyiha notebook ini ishga tushirishingiz mumkin!")