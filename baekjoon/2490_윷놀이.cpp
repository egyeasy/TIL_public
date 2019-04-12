#include <iostream>

using namespace std;

int main()
{
	int a, b, c, d;

	for (int i = 0; i < 3; i++) {
		cin >> a >> b >> c >> d;
		int value = a + b + c + d;
		if (value == 4)
			cout << "E\n";
		else if (value == 3)
			cout << "A\n";
		else if (value == 2)
			cout << "B\n";
		else if (value == 1)
			cout << "C\n";
		else
			cout << "D\n";
	}

	return 0;
}