-- find the names of all sellers who did not make any sales in the year 2020

select seller_name
from seller
where seller_id not in (
select distinct seller_id
from orders
where sale_date between '2020-01-01' and '2020-12-31'
group by seller_id
)
order by seller_name;
