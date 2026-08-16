select min(log_id) as start_id, max(log_id) as end_id
from (
SELECT 
        log_id,
        log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
FROM logs
order by log_id
) group by grp
order by start_id