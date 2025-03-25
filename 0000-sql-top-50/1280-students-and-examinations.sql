 -- Write your PostgreSQL query statement below
 -- takeaway: cross join to get a list of all students and disciplines as result set
SELECT st.student_id, st.student_name,
su.subject_name, COALESCE(count(e.student_id),0) as attended_exams
FROM Students st
CROSS JOIN Subjects su
LEFT JOIN Examinations e 
    ON e.student_id = st.student_id
    AND su.subject_name = E.subject_name
GROUP BY 1,2,3
ORDER BY st.student_id ASC, su.subject_name ASC