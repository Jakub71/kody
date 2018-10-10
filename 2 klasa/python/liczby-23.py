#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczbu-23.py
#
def liczby2(a = 10, b = 99):
    for liczba in range(a, b):
        if liczba % 11 != 0:
            print(liczba)
    print()   
def liczby3(a = 100, b = 999):
    for liczba in range(a, b):
        if liczba % 11 != 0:
            print(liczba)
        print()
        
def main(args):
    print(liczby2())
    print(liczby3())
    return 0
    
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
