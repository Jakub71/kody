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
    rok_naboru = IntegerField(default=0)
    rok_matury = IntegerField(default=0)

class Uczen(BazaModel):
    
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = IntegerField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egz_hum = FloatField(default = 0)
    egz_mat = FloatField(default = 0)
    egz_jez = FloatField(default = 0)
    
class Przedmiot(BazaModel):
   
    przedmiot = CharField(null=False)
    imie_naucz = CharField(null=False)
    nazwisko_naucz = CharField(null=False)
    plec_naucz = IntegerField()
    
class Ocena(BazaModel):
    
    datad = DateField()
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    ocena = FloatField(null=False)
    
def main(args):
    if os.path.exists(baza_plik):
        os.remove(baza_plik)
    baza.connect() # połączenie z bazą
    baza.create_tables([Klasa, Uczen, Przedmiot, Ocena])
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
