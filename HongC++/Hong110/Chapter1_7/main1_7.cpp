#include <iostream>

using namespace std;

void doSomething(int x)
{
	x = 123;
	cout << x << endl; // #2
}


int main()
{
	int x = 0;

	cout << x << " " << &x << endl;

	{
		//int x = 1;
		x = 1;
		cout << x << " " << &x << endl;

	}

	cout << x << " " << &x << endl;

	x = 0;

	cout << x << endl; // #1
	doSomething(x);
	cout << x << endl; // #3

	return 0;

}