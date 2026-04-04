# Write your MySQL query statement below
select pr.project_id,round(avg(emp.experience_years),2) as average_years
from Project as pr  join Employee as emp
on pr.employee_id=emp.employee_id 
group by pr.project_id
/*Union
select pr.project_id,avg(emp.experience_years) as average_years
from Project as pr right join Employee as emp
on pr.employee_id=emp.employee_id
group by pr.project_id */