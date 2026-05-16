# Write your MySQL query statement below
select person_name from 
(select turn,person_name,sum(weight) over (order by turn) as Total_weight
from queue ) as f where Total_weight<=1000 
order by Total_weight desc limit 1