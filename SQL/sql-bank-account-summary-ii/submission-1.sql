select name, SUM(t.amount) as balance
from users u
join transactions t on u.account = t.account
group by u.account, u.name
having sum(t.amount) > 10000