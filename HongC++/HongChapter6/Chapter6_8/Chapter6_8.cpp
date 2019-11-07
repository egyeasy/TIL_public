#include <iostream>

using namespace std;

void printArray(int array[]) // int *array와 결과가 같다
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
	cout << sizeof((*ms).array) << endl; // 20 - array 사이즈가 나옴
}

int main()
{
	int array[5] = { 9, 7, 5, 3, 1 };

	cout << array << endl;

	cout << &(array[0]) << endl; // array 0번째 index의 요소의 주소


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

	cout << *ptr << " " << *(ptr + 1) << endl; // 포인터 연산

	// struct
	MyStruct ms;
	doSth(&ms);


	return 0;
}