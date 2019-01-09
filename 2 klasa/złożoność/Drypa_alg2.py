#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    a = 0
    while a <= 0 or a >= 100:
        a = int(input("Podaj liczbę: "))
        
    i = 2
    
    while i > 0:
        if a == i:
            print("Liczba jest parzysta")
            break
        else:
            i = i + 2
            if i > a:
                print("Liczba nie jest parzysta")
                break
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
