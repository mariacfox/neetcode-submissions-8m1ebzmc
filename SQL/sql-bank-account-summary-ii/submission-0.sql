select name, balance
from users u
join (
select account, sum(amount) as balance
from transactions
group by account
) b on u.account = b.account
where b.balance > 10000