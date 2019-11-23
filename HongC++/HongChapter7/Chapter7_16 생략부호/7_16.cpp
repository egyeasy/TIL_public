#include <iostream>
#include <cstdarg> // for ellipsis
using namespace std;

double findAverage(int count, ...)
{
	double sum = 0;

	va_list list; // 문자열로 받는다.

	va_start(list, count); // 두 번째 인자로 들어오는 arg의 개수를 알려준다

	for (int arg = 0; arg < count; ++arg)
		sum += va_arg(list, int);

	va_end(list);

	return sum / count;
}

int main()
{
	cout << findAverage(1, 1, 2, 3, "Hello", 'c') << endl; // 1개만 되고 나머지는 무시됨
	cout << findAverage(3, 1, 2, 3) << endl;
	cout << findAverage(5, 1, 2, 3, 4, 5) << endl;
	cout << findAverage(10, 1, 2, 3, 4, 5) << endl; // 이상한 숫자가 도출
}