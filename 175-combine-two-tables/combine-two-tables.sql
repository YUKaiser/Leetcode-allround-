# Write your MySQL query statement below
select firstName, lastName, city, state
from person as p
left join address as b
on p.personId=b.personId
where p.personId is not null; 
