#include <iostream>

using namespace std;

int i, n, p1, p2, fib;

int main()
{
    cout << "Podaj n: ";
    cin >> n;
    if(n < 3)
        if(n == 0)
            fib = 0;
        else
		fib=1;
	else
    p1=p2=1;
    for(i=3; i<=n; i++)
	{
		fib=p1+p2;
		p2=p1;
		p1=fib;
	}
	cout << "F(" << n << ")=" << fib << endl;
    return 0;
}
