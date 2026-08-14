-- Write a SQL query to find the names of all salespeople who have not made any orders with the company named "CRIMSON".

select name
from sales_person sp
where sp.sales_id not in (
    select o.sales_id
    from orders o 
    join company c on o.com_id = c.com_id
    where c.name = 'CRIMSON'
)

