#include <iostream>
// #define PRICE_PER_ITEM 30
#include "MY_CONSTANTS.h"

using namespace std;

void printNumber(const int my_number)
{
	// my_number = 456; // ������� �˾ƺ��� ����� ����Ƿ� �����ϴ� ��
	int n = my_number; // �����ϰ��� �Ѵٸ� �����ؼ� ����.

	cout << my_number << endl;
}

int main()
{
	using namespace std;

	const double gravity{ 9.8 };

	// gravity = 1.2; // ���� �ٲ� �� ����.

	printNumber(123);

	const int my_const(123); // ������ Ÿ�� ���
	constexpr int my_const2(123);

	int number;
	cin >> number;

	const int special_number(number); // ��Ÿ�� ��� - ������ �Ǿ�� ������
	// constexpr int special_number(number); // �̷��� �� �� ����

	const int price_per_item = 30;

	int num_item = 123;
	int price = num_item * price_per_item;

	double radius;
	cin >> radius;

	double circumference = 2.0 * radius * constants::pi;


	return 0;
}