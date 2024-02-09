SELECT tr_name, tr_time FROM track 
WHERE tr_time = (SELECT MAX(tr_time) FROM track)

SELECT tr_name FROM track
WHERE tr_time >= 210

SELECT col_name FROM collection 
WHERE col_year BETWEEN 2018 AND 2020 

SELECT name FROM perfomen 
WHERE name NOT LIKE '% %'

SELECT tr_name FROM track 
WHERE tr_name LIKE '%мой%' OR  tr_name LIKE '%my%'






