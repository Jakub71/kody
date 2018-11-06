/*
 * anagram.cpp
 */
#include <iostream>
using namespace std;
int zlicz(char tb[]) {
    int i = 0;
     while(tb[i] != '\0') i++;
     return i;
 }
 
 void wyswietl(char tekst[], int rozmiar) {
     for(int i = 0; i < rozmiar; i++) {
         cout << tekst[i];
    }
}
void anagram(char tb[], int roz) {
    //for zaczyna od ostatniego znaku
    for (int i = roz - 1; i >= 0; i--) {
        cout << tb[i];
        }
}
int main(int argc, char **argv){
    const int roz = 50; 
    char tekst[roz];
    cin.getline(tekst, roz);
    wyswietl(tekst, cin.gcount());
    cout << endl;
    anagram(tekst, cin.gcount());
    cout << endl;
	return 0;
}
 
