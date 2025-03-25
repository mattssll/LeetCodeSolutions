-- Write your PostgreSQL query statement below
-- first with self join
-- takeaways -> need to cast to NUMERIC after subtracting
-- join is more efficient solution, perhaps getting a lag would work as well
/*
SELECT 
    a1.machine_id,
    ROUND(AVG((a2.timestamp-a1.timestamp)::NUMERIC),3) AS processing_time
FROM Activity a1
JOIN Activity a2 
    on a1.machine_id = a2.machine_id
    and a1.process_id = a2.process_id
    and a1.activity_type = 'start'
    and a2.activity_type = 'end'
GROUP BY a1.machine_id
ORDER BY machine_id ASC;
*/

SELECT 
    machine_id,
    ROUND(((
        SUM(CASE WHEN activity_type = 'end' THEN timestamp END)-
        SUM(CASE WHEN activity_type = 'start' THEN timestamp END)
    )/COUNT(CASE WHEN activity_type = 'start' THEN 1 END))::NUMERIC, 3) AS processing_time
FROM Activity
GROUP BY machine_id
ORDER BY machine_id ASC
