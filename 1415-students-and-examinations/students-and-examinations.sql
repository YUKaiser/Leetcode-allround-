# Write your MySQL query statement below
select su.student_id,su.student_name,sub.subject_name,count(e.subject_name) as attended_exams
from students as su cross join 
subjects as sub  left join examinations as e
on su.student_id=e.student_id and e.subject_name=sub.subject_name
group by student_id,subject_name
order by student_id



 