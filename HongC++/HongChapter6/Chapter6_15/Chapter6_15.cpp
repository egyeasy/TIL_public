#include <iostream>

using namespace std;

void doSomething(const int x)
{
	cout << x << endl;
}

void doSomething2(const int& x) // 변수 복사 없이 가능
{
	cout << x << endl;
}

int main()
{
	int x = 5;
	int& ref_x = x;
	const int& ref1_x = x;

	const int x2 = 5;
	const int& ref2_x = x2;

	const int& ref_x2 = 3 + 4;

	cout << ref_x2 << endl;
	cout << &ref_x2 << endl;

	int a = 1;

	cout << endl;

	doSomething(a);
	doSomething(a + 2);
	doSomething(3);

	doSomething2(a);
	doSomething2(3);
	doSomething2(a + 3);

	

	return 0;
}