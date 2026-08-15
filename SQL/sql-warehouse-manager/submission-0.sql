select w.name as warehouse_name, sum(units * volume) as volume
from warehouse w
left join (
select product_id, width * length * height as volume
from products
) sub on w.product_id = sub.product_id
group by 1;