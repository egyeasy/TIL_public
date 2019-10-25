#include <iostream>

int main()
{
	using namespace std;

	// logical NOT
	bool x = true;
	bool y = false;

	cout << !x << endl;


	// logical AND
	cout << (x && y) << endl; // �ݵ�� 2���� ����� ��. &�� bitwise operator


	bool hit = true;
	int health = 10;

	if (hit == true && health < 20) // hit == true ��� hit�� �ᵵ ��
	{
		cout << "die" << endl;
	}
	else
		health -= 20;

	// logical OR ||
	x = true;
	y = false;

	cout << (x || y) << endl;

	int x1 = 5;
	int y1 = 7;

	//if (!x1 == y1) // false true(����ȯ)�� ���ϰ� ��
	if (x1 != y1)
	{
		cout << " x does not equal y" << endl;
	}
	else
		cout << " x equals y" << endl;


	int v = 1;

	if (v == 0 || v == 1)
		cout << "v is 0 or 1" << endl;

	// short circuit evaluation
	int x2 = 2;
	int y2 = 2;

	if (x2 == 1 && y2++ == 2)
	{
		// do something
	}

	cout << y2 << endl;


	// De Morgan's Law
	bool x3 = true;
	bool y3 = false;

	!(x && y);
	!x || !y;

	// XOR
	// false false -> false
	// false true true
	// true false true
	// true true false

	// but c++���� �����ڰ� ����. �׷��� �Ʒ��� ���� ��
	if (x3 != y3)
	{
		// do something
	}

	bool v1 = true;
	bool v2 = false;
	bool v3 = false;

	bool r1 = v1 || v2 && v3; // &&�� ||���� �켱������ ����.
	bool r2 = (v1 || v2) && v3;
	bool r3 = v1 || (v2 && v3); // �̷��� ���� �� �ٶ���

	cout << r1 << endl;
	cout << r2 << endl;




	return 0;
}