/*
 * Drypa_alg1.cpp
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a = 0;
    while (a <= 0 || a >= 100)
    {
        cout << "Podaj liczbę: ";
        cin >> a;
    }
    int i = 2;
    
    for (int b = 1; b != 100; b++){
        if (a == i){
            cout << "Liczba jest parzysta";
            break;
        }else {
            i = i + 2;
            if (i == 100){
                cout << "Liczba nie jest parzysta";
                break;
                }
            }
        }
    return 0;
}
