-- This script  lists all genres not linked to the show Dexter
-- switch database
use hbtn_0d_tvshows
-- query data
SELECT tg.name AS name
FROM tv_show_genres AS tsg
INNER JOIN tv_genres AS tg
ON tg.id=tsg.genre_id
INNER JOIN tv_shows AS ts
ON ts.id=tsg.show_id
WHERE ts.title != 'Dexter'
GROUP BY tg.name ORDER BY tg.name;
