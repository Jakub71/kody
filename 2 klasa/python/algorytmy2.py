#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  algorytmy2.py
#  
def main(args):
    n = int(input("Podaj liczbę:"))
    silnia = 1
    i = 1
    while i <= n:
        silnia = silnia * i
        i = i + 1
    print(silnia)
    

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
