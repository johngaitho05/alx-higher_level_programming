-- This script  lists all genres not linked to the show Dexter
-- switch database
use hbtn_0d_tvshows
-- query data
SELECT name
FROM tv_genres
WHERE id NOT IN (
SELECT DISTINCT tsg.genre_id
FROM tv_show_genres tsg
INNER JOIN tv_shows ts
ON ts.id=tsg.show_id
WHERE ts.title = 'Dexter')
ORDER BY name;
