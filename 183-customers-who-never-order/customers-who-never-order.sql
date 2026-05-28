# Write your MySQL query statement below
select name as Customers from Customers where
id not in (select c.id from customers as c join orders as o on c.id=o.customerId)