#include <iostream>
#include <string>

using namespace std;

class Something
{
public:
	// copy constructor - 복사할 때 실행되는 constructor
	Something(const Something& st_in)
	{
		m_value = st_in.m_value;

		cout << "Copy constructor" << endl;
	}

	Something()
	{
		cout << "contructor" << endl;
	}
	int m_value = 0;

	void setValue(int value) // 여기엔 const를 달 수 없다. 멤버 변수를 변경하고 있기 때문
	{
		m_value = value;
	}

	int getValue() const
	{
		return m_value;
	}

	string s_value = "default";
	const string& getSValue() const {
		cout << "const version";
		return s_value;
	}
	string& getSValue() {
		cout << "non const version";
		return s_value;
	}
};

void print(const Something& st)
{
	cout << &st << endl;

	cout << st.m_value << endl;
}

int main()
{
	class Something something;
	//something.setValue(3);

	cout << something.getValue() << endl;
	
	cout << &something << endl;

	Something something1;
	something1.getSValue() = "5fv"; // 값을 바꿔줄 수 있다.

	const Something something2;
	something2.getSValue(); // 바꿀 수 없다.

	return 0;
}