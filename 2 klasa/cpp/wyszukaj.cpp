/*
 * wyszukaj.cpp
 */

#include <iostream>
#include <cstdlib>
using namespace std;

void wypelnij_los(int tab[], int rozmiar)
{
    srand(time(NULL));  // inicjacja generatoraliczb pseudolosowych
    for(int i = 0; i < rozmiar; i++)
    {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int rozmiar)
{
    for(int i = 0; i < rozmiar; i++)
    {
        cout << tab[i] << ' ';
    }
}

void sort_insert(int tab[], int n)
{
    cout << "\nSortowanie przez wstawianie" << endl;
    int i, j, tmp;
    int licznik = 0;
    for(i = 1; i < n; i++)
    {
        tmp = tab[i];
        j = i - 1;
        while(j >= 0 && tab[j] >tmp)
        {
            tab[j+1] = tab[j];
            j--;
            licznik ++;
        }
        tab[j+1] = tmp;
    }
    cout << "Liczba porównań: " << licznik << endl;
}

int main(int argc, char **argv)
{
	int n = 20;
    int tab[n];
    wypelnij_los(tab, n);
    int szuk = 0;
    cout << "Podaj liczbę: ";
    cin >> szuk;
    
	return 0;
}

