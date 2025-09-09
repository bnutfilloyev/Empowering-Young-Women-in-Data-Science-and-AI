import sqlite3
import pandas as pd
import random
from datetime import datetime, timedelta

# Xodimlar ma'lumotlari uchun ma'lumotlar
names = [
    'Alisher Karimov', 'Malika Rahimova', 'Bobur Tursunov', 'Nilufar Usmanova', 
    'Sherzod Nazarov', 'Gulnara Abdullayeva', 'Jasur Hakimov', 'Sevara Isroilova',
    'Otabek Salimov', 'Madina Yusupova', 'Farrux Qosimov', 'Zulfiya Mirzayeva',
    'Davron Ergashev', 'Munira Sharipova', 'Sardor Ibragimov', 'Nigora Kamilova',
    'Rustam Jurayev', 'Dilfuza Nasriddinova', 'Akmal Raxmonov', 'Kamila Xolmatova',
    'Nodir Safarov', 'Gulshan Qurbanova', 'Umid Sultonov', 'Zarina Oripova',
    'Jamshid Kamolov', 'Shakhnoza Azimova', 'Eldor Hasanov', 'Nargiza Yuldasheva',
    'Anvar Muminov', 'Zilola Buriyeva', 'Muzaffar Tojibaev', 'Feruza Normatova',
    'Ulugbek Haydarov', 'Umida Rajabova', 'Botir Xudaykulov', 'Makhliyo Saidova',
    'Jahongir Iskandarov', 'Dildora Mamatova', 'Sarvar Ergashev', 'Gulnoza Aminova'
]

positions = [
    'Data Scientist', 'Software Engineer', 'Project Manager', 'Business Analyst',
    'DevOps Engineer', 'UI/UX Designer', 'Quality Assurance', 'Database Administrator',
    'System Administrator', 'Product Manager', 'Marketing Specialist', 'HR Manager',
    'Financial Analyst', 'Sales Manager', 'Customer Support', 'Content Writer'
]

departments = [
    'IT', 'Marketing', 'Sales', 'HR', 'Finance', 'Operations', 'R&D', 'Support'
]

cities = [
    'Toshkent', 'Samarqand', 'Buxoro', 'Andijon', 'Namangan', 'Farg\'ona', 
    'Qashqadaryo', 'Surxondaryo', 'Jizzax', 'Navoiy', 'Xorazm', 'Qoraqalpog\'iston'
]

# Xodimlar ma'lumotlar bazasini yaratish
def create_employees_db():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    
    # Jadval yaratish
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        department TEXT NOT NULL,
        salary INTEGER NOT NULL,
        hire_date DATE NOT NULL,
        age INTEGER NOT NULL,
        city TEXT NOT NULL
    )
    ''')
    
    # Ma'lumotlar qo'shish
    employees_data = []
    for i in range(100):
        name = random.choice(names)
        position = random.choice(positions)
        department = random.choice(departments)
        salary = random.randint(300, 2000) * 1000  # 300k - 2M so'm
        
        # Hire date (so'nggi 5 yil ichida)
        start_date = datetime.now() - timedelta(days=5*365)
        random_days = random.randint(0, 5*365)
        hire_date = start_date + timedelta(days=random_days)
        
        age = random.randint(22, 55)
        city = random.choice(cities)
        
        employees_data.append((name, position, department, salary, hire_date.strftime('%Y-%m-%d'), age, city))
    
    cursor.executemany('''
    INSERT INTO employees (name, position, department, salary, hire_date, age, city)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', employees_data)
    
    conn.commit()
    conn.close()
    print("✅ employees.db yaratildi - 100 ta xodim ma'lumoti")

