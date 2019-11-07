#include <iostream>

using namespace std;

void printArray(int array[]) // int *array�� ����� ����
{
	cout << sizeof(array) << endl; // 4

	*array = 100;
}

struct MyStruct
{
	int array[5] = { 9, 7, 5, 3, 1 };
};

void doSth(MyStruct *ms) // pointer
{
	// de-reference
	cout << sizeof((*ms).array) << endl; // 20 - array ����� ����
}

int main()
{
	int array[5] = { 9, 7, 5, 3, 1 };

	cout << array << endl;

	cout << &(array[0]) << endl; // array 0��° index�� ����� �ּ�


	cout << *array << endl; // 9


	char name[] = "jackjack";
	cout << *name << endl; // j

	int* ptr = array;
	cout << ptr << endl;
	cout << *ptr << endl;

	cout << sizeof(array) << endl; // 20

	cout << sizeof(ptr) << endl; // 4

	printArray(array);

	cout << array[0] << endl;

	cout << *ptr << " " << *(ptr + 1) << endl; // ������ ����

	// struct
	MyStruct ms;
	doSth(&ms);


	return 0;
}