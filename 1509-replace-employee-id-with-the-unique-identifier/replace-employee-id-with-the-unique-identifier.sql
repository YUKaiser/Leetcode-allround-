# Write your MySQL query statement below
select unique_id,name from  EmployeeUni as u right join employees as e on u.id=e.id;