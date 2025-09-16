-- SQLite Namuna Ma'lumotlar
-- ============================
-- Ushbu fayl SQLite jadvallar uchun namuna ma'lumotlarni o'z ichiga oladi.
-- Ushbu ma'lumotlar agregatsiya va guruhlash darslari uchun mo'ljallangan.

-- Bo'limlar jadvali
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_name TEXT NOT NULL UNIQUE,
    location TEXT,
    budget REAL,
    manager_name TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Bo'limlar ma'lumotlari
INSERT INTO departments (department_name, location, budget, manager_name) VALUES
('IT', 'Toshkent', 250000, 'Alisher Karimov'),
('Marketing', 'Toshkent', 180000, 'Malika Abdullayeva'),
('Sales', 'Samarqand', 220000, 'Bobur Yunusov'),
('HR', 'Toshkent', 120000, 'Nilufar Rahimova'),
('Finance', 'Toshkent', 200000, 'Jasur Toshev'),
('Operations', 'Andijon', 160000, 'Gulnara Hakimova'),
('Research', 'Buxoro', 300000, 'Farrux Salimov'),
('Support', 'Namangan', 100000, 'Zarina Umarova');

-- Kategoriyalar jadvali
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Kategoriyalar ma'lumotlari
INSERT INTO categories (category_name, description) VALUES
('Elektronika', 'Elektronik mahsulotlar va gadgetlar'),
('Kiyim', 'Erkaklar va ayollar kiyimlari'),
('Uy-joy', 'Uy uchun buyumlar va mebel'),
('Kitoblar', 'Badiiy va ilmiy adabiyot'),
('Sport', 'Sport anjomlari va aksessuarlar'),
('Oziq-ovqat', 'Oziq-ovqat mahsulotlari'),
('Salomatlik', 'Tibbiy va kosmetik mahsulotlar'),
('Avtomobil', 'Avtomobil ehtiyot qismlari'),
('Bolalar', 'Bolalar uchun mahsulotlar'),
('Hobbi', 'Dam olish va hobbilar uchun');

