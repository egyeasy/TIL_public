#include <iostream>
//#include "test.cpp" // ������ ������� ����
#include "MyConstants.h"

using namespace std;

int value = 123; // ���� ����

int a = 1;

static int g_a = 1;

//void doSomething()
//{
//	static int a = 1;
//	++a;
//	cout << a << endl;
//}

// forward declaration
extern int b;
extern void doSomething();

int main()
{
	cout << value << endl; // 123
	int value = 1; // name hiding(shadowing)�� �۵��Ͽ� ���� ������ ��ġ�� �ʰ� ��
	cout << value << endl; // 1

	// ���� ���� ������
	cout << ::value << endl;

	doSomething();
	doSomething();

	cout << b << endl;


	cout << "In main.cpp file " << Constants::pi << " " << &Constants::pi << endl;
	

	return 0;
}