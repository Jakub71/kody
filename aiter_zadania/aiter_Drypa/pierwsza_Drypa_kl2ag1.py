#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pierwsza_Drypa_kl2ag1.py

def main(args):
    n = int(input("Proszę podać liczbę: "))
    i = 2
    
    for a in range(n + 1):
        if not i * i <= n:
            print("Liczba pierwsza")
            return
            
        if not (n % i == 0):
               i += 1
        else: 
            print("Liczba złożona")  
            return

if __name__ == '__main__':
    import sys
sys.exit(main(sys.argv))
