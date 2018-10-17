/*
 * liczby-23.cpp
 */


#include <iostream>
using namespace std;

int liczby2() {
    int ile = 0; // deklaracja + inicjacja = definicja
    for (int i = 1; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (i !=j){ //instrukcja warunkowa (warunek)
                cout << i << j << " "; // wydrukuj i oraz j i zrób spację między nimi
                ile++;
            }
        }
    }
    return ile;
}


int main(int argc, char **argv)
{
	cout << "\n\nLiczb 2-cyfrowych: " << ile << endl;
	return 0;
}

