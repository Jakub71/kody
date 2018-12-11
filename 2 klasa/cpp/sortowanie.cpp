/*
 * sortowanie.cpp
 */


#include <iostream>
using namespace std;

void wypelnij_los(int tab[], int n) {
    srand(time(NULL));//inicjacja generatora liczb pseudolosowych
    for(int i = 0; i < n; i++) {
        tab[i] = rand() % 101;
    }
}

void drukuj(int tab[], int n) {
    for(int i = 0; i < n; i++) {
        cout << tab[i] << " ";
    }
}

void zamien(int &a, int &b){
    int tmp = a;
    a = b;
    b = tmp;
}

void zamien2(int tab[], int i){
    int tmp;
    tmp = tab[i];
    tab[i] = tab[i + 1];
    tab[i + 1] = tmp;
}
void sort_bubble(int tab[], int n){
    cout << "\nSortowanie bąbelkowe\n";
    int licznik = 0;
    for (int j = n - 1; j > 0; j--) {
        for(int i = 0; i < j; i++) {
            licznik++;
            if (tab[i]>tab[i+1])
                zamien2(tab, i);
        }
    }
    cout << "\nPowtórzeń: " << licznik << endl;
}

void sort_insert(int tab, int n) {
    cout << "\nSortowanie przez wstawianie\n";
    int i, j, tmp;
    for ( i = 1; i < n; i++) {
        tmp = tab[i];
        j = i - 1;
        while (j >= 0 && tab[j] > tmp) {
            tab[j+1] = tab[j];
            j--
        }
        tab[j+1] = tmp;
    }
}

int main(int argc, char **argv)
{
	int n = 20;
    int tab[n];
    wypelnij_los(tab, n);
    drukuj(tab, n);
    //int a = 10;
    //int b = 20;
    //zamien(a, b);
    //cout << a << " "<< b;
    cout << endl;
    sort_insert (tab, n);
    cout << endl;
    zamien2(tab, n);
    drukuj(tab, n);
    
	return 0;
}

