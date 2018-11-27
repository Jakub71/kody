/*
 * porega.cpp
 * 
 * Copyright 2018 kl2ag1 <kl2ag1@ubu08>
 */


#include <iostream>
using namespace std;

float potega_re(float x, int n) {
    if (n == 0) return 1;
    return potega_re(x, n-1) * x;
}

int main(int argc, char **argv)
{
	float podstawa;
    int wykladnik;
    cout << " Podstawa: "; cin >> podstawa;
    cout << " Wykładnik: "; cin >> wykladnik;
    cout << "Wyniki: " << potega_re(podstawa, wykladnik);
	return 0;
}

