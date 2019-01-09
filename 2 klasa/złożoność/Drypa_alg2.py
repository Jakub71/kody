#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Drypa_alg2.py
#  
def podaj():
    a = int(input("Podaj a:"))
    if a > 0 and a < 100:
        return a
    else:
        podaj()

def main(args):
    podaj()

    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
