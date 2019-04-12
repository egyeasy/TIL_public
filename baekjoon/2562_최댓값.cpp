#include <iostream>

using namespace std;

int main()
{	
	int value, max_idx;
	int max_value = 0;
	for (int i = 0; i < 9; i++)
	{
		cin >> value;
		if (value > max_value)
		{
			max_value = value;
			max_idx = i + 1;
		}
	}
	cout << max_value << "\n";
	cout << max_idx << "\n";
}