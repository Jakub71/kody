#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  liczbu-23.py
#
def liczby2():
    ile = 0
    for i in range(1, 10):
        for j in range(0, 10):
            if i!=j:
              print("{}{}".format(i, j), end=" ")
              ile += 1 
    return ile
    
def liczby3():
    ile = 0
    for i in range(1, 100):
        for j in range(0, 100):
            for i in range(1, 100):
        if liczba % 11 != 0:
            print(liczba)
        print()
        
def main(args):
    print(liczby2())
    
    return 0
    
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
