#include <iostream>

using namespace std;

enum class Colors
{
	BLACK,
	WHITE,
	RED,
	GREEN,
	BLUE
};

void printColorName(Colors color)
{
	/*if (color == Colors::BLACK)
		cout << "Black" << endl;
	else if (color == Colors::WHITE)
		cout << "White" << endl;
	else if (color == Colors::RED)
		cout << "Red" << endl;*/

	/*switch (color)
	{
	case Colors::BLACK:
		cout << "Black";
		break;
	case Colors::WHITE:
		cout << "White";
		break;
	case Colors::RED:
		cout << "Red";
		break;
	}*/

	switch (static_cast<int>(color))
	{
	case 0:
		cout << "Black" << endl;
	case 1:
		cout << "White" << endl;
		break;
	case 2:
		cout << "Red" << endl;
		break;
	}
}

int main()
{
	//printColorName(Colors::BLACK);

	int x;
	cin >> x;

	//switch (x)
	//{
	//case 0:
	//	cout << "Zero";
	//	break;
	//case 1:
	//	cout << "One";
	//	break;
	//case 2:
	//	cout << "Two";
	//	break;
	//}


	// 주의할 점
	switch (x)
	{
		int a;		// 변수 선언을 할 수 있다.
		int b = 5;	// but case문 안에서는 변수 할당을 할 수 없다. 그 이후에는 가능.
	}

	switch (x)
	{
		int a;
	case 0:
		int y;
		break;

	case 1:
		y = 5;		// case 0을 지나지 않으면 선언이 되지 않는 것이 문제.
		cout << y << endl;
	}

	// 헷갈리면 case도 block으로 싸면 됨

	switch (x)
	{
	case 0:
	{
		int y = 5;
		y = y + x;
	}

	default:
		cout << "Undefined input" << x << endl;
	}
	

	cout << endl;
}