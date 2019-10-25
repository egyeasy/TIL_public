#include <iostream>

int main()
{
	using namespace std;

	// logical NOT
	bool x = true;
	bool y = false;

	cout << !x << endl;


	// logical AND
	cout << (x && y) << endl; // 반드시 2개를 써줘야 함. &는 bitwise operator


	bool hit = true;
	int health = 10;

	if (hit == true && health < 20) // hit == true 대신 hit만 써도 됨
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

	//if (!x1 == y1) // false true(형변환)를 비교하게 됨
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

	// but c++에는 연산자가 없다. 그래서 아래와 같이 씀
	if (x3 != y3)
	{
		// do something
	}

	bool v1 = true;
	bool v2 = false;
	bool v3 = false;

	bool r1 = v1 || v2 && v3; // &&가 ||보다 우선순위가 높다.
	bool r2 = (v1 || v2) && v3;
	bool r3 = v1 || (v2 && v3); // 이렇게 쓰는 게 바람직

	cout << r1 << endl;
	cout << r2 << endl;




	return 0;
}