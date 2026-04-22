select round(count(b.player_id)/count(a.player_id),2) as fraction
from 
(select player_id,Min(event_date) as first_login_date from activity group by player_id)
 as a left join
activity as b on b.player_id=a.player_id
and Datediff(b.event_date,a.first_login_date)=1