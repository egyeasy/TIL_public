#include <iostream>

int getPrice(bool onSale)
{
	if (onSale)
		return 10;
	return 100;
}

int main(void)
{
	using namespace std;

	float a;

	sizeof(float);
	sizeof(a);

	sizeof a; // ��ȣ�� ��� �۵�

	// comma operator
	int x = 3;
	int y = 10;
	//int z = (++x, ++y);
	// Ǯ� ����
	++x;
	++y;
	int z = y;

	cout << x << " " << y << " " << z << endl;

	int a1 = 1, b = 10; // ���⼭�� comma �����ڰ� �ƴ϶� ���� �����ϴ� ��ȣ
	

	//z = a, b;

	cout << z << endl; // 1�� ��µ� -> �������� �켱������ ���� ������(=)���� ���� ����. a�� ���� �ȴ�.
	
	z = (++a1, b); // ���� ���� ����Ϸ��� ������Ѵ�.

	// conditional(arithmetric if)
	bool onSale = true;

	//const int price = (onSale == true) ? 10 : 100;

	const int price = getPrice(onSale);
	
	cout << price << endl;

	int x1 = 5;

	cout << ((x1 % 2 == 0) ? "even" : "odd") << endl; // ������ �켱���� ������ ��ȣ�� ���ξ� �Ѵ�.
	

	return 0;
}