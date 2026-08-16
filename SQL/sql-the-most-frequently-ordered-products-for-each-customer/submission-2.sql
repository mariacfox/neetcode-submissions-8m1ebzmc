-- most frequently ordered product(s) per customer
-- don't need all customers -- only those with 1+ order

with order_counts as (
select customer_id, product_id, count(*) as order_count
from orders
group by 1, 2

), common_prod as (
select customer_id, oc.product_id, dense_rank() over (partition by customer_id order by order_count desc) as prod_rank
    from order_counts oc
)
select cp.customer_id, cp.product_id, product_name
from common_prod cp
join products p on cp.product_id = p.product_id
join customers c on cp.customer_id = c.customer_id
where prod_rank = 1
-- solution works but seems messy