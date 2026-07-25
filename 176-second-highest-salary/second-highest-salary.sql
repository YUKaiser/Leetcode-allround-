# Write your MySQL query statement below
select IFNUll((select distinct salary from employee where salary <(select Max(salary) from employee )
order by salary desc limit 1),NULL) as SecondHighestSalary 

