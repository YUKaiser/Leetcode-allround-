# Write your MySQL query statement below
select Round(sum(if(odate=pdate,1,0))/count(id)*100,2) as immediate_percentage from
(select Distinct(customer_id) as id , min(order_date) as odate,min(customer_pref_delivery_date)
as pdate from Delivery group by customer_id) 
as t


