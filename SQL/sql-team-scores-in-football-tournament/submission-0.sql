-- alculate total points for each team

select t.team_id, team_name, coalesce(sum(num_points),0) as num_points
from teams t
left join (
select m.host_team as team_id, 
    case when host_goals > guest_goals then 3
        when host_goals = guest_goals then 1
        else 0 end as num_points
from matches m
UNION ALL
select m.guest_team as team_id, 
    case when guest_goals > host_goals then 3
        when guest_goals = host_goals then 1
        else 0 end as num_points
from matches m) sub on t.team_id = sub.team_id
group by 1, 2
order by num_points desc, team_id;