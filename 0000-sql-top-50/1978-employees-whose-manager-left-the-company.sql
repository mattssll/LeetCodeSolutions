/* takeaway:
 can use self join instead if not in with subquery...
 join clause: join emp id with manager id
 need to do e1.manager_id not null because source data has nulls in manager_id
 and e2.employee_id is null because then manager is not there anymore
*/

SELECT e1.employee_id FROM
Employees e1
LEFT JOIN Employees e2 ON e1.manager_id = e2.employee_id
WHERE e1.salary < 30000 
    and e1.manager_id is not null
    and e2.employee_id is null
ORDER BY e1.employee_id ASC

/* with subquery and IN
SELECT employee_id FROM
Employees
WHERE salary < 30000
AND manager_id not in (select employee_id FROM Employees)
order by employee_id asc
*/