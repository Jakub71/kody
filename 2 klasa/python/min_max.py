#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  min_max.py
import random

def minmax():
    a = int(input('Podaj liczbę: '))
    min = a
    max = a
    
    while True:
        a = int(input('Podaj liczbę: '))
        if a < 1:
            break
        if a < min:
            min = a
        if a > max:
            max = a
   
    return min, max

def minmax2(lista):
    min = max = lista[0]
    for a in lista:
        if a < min:
            min = a
        if a > max:
            max = a
    
    return min, max

def main(args):
    #~min, max = minmax()    
    #~print("Najmniejsza liczba: ", min)
    #~print("Największa liczba: ", max)
    
    
    lista = []
    for i in range(100):
        lista.append(random.randint(1,100))
    print(lista)
    min, max = minmax2(lista)
    print("Najmniejsza liczba: ", min)
    print("Największa liczba: ", max)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
