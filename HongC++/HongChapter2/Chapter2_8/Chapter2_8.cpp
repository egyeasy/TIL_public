#include <iostream>

int main()
{
	using namespace std;

	float pi = 3.14f; // long double일 경우에는 l을 씀
	int i = 12324u;

	unsigned int n = 5u;
	long n2 = 5L;
	double d = 6.0e-10;

	int x = 012; // 8진수를 의미
	cout << x << endl;

	x = 0xF;
	cout << x << endl;

	x = 0b1010;
	cout << x << endl;
	
	x = 0b1010'1111;
	cout << x << endl;

	const int price_per_item = 10;

	int num_items = 123;
	int price = num_items * price_per_item;



	return 0;
}