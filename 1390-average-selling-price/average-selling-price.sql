# Write your MySQL query statement below
select p.product_id,Round(IfNull(sum(p.price*un.units)/sum(units),0),2) as average_price from Prices as p left join 
UnitsSold as un on p.product_id=un.product_id
and un.purchase_date between p.start_date and p.end_date
group by p.product_id