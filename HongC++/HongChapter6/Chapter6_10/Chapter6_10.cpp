#include <iostream>

using namespace std;

const char* getName()
{
	return "JackJack";
}

int main()
{
	//char name[] = "Jack Jack";
	//char* name = "Jack Jack"; // �̰� ���尡 �� ��. Jack Jack�� ���ͷ���. ��� �������� ��õǾ����� ����
	const char* name = "Jack Jack"; // �̰� ����
	const char* name2 = "Jack Jack";

	cout << (uintptr_t)name << endl;
	cout << (uintptr_t)name2 << endl;

	cout << endl;

	int int_arr[5] = { 1, 2, 3, 4, 5 };
	char char_arr[] = "Hello, World!";
	const char* name3 = "Jack Jack";

	cout << int_arr << endl;
	cout << char_arr << endl;
	cout << name3 << endl;

	char c = 'Q';
	cout << &c << endl;

	return 0;
}