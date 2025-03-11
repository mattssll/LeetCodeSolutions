-- https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=top-sql-50
-- Write your PostgreSQL query statement below
--content consists of alphanumeric characters, 
-- '!', or ' ' and no other special characters.
SELECT tweet_id FROM tweets
WHERE length(COALESCE(content,''))>15;
-- good to clarify if coalesce here is necessary,
-- it is if we want to bring the records in case of nulls