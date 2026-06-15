# Write your MySQL query statement be
select id ,sum(con) as num from
(select requester_id as id
,count(requester_id) as con from RequestAccepted 
group by requester_id 
Union all
select accepter_id as id,count(accepter_id) as con from RequestAccepted
group by accepter_id ) as t1  group by id
order by num desc limit 1