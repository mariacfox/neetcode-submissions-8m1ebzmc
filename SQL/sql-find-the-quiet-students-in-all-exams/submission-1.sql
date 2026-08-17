SELECT student_id, student_name
FROM Student
WHERE student_id IN (
    -- students who took any exam
    SELECT student_id FROM Exam
    EXCEPT
    -- minus anyone who was ever highest or lowest
    SELECT student_id FROM (
        SELECT student_id,
            dense_rank() OVER (PARTITION BY exam_id ORDER BY score DESC) AS rnk_high,
            dense_rank() OVER (PARTITION BY exam_id ORDER BY score ASC)  AS rnk_low
        FROM Exam
    ) ranked
    WHERE rnk_high = 1 OR rnk_low = 1
)
order by student_id;