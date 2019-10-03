#include <iostream>
// #define PRICE_PER_ITEM 30
#include "MY_CONSTANTS.h"

using namespace std;

void printNumber(const int my_number)
{
	// my_number = 456; // 입출력을 알아보기 힘들게 만드므로 방지하는 편
	int n = my_number; // 변경하고자 한다면 복사해서 쓴다.

	cout << my_number << endl;
}

int main()
{
	using namespace std;

	const double gravity{ 9.8 };

	// gravity = 1.2; // 값을 바꿀 수 없다.

	printNumber(123);

	const int my_const(123); // 컴파일 타임 상수
	constexpr int my_const2(123);

	int number;
	cin >> number;

	const int special_number(number); // 런타임 상수 - 실행이 되어야 정해짐
	// constexpr int special_number(number); // 이렇게 쓸 수 없다

	const int price_per_item = 30;

	int num_item = 123;
	int price = num_item * price_per_item;

	double radius;
	cin >> radius;

	double circumference = 2.0 * radius * constants::pi;


	return 0;
}