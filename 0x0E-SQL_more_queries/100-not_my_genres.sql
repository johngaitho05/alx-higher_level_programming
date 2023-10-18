-- This script  lists all genres not linked to the show Dexter
-- query data
SELECT name
FROM tv_genres
WHERE id NOT IN (
SELECT DISTINCT tsg.genre_id
FROM tv_show_genres tsg
LEFT JOIN tv_shows ts
ON ts.id=tsg.show_id
WHERE ts.title = 'Dexter')
ORDER BY name;
