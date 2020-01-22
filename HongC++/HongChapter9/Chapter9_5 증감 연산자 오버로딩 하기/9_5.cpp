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

	// prefix(������)
	Digit& operator ++ ()
	{
		++m_digit;
		
		return *this; // �ڱ� �ڽ�(�� ���۷����� deref�� ��) ����
	}

	// postfix(������)
	Digit operator ++ (int) // Dummy�� �־ postfix�� �����Ѵ�
	{
		Digit temp(m_digit);

		++(*this); // �Ǵ� ++m_digit. ���� �����ε� �Լ��� ���.
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