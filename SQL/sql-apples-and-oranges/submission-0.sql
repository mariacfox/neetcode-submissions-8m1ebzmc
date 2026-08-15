select sale_date, apples_sold - oranges_sold as diff
from (
select distinct a.sale_date, b.sold_num as apples_sold,
    c.sold_num as oranges_sold
from sales a
left join sales b on a.sale_date = b.sale_date and b.fruit = 'apples'
left join sales c on a.sale_date = c.sale_date and c.fruit = 'oranges'
)
order by sale_date
;