-- Write a query to find the customer_id and name of customers who spent at least $100 in both June 2020 and July 2020.

with june_orders as (
select customer_id, sum(o.quantity * p.price) as order_spend
from orders o
join product p on o.product_id = p.product_id
where order_date between '2020-06-01' and '2020-06-30'
group by o.customer_id
having sum(o.quantity * p.price) >= 100
), july_orders as (
    select customer_id, sum(o.quantity * p.price) as order_spend
from orders o
join product p on o.product_id = p.product_id
where order_date between '2020-07-01' and '2020-07-31'
group by o.customer_id
having sum(o.quantity * p.price) >= 100
)
select c.customer_id, c.name
from customers c
join june_orders jo on c.customer_id = jo.customer_id
join july_orders ju on c.customer_id = ju.customer_id