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

	using std::cout; // namespace�� �ƴϹǷ� ǥ������ �ʿ䰡 ����.
	using std::endl;

	cout << "Hello " << endl;
	
	//using namespace a;
	//using namespace b;

	//cout << my_var << endl;

	cout << a::my_var << endl;
	cout << b::my_var << endl;

	// ���� �ʰ� �ʹٸ�
	{
		using namespace a;
		cout << my_var << endl;
	}
	//cout << my_var << endl; // �̰� ������ ambiguous
	{
		using namespace b;
		cout << my_var << endl;

	}
	



	return 0;
}