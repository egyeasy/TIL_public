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

	sizeof a; // 괄호가 없어도 작동

	// comma operator
	int x = 3;
	int y = 10;
	//int z = (++x, ++y);
	// 풀어서 쓰면
	++x;
	++y;
	int z = y;

	cout << x << " " << y << " " << z << endl;

	int a1 = 1, b = 10; // 여기서는 comma 연산자가 아니라 둘을 구분하는 기호
	

	//z = a, b;

	cout << z << endl; // 1이 출력됨 -> 연산자의 우선순위가 대입 연산자(=)보다 낮기 때문. a가 들어가게 된다.
	
	z = (++a1, b); // 뒤의 것을 출력하려면 싸줘야한다.

	// conditional(arithmetric if)
	bool onSale = true;

	//const int price = (onSale == true) ? 10 : 100;

	const int price = getPrice(onSale);
	
	cout << price << endl;

	int x1 = 5;

	cout << ((x1 % 2 == 0) ? "even" : "odd") << endl; // 연산자 우선순위 때문에 괄호로 감싸야 한다.
	

	return 0;
}