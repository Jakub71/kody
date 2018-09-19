#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#

def maks(a, b, c):
    maks = a
    if b > maks:
        maks = b
    if c > maks:
            maks = c
    return maks
    

    
def main(args):
    
    #a = int(input("Podaj pierwsza liczbe: "))
    #print(a)
    
    #b = int(input("Podaj druga liczbe: "))
    #print(b)
    #c = int(input("Podaj trzecia liczbe: "))
    #print(c)
    #if a > b and a > c:
     #   print("największe jest", a)
    #if b > a and b > c:
     #   print("największe jest", b)
    #if c > a and c > b:
     #   print("największe jest", c)
    #else:
     #   if c==a==b:
      #      print("wszystkie liczby są równe")
       # else:
        #    if c==a and c > b:
         #       print("1 i 3 liczba są najwieksze,mają wartość:",a)
          #  if c==b and b > a:
           #     print("2 i 3 liczba są najwieksze, mają wartość:",c)
            #if b==a and b > c:
             #print("1 i 2 liczba są najwieksze, mają wartość:",b)
             
    assert(maks(3, 2, 1) == 3)
    assert(maks(2, 3, 1) == 3)
    assert(maks(1, 2, 3) == 3)
    assert(maks(1, 1, 3) == 3)
    assert(maks(3, 1, 1) == 3)
    assert(maks(1, 3, 1) == 3)
    assert(maks(1, 3, 3) == 3)
    assert(maks(3, 3, 1) == 3)
    assert(maks(3, 3, 3) == 3)
    
    return 0
if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
