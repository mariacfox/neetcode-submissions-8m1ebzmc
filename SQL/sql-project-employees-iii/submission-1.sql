select project_id, employee_id
from (
select project_id, p.employee_id, experience_years,
    dense_rank() over (partition by project_id order by experience_years desc) as rank
from project p
inner join employee e on p.employee_id = e.employee_id
) t where rank = 1
order by project_id, employee_id