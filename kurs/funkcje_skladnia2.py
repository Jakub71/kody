#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje_skladnia2.py

def mnoz(a, b):
    print(a * b)
    
def mnoz2(*args): # zmienna lista argumentów
    wynik = 1
    for liczba in args:
        wynik *= liczba
    print(wynik)
    
def wylicz(imie1='Adam', imie2='Ewa', **kwargs): # słownik zmiennej długości
    print(imie1)
    print(imie2)
    for k, v in kwargs.items():
        print('{} {}'.format(k, v))
        
########### typy argumentów w funkcjach:
# pozycyjne wymagane
# nazwane wymagane
# argumenty domyślne niewymagane
#argumenty zmiennej długości: listy, słowniki
        
def main(args):
    #mnoz(4, 6)
    #mnoz2(1, 2, 3, 4, 5)
    wylicz(imie2='Ola', imie3='Piotr', imie4='dźefko')
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
