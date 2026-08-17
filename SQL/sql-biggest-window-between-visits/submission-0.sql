-- get largest window between consecutive visits and today
-- today is 2021-01-01

select user_id, max(next_visit::DATE - visit_date::DATE) as biggest_window
from (
    select user_id, visit_date, LEAD(visit_date, 1, '2021-01-01') OVER (partition by user_id ORDER BY visit_date) AS next_visit
    from user_visits
    order by user_id, DATE(visit_date)
)
group by user_id
order by user_id