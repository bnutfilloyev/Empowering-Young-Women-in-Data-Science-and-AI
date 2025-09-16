"""
PostgreSQL Ma'lumotlar Bazalarini Yaratish
==========================================

Ushbu script PostgreSQL da agregatsiya va guruhlash darslar uchun 
kerakli ma'lumotlar bazalari va jadvallarni yaratadi.

Talablar:
- PostgreSQL 12+ o'rnatilgan
- psycopg2-binary kutubxonasi
- Tegishli huquqlarga ega foydalanuvchi

Ishlatish:
python create_postgresql_db.py
"""

import psycopg2
import pandas as pd
from datetime import datetime, timedelta
import random
import json
from faker import Faker

# Fake ma'lumotlar generatori
fake = Faker(['en_US', 'uz_UZ'])
Faker.seed(42)  # Reproducible natijalar uchun

class PostgreSQLDatabaseCreator:
    def __init__(self):
        """PostgreSQL database yaratuvchi sinfi"""
        self.connection_params = {
            'host': 'localhost',
            'database': 'lesson_aggregation',
            'user': 'data_scientist',
            'password': 'secure_password123',
            'port': '5432'
        }
        self.conn = None
        self.cur = None
        
    def connect(self):
        """PostgreSQL ga ulanish"""
        try:
            self.conn = psycopg2.connect(**self.connection_params)
            self.cur = self.conn.cursor()
            print("✅ PostgreSQL ga muvaffaqiyatli ulanildi!")
            
            # PostgreSQL versiyasini tekshirish
            self.cur.execute("SELECT version();")
            version = self.cur.fetchone()[0]
            print(f"📊 PostgreSQL versiyasi: {version.split()[1]}")
            
        except psycopg2.Error as e:
            print(f"❌ PostgreSQL ulanish xatosi: {e}")
            print("\n🔧 Quyidagi bosqichlarni bajaring:")
            print("1. PostgreSQL xizmati ishlab turganini tekshiring")
            print("2. Ma'lumotlar bazasi yaratilganini tekshiring") 
            print("3. Foydalanuvchi va parol to'g'riligini tekshiring")
            return False
        return True
    
    def create_extensions(self):
        """Kerakli PostgreSQL extensions yaratish"""
        try:
            extensions = ['uuid-ossp', 'pg_stat_statements']
            
            for ext in extensions:
                try:
                    self.cur.execute(f"CREATE EXTENSION IF NOT EXISTS \"{ext}\";")
                    print(f"✅ Extension yaratildi: {ext}")
                except psycopg2.Error as e:
                    print(f"⚠️  Extension yaratilmadi {ext}: {e}")
            
            self.conn.commit()
            
        except Exception as e:
            print(f"❌ Extensions yaratishda xato: {e}")
    
    def drop_existing_tables(self):
        """Mavjud jadvallarni o'chirish (agar kerak bo'lsa)"""
        tables = ['sales', 'employees', 'products', 'customers', 'orders', 'categories', 'departments']
        
        try:
            for table in tables:
                self.cur.execute(f"DROP TABLE IF EXISTS {table} CASCADE;")
            
            self.conn.commit()
            print("🗑️  Eski jadvallar o'chirildi")
            
        except psycopg2.Error as e:
            print(f"❌ Jadvallarni o'chirishda xato: {e}")
    
    def create_departments_table(self):
        """Bo'limlar jadvali yaratish"""
        create_table_sql = """
        CREATE TABLE departments (
            department_id SERIAL PRIMARY KEY,
            department_name VARCHAR(100) NOT NULL UNIQUE,
            location VARCHAR(100),
            budget DECIMAL(12,2),
            manager_name VARCHAR(100),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        self.cur.execute(create_table_sql)
        
        # Namuna ma'lumotlar
        departments_data = [
            ('IT', 'Toshkent', 250000, 'Alisher Karimov'),
            ('Marketing', 'Toshkent', 180000, 'Malika Abdullayeva'),
            ('Sales', 'Samarqand', 220000, 'Bobur Yunusov'),
            ('HR', 'Toshkent', 120000, 'Nilufar Rahimova'),
            ('Finance', 'Toshkent', 200000, 'Jasur Toshev'),
            ('Operations', 'Andijon', 160000, 'Gulnara Hakimova'),
            ('Research', 'Buxoro', 300000, 'Farrux Salimov'),
            ('Support', 'Namangan', 100000, 'Zarina Umarova')
        ]
        
        insert_sql = """
        INSERT INTO departments (department_name, location, budget, manager_name)
        VALUES (%s, %s, %s, %s);
        """
        
        self.cur.executemany(insert_sql, departments_data)
        print("✅ Departments jadvali yaratildi: 8 ta bo'lim")
    
    def create_employees_table(self):
        """Xodimlar jadvali yaratish"""
        create_table_sql = """
        CREATE TABLE employees (
            employee_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE,
            phone VARCHAR(20),
            hire_date DATE,
            job_title VARCHAR(100),
            salary DECIMAL(10,2),
            department_id INTEGER REFERENCES departments(department_id),
            manager_id INTEGER REFERENCES employees(employee_id),
            age INTEGER,
            gender VARCHAR(10),
            city VARCHAR(50),
            experience_years INTEGER,
            performance_rating DECIMAL(3,2),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        self.cur.execute(create_table_sql)
        
        # Xodimlar ma'lumotlarini generatsiya qilish
        employees_data = []
        uzbek_names = [
            ('Alisher', 'Karimov'), ('Malika', 'Abdullayeva'), ('Bobur', 'Yunusov'),
            ('Nilufar', 'Rahimova'), ('Jasur', 'Toshev'), ('Gulnara', 'Hakimova'),
            ('Farrux', 'Salimov'), ('Zarina', 'Umarova'), ('Otabek', 'Nazarov'),
            ('Shahnoza', 'Qosimova'), ('Dilshod', 'Ergashev'), ('Feruza', 'Mirzayeva'),
            ('Sanjar', 'Usmonov'), ('Kamola', 'Rahmonova'), ('Ulugbek', 'Xolmatov'),
            ('Sevinch', 'Yunusova'), ('Temur', 'Narimanov'), ('Dildora', 'Hasanova'),
            ('Ravshan', 'Saidov'), ('Mohira', 'Karimova')
        ]
        
        job_titles = {
            1: ['Software Engineer', 'DevOps Engineer', 'Data Scientist', 'System Admin', 'Tech Lead'],
            2: ['Marketing Manager', 'Content Creator', 'SMM Specialist', 'Brand Manager', 'Marketing Analyst'],
            3: ['Sales Manager', 'Account Manager', 'Sales Representative', 'Business Developer', 'Key Account Manager'],
            4: ['HR Manager', 'Recruiter', 'HR Specialist', 'Training Coordinator', 'HR Analyst'],
            5: ['Financial Analyst', 'Accountant', 'Finance Manager', 'Budget Analyst', 'Controller'],
            6: ['Operations Manager', 'Process Analyst', 'Quality Assurance', 'Operations Coordinator', 'Logistics Manager'],
            7: ['Research Scientist', 'Data Analyst', 'Research Manager', 'Statistical Analyst', 'Research Coordinator'],
            8: ['Support Manager', 'Customer Service', 'Technical Support', 'Help Desk', 'Support Specialist']
        }
        
        cities = ['Toshkent', 'Samarqand', 'Buxoro', 'Andijon', 'Namangan', 'Qashqadaryo', 'Surxondaryo', 'Jizzax']
        
        for i in range(500):
            name_idx = i % len(uzbek_names)
            first_name, last_name = uzbek_names[name_idx]
            
            if i < len(uzbek_names):
                first_name, last_name = uzbek_names[i]
            else:
                first_name = fake.first_name()
                last_name = fake.last_name()
            
            department_id = random.randint(1, 8)
            job_title = random.choice(job_titles[department_id])
            
            # Salary ranges by department
            salary_ranges = {
                1: (1200000, 3500000),  # IT
                2: (800000, 2200000),   # Marketing  
                3: (900000, 2800000),   # Sales
                4: (700000, 1800000),   # HR
                5: (1000000, 2500000),  # Finance
                6: (800000, 2000000),   # Operations
                7: (1500000, 4000000),  # Research
                8: (600000, 1500000)    # Support
            }
            
            min_sal, max_sal = salary_ranges[department_id]
            salary = random.randint(min_sal, max_sal)
            
            hire_date = fake.date_between(start_date='-5y', end_date='today')
            age = random.randint(22, 55)
            experience = min(age - 22, (datetime.now().date() - hire_date).days // 365)
            
            employee_data = (
                first_name,
                last_name,
                f"{first_name.lower()}.{last_name.lower()}@company.uz",
                f"+998{random.randint(90, 99)}{random.randint(1000000, 9999999)}",
                hire_date,
                job_title,
                salary,
                department_id,
                None if i < 8 else random.randint(1, min(i, 50)),  # Manager
                age,
                random.choice(['Male', 'Female']),
                random.choice(cities),
                experience,
                round(random.uniform(3.0, 5.0), 2)
            )
            
            employees_data.append(employee_data)
        
        insert_sql = """
        INSERT INTO employees (first_name, last_name, email, phone, hire_date, job_title, 
                             salary, department_id, manager_id, age, gender, city, 
                             experience_years, performance_rating)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        self.cur.executemany(insert_sql, employees_data)
        print("✅ Employees jadvali yaratildi: 500 ta xodim")
    
    def create_categories_table(self):
        """Kategoriyalar jadvali yaratish"""
        create_table_sql = """
        CREATE TABLE categories (
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR(100) NOT NULL UNIQUE,
            description TEXT,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        self.cur.execute(create_table_sql)
        
        categories_data = [
            ('Elektronika', 'Elektronik mahsulotlar va gadgetlar'),
            ('Kiyim', 'Erkaklar va ayollar kiyimlari'),
            ('Uy-joy', 'Uy uchun buyumlar va mebel'),
            ('Kitoblar', 'Badiiy va ilmiy adabiyot'),
            ('Sport', 'Sport anjomlari va aksessuarlar'),
            ('Oziq-ovqat', 'Oziq-ovqat mahsulotlari'),
            ('Salomatlik', 'Tibbiy va kosmetik mahsulotlar'),
            ('Avtomobil', 'Avtomobil ehtiyot qismlari'),
            ('Bolalar', 'Bolalar uchun mahsulotlar'),
            ('Hobbi', 'Dam olish va hobbilar uchun')
        ]
        
        insert_sql = """
        INSERT INTO categories (category_name, description)
        VALUES (%s, %s);
        """
        
        self.cur.executemany(insert_sql, categories_data)
        print("✅ Categories jadvali yaratildi: 10 ta kategoriya")
    
    def create_products_table(self):
        """Mahsulotlar jadvali yaratish"""
        create_table_sql = """
        CREATE TABLE products (
            product_id SERIAL PRIMARY KEY,
            product_name VARCHAR(200) NOT NULL,
            category_id INTEGER REFERENCES categories(category_id),
            price DECIMAL(10,2),
            cost DECIMAL(10,2),
            stock_quantity INTEGER,
            supplier VARCHAR(100),
            rating DECIMAL(3,2),
            reviews_count INTEGER,
            weight_kg DECIMAL(8,2),
            is_available BOOLEAN DEFAULT TRUE,
            launch_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        self.cur.execute(create_table_sql)
        
        # Kategoriyalar bo'yicha mahsulotlar
        product_names = {
            1: ['iPhone 14', 'Samsung Galaxy', 'MacBook Pro', 'iPad Air', 'AirPods', 'Smart TV', 'Gaming Laptop', 'Bluetooth Speaker', 'Smart Watch', 'Wireless Charger'],
            2: ['Cotton T-Shirt', 'Jeans Pants', 'Winter Jacket', 'Summer Dress', 'Sneakers', 'Formal Shirt', 'Leather Boots', 'Casual Wear', 'Sports Jacket', 'Designer Bag'],
            3: ['Sofa Set', 'Dining Table', 'Bed Frame', 'Kitchen Cabinet', 'Office Chair', 'Bookshelf', 'Coffee Table', 'Wardrobe', 'Study Desk', 'Room Decor'],
            4: ['Python Programming', 'Data Science Guide', 'Machine Learning', 'Web Development', 'AI Fundamentals', 'Database Design', 'Algorithm Book', 'Software Architecture', 'DevOps Guide', 'Cybersecurity'],
            5: ['Football', 'Basketball', 'Tennis Racket', 'Gym Equipment', 'Running Shoes', 'Yoga Mat', 'Swimming Gear', 'Bicycle', 'Boxing Gloves', 'Sports Nutrition'],
            6: ['Organic Rice', 'Fresh Fruits', 'Vegetables', 'Dairy Products', 'Meat Products', 'Beverages', 'Snacks', 'Spices', 'Cooking Oil', 'Frozen Foods'],
            7: ['Vitamins', 'Skincare', 'Hair Care', 'Dental Care', 'Medical Device', 'Supplements', 'First Aid Kit', 'Perfume', 'Cosmetics', 'Health Monitor'],
            8: ['Car Battery', 'Engine Oil', 'Brake Pads', 'Tires', 'Car Accessories', 'GPS Navigator', 'Car Charger', 'Floor Mats', 'Seat Covers', 'Car Tools'],
            9: ['Baby Clothes', 'Toys', 'Baby Food', 'Stroller', 'Car Seat', 'Educational Games', 'Baby Care', 'Diapers', 'Baby Monitor', 'Nursery Items'],
            10: ['Art Supplies', 'Musical Instrument', 'Gardening Tools', 'Craft Materials', 'Board Games', 'Puzzle', 'Collectibles', 'DIY Kits', 'Photography', 'Outdoor Gear']
        }
        
        suppliers = ['TechCorp LLC', 'Fashion House', 'Home & Living', 'BookWorld', 'SportZone', 'FreshMart', 'HealthPlus', 'AutoParts Co', 'KidsWorld', 'HobbyShop']
        
        products_data = []
        
        for category_id in range(1, 11):
            for i in range(100):  # Har kategoriyada 100 ta mahsulot
                product_name = f"{random.choice(product_names[category_id])} Model {i+1}"
                
                # Kategoriyaga mos narx diapazoni
                price_ranges = {
                    1: (100, 5000), 2: (50, 800), 3: (200, 3000), 4: (20, 200),
                    5: (30, 1000), 6: (5, 100), 7: (15, 500), 8: (50, 1500),
                    9: (25, 300), 10: (10, 500)
                }
                
                min_price, max_price = price_ranges[category_id]
                price = round(random.uniform(min_price, max_price), 2)
                cost = round(price * random.uniform(0.4, 0.7), 2)  # 40-70% dan cost
                
                product_data = (
                    product_name,
                    category_id,
                    price,
                    cost,
                    random.randint(0, 500),
                    random.choice(suppliers),
                    round(random.uniform(3.0, 5.0), 2),
                    random.randint(0, 1000),
                    round(random.uniform(0.1, 50.0), 2),
                    random.choice([True, True, True, False]),  # 75% available
                    fake.date_between(start_date='-3y', end_date='today')
                )
                
                products_data.append(product_data)
        
        insert_sql = """
        INSERT INTO products (product_name, category_id, price, cost, stock_quantity,
                            supplier, rating, reviews_count, weight_kg, is_available, launch_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        self.cur.executemany(insert_sql, products_data)
        print("✅ Products jadvali yaratildi: 1000 ta mahsulot")
    
    def create_customers_table(self):
        """Mijozlar jadvali yaratish"""
        create_table_sql = """
        CREATE TABLE customers (
            customer_id SERIAL PRIMARY KEY,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE,
            phone VARCHAR(20),
            birth_date DATE,
            gender VARCHAR(10),
            city VARCHAR(50),
            region VARCHAR(50),
            registration_date DATE,
            customer_type VARCHAR(20),
            total_spent DECIMAL(12,2) DEFAULT 0,
            order_count INTEGER DEFAULT 0,
            last_order_date DATE,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        self.cur.execute(create_table_sql)
        
        customers_data = []
        uzbek_regions = ['Toshkent', 'Samarqand', 'Buxoro', 'Andijon', 'Namangan', 'Farg\'ona', 
                        'Qashqadaryo', 'Surxondaryo', 'Jizzax', 'Sirdaryo', 'Navoiy', 'Xorazm', 'Qaraqalpog\'iston']
        
        customer_types = ['Premium', 'Regular', 'Bronze', 'Silver', 'Gold']
        
        for i in range(2000):
            if i < 50:
                # O'zbek ismlar
                uzbek_names = [
                    ('Akmal', 'Toshev'), ('Dilnoza', 'Karimova'), ('Jahongir', 'Abdullayev'),
                    ('Sevara', 'Rahimova'), ('Islom', 'Yunusov'), ('Madina', 'Hakimova'),
                    ('Bekzod', 'Salimov'), ('Gulnara', 'Umarova'), ('Farrux', 'Nazarov'),
                    ('Nilufar', 'Qosimova')
                ]
                first_name, last_name = uzbek_names[i % len(uzbek_names)]
            else:
                first_name = fake.first_name()
                last_name = fake.last_name()
            
            birth_date = fake.date_between(start_date='-60y', end_date='-18y')
            registration_date = fake.date_between(start_date='-2y', end_date='today')
            
            region = random.choice(uzbek_regions)
            cities_by_region = {
                'Toshkent': ['Toshkent', 'Angren', 'Bekobod', 'Chirchiq'],
                'Samarqand': ['Samarqand', 'Bulung\'ur', 'Jomboy', 'Kattaqo\'rg\'on'],
                'Buxoro': ['Buxoro', 'Gazli', 'Kogon', 'Olot'],
                'Andijon': ['Andijon', 'Xonobod', 'Marhamat', 'Baliqchi'],
                'Namangan': ['Namangan', 'Chortoq', 'Pop', 'Uychi'],
                'Farg\'ona': ['Farg\'ona', 'Marg\'ilon', 'Qo\'qon', 'Rishton']
            }
            city = random.choice(cities_by_region.get(region, [region]))
            
            customer_data = (
                first_name,
                last_name,
                f"{first_name.lower()}.{last_name.lower()}{i}@email.uz",
                f"+998{random.randint(90, 99)}{random.randint(1000000, 9999999)}",
                birth_date,
                random.choice(['Male', 'Female']),
                city,
                region,
                registration_date,
                random.choice(customer_types),
                round(random.uniform(0, 50000000), 2),
                random.randint(0, 50),
                registration_date + timedelta(days=random.randint(1, 365)) if random.random() > 0.2 else None,
                random.choice([True, True, True, False])  # 75% active
            )
            
            customers_data.append(customer_data)
        
        insert_sql = """
        INSERT INTO customers (first_name, last_name, email, phone, birth_date, gender,
                             city, region, registration_date, customer_type, total_spent,
                             order_count, last_order_date, is_active)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        self.cur.executemany(insert_sql, customers_data)
        print("✅ Customers jadvali yaratildi: 2000 ta mijoz")
    
    def create_orders_table(self):
        """Buyurtmalar jadvali yaratish"""
        create_table_sql = """
        CREATE TABLE orders (
            order_id SERIAL PRIMARY KEY,
            customer_id INTEGER REFERENCES customers(customer_id),
            employee_id INTEGER REFERENCES employees(employee_id),
            order_date DATE,
            delivery_date DATE,
            total_amount DECIMAL(12,2),
            discount_amount DECIMAL(10,2) DEFAULT 0,
            tax_amount DECIMAL(10,2),
            shipping_cost DECIMAL(8,2),
            payment_method VARCHAR(50),
            order_status VARCHAR(20),
            delivery_city VARCHAR(50),
            delivery_region VARCHAR(50),
            notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        self.cur.execute(create_table_sql)
        
        orders_data = []
        payment_methods = ['Cash', 'Card', 'Bank Transfer', 'UzCard', 'Humo', 'PayMe', 'Click']
        order_statuses = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled', 'Returned']
        regions = ['Toshkent', 'Samarqand', 'Buxoro', 'Andijon', 'Namangan', 'Farg\'ona']
        
        for i in range(5000):
            order_date = fake.date_between(start_date='-1y', end_date='today')
            delivery_date = order_date + timedelta(days=random.randint(1, 14))
            
            total_amount = round(random.uniform(50000, 5000000), 2)
            discount_amount = round(total_amount * random.uniform(0, 0.2), 2)
            tax_amount = round(total_amount * 0.12, 2)  # 12% soliq
            shipping_cost = round(random.uniform(5000, 50000), 2)
            
            delivery_region = random.choice(regions)
            delivery_city = delivery_region  # Simplified
            
            order_data = (
                random.randint(1, 2000),  # customer_id
                random.randint(1, 500),   # employee_id
                order_date,
                delivery_date,
                total_amount,
                discount_amount,
                tax_amount,
                shipping_cost,
                random.choice(payment_methods),
                random.choice(order_statuses),
                delivery_city,
                delivery_region,
                f"Order #{i+1} notes" if random.random() > 0.7 else None
            )
            
            orders_data.append(order_data)
        
        insert_sql = """
        INSERT INTO orders (customer_id, employee_id, order_date, delivery_date, total_amount,
                          discount_amount, tax_amount, shipping_cost, payment_method, order_status,
                          delivery_city, delivery_region, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        self.cur.executemany(insert_sql, orders_data)
        print("✅ Orders jadvali yaratildi: 5000 ta buyurtma")
    
    def create_sales_table(self):
        """Sotilgan mahsulotlar jadvali yaratish"""
        create_table_sql = """
        CREATE TABLE sales (
            sale_id SERIAL PRIMARY KEY,
            order_id INTEGER REFERENCES orders(order_id),
            product_id INTEGER REFERENCES products(product_id),
            quantity INTEGER,
            unit_price DECIMAL(10,2),
            total_price DECIMAL(12,2),
            discount_percent DECIMAL(5,2) DEFAULT 0,
            profit_margin DECIMAL(10,2),
            sale_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        
        self.cur.execute(create_table_sql)
        
        sales_data = []
        
        # Har bir buyurtma uchun 1-5 ta mahsulot
        for order_id in range(1, 5001):
            products_count = random.randint(1, 5)
            
            for _ in range(products_count):
                product_id = random.randint(1, 1000)
                quantity = random.randint(1, 10)
                
                # Product price olish (simplified)
                unit_price = round(random.uniform(50, 2000), 2)
                total_price = round(unit_price * quantity, 2)
                discount_percent = round(random.uniform(0, 15), 2)
                
                # Profit margin hisoblash
                cost_price = round(unit_price * 0.6, 2)  # 60% cost
                profit_margin = round((unit_price - cost_price) * quantity, 2)
                
                # Order date ga mos sale_date
                sale_date = fake.date_between(start_date='-1y', end_date='today')
                
                sale_data = (
                    order_id,
                    product_id,
                    quantity,
                    unit_price,
                    total_price,
                    discount_percent,
                    profit_margin,
                    sale_date
                )
                
                sales_data.append(sale_data)
        
        insert_sql = """
        INSERT INTO sales (order_id, product_id, quantity, unit_price, total_price,
                         discount_percent, profit_margin, sale_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """
        
        self.cur.executemany(insert_sql, sales_data)
        print(f"✅ Sales jadvali yaratildi: {len(sales_data)} ta sotuv yozuvi")
    
    def create_indexes(self):
        """Performance uchun indexlar yaratish"""
        indexes = [
            "CREATE INDEX idx_employees_department ON employees(department_id);",
            "CREATE INDEX idx_employees_salary ON employees(salary);",
            "CREATE INDEX idx_products_category ON products(category_id);",
            "CREATE INDEX idx_products_price ON products(price);",
            "CREATE INDEX idx_orders_customer ON orders(customer_id);",
            "CREATE INDEX idx_orders_date ON orders(order_date);",
            "CREATE INDEX idx_sales_product ON sales(product_id);",
            "CREATE INDEX idx_sales_date ON sales(sale_date);",
            "CREATE INDEX idx_customers_region ON customers(region);"
        ]
        
        for idx_sql in indexes:
            try:
                self.cur.execute(idx_sql)
                print(f"✅ Index yaratildi")
            except psycopg2.Error as e:
                print(f"⚠️  Index yaratilmadi: {e}")
        
        self.conn.commit()
        print("🔍 Barcha indexlar yaratildi")
    
    def display_statistics(self):
        """Yaratilgan ma'lumotlar statistikasi"""
        print("\n📊 MA'LUMOTLAR BAZASI STATISTIKASI")
        print("=" * 35)
        
        tables = ['departments', 'employees', 'categories', 'products', 'customers', 'orders', 'sales']
        
        for table in tables:
            self.cur.execute(f"SELECT COUNT(*) FROM {table};")
            count = self.cur.fetchone()[0]
            print(f"📋 {table.capitalize()}: {count:,} ta yozuv")
        
        # Qo'shimcha statistika
        print("\n📈 QOSHIMCHA STATISTIKA")
        print("-" * 25)
        
        # Bo'limlar bo'yicha xodimlar
        self.cur.execute("""
            SELECT d.department_name, COUNT(e.employee_id) as employee_count
            FROM departments d
            LEFT JOIN employees e ON d.department_id = e.department_id
            GROUP BY d.department_name
            ORDER BY employee_count DESC;
        """)
        
        print("👥 Bo'limlar bo'yicha xodimlar:")
        for row in self.cur.fetchall():
            print(f"   {row[0]}: {row[1]} ta")
        
        # Kategoriyalar bo'yicha mahsulotlar
        self.cur.execute("""
            SELECT c.category_name, COUNT(p.product_id) as product_count
            FROM categories c
            LEFT JOIN products p ON c.category_id = p.category_id
            GROUP BY c.category_name
            ORDER BY product_count DESC;
        """)
        
        print("\n🛍️ Kategoriyalar bo'yicha mahsulotlar:")
        for row in self.cur.fetchall():
            print(f"   {row[0]}: {row[1]} ta")
        
        # Yillik sotuvlar
        self.cur.execute("""
            SELECT 
                EXTRACT(YEAR FROM sale_date) as year,
                COUNT(*) as sales_count,
                SUM(total_price) as total_revenue
            FROM sales
            GROUP BY EXTRACT(YEAR FROM sale_date)
            ORDER BY year;
        """)
        
        print("\n💰 Yillik sotuvlar:")
        for row in self.cur.fetchall():
            year, count, revenue = row
            print(f"   {int(year)}: {count:,} ta sotuv, {revenue:,.0f} so'm")
    
    def close_connection(self):
        """Ulanishni yopish"""
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()
        print("\n🔐 Ma'lumotlar bazasi ulanishi yopildi")

def main():
    """Asosiy funksiya"""
    print("🚀 PostgreSQL Ma'lumotlar Bazasini Yaratish Boshlandi")
    print("=" * 55)
    
    creator = PostgreSQLDatabaseCreator()
    
    try:
        # Ulanish
        if not creator.connect():
            return
        
        print("\n🔧 Ma'lumotlar bazasini sozlash...")
        
        # Extensions yaratish
        creator.create_extensions()
        
        # Eski jadvallarni o'chirish
        creator.drop_existing_tables()
        
        print("\n📋 Jadvallarni yaratish...")
        
        # Jadvallarni ketma-ket yaratish
        creator.create_departments_table()
        creator.create_employees_table()
        creator.create_categories_table()
        creator.create_products_table()
        creator.create_customers_table()
        creator.create_orders_table()
        creator.create_sales_table()
        
        # Indexlar yaratish
        creator.create_indexes()
        
        # O'zgarishlarni saqlash
        creator.conn.commit()
        
        # Statistika ko'rsatish
        creator.display_statistics()
        
        print("\n🎉 Ma'lumotlar bazasi muvaffaqiyatli yaratildi!")
        print("✅ Endi lecture.ipynb faylini ochib o'qishni boshlashingiz mumkin")
        
    except Exception as e:
        print(f"❌ Xato yuz berdi: {e}")
        if creator.conn:
            creator.conn.rollback()
    
    finally:
        creator.close_connection()

if __name__ == "__main__":
    main()
