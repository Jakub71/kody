#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  algorytmy1.py
#  
def wersja2():
    n = int(input("Liczba:"))
    for i in range(i, n, 2):
        print(i)
   
def wersja1():
    n = int(input("Liczba:"))
    i = 1
    while i < n:
        print(i)
        i = i + 2
## algorytm częsciowo poprawny, skonczony , o złozoności liniowej O(n)
def main(args):
    wersja1()
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
