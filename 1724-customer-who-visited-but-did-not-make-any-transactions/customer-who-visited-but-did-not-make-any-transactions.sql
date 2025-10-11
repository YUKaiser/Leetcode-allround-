# Write your MySQL query statement below
select customer_id,count(customer_id) as count_no_trans from Visits as vs
left join  transactions as tr on vs.visit_id=tr.visit_id where tr.transaction_id is null
group by customer_id
Union
select customer_id,Count(customer_id)as count_no_trans from Visits  as vs 
right join  transactions as tr on vs.visit_id=tr.visit_id
where tr.transaction_id is null group by customer_id
