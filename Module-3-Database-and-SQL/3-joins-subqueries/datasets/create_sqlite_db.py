#!/usr/bin/env python3
"""
JOIN va Subquerylar uchun SQLite ma'lumotlar bazasi yaratish
Module 3 - Dars 3: JOINlar va Subquerylar

Bu skript quyidagilarni yaratadi:
1. lesson_joins.db SQLite ma'lumotlar bazasi
2. Bir nechta bog'liq jadvallar
3. Realistic test ma'lumotlari
4. Indekslar performance uchun
"""

import sqlite3
import pandas as pd
import random
from datetime import datetime, timedelta
import string
from faker import Faker

# Faker obyektini yaratish
fake = Faker(['en_US', 'uz_UZ'])

# SQLite ma'lumotlar bazasi fayli
DB_PATH = 'lesson_joins.db'

def create_database_and_tables():
    """
    Ma'lumotlar bazasi va jadvallar yaratish
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print("🔗 SQLite ma'lumotlar bazasiga ulandi...")

        # 1. Regions jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS regions (
                region_id INTEGER PRIMARY KEY AUTOINCREMENT,
                region_name TEXT NOT NULL,
                country TEXT NOT NULL,
                population INTEGER,
                area_km2 REAL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 2. Categories jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                category_name TEXT NOT NULL,
                description TEXT,
                parent_category_id INTEGER REFERENCES categories(category_id),
                is_active INTEGER DEFAULT 1,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 3. Suppliers jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
                contact_person TEXT,
                email TEXT,
                phone TEXT,
                address TEXT,
                region_id INTEGER REFERENCES regions(region_id),
                established_year INTEGER,
                rating REAL CHECK (rating >= 0 AND rating <= 5),
                is_active INTEGER DEFAULT 1,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 4. Customers jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                birth_date TEXT,
                gender TEXT CHECK (gender IN ('Male', 'Female', 'Other')),
                address TEXT,
                region_id INTEGER REFERENCES regions(region_id),
                customer_type TEXT CHECK (customer_type IN ('Regular', 'Premium', 'VIP')),
                registration_date TEXT DEFAULT CURRENT_DATE,
                last_login TEXT,
                is_active INTEGER DEFAULT 1,
                total_spent REAL DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 5. Departments jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                department_id INTEGER PRIMARY KEY AUTOINCREMENT,
                department_name TEXT NOT NULL,
                description TEXT,
                manager_id INTEGER,
                budget REAL,
                established_date TEXT,
                location TEXT,
                is_active INTEGER DEFAULT 1,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 6. Employees jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
                employee_code TEXT UNIQUE,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT,
                birth_date TEXT,
                hire_date TEXT NOT NULL,
                department_id INTEGER REFERENCES departments(department_id),
                position_title TEXT,
                salary REAL NOT NULL,
                manager_id INTEGER REFERENCES employees(employee_id),
                region_id INTEGER REFERENCES regions(region_id),
                experience_years INTEGER DEFAULT 0,
                education_level TEXT,
                is_active INTEGER DEFAULT 1,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 7. Products jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_code TEXT UNIQUE NOT NULL,
                product_name TEXT NOT NULL,
                description TEXT,
                category_id INTEGER REFERENCES categories(category_id),
                supplier_id INTEGER REFERENCES suppliers(supplier_id),
                unit_price REAL NOT NULL,
                cost_price REAL,
                stock_quantity INTEGER DEFAULT 0,
                reorder_level INTEGER DEFAULT 10,
                weight REAL,
                dimensions TEXT,
                color TEXT,
                brand TEXT,
                model TEXT,
                warranty_months INTEGER,
                rating REAL CHECK (rating >= 0 AND rating <= 5),
                reviews_count INTEGER DEFAULT 0,
                is_active INTEGER DEFAULT 1,
                launch_date TEXT,
                discontinue_date TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 8. Orders jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_number TEXT UNIQUE NOT NULL,
                customer_id INTEGER REFERENCES customers(customer_id),
                employee_id INTEGER REFERENCES employees(employee_id),
                order_date TEXT NOT NULL,
                required_date TEXT,
                shipped_date TEXT,
                delivery_date TEXT,
                shipping_address TEXT,
                billing_address TEXT,
                region_id INTEGER REFERENCES regions(region_id),
                payment_method TEXT,
                order_status TEXT CHECK (order_status IN ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled')),
                subtotal REAL NOT NULL,
                tax_amount REAL DEFAULT 0,
                shipping_cost REAL DEFAULT 0,
                discount_amount REAL DEFAULT 0,
                total_amount REAL NOT NULL,
                notes TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 9. Order_details jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_details (
                order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER REFERENCES orders(order_id),
                product_id INTEGER REFERENCES products(product_id),
                quantity INTEGER NOT NULL CHECK (quantity > 0),
                unit_price REAL NOT NULL,
                discount_percent REAL DEFAULT 0,
                line_total REAL NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 10. Reviews jadvali
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reviews (
                review_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER REFERENCES products(product_id),
                customer_id INTEGER REFERENCES customers(customer_id),
                order_id INTEGER REFERENCES orders(order_id),
                rating INTEGER CHECK (rating >= 1 AND rating <= 5),
                review_title TEXT,
                review_text TEXT,
                review_date TEXT DEFAULT CURRENT_DATE,
                is_verified INTEGER DEFAULT 0,
                helpful_votes INTEGER DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
        """)

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Barcha jadvallar muvaffaqiyatli yaratildi")
        return True

    except Exception as e:
        print(f"❌ Jadvallar yaratishda xatolik: {e}")
        return False

