#include <iostream>

using namespace std;

enum Type
{
	INT,
	FLOAT,
	CHAR
};

int main()
{
	int		i = 5;
	float	f = 3.0;
	char	c = 'a';

	void* ptr = nullptr;

	ptr = &i;
	ptr = &f;
	//ptr = &c;

	// cout << ptr + 1 << endl; // �����Ʈ ���ؾ� �ϴ��� �� �� ����

	//cout << &f << " " << ptr << endl;

	// cout << *ptr << endl;

	cout << *static_cast<float*>(ptr) << endl;

	Type type = FLOAT;

	if (type == FLOAT)
		cout << *static_cast<float*>(ptr) << endl;
	else if(type == INT)
		cout << *static_cast<int*>(ptr) << endl;



	return 0;
}