#include <iostream>

using namespace std;

int main()
{
	int value;
	int sum = 0;
	int min_value = 100;
	for (int i = 0; i < 7; i++)
	{
		cin >> value;
		if (value % 2)
		{
			if (value < min_value)
				min_value = value;
			sum += value;
		}
	}
	if (sum == 0)
	{
		cout << "-1\n";
	}
	else
	{
		cout << sum << "\n";
		cout << min_value << "\n";
	}

	return 0;
}