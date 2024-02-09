CREATE TABLE IF NOT EXISTS Perfomen (
	id SERIAL  PRIMARY KEY,
	name VARCHAR(40) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS MusicStile (
	id SERIAL  PRIMARY KEY,
	stile_name VARCHAR(40) UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS MusicStile_Perfomen (
	Perfomen_id INTEGER REFERENCES perfomen(id),
	MusicStile_id INTEGER REFERENCES MusicStile(id),
	CONSTRAINT pm PRIMARY KEY (Perfomen_id, MusicStile_id)
);
CREATE TABLE IF NOT EXISTS Album (
	id SERIAL  PRIMARY KEY,
	album_name VARCHAR(40) UNIQUE NOT NULL,
	al_year INTEGER null,
	CHECK (al_year > 1900 and al_year < 2100)
);
CREATE TABLE IF NOT EXISTS Perfomen_Album (
	Perfomen_id INTEGER REFERENCES perfomen(id),
	Album_id INTEGER REFERENCES Album(id),
	CONSTRAINT pa PRIMARY KEY (Perfomen_id, Album_id)
);
CREATE TABLE IF NOT EXISTS Track (
	id SERIAL  PRIMARY KEY,
	tr_name VARCHAR(40) NOT NULL,
	tr_time INTEGER NOT NULL,
	CHECK (tr_time > 0 and tr_time < 650),
	Album_id integer NOT NULL REFERENCES Album(id)
);
CREATE TABLE IF NOT EXISTS Collection (
	id SERIAL  PRIMARY KEY,
	col_name VARCHAR(40) UNIQUE NOT null,
	col_year INTEGER null,
	CHECK (col_year > 2000 and col_year < 2100)
);
CREATE TABLE IF NOT EXISTS Track_Collection (
	Track_id INTEGER REFERENCES Track(id),
	Collection_id INTEGER REFERENCES Collection(id),
	CONSTRAINT tc PRIMARY KEY (Track_id, Collection_id)
);
	