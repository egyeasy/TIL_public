#include <iostream>
#include <array>
#include <functional>
using namespace std;

int func(int x)
{
	return 5;
}

int goo()
{
	return 10;
}

bool isEven(const int& number)
{
	if (number % 2 == 0) return true;
	else return false;
}

bool isOdd(const int& number)
{
	if (number % 2 != 0) return true;
	else return false;
}

typedef bool(*check_fcn_t)(const int&);
using check_fcn_t = bool(*)(const int&);

void printNumbers(const array<int, 10>& my_array, bool (*check_fcn)(const int&) = isEven)
void printNumbers(const array<int, 10>& my_array, check_fcn_t check_fcn = isEven)
void printNumbers(const array<int, 10>& my_array, std::function<bool(const int&)> check_fcn = isEven)
{
	for (auto element : my_array)
	{
		if (check_fcn(element) == true) cout << element;
	}
	cout << endl;

}

int main()
{

	cout << func << endl;
	
	int(*fcnptr)(int) = func; // func를 실행()시키지 않고 주소만 받는다.

	cout << fcnptr << endl; // 괄호를 치면 실행이 됨

	//fcnptr = goo;
	
	cout << fcnptr << endl; // 10


	std::array<int, 10> my_array = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

	for (auto element : my_array)
	{
		if (element % 2 == 0) cout << element;
	}
	cout << endl;

	std::function<bool(const int&)> fcnptr1 = isEven;

	printNumbers(my_array, isEven);
	printNumbers(my_array, isOdd);

	fcnptr1 = isOdd;

	printNumbers(my_array, fcnptr1);


	return 0;
}