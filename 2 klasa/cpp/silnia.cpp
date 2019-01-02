/*
 * silnia.cpp
 * 
 * Copyright 2018 kl2ag1 <kl2ag1@ubu08>
 */


#include <iostream>
using namespace std;

float silnia_re(int n) {
    if (n == 0) return 1;
    return silnia_re(n-1) * n;
}

int silnia_it(int n){
    int silnia = 1;
    int i;
    for (i = 1; i <= n; i++)
        silnia = silnia * i;
    return silnia;
    }
int main(int argc, char **argv)
{
    int n;
    cout << " Podaj liczbę: "; cin >> n;
    cout << "Wyniki: " << silnia_it(n);
	return 0;
}

