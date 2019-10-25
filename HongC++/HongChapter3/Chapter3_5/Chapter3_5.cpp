#include <iostream>
#include <cmath>

int main()
{
	using namespace std;

	int x, y;
	//cin >> x >> y;
	//cout << "Your input values are : " << x << " " << y << endl;

	/*if (x == y)
		cout << "equal" << endl;
	if (x != y)
		cout << "Not equal" << endl;
	if (x > y)
		cout << "x is greater than y" << endl;
	*/

	double d1(100 - 99.99);  // 0.001
	double d2(10 - 9.99); // 0.001

	if (d1 == d2)
		cout << "equal" << endl;
	else
	{
		cout << "Not equal" << endl;

		if (d1 > d2) cout << "d1 > d2" << endl;
		else //if(d1 < d2)
			cout << "d1 < d2" << endl;
	}

	cout << std::abs(d1 - d2) << endl;

	const double epsilon = 1e-10;

	if (std::abs(d1 - d2) < epsilon)
		cout << "Approximately equal" << endl;
	else
		cout << "Not equal" << endl;
	


	return 0;
}