#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat.py
#  
#  Copyright 2018  <>


    
def main(args):
    
    a = int(input("Podaj długość boku a: "))
    b = int(input("Podaj długość boku b: "))
    znak = input("Podaj znak: ")
 
    for i in range(a):
        for j in range (b):
            if j == 0 or j == b - 1 or i == 0 or i == a - 1:
                print(znak, end=' ')
            else:
                print(" ", end=' ')
        print()
    
    return 0

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
