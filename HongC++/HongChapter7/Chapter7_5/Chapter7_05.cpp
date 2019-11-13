#include <iostream>
#include <array>
#include <tuple>

using namespace std;

std::tuple<int, double> getTuple()
{
	double a = 10;
	double d = 3.14;
	return std::make_tuple(a, d);
}

int* getValue(int x)
{
	int value = x * 2;
	return &value;
}

int* allocateMemory(int size)
{
	return new int[size];
}

int& getVal(int x)
{
	int value = x * 2;
	return value;
}

int& get(std::array<int, 100>& my_array, int ix)
{
	return my_array[ix];
}

struct S
{
	int a, b, c, d;
};

S getStruct()
{
	S my_s{ 1, 2, 3, 4 };
	return my_s;
}

int main()
{
	int *value = getValue(3);

	//int* array = new int[10];
	int* array = allocateMemory(1024);
	delete[] array;

	int &val = getVal(5);

	cout << val << endl;

	std::array<int, 100> my_array;
	my_array[30] = 10;
	
	// 데이터 일부를 고치고 싶다.
	get(my_array, 30) = 1024;

	cout << my_array[30] << endl;

	S my_s = getStruct();
	cout << my_s.a << endl;

	// tuple
	std::tuple<int, double> my_tp = getTuple();
	cout << std::get<0>(my_tp) << endl; // a
	cout << std::get<1>(my_tp) << endl; // d

	auto [a, d] = getTuple();
	cout << a << endl;
	cout << d << endl;

	return 0;
}