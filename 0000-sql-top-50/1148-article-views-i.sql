-- Write your PostgreSQL query statement below
-- https://leetcode.com/problems/article-views-i/?envType=study-plan-v2&envId=top-sql-50
--Write a solution to find 
--all the authors that viewed at least one of their own articles.
SELECT author_id AS id
FROM Views
WHERE viewer_id = author_id
GROUP BY author_id