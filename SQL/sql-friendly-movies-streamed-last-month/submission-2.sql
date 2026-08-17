select distinct title as TITLE
from tv_program tv
join content c on tv.content_id = c.content_id
    and c.kids_content = 'Y'
    and c.content_type = 'Movies'
    and tv.program_date >= '2020-06-01' and tv.program_date < '2020-07-01'