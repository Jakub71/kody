#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = input("Podaj ilość typowanych liczb: ")
    maksliczba = input("Podaj maks. losowana liczbę: ")
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))
    exit()

    liczba = random.randint(1, 10)
    # komentarz
    # komentarz
    for i in range(3):
        odp = input("Podaj liczbę od 1 do 10: ")
        print(" Podałeś liczbę:", odp)

        if liczba == int(odp):
            print("Zgadłeś!")
            break  # przerywa działania petli
        else:
            print("Jeszcze raz!!!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
