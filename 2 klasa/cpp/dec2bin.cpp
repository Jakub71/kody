/*
 * dek2bin.cpp
 */


#include <iostream>
using namespace std;

void dec2bin(int l)
{
    int i=0;
    int tab[8];
    while(l != 0)
    {
        tab[i++]=l%2;
        l/=2;
    }

    for(int j=i-1;j>=0;j--)
        cout << tab[j];
}

int main(int argc, char **argv)
{
    int liczba;
    cout << "Podaj liczbę od 0 do 255: ";
    cin >> liczba;
    cout << liczba << " po zamianie na postać binarną: ";
    dec2bin(liczba);
    cout << endl;

    return 0;
}

