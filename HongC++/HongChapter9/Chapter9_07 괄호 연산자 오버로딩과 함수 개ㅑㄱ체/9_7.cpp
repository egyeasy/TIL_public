#include <iostream>
using namespace std;

class Accumulator
{
private:
	int m_counter = 0;

public:
	int operator()(int i) { return (m_counter += i); }
};

int main()
{
	Accumulator acc;
	cout << acc(10) << endl; // 현재 있는 값에 10을 더함
	cout << acc(20) << endl; // 10 + 20

	return 0;
}