/*
 * wskazniki.cxx
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int x = 11;
    cout <<"Wartość x"<< x << endl;
    cout << "Adres x" << &x << endl;
    cout << "Wartośc pod adresem "<< * &x << endl;
    cout << "rozmiar x " << sizeof(x) << endl;
    
    int *px;
    px = &x;
    cout << "Wartość wskaźnika "<< px << endl;
    cout << "wartość wskazywana przez wskaźnik: "<< *px << endl;
    *px = 20;
    cout << *px << endl;
    cout << px << endl;
    int y = 50;
    px = &y;
    cout << *px << endl; 
	return 0;
}

