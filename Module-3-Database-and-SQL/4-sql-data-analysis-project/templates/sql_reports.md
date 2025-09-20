# SQL Hisobotlar Namunalari

Bu faylda turli xil biznes hisobotlari uchun SQL so'rovlari namunalari berilgan.

## 📈 Kunlik Hisobotlar

### 1. Kunlik Sotuvlar Hisoboti
```sql
-- Bugungi sotuvlar
SELECT 
    DATE('now') as report_date,
    COUNT(DISTINCT o.id) as total_orders,
    COUNT(DISTINCT o.customer_id) as unique_customers,
    ROUND(SUM(o.total_amount), 2) as total_revenue,
    ROUND(AVG(o.total_amount), 2) as avg_order_value,
    SUM(oi.quantity) as total_items_sold
FROM orders o
JOIN order_items oi ON o.id = oi.order_id
WHERE DATE(o.order_date) = DATE('now');
```

### 2. Mahsulot Performance (Kunlik)
```sql
-- Eng yaxshi mahsulotlar bugun
SELECT 
    p.name as product_name,
    c.name as category,
    SUM(oi.quantity) as quantity_sold,
    ROUND(SUM(oi.quantity * oi.price), 2) as revenue,
    COUNT(DISTINCT o.customer_id) as unique_buyers
FROM products p
JOIN categories c ON p.category_id = c.id
JOIN order_items oi ON p.id = oi.product_id
JOIN orders o ON oi.order_id = o.id
WHERE DATE(o.order_date) = DATE('now')
GROUP BY p.id, p.name, c.name
ORDER BY revenue DESC
LIMIT 10;
```

## 📊 Haftalik Hisobotlar

### 3. Haftalik Trend Tahlili
```sql
-- Oxirgi hafta vs avvalgi hafta
WITH this_week AS (
    SELECT 
        COUNT(*) as orders_count,
        ROUND(SUM(total_amount), 2) as revenue
    FROM orders
    WHERE order_date >= DATE('now', '-7 days')
),
last_week AS (
    SELECT 
        COUNT(*) as orders_count,
        ROUND(SUM(total_amount), 2) as revenue
    FROM orders
    WHERE order_date >= DATE('now', '-14 days') 
    AND order_date < DATE('now', '-7 days')
)
SELECT 
    tw.orders_count as this_week_orders,
    lw.orders_count as last_week_orders,
    tw.orders_count - lw.orders_count as orders_change,
    ROUND((tw.orders_count - lw.orders_count) * 100.0 / lw.orders_count, 2) as orders_change_percent,
    tw.revenue as this_week_revenue,
    lw.revenue as last_week_revenue,
    tw.revenue - lw.revenue as revenue_change,
    ROUND((tw.revenue - lw.revenue) * 100.0 / lw.revenue, 2) as revenue_change_percent
FROM this_week tw
CROSS JOIN last_week lw;
```

### 4. Mijozlar Faolligi (Haftalik)
```sql
-- Haftalik mijozlar segmentatsiyasi
SELECT 
    'Yangi mijozlar' as segment,
    COUNT(*) as customer_count
FROM customers
WHERE created_at >= DATE('now', '-7 days')

UNION ALL

SELECT 
    'Qaytgan mijozlar' as segment,
    COUNT(DISTINCT o.customer_id) as customer_count
FROM orders o
WHERE o.order_date >= DATE('now', '-7 days')
AND o.customer_id IN (
    SELECT customer_id 
    FROM orders 
    WHERE order_date < DATE('now', '-7 days')
);
```

## 📅 Oylik Hisobotlar

### 5. Oylik Biznes Dashboard
```sql
-- Asosiy KPI'lar (bu oy)
WITH monthly_metrics AS (
    SELECT 
        strftime('%Y-%m', order_date) as month,
        COUNT(DISTINCT id) as total_orders,
        COUNT(DISTINCT customer_id) as unique_customers,
        ROUND(SUM(total_amount), 2) as total_revenue,
        ROUND(AVG(total_amount), 2) as avg_order_value
    FROM orders
    WHERE strftime('%Y-%m', order_date) = strftime('%Y-%m', 'now')
    GROUP BY strftime('%Y-%m', order_date)
),
previous_month AS (
    SELECT 
        COUNT(DISTINCT id) as prev_orders,
        COUNT(DISTINCT customer_id) as prev_customers,
        ROUND(SUM(total_amount), 2) as prev_revenue
    FROM orders
    WHERE strftime('%Y-%m', order_date) = strftime('%Y-%m', DATE('now', '-1 month'))
)
SELECT 
    mm.*,
    pm.prev_orders,
    mm.total_orders - pm.prev_orders as orders_growth,
    ROUND((mm.total_orders - pm.prev_orders) * 100.0 / pm.prev_orders, 2) as orders_growth_percent,
    pm.prev_revenue,
    mm.total_revenue - pm.prev_revenue as revenue_growth,
    ROUND((mm.total_revenue - pm.prev_revenue) * 100.0 / pm.prev_revenue, 2) as revenue_growth_percent
FROM monthly_metrics mm
CROSS JOIN previous_month pm;
```

