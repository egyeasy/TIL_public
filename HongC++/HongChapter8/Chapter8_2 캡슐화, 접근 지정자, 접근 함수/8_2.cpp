#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Date
{
	int m_month;
	int m_day;
	int m_year;

public:
	void setDate(const int& month_input, const int& day_input, const int& year_input)
	{
		m_month = month_input;
		m_day = day_input;
		m_year = year_input;
	}

	void setMonth(const int& month_input)
	{
		m_month = month_input;
	}

	// setDay, setYear ...

	const int& getDay() // get에서 day 를 바꾸지 못하도록
	{
		return m_day;
	}

	void copyFrom(const Date& original)
	{
		m_month = original.m_month;
		m_day = original.m_day;
		m_year = original.m_year;
	}
};

int main()
{
	Date today; // { 9, 4, 2025 };
	//today.m_month = 8;
	//today.m_day = 4;
	//today.m_year = 2025;

	today.setDate(8, 4, 2025);
	today.setMonth(10);

	cout << today.getDay() << endl;

	Date copy;
	//copy.setDate(today.getMonth(), today.getDay(), today.getYear());
	// 이게 귀찮을 때
	copy.copyFrom(today);

	//copy.m_day = 123;
	//today.m_month = 45;

	return 0;
}