#include <iostream>
#include <typeinfo>

using namespace std;

struct Something
{
	int a, b, c, d; // 4 x 4 = 16 bytes
};

int main()
{
	int x = 5;

	cout << x << endl;
	cout << &x << endl; // & : address of operator
	cout << (int)&x << endl;

	// de-reference operator (*)
	cout << *&x << endl; // 이 메모리 주소에 실제로 담겨있는게 뭐냐

	
	int *ptr_x = &x; //  변수가 포인터임을 표시
	int *ptr_y = &x, *ptr_z = &x;

	typedef int* pint;
	pint ptr_k = &x, ptr_j = &x;

	cout << *ptr_x << endl;

	cout << "\n" << endl;

	double d = 1.0;
	double* ptr_d = &d;
	cout << ptr_d << endl;
	cout << *ptr_d << endl;

	cout << typeid(ptr_x).name() << endl; // int *

	cout << sizeof(x) << endl;
	cout << sizeof(d) << endl;
	cout << sizeof(&x) << " " << sizeof(ptr_x) << endl; // 4 4
	cout << sizeof(&d) << " " << sizeof(ptr_d) << endl; // 4 4

	Something ss;
	Something* ptr_s;

	cout << sizeof(Something) << endl; // 16
	cout << sizeof(ptr_s) << endl;	   // 4

	int* ptr_a;

	//cout << *ptr_a << endl; // error - uninitialized


	return 0;
}