-- report the IDs of transactions that have the maximum amount on their respective day. If multiple transactions on the same day share the maximum amount, include all of them.

SELECT transaction_id
FROM transactions
WHERE (DATE(day), amount) IN (
    SELECT DATE(day), MAX(amount)
    FROM transactions
    GROUP BY DATE(day)
)
ORDER BY transaction_id;