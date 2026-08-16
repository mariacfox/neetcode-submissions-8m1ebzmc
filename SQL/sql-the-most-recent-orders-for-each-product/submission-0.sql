select product_name, product_id, order_id, order_date
from (
select p.product_name, p.product_id, o.order_id, o.order_date,
    dense_rank() OVER (partition by p.product_name order by o.order_date desc) as rank
from products p
join orders o on p.product_id = o.product_id
order by p.product_id, order_id, order_date
) where rank = 1
order by product_name, product_id, order_id