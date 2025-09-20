# 📊 E-commerce Ma'lumotlar Lug'ati

## Jadvallar tuzilishi

### 1. 🏷️ categories
Ma'lumotlar kategoriyalari jadvali

| Ustun nomi | Ma'lumot turi | Tavsif |
|------------|---------------|---------|
| `category_id` | INTEGER (PK) | Kategoriya identifikatori |
| `category_name` | TEXT | Kategoriya nomi |
| `description` | TEXT | Kategoriya tavsifi |
| `created_at` | DATETIME | Yaratilgan vaqt |

**Namunaviy qiymatlar:**
- Elektronika, Kiyim va Poyafzal, Uy va Bog', Kitoblar, Sport va Faollik

---

### 2. 🛍️ products  
Mahsulotlar katalogi jadvali

| Ustun nomi | Ma'lumot turi | Tavsif |
|------------|---------------|---------|
| `product_id` | INTEGER (PK) | Mahsulot identifikatori |
| `product_name` | TEXT | Mahsulot nomi |
| `category_id` | INTEGER (FK) | Kategoriya havolasi |
| `price` | REAL | Sotish narxi (so'm) |
| `cost` | REAL | Tannarx (so'm) |
| `stock_quantity` | INTEGER | Ombordagi miqdor |
| `rating` | REAL | O'rtacha reyting (1-5) |
| `reviews_count` | INTEGER | Sharhlar soni |
| `weight_kg` | REAL | Og'irligi (kg) |
| `created_at` | DATETIME | Yaratilgan vaqt |

**Narx oralig'i:**
- Elektronika: 500,000 - 25,000,000 so'm
- Kiyim: 50,000 - 1,500,000 so'm
- Boshqa: 25,000 - 1,000,000 so'm

---

### 3. 👥 customers
Mijozlar ma'lumotlari jadvali

| Ustun nomi | Ma'lumot turi | Tavsif |
|------------|---------------|---------|
| `customer_id` | INTEGER (PK) | Mijoz identifikatori |
| `first_name` | TEXT | Ism |
| `last_name` | TEXT | Familiya |
| `email` | TEXT | Email manzil |
| `phone` | TEXT | Telefon raqam |
| `birth_date` | DATE | Tug'ilgan sana |
| `gender` | TEXT | Jinsi (Male/Female) |
| `city` | TEXT | Shahar |
| `region` | TEXT | Viloyat |
| `registration_date` | DATE | Ro'yxatdan o'tgan sana |
| `customer_segment` | TEXT | Mijoz segmenti |
| `created_at` | DATETIME | Yaratilgan vaqt |

**Mijoz segmentlari:**
- Bronze, Silver, Gold, Platinum, VIP

**Hududlar:**
- 13 ta O'zbekiston viloyati va Toshkent shahri

---

### 4. 🛒 orders
Buyurtmalar jadvali

| Ustun nomi | Ma'lumot turi | Tavsif |
|------------|---------------|---------|
| `order_id` | INTEGER (PK) | Buyurtma identifikatori |
| `customer_id` | INTEGER (FK) | Mijoz havolasi |
| `order_date` | DATE | Buyurtma sanasi |
| `order_status` | TEXT | Buyurtma holati |
| `total_amount` | REAL | Jami summa (so'm) |
| `discount_amount` | REAL | Chegirma summasi (so'm) |
| `shipping_cost` | REAL | Yetkazib berish narxi (so'm) |
| `payment_method` | TEXT | To'lov usuli |
| `delivery_city` | TEXT | Yetkazib berish shahri |
| `delivery_region` | TEXT | Yetkazib berish viloyati |
| `delivery_date` | DATE | Yetkazib berilgan sana |
| `created_at` | DATETIME | Yaratilgan vaqt |

**Buyurtma holatlari:**
- Pending (5%), Processing (10%), Shipped (15%), Delivered (60%), Cancelled (8%), Returned (2%)

**To'lov usullari:**
- Credit Card, Debit Card, UzCard, Humo, Click, PayMe, Cash, Bank Transfer

---

### 5. 📦 order_items
Buyurtma tarkibi jadvali

| Ustun nomi | Ma'lumot turi | Tavsif |
|------------|---------------|---------|
| `item_id` | INTEGER (PK) | Element identifikatori |
| `order_id` | INTEGER (FK) | Buyurtma havolasi |
| `product_id` | INTEGER (FK) | Mahsulot havolasi |
| `quantity` | INTEGER | Miqdor |
| `unit_price` | REAL | Birlik narxi (so'm) |
| `total_price` | REAL | Jami narx (so'm) |
| `discount_percent` | REAL | Chegirma foizi |
| `created_at` | DATETIME | Yaratilgan vaqt |

## 👁️ Views (Ko'rinishlar)

### 1. order_summary
Buyurtmalar umumiy ko'rinishi

**Tarkibi:**
- Buyurtma asosiy ma'lumotlari
- Mijoz ma'lumotlari
- Buyurtmadagi mahsulotlar soni
- Umumiy miqdor

### 2. product_performance
Mahsulotlar samaradorligi

**Tarkibi:**
- Mahsulot nomi va kategoriyasi
- Sotilgan miqdor va daromad
- Buyurtma bergan sonlar
- O'rtacha sotish narxi

### 3. customer_analytics
Mijozlar tahlili

**Tarkibi:**
- Mijoz asosiy ma'lumotlari
- Jami buyurtmalar va xarid summalari
- O'rtacha buyurtma qiymati
- Birinchi va oxirgi buyurtma sanalari

## 📊 Ma'lumotlar statistikasi

### Yozuvlar soni:
- **Kategoriyalar**: 10 ta
- **Mahsulotlar**: 100 ta
- **Mijozlar**: 2,000 ta
- **Buyurtmalar**: ~10,000 ta
- **Buyurtma elementlari**: ~20,000 ta

### Vaqt oralig'i:
- **2023-2024** yillar
- Mavsumiy ta'sirlar hisobga olingan
- Qish va yoz oylarida ko'proq savdo

### Narx oralig'i:
- **Minimal buyurtma**: ~50,000 so'm
- **Maksimal buyurtma**: ~50,000,000 so'm
- **O'rtacha buyurtma**: ~1,500,000 so'm

## 🔍 Indekslar

Performance uchun yaratilgan indekslar:
- `products(category_id, price)`
- `customers(region, customer_segment)`  
- `orders(customer_id, order_date, order_status)`
- `order_items(order_id, product_id)`

## 💡 Tahlil uchun maslahatlar

### 1. **Mavsumiy trendlar**
```sql
SELECT strftime('%Y-%m', order_date) as month, 
       COUNT(*) as orders_count,
       SUM(total_amount) as revenue
FROM orders 
GROUP BY strftime('%Y-%m', order_date)
ORDER BY month;
```

### 2. **TOP kategoriyalar**
```sql
SELECT c.category_name, 
       COUNT(oi.item_id) as items_sold,
       SUM(oi.total_price) as revenue
FROM categories c
JOIN products p ON c.category_id = p.category_id
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY c.category_name
ORDER BY revenue DESC;
```

### 3. **Mijozlar segmentatsiyasi**
```sql
SELECT customer_segment,
       COUNT(*) as customers_count,
       AVG(total_spent) as avg_spent
FROM customer_analytics
GROUP BY customer_segment;
```

---

*📈 Ushbu ma'lumotlar to'plami real biznes stsenariylari uchun mo'ljallangan va SQL ko'nikmalarini rivojlantirish uchun ideal!*