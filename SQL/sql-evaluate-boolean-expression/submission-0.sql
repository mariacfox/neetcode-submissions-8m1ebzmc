-- Write a query to evaluate each boolean expression and return the result as true or false

SELECT 
    left_operand, 
    operator, 
    right_operand,
    CASE 
        WHEN operator = '=' AND v.value = v2.value THEN 'true'
        WHEN operator = '>' AND v.value > v2.value THEN 'true'
        WHEN operator = '<' AND v.value < v2.value THEN 'true'
        ELSE 'false'
    END AS value
FROM expressions e
JOIN variables v ON e.left_operand = v.name
JOIN variables v2 ON e.right_operand = v2.name