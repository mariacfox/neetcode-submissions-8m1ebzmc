
select task_id, generate_series(1, subtasks_count, 1) as subtask_id
from Tasks
except
select * from Executed