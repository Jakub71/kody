/*
 * znak.cpp
*/


#include <iostream>

using namespace std;

void licz_znaki(char tab[]){
    int i = 0;
    int biale, inter, licz;
    biale = inter = licz = 0;
    while(tab[i] != '\0') {
        cout << tab[i] << " ";
       //~ if (tab[i] == ' ' || tab[i] == '\t')
          //~  biale++;
        //~else
           //~ cout << tab[i];
        switch (tab[i]) {
            case ' ': biale++; break;
            case '\t': biale++; break;
            case ',': inter++; break;
            case '.': inter++; break;
            default: licz++; break;
        }
        i++; 
    }
    cout << "\nZnaków białych: " << biale << endl; 
    cout << "\nZnaków interpunkcyjnych: " << inter << endl;
    cout << "\nReszta: " << licz << endl;   
}

void ascii(char tab[]) {
    int i = 0;
    while(tab[i] != '\0') {
        cout << (int)tab[i] << " ";
        i++;
    }
}
// A-Z ASC2 65-90, a-z ASC2 97- 122 ( zakresy dużych i małych liter)
void zamiana_liter(char tab[]){
    int i = 0;
    int z = 0;
    while(tab[i] != '\0') {
        z = (int)tab[i];
        if (z >= 65 && z <= 90){
         z = z + 32;   
         }
         cout << (char)z << " ";   
        i++;
    }
    
}
int main(int argc, char **argv)
{
    const int rozmiar = 30; // deklaracja stałej
    char znaki[rozmiar]; // deklaracja tablicy znakowej 
    cout << "Jak się nazywasz? ";
    cin.getline(znaki, rozmiar);
    cout << "Cześć " << znaki << endl;
    // licz_znaki(znaki);
    ascii(znaki);
	zamiana_liter(znaki);
	return 0;
}

