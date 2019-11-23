#include <iostream>
#include <vector>

using namespace std;

void printStack(const std::vector<int>& stack)
{
	for (auto& e : stack)
		cout << e << " ";
	cout << endl;
}

int main()
{
	// int *v_ptr = new int[3]{1, 2, 3};

	std::vector<int> v{ 1, 2, 3 };

	// size, capacity(용량)
	
	for (auto& e : v)
		cout << e << " ";
	cout << endl;


	cout << v.size() << " " << v.capacity() << endl; // 3
	
	v.resize(10);

	cout << v.size() << " " << v.capacity() << endl;

	for (auto& e : v)
		cout << e << " ";
	cout << endl;

	v.resize(2);

	for (auto& e : v)
		cout << e << " ";
	cout << endl;

	cout << v.size() << " " << v.capacity() << endl; // 2 10

	int* ptr = v.data();

	cout << ptr[2] << endl;


	v.reserve(1024);

	for (auto& e : v)
		cout << e << " ";
	cout << endl;


	// 스택
	std::vector<int> stack;

	stack.push_back(3);
	printStack(stack);

	stack.push_back(5);
	printStack(stack);
	
	stack.push_back(7);
	printStack(stack);
	
	stack.pop_back();
	printStack(stack);
	
	stack.pop_back();
	printStack(stack);



	return 0;
}