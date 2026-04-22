# Write your MySQL query statement bel
select max(num) as num from (select num from Mynumbers
group by num
having count(num)=1) 
as final
