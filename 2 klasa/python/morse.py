#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  morse.py

kod = {'A':'.-', 'B':'-...', 
        'C':'-.-.', 'D':'-..', 'E':'.', 
        'F':'..-.', 'G':'--.', 'H':'....', 
        'I':'..', 'J':'.---', 'K':'-.-', 
        'L':'.-..', 'M':'--', 'N':'-.', 
        'O':'---', 'P':'.--.', 'Q':'--.-', 
        'R':'.-.', 'S':'...', 'T':'-', 
        'U':'..-', 'V':'...-', 'W':'.--', 
        'X':'-..-', 'Y':'-.--', 'Z':'--..', 
        '1':'.----', '2':'..---', '3':'...--', 
        '4':'....-', '5':'.....', '6':'-....', 
        '7':'--...', '8':'---..', '9':'----.', 
        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
        '?':'..--..', '/':'-..-.', '-':'-....-', 
        '(':'-.--.', ')':'-.--.-', ' ':' '}

def koduj():
    tekst = input('Podaj tekst: ').upper() 
    for l in tekst:
        print(kod[l])

def dekoduj():
    tekst = []
    litera = ' '
    while litera > '':
        litera = input('Podaj Kod Morsea: ')
        tekst.append(litera)
    print(tekst)
    
    
def main(args):
    dekoduj()
    koduj()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
