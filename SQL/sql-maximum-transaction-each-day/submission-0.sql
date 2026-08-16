-- report the IDs of transactions that have the maximum amount on their respective day. If multiple transactions on the same day share the maximum amount, include all of them.

select t.transaction_id
from transactions t
join (
    select transaction_id, day, amount, DENSE_RANK() over (partition by DATE(day) order by amount desc) as max_amt
    from transactions
) tmax on t.transaction_id = tmax.transaction_id 
where tmax.max_amt = 1
order by t.transaction_id