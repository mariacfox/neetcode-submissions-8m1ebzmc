select 
    d.name as department,
    e.name as employee,
    e.salary
from employee e
join department d on e.department_id = d.id
where (e.department_id, e.salary) in (
    select 
        department_id,
        max(salary)
    from employee
    group by department_id
)