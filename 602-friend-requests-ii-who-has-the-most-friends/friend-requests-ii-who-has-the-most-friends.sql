# Write your MySQL query statement be
select id,count(*) as num from 
(select requester_id as id from RequestAccepted
Union ALL
select accepter_id from RequestAccepted) as t1
group by id
order by num desc limit 1
