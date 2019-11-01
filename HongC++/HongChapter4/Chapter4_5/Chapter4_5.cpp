#include <iostream>
#include <typeinfo>

int main()
{
	using namespace std;

	int a = 123;
	cout << typeid(a).name() << endl; // int

	float b = 1.0f;
	double d = b; // numeric promotion - 더 큰 type이 되면 문제가 없다.

	cout << typeid(d).name() << endl;

	int e = 30000;
	char f = e; // char에 들어가지 않는 큰 수 - signed면 127까지밖에 안됨.
	
	cout << static_cast<int>(f) << endl; // 48 이라는 엉뚱한 숫자 출력

	double dd = 0.123456789;
	float ff = dd;


	//cout << std::setprecision(12) << ff << endl; // 나름 최선을 다해 저장하지만 정밀도를 보장하지는 못한다.

	cout << 5u - 10 << endl; // unsigned 5라는 뜻 - 엄청 큰 숫자가 뜸

	// 명시적 형변환
	int ii = int(4.0); // c++ style. 
	ii = static_cast<int>(4.0); // c style


	

	return 0;
}