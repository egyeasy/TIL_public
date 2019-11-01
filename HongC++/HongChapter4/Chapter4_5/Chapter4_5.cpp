#include <iostream>
#include <typeinfo>

int main()
{
	using namespace std;

	int a = 123;
	cout << typeid(a).name() << endl; // int

	float b = 1.0f;
	double d = b; // numeric promotion - �� ū type�� �Ǹ� ������ ����.

	cout << typeid(d).name() << endl;

	int e = 30000;
	char f = e; // char�� ���� �ʴ� ū �� - signed�� 127�����ۿ� �ȵ�.
	
	cout << static_cast<int>(f) << endl; // 48 �̶�� ������ ���� ���

	double dd = 0.123456789;
	float ff = dd;


	//cout << std::setprecision(12) << ff << endl; // ���� �ּ��� ���� ���������� ���е��� ���������� ���Ѵ�.

	cout << 5u - 10 << endl; // unsigned 5��� �� - ��û ū ���ڰ� ��

	// ����� ����ȯ
	int ii = int(4.0); // c++ style. 
	ii = static_cast<int>(4.0); // c style


	

	return 0;
}