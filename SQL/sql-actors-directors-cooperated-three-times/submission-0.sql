select actor_id, director_id
from actor_director
group by actor_id, director_id
having count(timestamp) > 2