# Write your MySQL query statement below
select reg.contest_id ,round((count(reg.user_id)/(select count(*) from users)*100),2) as percentage
from Users as u join register as reg
on u.user_id=reg.user_id
group by reg.contest_id 
order by percentage desc,reg.contest_id