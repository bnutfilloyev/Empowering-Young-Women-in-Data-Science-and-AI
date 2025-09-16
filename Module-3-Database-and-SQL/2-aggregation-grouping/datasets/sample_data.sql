-- PostgreSQL Namuna Ma'lumotlar
-- =============================
-- Ushbu fayl PostgreSQL jadvallar uchun namuna ma'lumotlarni o'z ichiga oladi.
-- Ushbu ma'lumotlar agregatsiya va guruhlash darslari uchun mo'ljallangan.

-- Database yaratish
CREATE DATABASE lesson_aggregation 
    OWNER data_scientist
    ENCODING 'UTF8';

-- Database ga ulanish
\c lesson_aggregation;

-- Extensions yaratish
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Bo'limlar jadvali
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100),
    budget DECIMAL(12,2),
    manager_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Namuna mijozlar ma'lumotlari
INSERT INTO customers (first_name, last_name, email, phone, birth_date, gender, city, region, registration_date, customer_type, total_spent, order_count, is_active) VALUES
('Akmal', 'Toshev', 'akmal.toshev@email.uz', '+998901234567', '1985-05-15', 'Male', 'Toshkent', 'Toshkent', '2023-01-15', 'Premium', 5500000, 25, TRUE),
('Dilnoza', 'Karimova', 'dilnoza.karimova@email.uz', '+998902345678', '1990-08-22', 'Female', 'Samarqand', 'Samarqand', '2023-02-10', 'Gold', 3200000, 18, TRUE),
('Jahongir', 'Abdullayev', 'jahongir.abdullayev@email.uz', '+998903456789', '1988-12-03', 'Male', 'Buxoro', 'Buxoro', '2023-03-05', 'Silver', 1800000, 12, TRUE),
('Sevara', 'Rahimova', 'sevara.rahimova@email.uz', '+998904567890', '1992-03-18', 'Female', 'Andijon', 'Andijon', '2023-01-20', 'Regular', 950000, 8, TRUE),
('Islom', 'Yunusov', 'islom.yunusov@email.uz', '+998905678901', '1987-07-12', 'Male', 'Namangan', 'Namangan', '2023-04-12', 'Bronze', 650000, 5, TRUE);

-- Mahsulotlar jadvali
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

-- Namuna mahsulotlar ma'lumotlari
INSERT INTO products (product_name, category_id, price, cost, stock_quantity, supplier, rating, reviews_count, weight_kg, is_available, launch_date) VALUES
('iPhone 14 Pro', 1, 15000000, 9000000, 50, 'TechCorp LLC', 4.8, 1250, 0.206, TRUE, '2023-01-15'),
('Samsung Galaxy S23', 1, 12000000, 7200000, 35, 'TechCorp LLC', 4.6, 890, 0.168, TRUE, '2023-02-20'),
('Cotton T-Shirt', 2, 150000, 90000, 200, 'Fashion House', 4.2, 345, 0.2, TRUE, '2023-01-10'),
('Jeans Pants', 2, 350000, 210000, 150, 'Fashion House', 4.4, 567, 0.8, TRUE, '2023-02-05'),
('Sofa Set', 3, 8500000, 5100000, 25, 'Home & Living', 4.5, 123, 85.5, TRUE, '2023-03-01'),
('Python Programming Book', 4, 120000, 72000, 80, 'BookWorld', 4.9, 234, 0.5, TRUE, '2023-01-05'),
('Football', 5, 85000, 51000, 120, 'SportZone', 4.3, 167, 0.45, TRUE, '2023-02-15'),
('Organic Rice 5kg', 6, 55000, 33000, 300, 'FreshMart', 4.1, 89, 5.0, TRUE, '2023-01-20'),
('Vitamin Complex', 7, 95000, 57000, 180, 'HealthPlus', 4.4, 145, 0.1, TRUE, '2023-03-10'),
('Car Battery', 8, 750000, 450000, 45, 'AutoParts Co', 4.2, 78, 18.5, TRUE, '2023-02-25');

-- Buyurtmalar jadvali
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
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
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Namuna buyurtmalar ma'lumotlari
INSERT INTO orders (customer_id, order_date, delivery_date, total_amount, discount_amount, tax_amount, shipping_cost, payment_method, order_status, delivery_city, delivery_region) VALUES
(1, '2024-01-15', '2024-01-18', 15500000, 500000, 1860000, 25000, 'Card', 'Delivered', 'Toshkent', 'Toshkent'),
(2, '2024-01-20', '2024-01-23', 12350000, 200000, 1482000, 30000, 'UzCard', 'Delivered', 'Samarqand', 'Samarqand'),
(3, '2024-01-25', '2024-01-28', 8650000, 150000, 1038000, 45000, 'Click', 'Shipped', 'Buxoro', 'Buxoro'),
(1, '2024-02-01', '2024-02-05', 635000, 35000, 76200, 15000, 'PayMe', 'Delivered', 'Toshkent', 'Toshkent'),
(4, '2024-02-10', '2024-02-14', 485000, 15000, 58200, 20000, 'Cash', 'Processing', 'Andijon', 'Andijon'),
(5, '2024-02-15', '2024-02-18', 270000, 0, 32400, 25000, 'Humo', 'Delivered', 'Namangan', 'Namangan'),
(2, '2024-02-20', '2024-02-24', 1250000, 50000, 150000, 30000, 'Bank Transfer', 'Delivered', 'Samarqand', 'Samarqand'),
(3, '2024-02-25', '2024-03-01', 895000, 45000, 107400, 20000, 'Card', 'Cancelled', 'Buxoro', 'Buxoro'),
(1, '2024-03-01', '2024-03-05', 1850000, 100000, 222000, 35000, 'UzCard', 'Delivered', 'Toshkent', 'Toshkent'),
(4, '2024-03-10', '2024-03-15', 650000, 25000, 78000, 15000, 'Click', 'Shipped', 'Andijon', 'Andijon');

-- Sotuvlar jadvali
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
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_sales_product ON sales(product_id);
CREATE INDEX idx_sales_date ON sales(sale_date);
CREATE INDEX idx_customers_region ON customers(region);

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
    CONCAT(cust.first_name, ' ', cust.last_name) as customer_name,
    o.delivery_region
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
JOIN orders o ON s.order_id = o.order_id
JOIN customers cust ON o.customer_id = cust.customer_id;

-- Statistika ko'rish uchun funksiya
CREATE OR REPLACE FUNCTION get_table_stats()
RETURNS TABLE(table_name TEXT, row_count BIGINT) AS $$
BEGIN
    RETURN QUERY
    SELECT 'departments'::TEXT, COUNT(*)::BIGINT FROM departments
    UNION ALL
    SELECT 'categories'::TEXT, COUNT(*)::BIGINT FROM categories
    UNION ALL
    SELECT 'customers'::TEXT, COUNT(*)::BIGINT FROM customers
    UNION ALL
    SELECT 'products'::TEXT, COUNT(*)::BIGINT FROM products
    UNION ALL
    SELECT 'orders'::TEXT, COUNT(*)::BIGINT FROM orders
    UNION ALL
    SELECT 'sales'::TEXT, COUNT(*)::BIGINT FROM sales;
END;
$$ LANGUAGE plpgsql;

-- Qo'shimcha foydalanuvchi yaratish (agar kerak bo'lsa)
-- CREATE USER student WITH PASSWORD 'student123';
-- GRANT SELECT ON ALL TABLES IN SCHEMA public TO student;

-- Ma'lumotlar bazasi tayyor!
SELECT 'PostgreSQL ma''lumotlar bazasi muvaffaqiyatli yaratildi!' as status;
