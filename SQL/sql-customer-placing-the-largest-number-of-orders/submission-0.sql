select customer_number
from (
select customer_number, count(*) as num_orders
from orders
group by 1) sub
order by num_orders desc
limit 1;