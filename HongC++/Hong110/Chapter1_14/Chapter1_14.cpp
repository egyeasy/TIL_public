#include <iostream>
#include <algorithm>
using namespace std;

#define MY_NUMBER 333
#define MAX(a, b) (((a)>(b)) ? (a) : (b)) // °ýÈ£·Î ½Î¾ß ÇÑ´Ù.

#define LIKE_APPLE

void doSomething()
{
#ifdef LIKE_APPLE
	cout << "Apple " << endl;
#endif

#ifndef LIKE_APPLE
	cout << "Orange " << endl;
#endif
}

int main()
{
	cout << MY_NUMBER << endl;
	
	cout << MAX(1 + 3, 2) << endl;
	cout << max(1 + 3, 2) << endl;

	doSomething();

	return 0;
}