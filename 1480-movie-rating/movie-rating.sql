# Write your MySQL query statement below
(select u.name as results from Users as u JOin
MovieRating as mr on u.user_id=mr.user_id
group by mr.user_id,u.name
order by Count(*) Desc,u.name
  limit 1 )

  Union All
  (select m.title as results  from Movies as m join
   MovieRating as mr on m.movie_id=mr.movie_id
   where mr.created_at between "2020-02-01" and "2020-02-29"
   group by m.movie_id,m.title
   order by AVG(mr.rating) Desc,m.title
   limit 1
   )
  