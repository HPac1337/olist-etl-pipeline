-- Order Funnel: Drop-off rates at each stage of the order lifecycle

SELECT
    COUNT(*)                                                        AS total_orders,
    COUNT(CASE WHEN order_status != 'canceled' 
               AND order_approved_at IS NOT NULL THEN 1 END)        AS approved,
    COUNT(CASE WHEN order_status != 'canceled'
               AND order_delivered_carrier_date IS NOT NULL THEN 1 END) AS shipped,
    COUNT(CASE WHEN order_status = 'delivered' THEN 1 END)          AS delivered,
    ROUND(COUNT(CASE WHEN order_status != 'canceled'
               AND order_approved_at IS NOT NULL THEN 1 END) * 100.0 /
               NULLIF(COUNT(*), 0), 2)                              AS approval_rate_pct,
    ROUND(COUNT(CASE WHEN order_status != 'canceled'
               AND order_delivered_carrier_date IS NOT NULL THEN 1 END) * 100.0 /
               NULLIF(COUNT(*), 0), 2)                              AS ship_rate_pct,
    ROUND(COUNT(CASE WHEN order_status = 'delivered' THEN 1 END) * 100.0 /
               NULLIF(COUNT(*), 0), 2)                              AS delivery_rate_pct
FROM fact_orders