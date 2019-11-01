#include <iostream>

auto add(int x, int y) -> int;
// auto add(int x, int y) -> double;

int add(int x, int y)
{
	return x + (double)y;
}

auto add(double x, double y)
{
	return x + y;
}

int main()
{
	using namespace std;

	auto a = 123;
	auto d = 123.0;
	auto c = 1 + 2;

	auto result = add(12, 2);

	return 0;
}