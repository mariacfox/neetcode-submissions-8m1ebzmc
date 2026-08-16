-- (max) three most recent orders per customer

select c.name as customer_name, c.customer_id, order_id, order_date
from customers c
left join (
    select customer_id, order_id, order_date,
        ROW_NUMBER() over (partition by customer_id order by order_date desc) as rn
    from orders
    order by customer_id, order_date desc
) orders_rn on c.customer_id = orders_rn.customer_id
where orders_rn.rn <= 3
order by c.name, c.customer_id, orders_rn.order_date desc
