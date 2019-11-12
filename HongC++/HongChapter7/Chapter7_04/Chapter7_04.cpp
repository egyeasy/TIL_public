#include <iostream>

using namespace std;

void foo(int* ptr) // 주소만 input으로 들어갈 수 있다.
{
	cout << *ptr << " " << ptr << " " << &ptr << endl;
}

void foo(const int* ptr)
{
	cout << *ptr << " " << ptr << " " << &ptr << endl;

	//*ptr = 10;
}

void foo(double degree, double* sin_out, double* cos_out)
{
	cout << "sin cos" << endl;
	cout << sin_out << " " << cos_out << endl;
	*sin_out = 20;
	*cos_out = 30;
}

void foo(const int const * ptr, int* arr, int length)
{
	for (int i = 0; i < length; ++i)
	{
		cout << arr[i] << endl;
	}
	
	arr[0] = 1.0; // 이것도 가능

	int x = 1;

	// ptr = &x;
}

int main()
{
	int value = 5;

	cout << value << " " << &value << endl;

	int* ptr = &value;

	cout << "ptr: " << ptr << " " << &ptr << endl;

	foo(ptr);
	foo(&value);
	//foo(5); // 주소가 없어서 안됨. const int로도 안된다

	double degree = 30;
	double sin, cos;
	cout << "sin cos main: " << endl;
	cout << &sin << " " << &cos << endl;
	foo(degree, &sin, &cos);
	
	cout << sin << ' ' << cos << endl;
}