#include <iostream>
#include <string>

using namespace std;

class Something
{
public:
	// copy constructor - ������ �� ����Ǵ� constructor
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

	void setValue(int value) // ���⿣ const�� �� �� ����. ��� ������ �����ϰ� �ֱ� ����
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
	something1.getSValue() = "5fv"; // ���� �ٲ��� �� �ִ�.

	const Something something2;
	something2.getSValue(); // �ٲ� �� ����.

	return 0;
}