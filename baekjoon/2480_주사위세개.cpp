#include <iostream>

using namespace std;

int main()
{
	int a, b, c;
	int max_value;
	cin >> a >> b >> c;

	if ((a == b) && (b == c))
		cout << 10000 + a * 1000 << "\n";
	else if ((a == b) || (a == c))
		cout << 1000 + a * 100 << "\n";
	else if (b == c)
		cout << 1000 + b * 100 << "\n";
	else
		{
			if ((a >= b) && (b >= c))
				max_value = a;
			else if ((a >= c) && (c >= b))
				max_value = a;
			else if ((b >= a) && (a >= c))
				max_value = b;
			else if ((b >= c) && (c >= a))
				max_value = b;
			else if ((c >= a) && (a >= b))
				max_value = c;
			else
				max_value = c;
			cout << max_value * 100 << "\n";
		}
	}