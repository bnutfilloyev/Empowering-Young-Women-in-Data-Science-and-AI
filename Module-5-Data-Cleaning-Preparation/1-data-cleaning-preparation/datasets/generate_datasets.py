"""
Sample Dataset Generator for Data Cleaning Practice

Bu script amaliy mashg'ulotlar uchun turli xil muammoli ma'lumotlar yaratadi.
"""

import pandas as pd
import numpy as np

def create_employee_dataset(n_rows=100, missing_rate=0.15, duplicate_rate=0.05):
    """
    Xodimlar ma'lumotlari yaratish (missing values va duplicates bilan)
    
    Parameters:
    -----------
    n_rows : int
        Qatorlar soni
    missing_rate : float
        Missing values foizi (0-1)
    duplicate_rate : float
        Takroriy qatorlar foizi (0-1)
    """
    np.random.seed(42)
    
    # Asosiy ma'lumotlar
    names = ['Ali', 'Vali', 'Sardor', 'Malika', 'Nigora', 'Aziz', 'Dildora', 
             'Jasur', 'Zarina', 'Kamol', 'Shoira', 'Anvar', 'Gulnora', 'Bobur']
    
    departments = ['IT', 'HR', 'Marketing', 'Finance', 'Sales']
    positions = ['Junior', 'Middle', 'Senior', 'Lead', 'Manager']
    cities = ['Toshkent', 'Samarqand', 'Buxoro', "Farg'ona", 'Namangan']
    
    data = {
        'ID': range(1, n_rows + 1),
        'Ism': np.random.choice(names, n_rows),
        'Yosh': np.random.randint(22, 50, n_rows),
        'Jins': np.random.choice(['Erkak', 'Ayol'], n_rows),
        'Bo\'lim': np.random.choice(departments, n_rows),
        'Lavozim': np.random.choice(positions, n_rows),
        'Ish_Tajribasi': np.random.randint(0, 20, n_rows),
        'Maosh': np.random.randint(3000000, 30000000, n_rows),
        'Shahar': np.random.choice(cities, n_rows),
        'Email': [f"user{i}@company.uz" for i in range(1, n_rows + 1)]
    }
    
    df = pd.DataFrame(data)
    
    # Missing values qo'shish
    for col in ['Yosh', 'Bo\'lim', 'Lavozim', 'Ish_Tajribasi', 'Maosh', 'Shahar', 'Email']:
        n_missing = int(len(df) * missing_rate * np.random.random())
        missing_indices = np.random.choice(df.index, n_missing, replace=False)
        df.loc[missing_indices, col] = np.nan
    
    # Duplicates qo'shish
    n_duplicates = int(len(df) * duplicate_rate)
    if n_duplicates > 0:
        duplicate_indices = np.random.choice(df.index, n_duplicates, replace=False)
        duplicates = df.loc[duplicate_indices].copy()
        df = pd.concat([df, duplicates], ignore_index=True)
    
    return df


def create_customer_dataset(n_rows=200, missing_rate=0.2):
    """
    Mijozlar ma'lumotlari yaratish
    """
    np.random.seed(100)
    
    data = {
        'Customer_ID': range(1, n_rows + 1),
        'Yosh': np.random.randint(18, 70, n_rows),
        'Jins': np.random.choice(['Erkak', 'Ayol'], n_rows),
        'Daromad': np.random.randint(2000000, 50000000, n_rows),
        'Xarid_Soni': np.random.randint(1, 50, n_rows),
        'Jami_Xarajat': np.random.randint(100000, 10000000, n_rows),
        'Sodiqlik_Darajasi': np.random.choice(['Past', 'O\'rta', 'Yuqori'], n_rows),
        'Ro\'yxatdan_o\'tgan': pd.date_range('2020-01-01', periods=n_rows, freq='D')
    }
    
    df = pd.DataFrame(data)
    
    # Missing values
    for col in ['Yosh', 'Daromad', 'Xarid_Soni', 'Jami_Xarajat', 'Sodiqlik_Darajasi']:
        n_missing = int(len(df) * missing_rate * np.random.random())
        missing_indices = np.random.choice(df.index, n_missing, replace=False)
        df.loc[missing_indices, col] = np.nan
    
    return df


def create_product_dataset(n_rows=150):
    """
    Mahsulotlar ma'lumotlari yaratish
    """
    np.random.seed(200)
    
    categories = ['Electronics', 'Clothing', 'Food', 'Books', 'Home']
    brands = ['Brand_A', 'Brand_B', 'Brand_C', 'Brand_D', 'Brand_E']
    
    data = {
        'Product_ID': range(1, n_rows + 1),
        'Nomi': [f'Product_{i}' for i in range(1, n_rows + 1)],
        'Kategoriya': np.random.choice(categories, n_rows),
        'Brand': np.random.choice(brands, n_rows),
        'Narx': np.random.randint(10000, 5000000, n_rows),
        'Sotilgan_Soni': np.random.randint(0, 1000, n_rows),
        'Reyting': np.random.uniform(1, 5, n_rows).round(1),
        'Mavjud': np.random.choice(['Ha', 'Yo\'q'], n_rows)
    }
    
    df = pd.DataFrame(data)
    
    # Missing values
    for col in ['Brand', 'Narx', 'Sotilgan_Soni', 'Reyting']:
        n_missing = int(len(df) * 0.1 * np.random.random())
        missing_indices = np.random.choice(df.index, n_missing, replace=False)
        df.loc[missing_indices, col] = np.nan
    
    return df


if __name__ == "__main__":
    # Datasets yaratish
    print("Creating datasets...")
    
    # 1. Employee dataset
    df_employee = create_employee_dataset(n_rows=100, missing_rate=0.15, duplicate_rate=0.05)
    df_employee.to_csv('employees.csv', index=False)
    print(f"✅ employees.csv yaratildi: {df_employee.shape}")
    print(f"   Missing values: {df_employee.isnull().sum().sum()}")
    print(f"   Duplicates: {df_employee.duplicated().sum()}")
    
    # 2. Customer dataset
    df_customer = create_customer_dataset(n_rows=200, missing_rate=0.2)
    df_customer.to_csv('customers.csv', index=False)
    print(f"\n✅ customers.csv yaratildi: {df_customer.shape}")
    print(f"   Missing values: {df_customer.isnull().sum().sum()}")
    
    # 3. Product dataset
    df_product = create_product_dataset(n_rows=150)
    df_product.to_csv('products.csv', index=False)
    print(f"\n✅ products.csv yaratildi: {df_product.shape}")
    print(f"   Missing values: {df_product.isnull().sum().sum()}")
    
    print("\n" + "="*60)
    print("📊 Barcha datasetlar tayyor!")
    print("="*60)
    print("\nFayllar:")
    print("- employees.csv (Xodimlar)")
    print("- customers.csv (Mijozlar)")
    print("- products.csv (Mahsulotlar)")
    print("\n💡 Ushbu fayllarni lecture.ipynb, practical.ipynb, va homework.ipynb da ishlatishingiz mumkin!")
