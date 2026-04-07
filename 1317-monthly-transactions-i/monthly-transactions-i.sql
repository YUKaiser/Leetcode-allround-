# Write your MySQL query statement below
select date_format(trans_date,"%Y-%m") as month,
country,count(trans_date) as trans_count,
sum(state='approved') as approved_count,
sum(amount) as trans_total_amount,
Sum(Case when state='approved'then amount else 0 End) as approved_total_amount
from transactions group by month,country