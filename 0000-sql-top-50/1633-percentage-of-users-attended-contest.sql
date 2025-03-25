/*
Takeaways:
    - for ratios and such we use counts
    - for pgsql need to *1.0
*/
SELECT 
    contest_id,
    ROUND(COUNT(user_id)*1.0/(SELECT count(user_id) FROM users)*100
    ,2)
        AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage desc, contest_id ASC