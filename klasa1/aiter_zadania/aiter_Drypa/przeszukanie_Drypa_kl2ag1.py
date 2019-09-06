#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  przeszukanie_Drypa_kl2ag1.py
import random

def wypelnij(szuk):
    for i in range(10):
        szuk.append(random.randint(0, 50))
    print(szuk)
    
def main(args):
    i = 0
    szuk = []
    wypelnij(szuk)
    i = int(input("Podaj liczbę: "))
    for a in range (len(szuk)):
        if szuk.count(i) == 0 or i > 51:
            print("Nieznaleziono elementu")
            i += 1
            return
        else:
            print("Znaleziono element")
            return
            
    return 0
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
