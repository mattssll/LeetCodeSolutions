-- keys:
-- dense_rank instead of rank
-- can't use window functions on where so need to use cte
WITH cte
     AS (SELECT departmentid,
                NAME,
                salary,
                Dense_rank()
                  OVER (
                    partition BY departmentid
                    ORDER BY salary DESC) rk
         FROM   employee)
SELECT d.NAME   AS Department,
       cte.NAME AS Employee,
       salary
FROM   cte
       JOIN department d
         ON cte.departmentid = d.id
WHERE  rk <= 3 