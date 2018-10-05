DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    IDucznia INTEGER PRIMARY KEY,
    Ocena INTEGER,
    Data DATE,
    IDprzedmiotu INTEGER
);

DROP TABLE IF EXISTS przedmioty;
CREATE TABLE przedmioty (
    IDprzedmiotu INTEGER PRIMARY KEY,
    NazwaPrzedmiotu TEXT,
    Nazwisko_naucz TEXT,
    Imie_naucz TEXT,
    FOREIGN KEY (IDprzedmiotu) REFERENCES oceny(IDprzedmiotu)
);

DROP TABLE IF EXISTS uczniowie;
CREATE TABLE uczniowie (
    IDucznia INTEGER PRIMARY KEY,
    nazwisko TEXT,
    imie TEXT,
    ulica TEXT,
    dom INTEGER ,
    IDklasy TEXT,
    FOREIGN KEY (IDucznia) REFERENCES oceny(IDucznia)
);
