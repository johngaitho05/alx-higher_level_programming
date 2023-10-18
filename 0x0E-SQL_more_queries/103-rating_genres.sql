-- This script lists all genres in the database hbtn_0d_tvshows_rate by their rating.
select tg.name as name, sum(tsr.rate) as rating
from tv_show_ratings tsr
right join tv_show_genres tsg
on tsg.show_id=tsr.show_id
left join tv_genres tg
on tg.id=tsg.genre_id
group by tg.name
order by rating desc;
