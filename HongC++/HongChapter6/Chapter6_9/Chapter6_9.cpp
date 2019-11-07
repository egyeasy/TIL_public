#include <iostream>

using namespace std;

int main()
{
	double value = 7;
	double* ptr = &value;

	cout << uintptr_t(ptr - 1) << endl;
	cout << uintptr_t(ptr) << endl;
	cout << uintptr_t(ptr + 1) << endl;
	cout << uintptr_t(ptr + 2) << endl;


	cout << endl;

	int array[] = { 9, 7, 5, 3, 1 };

	cout << array[0] << " " << (uintptr_t) & array[0] << endl;
	cout << array[1] << " " << (uintptr_t) & array[1] << endl;
	cout << array[2] << " " << (uintptr_t) & array[2] << endl;
	cout << array[3] << " " << (uintptr_t) & array[3] << endl;
	cout << array[4] << " " << (uintptr_t) & array[4] << endl;

	cout << endl;

	int* ptr2 = array;
	for (int i = 0; i < 5; i++)
	{
		cout << *(ptr2 + i) << " " << (uintptr_t)(ptr2 + i) << endl;
	}

	char name[] = "jack jack";
	const int n_name = sizeof(name) / sizeof(name[0]);

	cout << endl;

	for (int i = 0; i < n_name; i++)
	{
		cout << *(name + i); // jack jack
	}

	cout << endl;

	char* ptr3 = name;

	while (true)
	{
		if (*ptr3 == '\0')
			break;
		cout << *(ptr3++);
	}

	return 0;
}