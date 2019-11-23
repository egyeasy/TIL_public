#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

void addOne(int& y)
{
	cout << y << " " << &y << endl;
	y = y + 1;
}

void getSinCos(const double degree, double& sin_out, double& cos_out) // degree는 영향을 못 미치고, double은 함수를 호출한 곳에 영향을 미칠 수 있게 됨
{
	static const double pi = 3.141592;
	double radians = degree * pi / 180.0;
	sin_out = std::sin(radians);
	cos_out = std::cos(radians);
}

void foo(const int& x)
{
	cout << x << endl;
}

typedef int* pint;

void foo1(int*& ptr) // int* 대신 pint를 써도 됨
{
	cout << ptr << " " << &ptr << endl;
}

void printElements(int (&arr)[4]) // 대괄호 안에 개수가 반드시 들어가야 함
{

}

void printElements(vector<int>& arr) // const가 들어가도 됨
{

}


int main()
{
	int x = 5;

	cout << x << " " << &x << endl;

	addOne(x);

	cout << x << " " << &x << endl;

	double sin(0.0);
	double cos(0.0);

	getSinCos(30.0, sin, cos);

	cout << sin << " " << cos << endl;

	// foo(6);

	// 포인터에 의한 레퍼런스 보내기
	int x1 = 5;
	int* ptr = &x1;

	// foo(ptr); // 에러
	foo1(ptr);

	// int arr[]{ 1, 2, 3, 4 };
	vector<int> arr{ 1 , 2, 3, 4 };

	printElements(arr);
	

	return 0;
}