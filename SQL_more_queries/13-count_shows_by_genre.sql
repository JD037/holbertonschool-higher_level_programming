-- 13-count_shows_by_genre.sql

-- Script to list all genres and the number of shows linked to each

SELECT tv_genres.name AS genre, COUNT(tv_shows.title) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY genre
HAVING COUNT(tv_shows.title) > 0
ORDER BY number_of_shows DESC;
