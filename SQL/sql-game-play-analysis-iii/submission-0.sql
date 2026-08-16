select player_id, event_date, SUM(games_played) OVER (partition BY player_id order by event_date) as games_played_so_far
from activity
group by 1, 2
order by 1, 2;