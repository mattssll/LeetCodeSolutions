with result_set AS (
SELECT 
    s.user_id AS s_user_id,
    SUM(CASE WHEN action = 'confirmed' THEN 1 ELSE 0 END) AS confirmed,
    COUNT(c.time_stamp) AS total_requests
FROM Signups AS s
LEFT JOIN Confirmations AS c ON s.user_id = c.user_id
GROUP BY s_user_id
) 
SELECT 
    s_user_id AS user_id,
    CASE WHEN total_requests = 0 THEN 0 ELSE (confirmed*1.0/ total_requests) END AS confirmation_rate 
FROM result_set;
