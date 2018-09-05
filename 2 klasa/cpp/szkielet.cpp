/*
 * szkielet.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int liczba; // deklaracja zmiennej liczba typu integer czyli liczb całkowitych
    liczba = 12.78; //przyłączenie danych
    //std::cout << liczba;
    cout << liczba;
    
    int a, b, c, d; //deklaracja
    a = b = c = d = 0;// inicjalizacja -pierwsza wartość podana
    a = 10;
    b = 2*a;
    c =b-a;
    d = a / b;// dzielenie
    
    cout << "\n" << a << " " << b << " " << (b - a);      //"\n" przejście do nowej linii
    cout << " " << d;
	return 0;
}

