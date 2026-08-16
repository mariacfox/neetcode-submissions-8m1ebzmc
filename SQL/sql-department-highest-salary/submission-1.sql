select 
    d.name as department,
    e.name as employee,
    e.salary
from employee e
JOIN department d ON e.department_id = d.id
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM employee e2
    WHERE e2.department_id = e.department_id
);
-- simpler than my original solution