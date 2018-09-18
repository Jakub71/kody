#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abc.py
#


def maks(a, b, c):
    m = None
     if a > b:
         ifa > c: 
            m = a
    elif b > c:
        m = b
    print("Najwieksza:", m)
    return m;
    
def main(args):
   assert(maks(3, 2, 1) == 3)
   assert(maks(2, 3, 1) == 3)
   assert(maks(1, 2, 3) == 3)
   assert(maks(1, 1, 3) == 3)
   assert(maks(3, 1, 1) == 3)
   assert(maks(3, 3, 1) == 3)
   assert(maks(3, 3, 3)
        
   
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
