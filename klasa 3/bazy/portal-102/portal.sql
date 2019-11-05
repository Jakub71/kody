DROP TABLE IF EXISTS znajomosci;
CREATE TABLE znajomosci (
 znajomy1 INTEGER NOT NULL REFERENCES uzytkownicy(id_uzytkownika) ON DELETE CASCADE,
 znajomy2 INTEGER NOT NULL REFERENCES uzytkownicy(id_uzytkownika) ON DELETE CASCADE,
 data DATE NOT NULL,
 PRIMARY KEY(znajomy1, znajomy2)
);

DROP TABLE IF EXISTS uzytkownicy;
CREATE TABLE uzytkownicy (
 id_uzytkownika INTEGER PRIMARY KEY AUTOINCREMENT,
 imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
 nazwisko VARCHAR(40) NOT NULL CHECK (nazwisko <> ''),
 id_kraju INTEGER,
 plec CHAR(1),
 FOREIGN KEY (id_kraju) REFERENCES kraje(id_kraje)
 ON DELETE CASCADE
);

DROP TABLE IF EXISTS kraje;
CREATE TABLE kraje (
 id_kraje INTEGER PRIMARY KEY AUTOINCREMENT,
 kraj TEXT
);

DROP TABLE IF EXISTS zdjecia;
CREATE TABLE zdjecia (
 id_zdjecia INTEGER PRIMARY KEY AUTOINCREMENT,
 data_dodania DATE,
 id_uzytkownika INTEGER,
 szerokosc INTEGER,
 wysokosc INTEGER,
 FOREIGN KEY (id_uzytkownika) REFERENCES uzytkownicy(id_uzytkownika)
 ON DELETE CASCADE
);



