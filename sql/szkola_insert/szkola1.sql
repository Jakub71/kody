DROP TABLE IF EXISTS tbUczniowie;
CREATE TABLE tbUczniowie (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	imie TEXT,
	nazwisko TEXT,
	plec INTEGER,
	idKlasa INTEGER NOT NULL REFERENCES tbklasy(id),
	egzHum NUMERIC NOT NULL DEFAULT 0,
	egzMat NUMERIC NOT NULL DEFAULT 0,
	egzJez NUMERIC NOT NULL DEFAULT 0
);

DROP TABLE IF EXISTS tbKlasy;
CREATE TABLE tbKlasy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	klasa TEXT,
	rokNaboru INTEGER,
	rokMatury INTEGER
);
DROP TABLE IF EXISTS tbPrzedmioty;
CREATE TABLE tbPrzedmioty (
id INTEGER PRIMARY KEY AUTOINCREMENT,
przedmiot TEXT,
nazwiskoNaucz TEXT,
imieNaucz TEXT,
plecNaucz INTEGER
);
DROP TABLE IF EXISTS tbOceny;
CREATE TABLE tbOceny (
id INTEGER PRIMARY KEY AUTOINCREMENT,
ocena NUMERIC,
datad DATE,
idUczen INTEGER NOT NULL DEFAULT 0,
idPrzedmiot INTEGER NOT NULL DEFAULT 0,
FOREIGN KEY (idUczen) REFERENCES tbUczniowie(id)
FOREIGN KEY (idPrzedmiot) REFERENCES tbPrzedmioty(id)
);
INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL,'1A', 2015, 2018);
INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL,'1A', 2015, 2018);
INSERT INTO tbKlasy(id, klasa, rokNaboru, rokMatury) VALUES (NULL,'1B', 2015, 2018);

INSERT INTO tbUczniowie VALUES (NULL, 'Adam', 'Kowalski', 0, 3, 80.6, 50, 90.5);
INSERT INTO tbUczniowie VALUES (NULL, 'Ilona', 'Nowak', 1, 2, 50.6, 78.9, 80);
INSERT INTO tbUczniowie VALUES (NULL, 'Jaś', 'Fasola', 0, 1, 70.7, 67.7, 90);

INSERT INTO tbPrzedmioty(id, przedmiot, nazwiskoNaucz, imieNaucz, plecNaucz) VALUES (NULL,'biologia', 'Henryszewski', 'Robert', 0);
INSERT INTO tbPrzedmioty(id, przedmiot, nazwiskoNaucz, imieNaucz, plecNaucz) VALUES (NULL,'fizyka', 'Ignaczak', 'Jolanta', 1);

INSERT INTO tbOceny(id, ocena,datad, idUczen, idPrzedmiot) VALUES (NULL, 4.5, '2015-10-01', 'Adam Kowalski', 'biologia');
INSERT INTO tbOceny(id, ocena,datad, idUczen, idPrzedmiot) VALUES (NULL, 3, '2015-09-29','Adam Kowalski', 'fizyka');
INSERT INTO tbOceny(id, ocena,datad, idUczen, idPrzedmiot) VALUES (NULL, 4, '2015-09-25', 'Ilona Nowak', 'biologia');
INSERT INTO tbOceny(id, ocena,datad, idUczen, idPrzedmiot) VALUES (NULL, 3.5,'2015-10-05', 'Ilona Nowak', 'fizyka');
INSERT INTO tbOceny(id, ocena,datad, idUczen, idPrzedmiot) VALUES (NULL, 5, '2015-09-29', 'Jaś Fasola', 'biologia');
INSERT INTO tbOceny(id, ocena,datad, idUczen, idPrzedmiot) VALUES (NULL, 2, '2015-10-02', 'Jaś Fasola','fizyka');