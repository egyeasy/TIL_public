#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

void addOne(int& y)
{
	cout << y << " " << &y << endl;
	y = y + 1;
}

void getSinCos(const double degree, double& sin_out, double& cos_out) // degree�� ������ �� ��ġ��, double�� �Լ��� ȣ���� ���� ������ ��ĥ �� �ְ� ��
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

void foo1(int*& ptr) // int* ��� pint�� �ᵵ ��
{
	cout << ptr << " " << &ptr << endl;
}

void printElements(int (&arr)[4]) // ���ȣ �ȿ� ������ �ݵ�� ���� ��
{

}

void printElements(vector<int>& arr) // const�� ���� ��
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

	// �����Ϳ� ���� ���۷��� ������
	int x1 = 5;
	int* ptr = &x1;

	// foo(ptr); // ����
	foo1(ptr);

	// int arr[]{ 1, 2, 3, 4 };
	vector<int> arr{ 1 , 2, 3, 4 };

	printElements(arr);
	

	return 0;
}