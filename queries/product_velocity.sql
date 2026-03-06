-- Product Velocity: Units sold per day by category
-- Measures how quickly products move off the shelf by category

SELECT
    p.product_category_name,
    COUNT(oi.order_item_id)                                         AS total_units_sold,
    COUNT(DISTINCT o.order_purchase_timestamp::DATE)                AS days_with_sales,
    ROUND(
        COUNT(oi.order_item_id) * 1.0 /
        NULLIF(COUNT(DISTINCT o.order_purchase_timestamp::DATE), 0)
    , 2)                                                            AS units_per_day,
    ROUND(SUM(oi.price), 2)                                         AS total_revenue
FROM fact_order_items oi
JOIN fact_orders o         ON oi.order_id = o.order_id
JOIN dim_products p        ON oi.product_id = p.product_id
WHERE o.order_status = 'delivered'
GROUP BY p.product_category_name
ORDER BY units_per_day DESC