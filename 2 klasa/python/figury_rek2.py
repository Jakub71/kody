#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury_rek.py
import turtle

def rysuj(bok, kat, przyrost, warunek):
    turtle.forward(bok)
    turtle.right(kat)
    if kat < warunek:
        kat += 1
        rysuj(bok, kat, przyrost, warunek)


def main(args):
    bok = int(input("Podaj bok: "))
    kat = int(input("Podaj kąt: "))
    przyrost = 10
    warunek = 180
    turtle.setup(800, 600)
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    turtle.speed(10)
    
    rysuj(bok, kat, przyrost, warunek)
    
    turtle.end_fill()
    turtle.done()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
