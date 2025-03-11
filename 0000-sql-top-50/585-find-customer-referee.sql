-- Write your PostgreSQL query statement below
-- https://leetcode.com/problems/find-customer-referee/?envType=study-plan-v2&envId=top-sql-50
SELECT name FROM Customer
where COALESCE(referee_id,0) != 2;