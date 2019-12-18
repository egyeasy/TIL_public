#include "Calc.h"


Calc& Calc::add(int value) {m_value += value; return *this; }
Calc& Calc::sub(int value) { m_value -= value; return *this; }
Calc& Calc::mult(int value) { m_value *= value; return *this; }

void Calc::print()
{
	using namespace std;
	cout << m_value << endl;
}