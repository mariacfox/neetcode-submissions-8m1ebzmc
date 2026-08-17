select min(distance) as shortest
from (
SELECT
    p1.x, p2.x, ABS(p1.x - p2.x) AS distance
FROM point p1
JOIN point p2 ON p1.x != p2.x
);