"""
PostgreSQL Ulanish Namunalari
============================

Ushbu fayl PostgreSQL ga turli usullar bilan ulanish namunalarini ko'rsatadi.
"""

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import os
from datetime import datetime

class PostgreSQLConnection:
    """PostgreSQL ulanish sinfi"""
    
    def __init__(self):
        """Ulanish parametrlarini sozlash"""
        self.connection_params = {
            'host': 'localhost',
            'database': 'lesson_aggregation',
            'user': 'data_scientist',
            'password': 'secure_password123',
            'port': '5432'
        }
        
    def test_psycopg2_connection(self):
        """psycopg2 bilan ulanishni tekshirish"""
        print("🔌 psycopg2 ulanishini tekshirish...")
        
        try:
            # Ulanish yaratish
            conn = psycopg2.connect(**self.connection_params)
            cur = conn.cursor()
            
            # Test query
            cur.execute("SELECT version(), current_database(), current_user, now();")
            result = cur.fetchone()
            
            print("✅ psycopg2 ulanish muvaffaqiyatli!")
            print(f"📊 PostgreSQL versiyasi: {result[0].split()[1]}")
            print(f"🗄️ Database: {result[1]}")
            print(f"👤 Foydalanuvchi: {result[2]}")
            print(f"⏰ Vaqt: {result[3]}")
            
            # Ulanishni yopish
            cur.close()
            conn.close()
            
            return True
            
        except psycopg2.Error as e:
            print(f"❌ psycopg2 ulanish xatosi: {e}")
            return False
    
    def test_sqlalchemy_connection(self):
        """SQLAlchemy bilan ulanishni tekshirish"""
        print("\n🔌 SQLAlchemy ulanishini tekshirish...")
        
        try:
            # Connection string yaratish
            connection_string = (
                f"postgresql://{self.connection_params['user']}:"
                f"{self.connection_params['password']}@"
                f"{self.connection_params['host']}:"
                f"{self.connection_params['port']}/"
                f"{self.connection_params['database']}"
            )
            
            # Engine yaratish
            engine = create_engine(connection_string)
            
            # Test query
            query = """
            SELECT 
                current_database() as database,
                current_user as user,
                version() as version,
                now() as current_time
            """
            
            df = pd.read_sql(query, engine)
            
            print("✅ SQLAlchemy ulanish muvaffaqiyatli!")
            print(f"🗄️ Database: {df['database'][0]}")
            print(f"👤 Foydalanuvchi: {df['user'][0]}")
            print(f"📊 PostgreSQL: {df['version'][0].split()[1]}")
            print(f"⏰ Vaqt: {df['current_time'][0]}")
            
            return True
            
        except Exception as e:
            print(f"❌ SQLAlchemy ulanish xatosi: {e}")
            return False
    
    def test_database_tables(self):
        """Ma'lumotlar bazasidagi jadvallarni tekshirish"""
        print("\n📋 Jadvallarni tekshirish...")
        
        try:
            conn = psycopg2.connect(**self.connection_params)
            
            # Jadvallar ro'yxati
            query = """
            SELECT 
                table_name,
                table_rows
            FROM information_schema.tables t
            LEFT JOIN (
                SELECT 
                    schemaname,
                    tablename,
                    n_tup_ins as table_rows
                FROM pg_stat_user_tables
            ) s ON t.table_name = s.tablename
            WHERE t.table_schema = 'public'
            ORDER BY table_name;
            """
            
            df = pd.read_sql(query, conn)
            
            if len(df) > 0:
                print("✅ Jadvallar topildi:")
                for _, row in df.iterrows():
                    rows = row['table_rows'] if row['table_rows'] else 0
                    print(f"   📊 {row['table_name']}: {rows} ta yozuv")
            else:
                print("⚠️ Jadvallar topilmadi. create_postgresql_db.py ni ishga tushiring.")
            
            conn.close()
            return True
            
        except Exception as e:
            print(f"❌ Jadvallarni tekshirishda xato: {e}")
            return False
    
    def get_connection_info(self):
        """Ulanish ma'lumotlarini ko'rsatish"""
        print("\n📋 ULANISH MA'LUMOTLARI")
        print("-" * 25)
        for key, value in self.connection_params.items():
            if key == 'password':
                print(f"{key}: {'*' * len(value)}")
            else:
                print(f"{key}: {value}")
    
    def test_aggregation_sample(self):
        """Agregatsiya uchun namuna so'rov"""
        print("\n🧮 Agregatsiya namuna so'rovi...")
        
        try:
            conn = psycopg2.connect(**self.connection_params)
            
            # Namuna aggregation query
            query = """
            SELECT 
                COUNT(*) as total_employees,
                AVG(salary) as avg_salary,
                MIN(salary) as min_salary,
                MAX(salary) as max_salary,
                SUM(salary) as total_salary
            FROM employees;
            """
            
            df = pd.read_sql(query, conn)
            
            if len(df) > 0:
                print("✅ Xodimlar bo'yicha statistika:")
                row = df.iloc[0]
                print(f"   👥 Jami xodimlar: {row['total_employees']}")
                print(f"   💰 O'rtacha maosh: {row['avg_salary']:,.0f} so'm")
                print(f"   📉 Minimal maosh: {row['min_salary']:,.0f} so'm")
                print(f"   📈 Maksimal maosh: {row['max_salary']:,.0f} so'm")
                print(f"   💵 Jami maosh fondi: {row['total_salary']:,.0f} so'm")
            else:
                print("⚠️ Employees jadvali bo'sh yoki mavjud emas")
            
            conn.close()
            return True
            
        except Exception as e:
            print(f"❌ Agregatsiya so'rovida xato: {e}")
            return False

def main():
    """Asosiy test funksiyasi"""
    print("🧪 POSTGRESQL ULANISH TESTLARI")
    print("=" * 35)
    
    connector = PostgreSQLConnection()
    
    # Ulanish ma'lumotlarini ko'rsatish
    connector.get_connection_info()
    
    # Testlarni o'tkazish
    tests = [
        connector.test_psycopg2_connection,
        connector.test_sqlalchemy_connection,
        connector.test_database_tables,
        connector.test_aggregation_sample
    ]
    
    success_count = 0
    
    for test in tests:
        try:
            if test():
                success_count += 1
        except Exception as e:
            print(f"❌ Test xatosi: {e}")
    
    print(f"\n📊 NATIJALAR: {success_count}/{len(tests)} test muvaffaqiyatli")
    
    if success_count == len(tests):
        print("🎉 Barcha testlar o'tdi! PostgreSQL tayyor.")
        print("✅ Endi lecture.ipynb ni ochishingiz mumkin.")
    else:
        print("⚠️ Ba'zi testlar muvaffaqiyatsiz. Sozlamalarni tekshiring.")
        print("\n🔧 TEKSHIRISH RO'YXATI:")
        print("   1. PostgreSQL xizmati ishlab turibmi?")
        print("   2. lesson_aggregation database yaratilganmi?")
        print("   3. data_scientist foydalanuvchi mavjudmi?")
        print("   4. Parol to'g'rimi?")
        print("   5. create_postgresql_db.py ishga tushirilganmi?")

if __name__ == "__main__":
    main()