def create_indexes():
    """
    Performance uchun indekslar yaratish
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print("🚀 Indekslar yaratilmoqda...")

        # Tez-tez ishlatiluvchi foreign key lar uchun
        indexes = [
            "CREATE INDEX IF NOT EXISTS idx_customers_region ON customers(region_id);",
            "CREATE INDEX IF NOT EXISTS idx_employees_department ON employees(department_id);",
            "CREATE INDEX IF NOT EXISTS idx_employees_manager ON employees(manager_id);",
            "CREATE INDEX IF NOT EXISTS idx_products_category ON products(category_id);",
            "CREATE INDEX IF NOT EXISTS idx_products_supplier ON products(supplier_id);",
            "CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);",
            "CREATE INDEX IF NOT EXISTS idx_orders_employee ON orders(employee_id);",
            "CREATE INDEX IF NOT EXISTS idx_orders_region ON orders(region_id);",
            "CREATE INDEX IF NOT EXISTS idx_order_details_order ON order_details(order_id);",
            "CREATE INDEX IF NOT EXISTS idx_order_details_product ON order_details(product_id);",
            "CREATE INDEX IF NOT EXISTS idx_reviews_product ON reviews(product_id);",
            "CREATE INDEX IF NOT EXISTS idx_reviews_customer ON reviews(customer_id);",

            # Sana va vaqt ustunlari uchun
            "CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(order_date);",
            "CREATE INDEX IF NOT EXISTS idx_customers_registration ON customers(registration_date);",
            "CREATE INDEX IF NOT EXISTS idx_employees_hire_date ON employees(hire_date);",

            # Qidiruv uchun
            "CREATE INDEX IF NOT EXISTS idx_customers_email ON customers(email);",
            "CREATE INDEX IF NOT EXISTS idx_employees_email ON employees(email);",
            "CREATE INDEX IF NOT EXISTS idx_products_name ON products(product_name);",
            "CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(order_status);",

            # Kompleks indekslar
            "CREATE INDEX IF NOT EXISTS idx_orders_customer_date ON orders(customer_id, order_date);",
            "CREATE INDEX IF NOT EXISTS idx_products_category_active ON products(category_id, is_active);",
            "CREATE INDEX IF NOT EXISTS idx_customers_type_active ON customers(customer_type, is_active);"
        ]

        for index_sql in indexes:
            cursor.execute(index_sql)

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Barcha indekslar yaratildi")
        return True

    except Exception as e:
        print(f"❌ Indekslar yaratishda xatolik: {e}")
        return False

def insert_sample_data():
    """
    Test ma'lumotlarini kiritish
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print("📊 Test ma'lumotlari kiritilmoqda...")

        # 1. Regions
        regions_data = [
            ('Toshkent shahri', 'Uzbekistan', 2500000, 334.8),
            ('Toshkent viloyati', 'Uzbekistan', 2800000, 15250.0),
            ('Samarqand viloyati', 'Uzbekistan', 3700000, 16773.0),
            ('Farg\'ona viloyati', 'Uzbekistan', 3600000, 6800.0),
            ('Andijon viloyati', 'Uzbekistan', 3000000, 4200.0),
            ('Namangan viloyati', 'Uzbekistan', 2700000, 7900.0),
            ('Qashqadaryo viloyati', 'Uzbekistan', 3200000, 28400.0),
            ('Surxondaryo viloyati', 'Uzbekistan', 2500000, 20800.0),
            ('Buxoro viloyati', 'Uzbekistan', 1800000, 39400.0),
            ('Navoiy viloyati', 'Uzbekistan', 1000000, 110800.0),
            ('Jizzax viloyati', 'Uzbekistan', 1400000, 20500.0),
            ('Sirdaryo viloyati', 'Uzbekistan', 800000, 5100.0),
            ('Xorazm viloyati', 'Uzbekistan', 1800000, 6300.0),
            ('Qoraqalpog\'iston', 'Uzbekistan', 1900000, 166600.0)
        ]

        cursor.executemany(
            "INSERT OR IGNORE INTO regions (region_name, country, population, area_km2) VALUES (?, ?, ?, ?)",
            regions_data
        )

        # 2. Categories (ierarxik struktura)
        categories_data = [
            ('Elektronika', 'Elektron qurilmalar va aksessuarlar', None),
            ('Kiyim va poyabzal', 'Erkaklar, ayollar va bolalar kiyimlari', None),
            ('Uy-ro\'zg\'or buyumlari', 'Uy uchun zarur buyumlar', None),
            ('Kitob va o\'quv qo\'llanmalari', 'Har xil adabiyotlar', None),
            ('Sport va faollik', 'Sport anjomlari va faollik uchun', None),
            ('Go\'zallik va parvarish', 'Kosmetika va shaxsiy parvarish', None),
            ('Avtomobil ehtiyot qismlari', 'Mashina uchun ehtiyot qismlar', None),

            # Kichik kategoriyalar
            ('Smartfonlar', 'Mobil telefonlar', 1),
            ('Noutbuklar', 'Portativ kompyuterlar', 1),
            ('Televizorlar', 'LCD, LED, Smart TV', 1),
            ('Erkaklar kiyimi', 'Erkaklar uchun kiyimlar', 2),
            ('Ayollar kiyimi', 'Ayollar uchun kiyimlar', 2),
            ('Bolalar kiyimi', 'Bolalar uchun kiyimlar', 2),
            ('Oshxona anjomlari', 'Oshxona uchun', 3),
            ('Yotoqxona mebeli', 'Yotoqxona uchun mebel', 3)
        ]

        cursor.executemany(
            "INSERT OR IGNORE INTO categories (category_name, description, parent_category_id) VALUES (?, ?, ?)",
            categories_data
        )

        # 3. Suppliers
        for i in range(50):
            supplier_data = (
                fake.company(),
                fake.name(),
                fake.email(),
                fake.phone_number(),
                fake.address(),
                random.randint(1, 14),  # region_id
                random.randint(1990, 2020),  # established_year
                round(random.uniform(2.5, 5.0), 2),  # rating
                random.choice([1, 1, 1, 0])  # is_active (80% True)
            )
            cursor.execute(
                """INSERT OR IGNORE INTO suppliers
                   (company_name, contact_person, email, phone, address, region_id,
                    established_year, rating, is_active)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                supplier_data
            )

        # 4. Customers
        for i in range(1000):
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=80)
            registration_date = fake.date_between(start_date='-3y', end_date='today')

            customer_data = (
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                fake.phone_number(),
                birth_date.isoformat(),
                random.choice(['Male', 'Female']),
                fake.address(),
                random.randint(1, 14),  # region_id
                random.choice(['Regular', 'Regular', 'Premium', 'VIP']),  # customer_type
                registration_date.isoformat(),
                fake.date_time_between(start_date=registration_date, end_date='now').isoformat(),  # last_login
                random.choice([1, 1, 1, 1, 0]),  # is_active (90% True)
                round(random.uniform(0, 50000000), 2)  # total_spent
            )
            cursor.execute(
                """INSERT OR IGNORE INTO customers
                   (first_name, last_name, email, phone, birth_date, gender, address,
                    region_id, customer_type, registration_date, last_login, is_active, total_spent)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                customer_data
            )

        # 5. Departments
        departments_data = [
            ('Savdo bo\'limi', 'Mijozlar bilan ishlash va savdo', None, 1000000000, '2020-01-01', 'Toshkent'),
            ('Marketing', 'Reklama va marketing faoliyati', None, 500000000, '2020-01-01', 'Toshkent'),
            ('IT bo\'limi', 'Axborot texnologiyalari', None, 800000000, '2020-01-01', 'Toshkent'),
            ('Moliya bo\'limi', 'Moliyaviy hisoblar', None, 600000000, '2020-01-01', 'Toshkent'),
            ('HR bo\'limi', 'Kadrlar bilan ishlash', None, 400000000, '2020-01-01', 'Toshkent'),
            ('Logistika', 'Yetkazib berish va omborxona', None, 700000000, '2020-01-01', 'Toshkent'),
            ('Mijozlarga xizmat', 'Mijozlarni qo\'llab-quvvatlash', None, 300000000, '2020-01-01', 'Toshkent'),
            ('Sifat nazorati', 'Mahsulot sifatini nazorat qilish', None, 250000000, '2020-01-01', 'Toshkent')
        ]

        cursor.executemany(
            """INSERT OR IGNORE INTO departments
               (department_name, description, manager_id, budget, established_date, location)
               VALUES (?, ?, ?, ?, ?, ?)""",
            departments_data
        )

        # 6. Employees
        positions = [
            'Meneger', 'Savdo vakili', 'Analitik', 'Dasturchi', 'Dizayner',
            'Hisobchi', 'HR specialist', 'Logist', 'Konsultant', 'Nazoratchi'
        ]

        education_levels = ['O\'rta', 'O\'rta maxsus', 'Oliy', 'Magistr', 'PhD']

        for i in range(200):
            hire_date = fake.date_between(start_date='-5y', end_date='today')
            experience_years = (datetime.now().date() - hire_date).days // 365

            employee_data = (
                f'EMP{str(i+1).zfill(4)}',  # employee_code
                fake.first_name(),
                fake.last_name(),
                fake.email(),
                fake.phone_number(),
                fake.date_of_birth(minimum_age=22, maximum_age=65).isoformat(),
                hire_date.isoformat(),
                random.randint(1, 8),  # department_id
                random.choice(positions),
                random.randint(3000000, 25000000),  # salary
                None,  # manager_id (keyinroq update qilamiz)
                random.randint(1, 14),  # region_id
                experience_years,
                random.choice(education_levels),
                random.choice([1, 1, 1, 1, 0])  # is_active (90% True)
            )
            cursor.execute(
                """INSERT OR IGNORE INTO employees
                   (employee_code, first_name, last_name, email, phone, birth_date, hire_date,
                    department_id, position_title, salary, manager_id, region_id,
                    experience_years, education_level, is_active)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                employee_data
            )

        # Manager_id larni yangilash
        for dept_id in range(1, 9):
            cursor.execute(
                """UPDATE departments SET manager_id = (
                    SELECT employee_id FROM employees
                    WHERE department_id = ? AND is_active = 1
                    ORDER BY hire_date LIMIT 1
                ) WHERE department_id = ?""",
                (dept_id, dept_id)
            )

        # Ba'zi xodimlar uchun manager_id ni o'rnatish
        cursor.execute(
            """UPDATE employees SET manager_id = (
                SELECT manager_id FROM departments
                WHERE departments.department_id = employees.department_id
            ) WHERE employee_id NOT IN (
                SELECT manager_id FROM departments WHERE manager_id IS NOT NULL
            )"""
        )

        conn.commit()
        print("✅ 1-qism: Regions, Categories, Suppliers, Customers, Departments, Employees kiritildi")

        # 7. Products
        product_names = {
            8: ['iPhone 15', 'Samsung Galaxy S24', 'Xiaomi Redmi Note', 'Huawei P60', 'OnePlus 11'],
            9: ['MacBook Pro', 'Dell XPS', 'HP Pavilion', 'Lenovo ThinkPad', 'Asus ZenBook'],
            10: ['LG OLED TV', 'Samsung QLED', 'Sony Bravia', 'TCL Smart TV', 'Hisense 4K'],
            11: ['Ko\'ylak', 'Shimlar', 'Palto', 'Futbolka', 'Kamar'],
            12: ['Ko\'ylak', 'Yubka', 'Bluza', 'Jilet', 'Kurtka'],
            13: ['Bolalar ko\'ylagi', 'Bolalar shimlari', 'Oyoq kiyim', 'Sharf', 'Qo\'lqop'],
            14: ['Blender', 'Mikroto\'lqinli pech', 'Elektr choynagi', 'Toster', 'Oshxona mashinasi'],
            15: ['Karyola', 'Shkaf', 'Stol', 'Kreslo', 'Yastiq']
        }

        brands = ['Samsung', 'Apple', 'Xiaomi', 'LG', 'Sony', 'Dell', 'HP', 'Asus', 'Nike', 'Adidas']
        colors = ['Qora', 'Oq', 'Kulrang', 'Ko\'k', 'Qizil', 'Yashil', 'Sariq', 'Binafsha']

        product_counter = 1
        for category_id, names in product_names.items():
            for name in names:
                for variant in range(random.randint(2, 5)):
                    unit_price = random.randint(100000, 10000000)
                    cost_price = int(unit_price * random.uniform(0.6, 0.8))

                    product_data = (
                        f'PRD{str(product_counter).zfill(6)}',  # product_code
                        f'{name} {random.choice(["Pro", "Max", "Plus", "Standard", "Lite"])}',
                        fake.text(max_nb_chars=200),
                        category_id,
                        random.randint(1, 50),  # supplier_id
                        unit_price,
                        cost_price,
                        random.randint(0, 1000),  # stock_quantity
                        random.randint(5, 50),  # reorder_level
                        round(random.uniform(0.1, 50.0), 3),  # weight
                        f'{random.randint(10, 100)}x{random.randint(10, 100)}x{random.randint(5, 50)}',  # dimensions
                        random.choice(colors),
                        random.choice(brands),
                        f'Model {random.randint(100, 999)}',
                        random.choice([6, 12, 24, 36]),  # warranty_months
                        round(random.uniform(1.5, 5.0), 2),  # rating
                        random.randint(0, 500),  # reviews_count
                        random.choice([1, 1, 1, 0]),  # is_active (85% True)
                        fake.date_between(start_date='-2y', end_date='today').isoformat(),  # launch_date
                        None  # discontinue_date
                    )
                    cursor.execute(
                        """INSERT OR IGNORE INTO products
                           (product_code, product_name, description, category_id, supplier_id,
                            unit_price, cost_price, stock_quantity, reorder_level, weight,
                            dimensions, color, brand, model, warranty_months, rating,
                            reviews_count, is_active, launch_date, discontinue_date)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        product_data
                    )
                    product_counter += 1

        conn.commit()
        print("✅ 2-qism: Products kiritildi")

        # 8. Orders va Order_details
        payment_methods = ['Naqd', 'Plastik karta', 'Bank o\'tkazmasi', 'Online to\'lov']
        order_statuses = ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']

        for i in range(2000):
            order_date = fake.date_between(start_date='-1y', end_date='today')
            required_date = order_date + timedelta(days=random.randint(1, 14))

            # Order asosiy ma'lumotlari
            order_data = (
                f'ORD{str(i+1).zfill(6)}',  # order_number
                random.randint(1, 1000),  # customer_id
                random.randint(1, 200),  # employee_id
                order_date.isoformat(),
                required_date.isoformat(),
                None if random.random() < 0.3 else (order_date + timedelta(days=random.randint(1, 7))).isoformat(),  # shipped_date
                None if random.random() < 0.4 else (order_date + timedelta(days=random.randint(2, 10))).isoformat(),  # delivery_date
                fake.address(),  # shipping_address
                fake.address(),  # billing_address
                random.randint(1, 14),  # region_id
                random.choice(payment_methods),
                random.choice(order_statuses),
                0,  # subtotal (keyinroq hisoblaymiz)
                0,  # tax_amount
                random.randint(50000, 200000),  # shipping_cost
                0,  # discount_amount
                0,  # total_amount
                fake.text(max_nb_chars=100) if random.random() < 0.3 else None  # notes
            )

            cursor.execute(
                """INSERT OR IGNORE INTO orders
                   (order_number, customer_id, employee_id, order_date, required_date,
                    shipped_date, delivery_date, shipping_address, billing_address,
                    region_id, payment_method, order_status, subtotal, tax_amount,
                    shipping_cost, discount_amount, total_amount, notes)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                order_data
            )

            order_id = cursor.lastrowid

            # Agar order_id None bo'lsa, keyingi order ga o'tamiz
            if order_id is None:
                continue

            # Order details
            num_items = random.randint(1, 8)
            subtotal = 0

            for j in range(num_items):
                # Random mahsulot tanlash
                cursor.execute("SELECT product_id, unit_price FROM products WHERE is_active = 1 ORDER BY RANDOM() LIMIT 1")
                product_info = cursor.fetchone()

                if product_info:
                    product_id, base_price = product_info
                    quantity = random.randint(1, 5)
                    unit_price = base_price * random.uniform(0.9, 1.1)  # Narx o'zgarishi
                    discount_percent = random.choice([0, 0, 0, 5, 10, 15, 20])
                    line_total = quantity * unit_price * (1 - discount_percent/100)

                    subtotal += line_total

                    order_detail_data = (
                        order_id,
                        product_id,
                        quantity,
                        unit_price,
                        discount_percent,
                        line_total
                    )

                    cursor.execute(
                        """INSERT OR IGNORE INTO order_details
                           (order_id, product_id, quantity, unit_price, discount_percent, line_total)
                           VALUES (?, ?, ?, ?, ?, ?)""",
                        order_detail_data
                    )

            # Order summalarini yangilash
            tax_amount = subtotal * 0.12  # 12% soliq
            discount_amount = subtotal * random.uniform(0, 0.1)  # 0-10% chegirma

            cursor.execute("SELECT shipping_cost FROM orders WHERE order_id = ?", (order_id,))
            shipping_cost_result = cursor.fetchone()

            if shipping_cost_result is None:
                # Order topilmadi, keyingi order ga o'tamiz
                continue

            shipping_cost = shipping_cost_result[0]

            total_amount = subtotal + tax_amount + shipping_cost - discount_amount

            cursor.execute(
                """UPDATE orders SET
                   subtotal = ?, tax_amount = ?, discount_amount = ?, total_amount = ?
                   WHERE order_id = ?""",
                (subtotal, tax_amount, discount_amount, total_amount, order_id)
            )

        conn.commit()
        print("✅ 3-qism: Orders va Order_details kiritildi")

        # 9. Reviews
        for i in range(1500):
            # Random order_detail tanlash
            cursor.execute(
                """SELECT od.product_id, o.customer_id, o.order_id
                   FROM order_details od
                   JOIN orders o ON od.order_id = o.order_id
                   WHERE o.order_status = 'Delivered'
                   ORDER BY RANDOM() LIMIT 1"""
            )

            order_info = cursor.fetchone()
            if order_info:
                product_id, customer_id, order_id = order_info

                review_data = (
                    product_id,
                    customer_id,
                    order_id,
                    random.randint(1, 5),  # rating
                    fake.sentence(nb_words=random.randint(3, 8)),  # review_title
                    fake.text(max_nb_chars=500) if random.random() < 0.7 else None,  # review_text
                    fake.date_between(start_date='-6m', end_date='today').isoformat(),  # review_date
                    random.choice([1, 1, 0]),  # is_verified (70% True)
                    random.randint(0, 50)  # helpful_votes
                )

                cursor.execute(
                    """INSERT OR IGNORE INTO reviews
                       (product_id, customer_id, order_id, rating, review_title,
                        review_text, review_date, is_verified, helpful_votes)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    review_data
                )

        # Mahsulotlar uchun o'rtacha rating va review count ni yangilash
        cursor.execute(
            """UPDATE products SET
               rating = (
                   SELECT ROUND(AVG(rating), 2)
                   FROM reviews
                   WHERE reviews.product_id = products.product_id
               ),
               reviews_count = (
                   SELECT COUNT(*)
                   FROM reviews
                   WHERE reviews.product_id = products.product_id
               )
               WHERE product_id IN (SELECT DISTINCT product_id FROM reviews)"""
        )

        # Mijozlar uchun total_spent ni yangilash
        cursor.execute(
            """UPDATE customers SET total_spent = (
                   SELECT COALESCE(SUM(total_amount), 0)
                   FROM orders
                   WHERE orders.customer_id = customers.customer_id
               )
               WHERE customer_id IN (SELECT DISTINCT customer_id FROM orders)"""
        )

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ 4-qism: Reviews kiritildi va yangilanishlar amalga oshirildi")
        print("🎉 Barcha test ma'lumotlari muvaffaqiyatli kiritildi!")

        return True

    except Exception as e:
        print(f"❌ Ma'lumotlar kiritishda xatolik: {e}")
        return False

