#include <iostream>
#include <array>
#include <algorithm>

using namespace std;

//void printLength(array<int, 5> my_array)
void printLength(const array<int, 5>& my_array)
{
	cout << my_array.size() << endl;
}

int main()
{
	// int array[5] = { 1, 2, 3, 4, 5 }

	array<int, 5> my_arr = { 3, 1, 6, 4, 5 };
	my_arr = { 0, 1, 2, 3, 4 };
	my_arr = { 0, 1, 2 }; // �������� 0���� ä����

	cout << my_arr[0] << endl;
	cout << my_arr.at(0) << endl; // �Ȱ��� �۵�

	cout << my_arr.size() << endl;

	for (auto &element : my_arr)
		cout << element << " ";
	cout << endl;

	std::sort(my_arr.begin(), my_arr.end());

	for (auto& element : my_arr)
		cout << element << " ";
	cout << endl;


	return 0;
}