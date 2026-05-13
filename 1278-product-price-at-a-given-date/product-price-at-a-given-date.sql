/*select product_id,if(change_date <= '2019-08-16',new_price,10) as price
from (select * from products order by new_price d
*/
select product_id,new_price as price 
from products where (product_id,change_date)
in (select product_id,max(change_date) from products where change_date<='2019-08-16' group by product_id )
union
select product_id,10 as price from products 
where product_id not in(
    select product_id from products where change_date <='2019-08-16' 
)