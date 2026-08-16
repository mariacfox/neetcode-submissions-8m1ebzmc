-- most frequently ordered product(s) per customer
-- don't need all customers -- only those with 1+ order

SELECT customer_id, product_id, product_name
FROM (
    SELECT
        o.customer_id,
        o.product_id,
        p.product_name,
        RANK() OVER (PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) AS rnk
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN products p ON o.product_id = p.product_id
    GROUP BY o.customer_id, o.product_id, p.product_name
) temp
WHERE rnk = 1
ORDER BY customer_id, product_id;
-- cleaner solution