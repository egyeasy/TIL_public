#include <iostream>
using namespace std;

class A; // forward declaration

class B
{
private:
	int m_value = 2;
public:
	void doSomething(A& a);
};

class A
{
private:
	int m_value = 1;

	// friend class B;
	friend void B::doSomething(A& a);
};

void B::doSomething(A& a)
{
	cout << a.m_value << endl;
}

//void doSomething(A& a, B& b)
//{
//	cout << a.m_value << " " << b.m_value << endl; // 이렇게는 못 쓴다
//}


int main()
{
	A a;
	B b;
	b.doSomething(a);

	return 0;
}