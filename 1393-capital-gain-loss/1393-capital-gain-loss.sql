# Write your MySQL query statement below
# sell has corresponding buy in a previous day
# buy has a sell in an upcoming day
WITH cte_sell_buy_pair 
AS
(
SELECT 
    stock_name, 
    operation_day,
    CASE 
        WHEN operation = "Buy" 
        THEN price
        ELSE 0
    END AS buying_price,
    CASE 
        WHEN operation = "Buy" 
        THEN LEAD(price) OVER (PARTITION BY stock_name ORDER BY operation_day ASC)
        ELSE 0
    END AS selling_price 
FROM Stocks
), pre_results AS (
SELECT 
    stock_name, 
    operation_day, 
    buying_price, 
    selling_price,
    selling_price - buying_price AS capital_gain_loss
FROM cte_sell_buy_pair
WHERE
    selling_price != 0
)
SELECT 
    stock_name,
    SUM(capital_gain_loss) AS capital_gain_loss
FROM pre_results
GROUP BY stock_name
;