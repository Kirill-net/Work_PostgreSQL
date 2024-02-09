
INSERT INTO perfomen (id, name) 
VALUES(1, 'Oleg Sluckiy'),
	  (2,'Aniya'),
	  (3, 'Gazmanov'),
	  (4, 'Dj_cool'),
	  (5, 'Dj_so'),
	  (6, 'Korney Chukovsky'),
	  (7, 'Lolita'),
	  (8, 'Rush')

INSERT INTO musicstile (id, stile_name) 
values (1, 'Jazz'),
	   (2, 'Rock'),
	   (3, 'Classic'),
	   (4, 'Retro'),
	   (5, 'Arthous'),
	   (6, 'Rave'),
	   (7, 'Dance')

INSERT INTO album (id, album_name, al_year) 
VALUES(1, 'yelow submarine', 2020),
	  (2,'Hit_1', 2021),
	  (3, 'salut of sprink', 2020),
	  (4, 'Cosmos', 2022),
	  (5, 'History', 2018),
	  (6, 'Shchelkunchic', 2019),
	  (7, 'wooosh', 2010),
	  (8, 'Trees of main', 2023),
	  (9, 'Hit_2', 2022),
	  (10, 'Best_hit_2023', 2023)

INSERT INTO track (id, tr_name, tr_time, album_id) 
VALUES (1, 'moon', 315, 4),
	   (2, 'hop hop', 230, 5),
	   (3, 'link stile', 220, 7),
	   (4, 'Root', 140, 1),
	   (5, 'black child', 187, 3),
	   (6, 'kill her', 266, 4),
	   (7, 'kosmo', 350, 10),
	   (8, 'History girl', 200, 5),
	   (9, 'Who am i', 185, 3),
	   (10, 'Bob', 173, 1),
	   (11, 'Looke at me', 215, 2),
	   (12, 'Friends', 217, 6),
	   (13, 'Goblins of wood', 222, 9),
	   (14, 'Blue', 115, 10),
	   (15, 'Sky', 320, 8),
	   (16, 'Full moon', 140, 8),
	   (17, 'Mirror', 177, 9),
	   (18, 'Magic', 189, 10),
	   (19, 'my dreem', 100, 10)

INSERT INTO collection (id, col_name, col_year)
VALUES (1, 'new-1', 2021),
	   (2, 'new-2', 2020),
	   (3, 'new-3', 2022),
	   (4, 'fff', 2023),
	   (5, 'Romantic', 2020),
	   (6, 'Romantic2', 2018),
	   (7, 'dance33', 2019),
	   (8, 'newdance', 2023)

INSERT INTO musicstile_perfomen (perfomen_id, musicstile_id)
VALUES (1, 2),
	   (1, 3),
	   (1, 1),
	   (1, 5),
	   (2, 2),
	   (3, 5),
	   (4, 3),
	   (4, 6),
	   (4, 7),
	   (5, 1),
	   (6, 3),
	   (7, 2),
	   (7, 4),
	   (7, 3),
	   (8, 2)

INSERT INTO perfomen_album (perfomen_id, album_id)
VALUES (1, 10),
	   (1, 3),
	   (1, 5),
	   (2, 8),
	   (2, 4),
	   (3, 9),
	   (3, 3),
	   (4, 9),
	   (4, 5),
	   (5, 1),
	   (6, 6),
	   (7, 7),
	   (7, 4),
	   (8, 4),
	   (8, 2)

insert into track_collection (collection_id, track_id)
values (1, 10),
	   (1, 2),
	   (1, 1),
	   (2, 6),
	   (2, 7),
	   (2, 9),
	   (3, 3),
	   (4, 3),
	   (4, 6),
	   (5, 10),
	   (6, 1),
	   (6, 2),
	   (6, 5),
	   (6, 8),
	   (6, 7),
	   (6, 10),
	   (6, 3),
	   (7, 7),
	   (7, 4),
	   (8, 1),
	   (8, 2)
	  


