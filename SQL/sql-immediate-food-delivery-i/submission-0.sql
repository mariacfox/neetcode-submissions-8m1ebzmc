select round(sum(immediate)/count(*)::decimal*100, 2) as immediate_percentage
from (
select delivery_id, 
case when order_date = customer_pref_delivery_date then 1
        else 0 end as immediate
from delivery
) sub;