-- Mijozlar jadvali
CREATE TABLE customers (
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
    customer_type TEXT,
    total_spent REAL DEFAULT 0,
    order_count INTEGER DEFAULT 0,
    is_active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Namuna mijozlar ma'lumotlari
INSERT INTO customers (first_name, last_name, email, phone, birth_date, gender, city, region, registration_date, customer_type, total_spent, order_count, is_active) VALUES
('Akmal', 'Toshev', 'akmal.toshev@email.uz', '+998901234567', '1985-05-15', 'Male', 'Toshkent', 'Toshkent', '2023-01-15', 'Premium', 5500000, 25, 1),
('Dilnoza', 'Karimova', 'dilnoza.karimova@email.uz', '+998902345678', '1990-08-22', 'Female', 'Samarqand', 'Samarqand', '2023-02-10', 'Gold', 3200000, 18, 1),
('Jahongir', 'Abdullayev', 'jahongir.abdullayev@email.uz', '+998903456789', '1988-12-03', 'Male', 'Buxoro', 'Buxoro', '2023-03-05', 'Silver', 1800000, 12, 1),
('Sevara', 'Rahimova', 'sevara.rahimova@email.uz', '+998904567890', '1992-03-18', 'Female', 'Andijon', 'Andijon', '2023-01-20', 'Regular', 950000, 8, 1),
('Islom', 'Yunusov', 'islom.yunusov@email.uz', '+998905678901', '1987-07-12', 'Male', 'Namangan', 'Namangan', '2023-04-12', 'Bronze', 650000, 5, 1);

-- Xodimlar jadvali
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    department_id INTEGER,
    position TEXT,
    salary REAL,
    hire_date DATE,
    age INTEGER,
    email TEXT,
    phone TEXT,
    is_active INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Xodimlar ma'lumotlari
INSERT INTO employees (first_name, last_name, department_id, position, salary, hire_date, age, email, phone, is_active) VALUES
('Alisher', 'Karimov', 1, 'IT Director', 8000000, '2020-01-15', 35, 'alisher.karimov@company.uz', '+998901234501', 1),
('Malika', 'Abdullayeva', 2, 'Marketing Manager', 6500000, '2021-03-10', 32, 'malika.abdullayeva@company.uz', '+998902345602', 1),
('Bobur', 'Yunusov', 3, 'Sales Manager', 7000000, '2019-07-20', 38, 'bobur.yunusov@company.uz', '+998903456703', 1),
('Nilufar', 'Rahimova', 4, 'HR Specialist', 4500000, '2022-01-05', 29, 'nilufar.rahimova@company.uz', '+998904567804', 1),
('Jasur', 'Toshev', 5, 'Finance Analyst', 6000000, '2020-09-12', 34, 'jasur.toshev@company.uz', '+998905678905', 1),
('Gulnara', 'Hakimova', 6, 'Operations Manager', 5500000, '2021-11-08', 31, 'gulnara.hakimova@company.uz', '+998906789006', 1),
('Farrux', 'Salimov', 7, 'Research Scientist', 9000000, '2018-05-22', 42, 'farrux.salimov@company.uz', '+998907890107', 1),
('Zarina', 'Umarova', 8, 'Support Specialist', 3500000, '2023-02-14', 27, 'zarina.umarova@company.uz', '+998908901208', 1);

-- Mahsulotlar jadvali
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category_id INTEGER,
    price REAL,
    cost REAL,
    stock_quantity INTEGER,
    supplier TEXT,
    rating REAL,
    reviews_count INTEGER,
    weight_kg REAL,
    is_available INTEGER DEFAULT 1,
    launch_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Namuna mahsulotlar ma'lumotlari
INSERT INTO products (product_name, category_id, price, cost, stock_quantity, supplier, rating, reviews_count, weight_kg, is_available, launch_date) VALUES
('iPhone 14 Pro', 1, 15000000, 9000000, 50, 'TechCorp LLC', 4.8, 1250, 0.206, 1, '2023-01-15'),
('Samsung Galaxy S23', 1, 12000000, 7200000, 35, 'TechCorp LLC', 4.6, 890, 0.168, 1, '2023-02-20'),
('Cotton T-Shirt', 2, 150000, 90000, 200, 'Fashion House', 4.2, 345, 0.2, 1, '2023-01-10'),
('Jeans Pants', 2, 350000, 210000, 150, 'Fashion House', 4.4, 567, 0.8, 1, '2023-02-05'),
('Sofa Set', 3, 8500000, 5100000, 25, 'Home & Living', 4.5, 123, 85.5, 1, '2023-03-01'),
('Python Programming Book', 4, 120000, 72000, 80, 'BookWorld', 4.9, 234, 0.5, 1, '2023-01-05'),
('Football', 5, 85000, 51000, 120, 'SportZone', 4.3, 167, 0.45, 1, '2023-02-15'),
('Organic Rice 5kg', 6, 55000, 33000, 300, 'FreshMart', 4.1, 89, 5.0, 1, '2023-01-20'),
('Vitamin Complex', 7, 95000, 57000, 180, 'HealthPlus', 4.4, 145, 0.1, 1, '2023-03-10'),
('Car Battery', 8, 750000, 450000, 45, 'AutoParts Co', 4.2, 78, 18.5, 1, '2023-02-25');

-- Buyurtmalar jadvali
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    employee_id INTEGER,
    order_date DATE,
    delivery_date DATE,
    total_amount REAL,
    discount_amount REAL DEFAULT 0,
    tax_amount REAL,
    shipping_cost REAL,
    payment_method TEXT,
    order_status TEXT,
    delivery_city TEXT,
    delivery_region TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Namuna buyurtmalar ma'lumotlari
INSERT INTO orders (customer_id, employee_id, order_date, delivery_date, total_amount, discount_amount, tax_amount, shipping_cost, payment_method, order_status, delivery_city, delivery_region) VALUES
(1, 3, '2024-01-15', '2024-01-18', 15500000, 500000, 1860000, 25000, 'Card', 'Delivered', 'Toshkent', 'Toshkent'),
(2, 3, '2024-01-20', '2024-01-23', 12350000, 200000, 1482000, 30000, 'UzCard', 'Delivered', 'Samarqand', 'Samarqand'),
(3, 3, '2024-01-25', '2024-01-28', 8650000, 150000, 1038000, 45000, 'Click', 'Shipped', 'Buxoro', 'Buxoro'),
(1, 2, '2024-02-01', '2024-02-05', 635000, 35000, 76200, 15000, 'PayMe', 'Delivered', 'Toshkent', 'Toshkent'),
(4, 2, '2024-02-10', '2024-02-14', 485000, 15000, 58200, 20000, 'Cash', 'Processing', 'Andijon', 'Andijon'),
(5, 2, '2024-02-15', '2024-02-18', 270000, 0, 32400, 25000, 'Humo', 'Delivered', 'Namangan', 'Namangan'),
(2, 3, '2024-02-20', '2024-02-24', 1250000, 50000, 150000, 30000, 'Bank Transfer', 'Delivered', 'Samarqand', 'Samarqand'),
(3, 3, '2024-02-25', '2024-03-01', 895000, 45000, 107400, 20000, 'Card', 'Cancelled', 'Buxoro', 'Buxoro'),
(1, 1, '2024-03-01', '2024-03-05', 1850000, 100000, 222000, 35000, 'UzCard', 'Delivered', 'Toshkent', 'Toshkent'),
(4, 1, '2024-03-10', '2024-03-15', 650000, 25000, 78000, 15000, 'Click', 'Shipped', 'Andijon', 'Andijon');

-- Sotuvlar jadvali
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    total_price REAL,
    discount_percent REAL DEFAULT 0,
    profit_margin REAL,
    sale_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Namuna sotuvlar ma'lumotlari
INSERT INTO sales (order_id, product_id, quantity, unit_price, total_price, discount_percent, profit_margin, sale_date) VALUES
(1, 1, 1, 15000000, 15000000, 3.0, 5850000, '2024-01-15'),
(1, 3, 2, 150000, 300000, 0, 120000, '2024-01-15'),
(2, 2, 1, 12000000, 12000000, 1.5, 4680000, '2024-01-20'),
(2, 4, 1, 350000, 350000, 0, 140000, '2024-01-20'),
(3, 5, 1, 8500000, 8500000, 1.5, 3315000, '2024-01-25'),
(3, 6, 1, 120000, 120000, 0, 48000, '2024-01-25'),
(4, 7, 3, 85000, 255000, 5.0, 99450, '2024-02-01'),
(4, 8, 4, 55000, 220000, 5.0, 85800, '2024-02-01'),
(4, 9, 1, 95000, 95000, 0, 38000, '2024-02-01'),
(5, 3, 2, 150000, 300000, 0, 120000, '2024-02-10'),
(5, 7, 1, 85000, 85000, 0, 34000, '2024-02-10'),
(5, 8, 1, 55000, 55000, 0, 22000, '2024-02-10'),
(6, 6, 2, 120000, 240000, 0, 96000, '2024-02-15'),
(7, 10, 1, 750000, 750000, 2.0, 292500, '2024-02-20'),
(7, 2, 1, 12000000, 12000000, 4.0, 4680000, '2024-02-20'),
(9, 1, 1, 15000000, 15000000, 5.0, 5850000, '2024-03-01'),
(9, 4, 2, 350000, 700000, 0, 280000, '2024-03-01'),
(10, 3, 3, 150000, 450000, 2.0, 171000, '2024-03-10'),
(10, 8, 2, 55000, 110000, 0, 44000, '2024-03-10');

-- Indexlar yaratish (performance uchun)
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_products_price ON products(price);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_employee ON orders(employee_id);
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_sales_product ON sales(product_id);
CREATE INDEX idx_sales_date ON sales(sale_date);
CREATE INDEX idx_customers_region ON customers(region);
CREATE INDEX idx_employees_department ON employees(department_id);

-- Views yaratish (qulaylik uchun)
CREATE VIEW sales_summary AS
SELECT
    s.sale_id,
    s.order_id,
    p.product_name,
    c.category_name,
    s.quantity,
    s.unit_price,
    s.total_price,
    s.profit_margin,
    s.sale_date,
    o.customer_id,
    (cust.first_name || ' ' || cust.last_name) as customer_name,
    o.delivery_region
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
JOIN orders o ON s.order_id = o.order_id
JOIN customers cust ON o.customer_id = cust.customer_id;

-- Product summary view
CREATE VIEW product_summary AS
SELECT
    p.product_id,
    p.product_name,
    c.category_name,
    p.price,
    p.stock_quantity,
    p.rating,
    p.reviews_count,
    (p.price - p.cost) as profit_per_unit,
    (p.stock_quantity * p.price) as total_value
FROM products p
JOIN categories c ON p.category_id = c.category_id;

-- Customer summary view
CREATE VIEW customer_summary AS
SELECT
    c.customer_id,
    (c.first_name || ' ' || c.last_name) as full_name,
    c.region,
    c.customer_type,
    c.total_spent,
    c.order_count,
    ROUND(c.total_spent * 1.0 / c.order_count, 0) as avg_order_value,
    c.registration_date
FROM customers c;

-- Employee performance view
CREATE VIEW employee_performance AS
SELECT
    e.employee_id,
    (e.first_name || ' ' || e.last_name) as full_name,
    d.department_name,
    COUNT(o.order_id) as total_orders,
    ROUND(SUM(o.total_amount), 0) as total_sales,
    ROUND(AVG(o.total_amount), 0) as avg_order_value,
    COUNT(DISTINCT o.customer_id) as unique_customers
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
LEFT JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name, d.department_name;

-- Ma'lumotlar bazasi tayyor!
SELECT 'SQLite ma''lumotlar bazasi muvaffaqiyatli yaratildi!' as status;