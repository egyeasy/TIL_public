#include <iostream>
#include <iomanip>
#include <limits>
#include <cmath>

int main()
{
	using namespace std;

	/*float f;
	double d;
	long double ld;*/

	//cout << sizeof(f) << endl; // 4
	//cout << sizeof(d) << endl; // 8
	//cout << sizeof(ld) << endl; // 8

	/*cout << numeric_limits<float>::max() << endl;
	cout << numeric_limits<double>::max() << endl;
	cout << numeric_limits<long double>::max() << endl;


	cout << numeric_limits<float>::lowest() << endl;
	cout << numeric_limits<double>::lowest() << endl;
	cout << numeric_limits<long double>::lowest() << endl;*/

	float f(3.141592f);
	double d(3.141592);
	long double ld(3.141592);

	cout << 3.14 << endl;
	cout << 31.4e-1 << endl;
	cout << 31.4e1 << endl;

	cout << std::setprecision(16); // 16번째 자리 수까지 출력하도록 조절(iomanip library)
	cout << 1.0 / 3.0 << endl;
	
	f = 123456789.0f;
	cout << f << endl;

	d = 0.1;
	cout << d << endl;
	cout << std::setprecision(17);
	cout << d << endl;

	double d1(1.0);
	double d2(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1);

	cout << setprecision(17);

	cout << d1 << endl;
	cout << d2 << endl;

	
	double zero = 0.0;
	double posinf = 5.0 / zero;
	double neginf = -5.0 / zero;
	double nan = zero / zero;

	cout << posinf << " " << std::isnan(posinf) << endl;
	cout << neginf << " " << std::isnan(neginf) << endl;
	cout << nan << " " << std::isnan(nan) << endl;
	cout << 1.0 << " " << std::isnan(1.0) << endl;


	return 0;
}