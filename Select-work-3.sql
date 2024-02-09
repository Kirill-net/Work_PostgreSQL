SELECT COUNT(perfomen_id) FROM musicstile_perfomen 
GROUP BY musicstile_id 
ORDER BY musicstile_id 

SELECT COUNT(tr_name) FROM track t
JOIN album a ON t.album_id = a.id 
WHERE al_year BETWEEN 2019 AND 2020

SELECT AVG(tr_time) FROM track
GROUP BY album_id

SELECT DISTINCT name FROM perfomen p
WHERE name NOT IN (
SELECT name FROM perfomen p 
JOIN perfomen_album pa ON p.id = pa.perfomen_id
JOIN album a ON pa.album_id = a.id 
WHERE al_year = 2020
)

SELECT col_name FROM collection c
JOIN track_collection tc ON c.id = tc.collection_id
JOIN track t ON tc.track_id = t.id
JOIN perfomen_album pa ON t.album_id = pa.album_id
JOIN perfomen p ON pa.perfomen_id = p.id
WHERE name = 'Rush'




