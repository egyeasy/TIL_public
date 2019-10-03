#include <iostream>

namespace MySpace1
{
	namespace InnerSpace
	{
		int doSomething(int a, int b)
		{
			return a + b;
		}
	}
}

namespace MySpace2
{
	int doSomething(int a, int b)
	{
		return a * b;
	}
}

using namespace std;

int main(void)
{
	using namespace MySpace1::InnerSpace;

	//cout << MySpace1::doSomething(3, 4) << endl;
	//cout << MySpace2::doSomething(3, 4) << endl;

	doSomething(3, 4);


	return 0;
}