#include <iostream>

using namespace std;

void doSomething(int n)
{
	n = 10;
	cout << "in doSth " << n << endl;
}

void doSomething2(const int &n)
{
	// n = 10;
	cout << "in doSth " << n << endl;
}

void printElements(int(&arr)[5]) // ���� ǥ���ؾ� ��
{
	for (int i = 0; i < 5; i++)
	{
		// do sth
	}
}

struct Something
{
	int v1;
	float v2;
};

struct Other
{
	Something st;
};


int main()
{
	int value = 5;

	// pointer
	int* ptr = nullptr;
	ptr = &value;

	// reference
	int& ref = value;

	cout << ref << endl;

	ref = 10; // *ptr = 10;

	cout << value << " " << ref << endl;


	cout << &value << endl;
	cout << &ref << endl;
	cout << ptr << endl;
	cout << &ptr << endl;

	
	int x = 5;
	int& ref2 = x;
	
	const int y = 8;
	//int& ref2 = y; // �Ұ��� - ref2�� �� �ٲ���� ���� �ֱ� ����
	//const int& ref2 = y;

	int value1 = 5;
	int value2 = 10;

	int& ref3 = value1;

	cout << ref3 << endl;

	ref3 = value2;

	cout << ref3 << endl;


	int n = 5;
	cout << n << endl;

	doSomething(n);

	cout << n << endl;

	doSomething2(n);

	cout << n << endl;

	Other ot;
	ot.st.v1 = 1.0; // ����ؼ� ������ ���Ⱑ ������

	int& v1 = ot.st.v1;
	v1 = 1;


	int value4 = 5;
	int* const ptr4 = &value4; // �ּҸ� �� �ٲٴ� ��
	int& ref4 = value4;


	return 0;
}