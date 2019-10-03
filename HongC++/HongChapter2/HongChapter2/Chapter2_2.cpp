#include <iostream>

int main(void)
{
	using namespace std;

	short	j = 1; // 2 bytes = 2 * 8 bits = 16 bits
	//int		i = 1;
	long	l = 1;
	long long ll = 1;

	//cout << sizeof(short) << endl;
	//cout << sizeof(int) << endl;
	//cout << sizeof(long) << endl;
	//cout << sizeof(long long) << endl;

	//// 표현할 수 있는 가장 큰 숫자
	//cout << std::pow(2, sizeof(short) * 8 - 1) - 1 << endl; // 계산으로 구하기
	//cout << std::numeric_limits<short>::max() << endl; // 존재하는 함수로 구하기
	//cout << std::numeric_limits<short>::min() << endl;
	//cout << std::numeric_limits<short>::lowest() << endl;


	//short s = 32767;
	//s = s + 1; // 32768

	//cout << s << endl;

	//s = std::numeric_limits<short>::min();

	//cout << "min() " << s << endl;

	//s = s - 1;

	//cout << " " << s << endl;

	unsigned int i = -1;

	cout << i << endl;

	int k = 22 / 4;

	cout << k << endl;


	return 0;
}