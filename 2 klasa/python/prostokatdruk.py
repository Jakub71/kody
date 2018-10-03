#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prostokat.py
#  
#  Copyright 2018  <>


    
def main(args):
    a = int(input("Podaj długość boku a: "))
    
    b = int(input("Podaj długość boku b: "))
    
    znak = input("Podaj znak:")
    if i == 0 or i == x - 1:
        print(znak*y)
        continue
    for i in range(a):
        for j in range(b):
            print(znak, end='') 
        print()
    
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
