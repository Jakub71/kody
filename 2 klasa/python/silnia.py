#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potegi.py
#
def silnia_it(n):
    # 0! = 1
    # n! = 1*2 * ... *n
    wynik = 1
    
    for i in range(1, n + 1):
        wynik = wynik * i
        print(wynik)
    return wynik

def main(args):
    n = int(input("Podaj liczbę: "))
    silnia_it(n)
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))

