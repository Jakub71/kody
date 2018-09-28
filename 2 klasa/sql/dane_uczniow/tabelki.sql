DROP TABLE IF EXISTS dane_osobowe;
CREATE TABLE dane_osobowe (
    Nr_ucz INTEGER PRIMARY KEY,
    Dzien INTEGER,
    Miesiac INTEGER,
    Rok INTEGER,
    M_urodzenia TEXT,
    Wojewodztwo TEXT
);

DROP TABLE IF EXISTS nazwiska;
CREATE TABLE nazwiska (
    Nr_ucz INTEGER PRIMARY KEY,
    Nazwisko TEXT,
    Imie1 TEXT,
    Imie2 TEXT DEFAULT,
    FOREIGN KEY (Nr_ucz) REFERENCES dane_osobowe(Nr_ucz)
);

DROP TABLE IF EXISTS oceny;
CREATE TABLE oceny (
    Nr_ucz INTEGER PRIMARY KEY,
    Zach TEXT,
    Rel_Ety INTEGER DEFAULT,
    Jpol INTEGER DEFAULT,
    Jang INTEGER DEFAULT,
    Jniem INTEGER DEFAULT,
    Mat INTEGER DEFAULT,
    Hist INTEGER DEFAULT,
    Geog INTEGER DEFAULT,
    Biol INTEGER DEFAULT,
    Fiz INTEGER DEFAULT,
    Che INTEGER DEFAULT,
    Tech INTEGER DEFAULT,
    Info INTEGER DEFAULT,
    Plas INTEGER DEFAULT,
    PO INTEGER DEFAULT,
    WF TEXT DEFAULT,
    FOREIGN KEY (Nr_ucz) REFERENCES dane_osobowe(Nr_ucz)
);
