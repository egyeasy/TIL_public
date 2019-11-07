#include <iostream>

using namespace std;

int main()
{
	// int array[1000000]; // stack

	//int var;
	//var = 7;
	int *ptr = new int;
	*ptr = 7; // dereference

	//int* ptr2 = new int{ 7 }; // new int(7)로도 가능

	cout << ptr << endl;
	cout << *ptr << endl;

	// delete
	delete ptr;
	ptr = nullptr; // 쓸모가 없음을 명시

	cout << "After delete" << endl;
	if (ptr != nullptr)
	{
		cout << ptr << endl;
		cout << *ptr << endl;
	}
		
	int* ptr3 = new (std::nothrow) int{ 7 };

	if (ptr3)
	{
		cout << ptr3 << endl;
		cout << *ptr3 << endl;
	}
	else {
		cout << "Could not allocate memory" << endl;
	}

	int* ptr2 = ptr;

	delete ptr;
	ptr = nullptr;
	// 여기서 ptr2도 nullptr이 되어야 하는데 그렇지 않는다.
	// ptr2 = nullptr; 이라고 해주는 방법이 1.


	// memory leak
	while (true)
	{
		int* ptr = new int;
		cout << ptr << endl;

		delete ptr;
	}
	// 여기서는 block밖이므로 ptr이 사라짐. 그러나 할당되어 있음.




	return 0;
}