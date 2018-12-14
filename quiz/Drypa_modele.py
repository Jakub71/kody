#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py
from peewee import *

baza_plik = 'test.db'
baza =SqliteDatabase(baza_plik) #instancja bazy


### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza
        
class Kategoria(BazaModel):
    
    kategoria = CharField(null=False)

class Pytanie(BazaModel):
    
    pytanie = CharField(null=False)
    kategoria = ForeignKeyField(Kategoria, related_name='kategorie')
    
class Odpowiedz(BazaModel):
   
    pytanie = ForeignKeyField(Pytanie, related_name='pytania')
    odpowiedz = CharField(null=False)
    odpok = IntegerField()
    
