#include <iostream>
#include <vector>

using namespace std;

int main()
{
	// std::array<int, 5> array; // ����� �ݵ�� �������
	std::vector<int> array; // �ʼ��� �ƴ�

	std::vector<int> array2 = { 1, 2, 3, 4, 5 };

	cout << array2.size() << endl; // 5

	std::vector<int> array3 = { 1, 2, 3 };

	cout << array3.size() << endl; // 3

	std::vector<int> array4 = { 1, 2, 3, };

	cout << array4.size() << endl; // 3


	vector<int> arr = { 1,2, 3, 4,5 };

	for (auto& itr : arr)
		cout << itr << " ";
	cout << endl;

	cout << arr[1] << endl;
	cout << arr.at(1) << endl;

	cout << arr.size() << endl;

	arr.resize(10);

	arr.push_back(333);

	

	return 0;
}