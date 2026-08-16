with long as (
    select year, Wimbledon as player_id, 'wimbledon' as game
from championships
UNION ALL 
select year, Fr_open as player_id, 'Fr_open' as game
from championships
UNION ALL
select year, US_open as player_id, 'US_open' as game
from championships
UNION ALL
select year, Au_open as player_id, 'Au_open' as game
from championships
)
select p.player_id, player_name, count(*) as grand_slams_count
from players p
join long l on p.player_id = l.player_id
group by 1, 2