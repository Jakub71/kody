#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    ileliczb = int(input("Podaj ilość typowanych liczb: "))
    maksliczba = int(input("Podaj maks. losowaną liczbę: "))
    print("Wytypuj {} z {} liczb".format(ileliczb, maksliczba))

    # losowanie liczb

    liczby = []  # lista wylosowanych liczb
    for i in range(ileliczb):
        liczba = random.randint(1, maksliczba)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
    print(liczby)

        # odp = input("Podaj liczbę od 1 do 10: ")
        # print(" Podałeś liczbę:", odp)

        # if liczba == int(odp):
        #     print("Zgadłeś!")
        #     break  # przerywa działania petli
        # else:
        #     print("Jeszcze raz!!!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
