-- Seller Performance: On-time rate, average review score, and revenue per seller

SELECT
    s.seller_id,
    s.seller_city,
    s.seller_state,
    COUNT(DISTINCT oi.order_id)                                     AS total_orders,
    ROUND(SUM(oi.price), 2)                                         AS total_revenue,
    ROUND(AVG(r.review_score), 2)                                   AS avg_review_score,
    COUNT(CASE WHEN o.order_delivered_customer_date <= 
               o.order_estimated_delivery_date THEN 1 END)          AS on_time_deliveries,
    ROUND(
        COUNT(CASE WHEN o.order_delivered_customer_date <= 
                        o.order_estimated_delivery_date THEN 1 END) * 100.0 /
        NULLIF(COUNT(DISTINCT oi.order_id), 0)
    , 2)                                                            AS on_time_rate_pct
FROM fact_order_items oi
JOIN dim_sellers s          ON oi.seller_id = s.seller_id
JOIN fact_orders o          ON oi.order_id = o.order_id
LEFT JOIN fact_reviews r    ON o.order_id = r.order_id
WHERE o.order_status = 'delivered'
GROUP BY s.seller_id, s.seller_city, s.seller_state
ORDER BY total_revenue DESC