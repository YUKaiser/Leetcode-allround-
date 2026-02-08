# Write your MySQL query statement below
select si.user_id,round(avg(if(cr.action='confirmed',1.0,0)),2) as confirmation_rate
from signups as si left join
confirmations as cr on si.user_id=cr.user_id
group by user_id