### 6. Top Performerlar (Oylik)
```sql
-- Bu oyning top mijozlari
SELECT 
    c.first_name || ' ' || c.last_name as customer_name,
    c.city,
    COUNT(o.id) as orders_count,
    ROUND(SUM(o.total_amount), 2) as total_spent,
    RANK() OVER (ORDER BY SUM(o.total_amount) DESC) as spending_rank
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE strftime('%Y-%m', o.order_date) = strftime('%Y-%m', 'now')
GROUP BY c.id, c.first_name, c.last_name, c.city
ORDER BY total_spent DESC
LIMIT 20;
```

## 📊 Kategoriya Hisobotlari

### 7. Kategoriya Performance Tahlili
```sql
-- Kategoriyalar bo'yicha batafsil tahlil
WITH category_stats AS (
    SELECT 
        c.name as category,
        COUNT(DISTINCT p.id) as products_count,
        COUNT(DISTINCT o.id) as orders_count,
        SUM(oi.quantity) as total_quantity_sold,
        ROUND(SUM(oi.quantity * oi.price), 2) as total_revenue,
        ROUND(AVG(oi.price), 2) as avg_selling_price,
        COUNT(DISTINCT o.customer_id) as unique_customers
    FROM categories c
    JOIN products p ON c.id = p.category_id
    JOIN order_items oi ON p.id = oi.product_id
    JOIN orders o ON oi.order_id = o.id
    GROUP BY c.id, c.name
),
total_revenue AS (
    SELECT SUM(total_revenue) as grand_total FROM category_stats
)
SELECT 
    cs.*,
    ROUND(cs.total_revenue * 100.0 / tr.grand_total, 2) as revenue_percentage,
    ROUND(cs.total_revenue / cs.products_count, 2) as revenue_per_product,
    ROUND(cs.total_quantity_sold / cs.products_count, 2) as avg_quantity_per_product
FROM category_stats cs
CROSS JOIN total_revenue tr
ORDER BY cs.total_revenue DESC;
```

## 🏙️ Geografik Hisobotlar

### 8. Shaharlar bo'yicha Tahlil
```sql
-- Shaharlar performance ranking
WITH city_performance AS (
    SELECT 
        c.city,
        COUNT(DISTINCT c.id) as customers_count,
        COUNT(DISTINCT o.id) as orders_count,
        ROUND(SUM(o.total_amount), 2) as total_revenue,
        ROUND(AVG(o.total_amount), 2) as avg_order_value,
        ROUND(SUM(o.total_amount) / COUNT(DISTINCT c.id), 2) as revenue_per_customer
    FROM customers c
    LEFT JOIN orders o ON c.id = o.customer_id
    GROUP BY c.city
    HAVING COUNT(DISTINCT c.id) >= 5  -- Kamida 5 ta mijoz bo'lgan shaharlar
)
SELECT 
    *,
    RANK() OVER (ORDER BY total_revenue DESC) as revenue_rank,
    RANK() OVER (ORDER BY revenue_per_customer DESC) as efficiency_rank
FROM city_performance
ORDER BY total_revenue DESC;
```

## 📋 Inventar Hisobotlari

### 9. Stock Monitoring
```sql
-- Inventar holati va early warning
SELECT 
    p.name as product_name,
    c.name as category,
    p.stock_quantity as current_stock,
    COALESCE(SUM(oi.quantity), 0) as total_sold,
    ROUND(
        COALESCE(SUM(oi.quantity), 0) / 
        CASE 
            WHEN julianday('now') - julianday(MIN(o.order_date)) = 0 THEN 1
            ELSE julianday('now') - julianday(MIN(o.order_date))
        END, 2
    ) as daily_avg_sales,
    CASE 
        WHEN p.stock_quantity = 0 THEN 'Tugagan'
        WHEN p.stock_quantity <= 10 THEN 'Kam'
        WHEN p.stock_quantity <= 50 THEN 'O\'rta'
        ELSE 'Yetarli'
    END as stock_status,
    CASE 
        WHEN COALESCE(SUM(oi.quantity), 0) = 0 THEN 'Cheksiz'
        ELSE ROUND(p.stock_quantity / (
            COALESCE(SUM(oi.quantity), 0) / 
            CASE 
                WHEN julianday('now') - julianday(MIN(o.order_date)) = 0 THEN 1
                ELSE julianday('now') - julianday(MIN(o.order_date))
            END
        ), 0)
    END as days_until_stockout
FROM products p
JOIN categories c ON p.category_id = c.id
LEFT JOIN order_items oi ON p.id = oi.product_id
LEFT JOIN orders o ON oi.order_id = o.id
GROUP BY p.id, p.name, c.name, p.stock_quantity
ORDER BY 
    CASE 
        WHEN p.stock_quantity = 0 THEN 1
        WHEN p.stock_quantity <= 10 THEN 2
        WHEN p.stock_quantity <= 50 THEN 3
        ELSE 4
    END,
    p.stock_quantity ASC;
```

