#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  orm_peewee.py 

import os
from peewee import *

baza_plik = 'test.db'
baza =SqliteDatabase(baza_plik) #instancja bazy


### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza
        
class Klasa(BazaModel):
    nazwa = CharField(null=False)
    roknaboru = IntegerField(default=0)
    rokmatury = IntegerField(default=0)

class Uczniowie(BazaModel):
    id = CharField(null=False)
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = BooleanField()
    idklasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egzhum = FloatField(default = 0)
    egzmat = FloatField(default = 0)
    egzjez = FloatField(default = 0)
    
class Przedmiot(BazaModel):
    id = CharField(null=False)
    przedmiot = CharField(null=False)
    imienaucz = CharField(null=False)
    nazwiskonaucz = CharField(null=False)
    plecnaucz = BooleanField()
    
class Oceny(BazaModel):
    datad 
    id_uczen = ForeignKeyField(Klasa, related_name='uczniowie')
    id_przedmiot = ForeignKeyField(Klasa, related_name='uczniowie')
    ocena = 
    
def main(args):
    if os.path_exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Wynik])
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
