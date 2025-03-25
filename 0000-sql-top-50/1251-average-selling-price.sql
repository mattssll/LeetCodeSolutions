-- Takeaways:
-- COALESCE to handle NULLs, ROUND,
-- Join with DATE BETWEEN DATE_1 AND DATE_2

-- find avg selling price
-- rounder to 2 decimal places ROUND(val, 2)
-- no sold units than 0
SELECT 
    p.product_id,
-- u.purchase_date, u.units,  p.price
    COALESCE(ROUND(SUM(p.price*u.units*1.0)/SUM(u.units), 2),0) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u 
    ON p.product_id = u.product_id 
    AND u.purchase_date BETWEEN start_date and END_DATE
GROUP BY p.product_id