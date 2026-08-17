select employee_id
from (
select coalesce(e.employee_id, s.employee_id) as employee_id,
    name, salary
from employees e
full join salaries s on e.employee_id = s.employee_id
) 
where name is null or salary is null
order by employee_id;