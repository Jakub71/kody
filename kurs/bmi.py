#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bmi.py
#  
def bmi(masa, wzrost):
    
    bmi = masa / (wzrost / 100)**2
    print('BMI = {:.2f}'.format(bmi))
    if bmi < 18.5:
        print('Niedowaga')
    if bmi >= 18.5 and bmi < 24.9:
        print('Norma')
    if bmi >= 25 and bmi < 30:
        print('Nadwaga')
    if bmi >= 30:
        print('Otyłość')
    
def main(args):
    masa = int(input("Podaj swoją masę w kg:"))
    wzrost = int(input("Podaj swój wzrost w centymetrach:"))
    bmi(masa, wzrost)
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
