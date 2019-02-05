/*
 * dek2bin.cpp
 */


#include <iostream>
using namespace std;

void dec2any(int lliczba, int podstawa, int tab[]){
    int i = 0;
    do {
       tab[i] = liczba % podstawa;
       liczba = liczba / podstawa;
       i++; 
    }while ( liczba != 0);
    return i-1;
}

void bin2dec(int tab[]){
        ;
}
int main(int argc, char **argv)
{
    int tab[8];
    int liczba, podstawa;
    cout << "Podaj liczbę i podstawę systemu docelowego: ";
    cin > liczba >> podstawa;
    int i = dec2any(liczba, podstawa, tab);
    cout << "Wynik: ";

    return 0;
}

