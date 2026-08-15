select country from
(
select country, avg(duration) as avg_duration
from (
select c.name as country, ca.caller_id as id, ca.duration
from country c
left join person p on c.country_code = left(p.phone_number, 3)
left join calls ca on p.id = ca.caller_id
where ca.duration is not null

UNION ALL

select c.name as country, ca2.caller_id as id, ca2.duration
from country c
left join person p on c.country_code = left(p.phone_number, 3)
left join calls ca2 on p.id = ca2.callee_id
where ca2.duration is not null
)
group by 1
) where avg_duration > (select avg(duration) from calls);