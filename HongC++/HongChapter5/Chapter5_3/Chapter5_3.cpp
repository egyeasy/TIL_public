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


	// ������ ��
	switch (x)
	{
		int a;		// ���� ������ �� �� �ִ�.
		int b = 5;	// but case�� �ȿ����� ���� �Ҵ��� �� �� ����. �� ���Ŀ��� ����.
	}

	switch (x)
	{
		int a;
	case 0:
		int y;
		break;

	case 1:
		y = 5;		// case 0�� ������ ������ ������ ���� �ʴ� ���� ����.
		cout << y << endl;
	}

	// �򰥸��� case�� block���� �θ� ��

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