#include <iostream>
#include "MyConstants.h"

int b = 123;

void doSomething()
{
	using namespace std;

	cout << "Hello " << endl;

	cout << "In test.cpp file " << Constants::pi << " " << &Constants::pi << endl; // �ּұ��� ���
}