def create_views():
    """
    Ko'p ishlatiladigan so'rovlar uchun VIEW lar yaratish
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print("👁️ VIEW lar yaratilmoqda...")

        # 1. Customer summary view
        cursor.execute("""
            CREATE VIEW IF NOT EXISTS customer_summary AS
            SELECT
                c.customer_id,
                c.first_name || ' ' || c.last_name as full_name,
                c.email,
                c.customer_type,
                r.region_name,
                c.registration_date,
                COUNT(DISTINCT o.order_id) as total_orders,
                COALESCE(SUM(o.total_amount), 0) as total_spent,
                COALESCE(AVG(o.total_amount), 0) as avg_order_value,
                MAX(o.order_date) as last_order_date
            FROM customers c
            LEFT JOIN regions r ON c.region_id = r.region_id
            LEFT JOIN orders o ON c.customer_id = o.customer_id
            GROUP BY c.customer_id, c.first_name, c.last_name, c.email,
                     c.customer_type, r.region_name, c.registration_date;
        """)

        # 2. Product summary view
        cursor.execute("""
            CREATE VIEW IF NOT EXISTS product_summary AS
            SELECT
                p.product_id,
                p.product_name,
                p.product_code,
                c.category_name,
                s.company_name as supplier_name,
                p.unit_price,
                p.stock_quantity,
                p.rating,
                p.reviews_count,
                COALESCE(order_stats.total_sold, 0) as total_sold,
                COALESCE(order_stats.total_revenue, 0) as total_revenue
            FROM products p
            LEFT JOIN categories c ON p.category_id = c.category_id
            LEFT JOIN suppliers s ON p.supplier_id = s.supplier_id
            LEFT JOIN (
                SELECT
                    product_id,
                    SUM(quantity) as total_sold,
                    SUM(line_total) as total_revenue
                FROM order_details
                GROUP BY product_id
            ) order_stats ON p.product_id = order_stats.product_id;
        """)

        # 3. Employee performance view
        cursor.execute("""
            CREATE VIEW IF NOT EXISTS employee_performance AS
            SELECT
                e.employee_id,
                e.first_name || ' ' || e.last_name as full_name,
                e.employee_code,
                d.department_name,
                e.position_title,
                e.salary,
                r.region_name,
                COUNT(DISTINCT o.order_id) as orders_processed,
                COALESCE(SUM(o.total_amount), 0) as total_sales,
                COALESCE(AVG(o.total_amount), 0) as avg_order_value,
                CASE
                    WHEN e.salary > 0 THEN COALESCE(SUM(o.total_amount), 0) / e.salary
                    ELSE 0
                END as sales_to_salary_ratio
            FROM employees e
            LEFT JOIN departments d ON e.department_id = d.department_id
            LEFT JOIN regions r ON e.region_id = r.region_id
            LEFT JOIN orders o ON e.employee_id = o.employee_id
            GROUP BY e.employee_id, e.first_name, e.last_name, e.employee_code,
                     d.department_name, e.position_title, e.salary, r.region_name;
        """)

        # 4. Sales by region view
        cursor.execute("""
            CREATE VIEW IF NOT EXISTS sales_by_region AS
            SELECT
                r.region_id,
                r.region_name,
                COUNT(DISTINCT o.order_id) as total_orders,
                COUNT(DISTINCT o.customer_id) as unique_customers,
                COALESCE(SUM(o.total_amount), 0) as total_revenue,
                COALESCE(AVG(o.total_amount), 0) as avg_order_value,
                COUNT(DISTINCT CASE WHEN o.order_status = 'Delivered' THEN o.order_id END) as delivered_orders
            FROM regions r
            LEFT JOIN orders o ON r.region_id = o.region_id
            GROUP BY r.region_id, r.region_name;
        """)

        conn.commit()
        cursor.close()
        conn.close()

        print("✅ Barcha VIEW lar yaratildi")
        return True

    except Exception as e:
        print(f"❌ VIEW lar yaratishda xatolik: {e}")
        return False

def main():
    """
    Asosiy funksiya
    """
    print("🚀 SQLite JOIN va Subquery ma'lumotlar bazasi yaratish boshlandi...")
    print("=" * 70)

    # 1. Ma'lumotlar bazasi va jadvallar yaratish
    if not create_database_and_tables():
        return False

    # 2. Indekslar yaratish
    if not create_indexes():
        return False

    # 3. Test ma'lumotlarini kiritish
    if not insert_sample_data():
        return False

    # 4. VIEW lar yaratish
    if not create_views():
        return False

    print("\n" + "=" * 70)
    print("🎉 SQLite JOIN va Subquery ma'lumotlar bazasi tayyor!")
    print("\n📊 Yaratilgan jadvallar:")
    print("   • regions (14 ta viloyat)")
    print("   • categories (15 ta kategoriya)")
    print("   • suppliers (50 ta yetkazib beruvchi)")
    print("   • customers (1000 ta mijoz)")
    print("   • departments (8 ta bo'lim)")
    print("   • employees (200 ta xodim)")
    print("   • products (~100 ta mahsulot)")
    print("   • orders (2000 ta buyurtma)")
    print("   • order_details (ko'p qatorlar)")
    print("   • reviews (1500 ta sharh)")
    print("\n🔗 Ma'lumotlar bazasi fayli:")
    print(f"   {DB_PATH}")
    print("\n✅ Endi lecture.ipynb faylini ishga tushiring!")

    return True

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Jarayon foydalanuvchi tomonidan to'xtatildi")
    except Exception as e:
        print(f"\n❌ Kutilmagan xatolik: {e}")