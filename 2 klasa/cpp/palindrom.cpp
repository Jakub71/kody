/*
 * palindrom.cpp
 */


#include <iostream>

using namespace std;

int zlicz(char tb[]) {
    int i = 0;
     while(tb[i] != '\0') i++;
     return i;
 }
 
bool palindrom(char wyraz[], int rozmiar){
    rozmiar = cin.gcount();
    int polowa = rozmiar / 2
    bool czyPal = true;
    for(int i = 0; i < polowa ; i++) {
      if (i == rozmiar - 1) continue;   
      else{
        czyPal = false;
        break;  
        }   
    }  
}

int main(int argc, char **argv)
{   const int roz = 50;
    char tekst[roz];
    cout << ("Wprowadź wyraz: ");
    cin.getline(tekst, roz);
	palindrom(tekst, cin.gcount());
	return 0;
}

