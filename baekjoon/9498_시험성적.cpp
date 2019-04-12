#include "iostream"
using namespace std;

int main()
{
	int point;
	cin >> point;
	if (point >= 90)
		cout << "A\n";
	else if (point >= 80)
		cout << "B\n";
	else if (point >= 70)
		cout << "C\n";
	else if (point >= 60)
		cout << "D\n";
	else
		cout << "F\n";
	return 0;
}