-- Write your query below

select user_id, max(time_stamp) as last_stamp
from logins
-- use below if date_part('year', time_stamp) is not available
WHERE time_stamp >= '2020-01-01' AND time_stamp < '2021-01-01'
group by 1;