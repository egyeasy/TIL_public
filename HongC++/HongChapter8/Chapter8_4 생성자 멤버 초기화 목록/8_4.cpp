#include <iostream>
using namespace std;

class B
{
public:
	int m_b;

public:
	B(const int& m_b_in)
		: m_b(m_b_in)
	{}
};

class Something
{
private:
	int		m_i = 100;
	float	m_d = 100.0;
	char	m_c = 'F';
	int		m_arr[5] = { 100, 200, 300, 400, 500 }; // c++ 11 부터 가능
	B		m_b{ 1024 };

public:
	Something()
		: m_i(1), m_d(3.14), m_c('a'), m_arr{ 1, 2, 3, 4 ,5 }, m_b(m_i - 1) // 중괄호를 쓰면 형변환이 안된다(더 엄격하다)
	{
		/*m_i = 1;
		m_d = 3.14;
		m_c = 'a';*/
	}

	void print()
	{
		cout << m_i << " " << m_d << " " << m_c << endl;
	}

};