## 🎯 Mijozlar Segmentatsiyasi

### 10. RFM Tahlili (Recency, Frequency, Monetary)
```sql
-- Mijozlarni RFM asosida segmentlash
WITH customer_rfm AS (
    SELECT 
        c.id as customer_id,
        c.first_name || ' ' || c.last_name as customer_name,
        c.city,
        ROUND(julianday('now') - julianday(MAX(o.order_date)), 0) as recency_days,
        COUNT(o.id) as frequency,
        ROUND(SUM(o.total_amount), 2) as monetary
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    GROUP BY c.id, c.first_name, c.last_name, c.city
),
rfm_scores AS (
    SELECT 
        *,
        CASE 
            WHEN recency_days <= 30 THEN 5
            WHEN recency_days <= 60 THEN 4
            WHEN recency_days <= 90 THEN 3
            WHEN recency_days <= 180 THEN 2
            ELSE 1
        END as recency_score,
        CASE 
            WHEN frequency >= 10 THEN 5
            WHEN frequency >= 5 THEN 4
            WHEN frequency >= 3 THEN 3
            WHEN frequency >= 2 THEN 2
            ELSE 1
        END as frequency_score,
        CASE 
            WHEN monetary >= 1000 THEN 5
            WHEN monetary >= 500 THEN 4
            WHEN monetary >= 200 THEN 3
            WHEN monetary >= 100 THEN 2
            ELSE 1
        END as monetary_score
    FROM customer_rfm
)
SELECT 
    customer_name,
    city,
    recency_days,
    frequency,
    monetary,
    recency_score,
    frequency_score,
    monetary_score,
    CASE 
        WHEN recency_score >= 4 AND frequency_score >= 4 AND monetary_score >= 4 THEN 'VIP Champions'
        WHEN recency_score >= 3 AND frequency_score >= 3 AND monetary_score >= 3 THEN 'Loyal Customers'
        WHEN recency_score >= 4 AND frequency_score <= 2 THEN 'New Customers'
        WHEN recency_score <= 2 AND frequency_score >= 3 THEN 'At Risk'
        WHEN recency_score <= 2 AND frequency_score <= 2 THEN 'Lost Customers'
        ELSE 'Regular Customers'
    END as customer_segment
FROM rfm_scores
ORDER BY monetary DESC;
```

## 📈 Trend Prognozlari

### 11. Growth Trend Analysis
```sql
-- O'sish tendensiyalarini baholash
WITH monthly_trends AS (
    SELECT 
        strftime('%Y-%m', order_date) as month,
        COUNT(*) as orders,
        ROUND(SUM(total_amount), 2) as revenue,
        COUNT(DISTINCT customer_id) as customers
    FROM orders
    WHERE order_date >= DATE('now', '-12 months')
    GROUP BY strftime('%Y-%m', order_date)
    ORDER BY month
),
trends_with_lag AS (
    SELECT 
        *,
        LAG(orders, 1) OVER (ORDER BY month) as prev_orders,
        LAG(revenue, 1) OVER (ORDER BY month) as prev_revenue,
        LAG(customers, 1) OVER (ORDER BY month) as prev_customers
    FROM monthly_trends
)
SELECT 
    month,
    orders,
    revenue,
    customers,
    CASE 
        WHEN prev_orders IS NULL THEN 0
        ELSE ROUND((orders - prev_orders) * 100.0 / prev_orders, 2)
    END as orders_growth_percent,
    CASE 
        WHEN prev_revenue IS NULL THEN 0
        ELSE ROUND((revenue - prev_revenue) * 100.0 / prev_revenue, 2)
    END as revenue_growth_percent,
    CASE 
        WHEN prev_customers IS NULL THEN 0
        ELSE ROUND((customers - prev_customers) * 100.0 / prev_customers, 2)
    END as customers_growth_percent
FROM trends_with_lag
ORDER BY month;
```

---

**Foydalanish bo'yicha ko'rsatmalar:**

1. **Avtomatlashtirish**: Bu so'rovlarni cron job yoki scheduler orqali avtomatik ishga tushiring
2. **Parametrlashtirish**: Sana oralig'ini o'zgaruvchi qilib qo'ying
3. **Export**: Natijalarni CSV, Excel yoki PDF formatda eksport qiling
4. **Dashboards**: Power BI, Tableau yoki Grafana bilan integration qiling
5. **Alerts**: Critical ko'rsatkichlar uchun alert sistemasini sozlang