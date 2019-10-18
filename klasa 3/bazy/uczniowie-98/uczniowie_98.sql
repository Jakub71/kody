DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie (
 id_ucz CHAR(8) PRIMARY KEY,
 imie VARCHAR(30) NOT NULL CHECK (imie <> ''),
 nazwisko VARCHAR(40) NOT NULL CHECK (nazwisko <> ''),
 klasa CHAR(5) DEFAULT ''
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty (
 id_przedmioty INTEGER PRIMARY KEY AUTO_INCREMENT,
 przedmiot VARCHAR(70)NOT NULL CHECK (przedmiot <> '')
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


