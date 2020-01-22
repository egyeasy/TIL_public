#include <iostream>
using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }

	// 단항 연산자
	Cents operator - () const
	{
		return Cents(-m_cents);
	}

	bool operator ! () const
	{
		// !Cents(...)
		return (m_cents == 0) ? true : false;
	}

	friend std::ostream& operator << (std::ostream& out, const Cents& cents)
	{
		out << cents.m_cents;
		return out;
	}
};

int main()
{
	Cents cents1(6);
	Cents cents2(0);

	int a = 3;

	// 단항 연산자
	cout << -a << endl;
	cout << !a << endl;

	// -
	cout << cents1 << endl;
	cout << -cents1 << endl;
	cout << -Cents(-10) << endl;

	// not operator
	cout << endl;
	auto temp = !cents1; // temp는 bool type

	cout << !cents1 << " " << !cents2 << endl;

	return 0;
}
