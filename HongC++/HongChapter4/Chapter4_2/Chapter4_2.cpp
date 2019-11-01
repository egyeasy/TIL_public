#include <iostream>
//#include "test.cpp" // 가급적 사용하지 않음
#include "MyConstants.h"

using namespace std;

int value = 123; // 전역 변수

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
	int value = 1; // name hiding(shadowing)이 작동하여 전역 변수와 겹치지 않게 함
	cout << value << endl; // 1

	// 전역 영역 연산자
	cout << ::value << endl;

	doSomething();
	doSomething();

	cout << b << endl;


	cout << "In main.cpp file " << Constants::pi << " " << &Constants::pi << endl;
	

	return 0;
}