# Write your MySQL query statement below
# emp id pk
# managerId -> can be null

with managers_with_5_employees AS
(
SELECT 
managerId,
count(id) ctid
from Employee
Group by managerId
having ctid >=5
)
select name
from Employee
where id in (select managerId from managers_with_5_employees)