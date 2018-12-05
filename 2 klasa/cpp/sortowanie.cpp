/*
 * sortowanie.cpp
 */


#include <iostream>
using namespace std;

void wypelnij_los(int tab[], int roz) {
    srand(time(NULL));//inicjacja generatora liczb pseudolosowych
    for(int i = 0; i < roz; i++) {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int roz) {
    for(int i = 0; i < roz; i++) {
        cout << tab[i] << " ";
    }
}

void zamien(int a, int b){
    int tmp = a;
    a = b;
    b = tmp;
}

void sort_bubble(int tab[], int n){
    cout << "\nSortowanie bąbelkowe\n";
    for (int j = n - 1; j > 0; j--) {
        for(int i = 0; i < j; i++) {
            if (tab[i]>tab[i+1])
                zamien(tab[i], tab[i+1]);
        }
    }
}

int main(int argc, char **argv)
{
	int roz = 20;
    int tab[roz];
    //wypelnij_los(tab, rozmiar);
    //drukuj(tab, rozmiar);
    int a = 10;
    int b = 20;
    zamien(a, b);
    cout << a << " " << b;
	return 0;
}

