#include <iostream>
using namespace std;

class Digit
{
private:
	int m_digit;

public:
	Digit(int cents = 0) { m_digit = cents; }
	int getCents() const { return m_digit; }
	int& getCents() { return m_digit; }

	// prefix(전위형)
	Digit& operator ++ ()
	{
		++m_digit;
		
		return *this; // 자기 자신(의 레퍼런스를 deref한 것) 리턴
	}

	// postfix(후위형)
	Digit operator ++ (int) // Dummy를 넣어서 postfix를 정의한다
	{
		Digit temp(m_digit);

		++(*this); // 또는 ++m_digit. 위의 오버로딩 함수를 사용.
		return temp;
	}

	friend std::ostream& operator << (std::ostream& out, const Digit& d)
	{
		out << d.m_digit;
		return out;
	}
};

int main()
{
	Digit d(5);

	cout << ++d << endl;
	cout << d << endl;

	cout << d++ << endl;
	cout << d << endl;

	return 0;

}