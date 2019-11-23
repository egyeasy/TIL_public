#include <iostream>

using namespace std;

class Fraction
{
private:
	int m_numerator = 0;
	int m_denominator = 1;

public:
	Fraction()
	{
		m_numerator = 1;
		m_denominator = 1;
	}
	Fraction(const int& num_in, const int& denom_in)
	{
		m_numerator = num_in;
		m_denominator = denom_in;

		cout << "Fraction() Constructor" << endl;
	}
	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};


class Second
{
public:
	Second()
	{
		cout << "class Second constructor()" << endl;
	}
};

class First
{
	Second sec;
public:
	First()
	{
		cout << "class First constructor()" << endl;
	}
};

int main()
{
	//Fraction frac; // �����ڰ� �ϳ��� ���� �� �ݵ�� ��ȣ�� ������
	Fraction one_thirds(1, 3);
	one_thirds.print();

	Fraction one;
	one.print();
	//frac.print();

	First fir;

	return 0;
}