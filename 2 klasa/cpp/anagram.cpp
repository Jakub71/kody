/*
 * anagram.cpp
 */
#include <iostream>
using namespace std;


int zlicz(char tab[]){
    int i = 0;
    while(tab[i] != '\0') i++;
    return i;
}
void wyswietl(char tekst[], int roz) {
    for(int i = 0; i < roz; i++){
        cout << tekst[i];
    }    
}

void anagram(char tb[], int roz){
    for
    
    
}
int main(int argc, char **argv)
{
    char tekst[50];  
    cin.getline(tekst, 50);
    wyswietl(tekst, zlicz(tekst));  
	return 0;
}

