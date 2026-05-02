

select distinct num as ConsecutiveNums from (
     select num,
     lag(num) over (order by id) as prev,
     lead(num) over (order by id) as next
     from Logs 
) as p
where (prev=num) and num=next