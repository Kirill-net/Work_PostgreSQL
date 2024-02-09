SELECT tr_name, tr_time FROM track
ORDER BY tr_time DESC 
LIMIT 1

SELECT tr_name FROM track
WHERE tr_time >= 210

SELECT col_name FROM collection 
WHERE col_year >=2018 AND col_year <=2020 

SELECT name FROM perfomen 
WHERE name NOT LIKE '% %'

SELECT tr_name FROM track 
WHERE tr_name LIKE '%мой%' OR  tr_name LIKE '%my%'






