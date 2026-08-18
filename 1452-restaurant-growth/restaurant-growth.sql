# Write your MySQL query statement below
select distinct visited_on,amount,round(amount/7,2) as average_amount
from (select visited_on,
sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as amount
from customer) t 
limit 1000 offset 6