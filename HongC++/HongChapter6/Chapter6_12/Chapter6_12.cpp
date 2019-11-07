#include <iostream>

using namespace std;

int main()
{
	int length;

	//cin >> length;
	length = 6;

	//int array[length];
	int* array = new int[length] {11, 22, 33, 44, 55, 66};

	array[0] = 1;
	array[1] = 2;

	for (int i = 0; i < length; ++i)
	{
		cout << (uintptr_t) & array[i] << endl;
		cout << array[i] << endl;
	}

	delete[] array; // 긴 사이즈의 메모리를 삭제


	int fixedArray[] = { 1, 2, 3, 4, 5 };

	int* array2 = new int[5]{ 1, 2, 3, 4, 5 };

	for (int i = 0; i < 5; i++)
	{
		cout << array2[i] << endl;
	}

	delete[] array2;

	return 0;

}