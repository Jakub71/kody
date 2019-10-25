DROP TABLE IF EXISTS znajomosci;
CREATE TABLE znajomosci (
 znajomy1 INTEGER PRIMARY KEY,
 znajomy2 INTEGER,
 data DATE NOT NULL
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty (
 id_uzytkownika INTEGER PRIMARY KEY AUTO_INCREMENT,
 imie VARCHAR(70)NOT NULL CHECK (przedmiot <> '')
 nazwisko
 id_kraju
 plec BOOLEAN
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
 id_oceny INTEGER PRIMARY KEY AUTO_INCREMENT,
 data DATE NOT NULL,
 id_ucz CHAR(8) ,
 przedmiot INTEGER,
 oceny DECIMAL(3,2),
 FOREIGN KEY (id_ucz) REFERENCES uczniowie(id_ucz)
 ON DELETE CASCADE,
 FOREIGN KEY (przedmiot) REFERENCES przedmioty(id_przedmioty)
 ON DELETE SET NULL
);


