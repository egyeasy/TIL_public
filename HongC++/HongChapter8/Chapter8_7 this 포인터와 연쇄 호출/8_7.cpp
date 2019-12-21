#include <iostream>
using namespace std;

class Simple
{
private:
	int m_id;

public:
	Simple(int id)
	{
		this->setId(id); //  일반적으로 this->가 생략돼있는 것
		//(*this).setId(id); // 이것도 가능

		cout << this << endl;
	}

	void setId(int id) { m_id = id; }
	int	 getId() { return m_id; }
};


class Calc
{
private:
	int m_value;

public:
	Calc(int init_value)
		: m_value(init_value)
	{}

	Calc& add(int value) { m_value += value; return *this; }
	Calc& sub(int value) { m_value -= value; return *this; }
	Calc& mult(int value) { m_value *= value; return *this; }

	void print()
	{
		cout << m_value << endl;
	}
};


int main()
{
	Simple s1(1), s2(2);
	s1.setId(2);
	s2.setId(4);
 
	cout << &s1 << " " << &s2 << endl;
	
	// Simple::setId(&s2, 4);

	Calc cal(10);
	cal.add(10).sub(1).mult(2).print();
	//cal.sub(1);
	//cal.mult(2);
	//cal.print();
}