# Write your MySQL

with Con_num as(
     select num,
     lag(num) over (order by id) as prev,
     lead(num) over (order by id) as next
     from Logs
)
select distinct num as ConsecutiveNums from Con_num
where (prev-num)=0 and (next-num)=0