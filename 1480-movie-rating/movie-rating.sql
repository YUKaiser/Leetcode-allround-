# Write your MySQL query statement below

(select u.name as results from Users as u join 
(select user_id, max_u from
(
select user_id,count(user_id) as max_u from
movierating
group  by user_id)
as u1 where max_u=
(select Max(max_u) from (
select user_id,count(user_id) as max_u from
movierating
group  by user_id) as u2)) as up
on u.user_id=up.user_id
order by u.name limit 1)


Union ALL
(select m.title as results from Movies as m join 
(select movie_id,avgrate from (select movie_id,Avg(rating) as avgrate from MovieRating 
where created_at between "2020-02-01" and "2020-02-29" group by movie_id ) as m_id_t
 where avgrate=(select max(avgrate) from (select movie_id,Avg(rating) as avgrate from MovieRating where created_at between "2020-02-01" and "2020-02-29" group by movie_id) as t)) as m2 on m.movie_id=m2.movie_id order by m.title limit 1)