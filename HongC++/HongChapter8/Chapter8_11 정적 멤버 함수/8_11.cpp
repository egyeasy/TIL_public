#include <iostream>
using namespace std;

class Something
{
public:
	class _init
	{
	public:
		_init()
		{
			s_value = 9876;
		}
	};

public:
	static int s_value;
	int m_value;

	static _init s_initializer;

public:

	static int getValue()
	{
		//return m_value;
		//return this->s_value;
		return s_value;
	}

	int temp()
	{
		return this->s_value;
	}
};

int Something::s_value = 1024;
Something::_init Something::s_initializer;

int main()
{
	//cout << Something::s_value << endl; // 인스턴스가 없어서 쓸 수 없다.

	cout << Something::getValue << endl;

	Something s1, s2;
	cout << s1.getValue() << endl;
	//cout << s1.s_value << endl;

	//int (Something:: * fptr1)() = s1.temp;
	int (Something::*fptr1) () = &Something::temp;

	cout << (s2.*fptr1)() << endl;

	//int (Something::*fptr2)() = &Something::getValue;
	int (*fptr2)() = &Something::getValue;
	cout << fptr2() << endl;

	return 0;
}