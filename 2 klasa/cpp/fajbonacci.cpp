/*
 * silnia.cpp
 * 
 * Copyright 2018 kl2ag1 <kl2ag1@ubu08>
 */


#include <iostream>
using namespace std;

int fibonacci_it(int n){
    int a = 0; // wyraz n - 2
    int b = 1; // wyraz n - 1
    if (n < 1) return a;
    else if (n < 2) return b;
    int wynik = 0;
    for (int i = 2; i <= n; i++){
        wynik = a + b;
        a = b;
        b = wynik;
    }
    return wynik;
}
int fibonacci_re(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci_re(n-1) + fibonacci_re(n-2);
}

int main(int argc, char **argv)
{
    int n;
    cout << " Podaj numer ciągu: " << n << endl;
    for (int i=0; i <= n; i++){
        cout << fibonacci_re(i) << " ";
        if (i < 2) continue;
        else {
            cout << (float)fibonacci_it(i) / (float) fibonacci_it(i-1)<< endl;
            }
        
}
	return 0;
}

