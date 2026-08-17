select employee_id, COUNT(*) over (partition by team_id) as team_size
from employee
order by employee_id;