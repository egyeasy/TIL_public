#include <iostream>

using namespace std;

int foo(int x, int y); // x, y�� �Ķ����

int foo(int x, int y)
{
	return x + y;
} // x and y are destoryed here

int main()
{
	int x = 1, y = 2;

	foo(6, 7); // 6, 7 : arguments(actual parameters)
	foo(x, y + 1); // 6, 3�� argument

	return 0;
}