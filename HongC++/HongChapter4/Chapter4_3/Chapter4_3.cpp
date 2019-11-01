#include <iostream>

namespace a
{
	int my_var(10);
}

namespace b
{
	int my_var(20);
}

int main()
{
	//using namespace std;

	using std::cout; // namespace가 아니므로 표시해줄 필요가 없다.
	using std::endl;

	cout << "Hello " << endl;
	
	//using namespace a;
	//using namespace b;

	//cout << my_var << endl;

	cout << a::my_var << endl;
	cout << b::my_var << endl;

	// 쓰지 않고 싶다면
	{
		using namespace a;
		cout << my_var << endl;
	}
	//cout << my_var << endl; // 이건 여전히 ambiguous
	{
		using namespace b;
		cout << my_var << endl;

	}
	



	return 0;
}