# Write your MySQL query statement below
SELECT 
    reg.contest_id, 
    ROUND(COUNT(reg.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register AS reg
GROUP BY reg.contest_id
ORDER BY percentage DESC, reg.contest_id ASC;
