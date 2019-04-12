#include <iostream>

using namespace std;

int main()
{
	int value;
	int first = 0;
	int second = 0;
	int third = 0;
	int sum = 0;

	for (int i=0; i < 5; i++)
	{
		cin >> value;
		if (value >= first)
		{
			third = second;
			second = first;
			first = value;
		}
		else if (value >= second)
		{
			third = second;
			second = value;
		}
		else if (value >= third)
		{
			third = value;
		}
		sum += value;
	}
	cout << sum / 5 << "\n";
	cout << third << "\n";
}