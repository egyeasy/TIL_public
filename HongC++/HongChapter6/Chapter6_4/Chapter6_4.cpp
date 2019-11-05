#include <iostream>

using namespace std;

void printArray(int array[], int length)
{
	for (int index = 0; index < length; index++)
		cout << array[index] << " ";
	cout << endl;
}

int main()
{

	const int length = 5;

	int array[length] = { 3, 5, 2, 1, 4 };

	printArray(array, length);


	for (int start = 0; start < length; start++)
	{
		int min_idx = start;
		for (int i = start; i < length; i++)
		{
			if (array[i] < array[min_idx])
			{
				min_idx = i;
			}
		}
		int copy = array[start];
		array[start] = array[min_idx];
		array[min_idx] = copy;
	}

	printArray(array, length);


}