# Mahsulotlar ma'lumotlar bazasini yaratish
def create_products_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Jadval yaratish
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price DECIMAL(10,2) NOT NULL,
        stock INTEGER NOT NULL,
        supplier TEXT NOT NULL,
        rating DECIMAL(3,2),
        description TEXT
    )
    ''')
    
    # Mahsulot ma'lumotlari
    categories = ['Elektronika', 'Kiyim', 'Kitoblar', 'Sport', 'Uy-joy', 'Oziq-ovqat', 'Avtomobil', 'Go\'zallik']
    suppliers = ['Samsung', 'Apple', 'Xiaomi', 'Nike', 'Adidas', 'Zara', 'H&M', 'IKEA', 'LG', 'Sony']
    
    products_data = []
    for i in range(150):
        # Kategoriya asosida mahsulot nomi
        category = random.choice(categories)
        if category == 'Elektronika':
            names_list = ['Smartphone', 'Laptop', 'Televizor', 'Quloqchin', 'Planshet', 'Smart Watch']
        elif category == 'Kiyim':
            names_list = ['Ko\'ylak', 'Shim', 'Kurtka', 'Futbolka', 'Etik', 'Kepka']
        elif category == 'Kitoblar':
            names_list = ['Roman', 'Darslik', 'Ilmiy kitob', 'Bolalar kitobi', 'Tarix', 'Dasturlash']
        elif category == 'Sport':
            names_list = ['To\'p', 'Krossovka', 'Velosiped', 'Gimnastika anjomi', 'Suzish kostyumi']
        else:
            names_list = [f'{category} mahsuloti']
        
        name = f"{random.choice(names_list)} #{i+1}"
        price = round(random.uniform(10, 1000), 2)
        stock = random.randint(0, 500)
        supplier = random.choice(suppliers)
        rating = round(random.uniform(1.0, 5.0), 2)
        description = f"{category} kategoriyasidagi sifatli mahsulot"
        
        products_data.append((name, category, price, stock, supplier, rating, description))
    
    cursor.executemany('''
    INSERT INTO products (name, category, price, stock, supplier, rating, description)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', products_data)
    
    conn.commit()
    conn.close()
    print("✅ products.db yaratildi - 150 ta mahsulot ma'lumoti")

# Talabalar ma'lumotlar bazasini yaratish
def create_students_db():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    # Jadval yaratish
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        faculty TEXT NOT NULL,
        course INTEGER NOT NULL,
        gpa DECIMAL(3,2) NOT NULL,
        city TEXT NOT NULL,
        age INTEGER NOT NULL,
        scholarship BOOLEAN DEFAULT FALSE
    )
    ''')
    
    faculties = [
        'Informatika', 'Matematika', 'Fizika', 'Kimyo', 'Biologiya', 
        'Iqtisodiyot', 'Huquq', 'Tibbiyot', 'Muhandislik', 'Pedagogika'
    ]
    
    students_data = []
    for i in range(80):
        name = random.choice(names)
        faculty = random.choice(faculties)
        course = random.randint(1, 4)
        gpa = round(random.uniform(2.5, 4.0), 2)
        city = random.choice(cities)
        age = random.randint(18, 25)
        scholarship = gpa >= 3.5  # 3.5 dan yuqori GPA bo'lsa stipendiya
        
        students_data.append((name, faculty, course, gpa, city, age, scholarship))
    
    cursor.executemany('''
    INSERT INTO students (name, faculty, course, gpa, city, age, scholarship)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', students_data)
    
    conn.commit()
    conn.close()
    print("✅ students.db yaratildi - 80 ta talaba ma'lumoti")

if __name__ == "__main__":
    print("🗄️ Ma'lumotlar bazalarini yaratish boshlandi...")
    create_employees_db()
    create_products_db()
    create_students_db()
    print("\n🎉 Barcha ma'lumotlar bazalari muvaffaqiyatli yaratildi!")
    print("\nMa'lumotlar bazalari:")
    print("📊 employees.db - Xodimlar (100 ta)")
    print("🛍️ products.db - Mahsulotlar (150 ta)")  
    print("🎓 students.db - Talabalar (80 ta)")
