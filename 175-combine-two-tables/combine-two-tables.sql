# Write your MySQL query statement below
select p.firstName, p.lastName, b.city, b.state
from person as p
left join address as b
on p.personId=b.personId;
#where p.personId is not null; 
