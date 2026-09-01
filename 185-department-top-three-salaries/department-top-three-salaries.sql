# Write your MySQL query statement below
select Department,Employee,salary from (
select d.name as Department,e.name as Employee,e.salary as salary,
Dense_Rank() Over(Partition by e.departmentId Order by e.Salary desc) as rnk
from Employee as e join Department as d on e.departmentID=d.id) as t
where rnk<=3