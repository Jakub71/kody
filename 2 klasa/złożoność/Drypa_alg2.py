#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main(args):
    a = 0
    while a < 1 or a > 99:
        a = int(input('Podaj liczbę: '))
    print('podana liczba: {}'.format(a))
    for i in range(2, 102, 2):
        if a == i:
            print('{} jest liczbą parzystą'.format(a))
            break;
        if i == 100:
            print('{} nie jest liczbą parzystą'.format(a))
        return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
