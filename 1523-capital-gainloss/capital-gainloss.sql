# Write your MySQL query statement below
select t1.stock_name,(t1.price1-t2.price2) as capital_gain_loss from 
(select stock_name,sum(price) as price1 from stocks where operation="Sell" group by stock_name) as t1
join
(select stock_name,sum(price) as price2 from stocks where operation="Buy" group by stock_name) as t2
on t1.stock_name=t2.stock_name
#group by t1.stock_name