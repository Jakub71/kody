DROP TABLE IF EXISTS zamowienia;
CREATE TABLE zamowienia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NumerZamowienia INTEGER,
    Adresklienta TEXT,
    DataZamowienia DATE,
    SzczegolyZamowienia TEXT
);

DROP TABLE IF EXISTS zamowienia2;
CREATE TABLE zamowienia2 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    IDKlienta INTEGER,
    NazwaKlienta TEXT,
    Adres TEXT,
    KodPocztowy TEXT,
    Miasto TEXT,
    Wojewodztwo TEXT
);

DROP TABLE IF EXISTS dane_gus;
CREATE TABLE dane_gus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Liczba_mieszkancow INTEGER,
    Liczba_kobiet INTEGER,
    Grupa_wiekowa TEXT,
    Data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES miasta(id_miasta)
);

