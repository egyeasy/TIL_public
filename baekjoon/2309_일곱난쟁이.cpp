#include <iostream>

using namespace std;

int main()
{
	int heights[9], min_value, min_idx;
	int visited[9] = { 0 };
	int sum = 0;
	bool found = false;
	for (int i = 0; i < 9; i++)
	{
		cin >> heights[i];
		sum += heights[i];
	}
	for (int i = 0; i < 8; i++)
	{
		for (int j = i + 1; j < 9; j++)
		{
			if ((sum - heights[i] - heights[j]) == 100)
			{
				visited[i] = 1;
				visited[j] = 1;
				found = true;
				break;
			}
		}
		if (found)
		{
			break;
		}
	}
	for (int i = 0; i < 7; i++)
	{
		min_value = 10000;
		min_idx = 0;
		for (int idx = 0; idx < 9; idx++)
		{
			if (visited[idx] == 0 && heights[idx] < min_value)
			{
				min_value = heights[idx];
				min_idx = idx;
			}
		}
		visited[min_idx] = 1;
		cout << min_value << "\n";
	}
}