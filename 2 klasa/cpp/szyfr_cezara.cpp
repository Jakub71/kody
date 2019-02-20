/*
 * szyfr_cezara.cpp
 */
#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

#define MAKS 100

void deszyfruj(char tekst[], int klucz){

}

void szyfruj(char tekst[], int klucz){
    klucz = klucz % 26;
    int kod = 0;
    int ilosc = strlen(tekst);
    
    for(int i = 0; i < ilosc; i++)
    {
        kod = (int)tekst[i];
        if (tekst[i] == ' ')
        {
            ;
        }
        else if (kod < 91)
        {
            kod += klucz;
            if (kod > 90) kod -= 26;
        }
        else
        {
            kod += klucz;
            if (kod > 122) kod -=26;
        }
        
        tekst[i] = char(kod);
        cout << tekst[i];
    }

}


int main(int argc, char **argv)
{
    char tekst[MAKS];
    int klucz = 0;
    
    cout << "Podaj tekst: " << endl;
    cin.getline(tekst, MAKS);
    
    cout << "Podaj klucz: ";
    cin >> klucz;
    
    szyfruj(tekst, klucz);
    deszyfruj(tekst, klucz);
    return 0;
}
