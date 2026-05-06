-- return ordered by student_id; tie-breaker with exam_id
select student_id, exam_id, score
from (
select student_id, exam_id, score,
    ROW_NUMBER() over (partition by student_id order by score desc, exam_id) as score_rank
from exam_results )
where score_rank = 1
order by student_id