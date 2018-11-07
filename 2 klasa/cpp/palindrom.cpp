/*
 * palindrom.cpp
 */
#include <iostream>
#include <string.h>
using namespace std;

bool palindrom(char wyraz[], int roz){
    bool czyPal = true;
    for(int i = 0; i < roz / 2; i++) {
        if (wyraz[i] == wyraz[roz-1-i]) 
        ; // instrukcja pusta
        else {
        czyPal = false;
        break;  
        }   
    }  
    return czyPal;
}

int main(int argc, char **argv)
{   const int roz = 20;
    char tekst[roz];
    cout << ("Wprowadź wyraz: ");
    cin.getline(tekst, roz);
	if (palindrom(tekst, strlen(tekst))){
            cout << "Wyraz jest palindromem";
    }
    else{
        cout << "Wyraz nie jest palindromem";
        }
	return 0;
}

