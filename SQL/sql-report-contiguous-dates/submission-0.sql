WITH dated_states AS (
    SELECT fail_date AS date, 'failed' AS period_state
    FROM failed
    UNION ALL
    SELECT success_date AS date, 'succeeded' AS period_state
    FROM succeeded
),
grouped AS (
    SELECT
        date,
        period_state,
        ROW_NUMBER() OVER (ORDER BY date) 
            - ROW_NUMBER() OVER (PARTITION BY period_state ORDER BY date) AS grp
    FROM dated_states
    WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
)
SELECT period_state, MIN(date) AS start_date, MAX(date) AS end_date
FROM grouped
GROUP BY period_state, grp
ORDER BY start_date;