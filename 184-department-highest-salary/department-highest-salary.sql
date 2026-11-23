# Write your MySQL query statement below
With RankData as
(select d.name as Department,e.name as Employee,Salary,Dense_Rank() over(partition by departmentId order by salary Desc) as ran
from Employee as e join 
department as d on e.departmentId=d.id
) 
Select Department,Employee,
Salary from RankData
where ran=1
