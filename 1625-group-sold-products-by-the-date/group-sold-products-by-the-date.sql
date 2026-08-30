# Write your MySQL query statement below
#select sell_date, count(distinct(product))
#from Activities group by sell_date
select sell_date,
count(distinct product) as num_sold,
Group_concat(distinct product order by product  separator ',')  as products from activities
group by sell_date
order by sell_date