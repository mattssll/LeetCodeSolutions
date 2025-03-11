-- Write your PostgreSQL query statement below
-- https://leetcode.com/problems/big-countries/description/?envType=study-plan-v2&envId=top-sql-50
-- Write your PostgreSQL query statement below
SELECT name, population, area
FROM World
WHERE COALESCE(area,0) >=3000000 or COALESCE(population,0) >= 25000000