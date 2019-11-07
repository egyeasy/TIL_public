#include <iostream>

using namespace std;

int main()
{
	// int array[1000000]; // stack

	//int var;
	//var = 7;
	int *ptr = new int;
	*ptr = 7; // dereference

	//int* ptr2 = new int{ 7 }; // new int(7)�ε� ����

	cout << ptr << endl;
	cout << *ptr << endl;

	// delete
	delete ptr;
	ptr = nullptr; // ���� ������ ���

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
	// ���⼭ ptr2�� nullptr�� �Ǿ�� �ϴµ� �׷��� �ʴ´�.
	// ptr2 = nullptr; �̶�� ���ִ� ����� 1.


	// memory leak
	while (true)
	{
		int* ptr = new int;
		cout << ptr << endl;

		delete ptr;
	}
	// ���⼭�� block���̹Ƿ� ptr�� �����. �׷��� �Ҵ�Ǿ� ����.




	return 0;
}