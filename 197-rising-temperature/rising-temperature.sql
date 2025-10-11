# Write your MySQL query statement below
Select w1.id from weather as w1
join weather as w2 
on w1.recordDate=DATE_ADD(w2.recordDate,interval 1 day)
where w1.temperature > w2.temperature