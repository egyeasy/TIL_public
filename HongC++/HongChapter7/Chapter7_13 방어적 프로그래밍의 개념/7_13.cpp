#include <iostream>
#include <string>

using namespace std;

int main()
{
	// semantic errors

	int x;
	cin >> x;

	if (x >= 5)
		cout << "x is greater than 5" << endl;

	// violated assumption

	string hello = "Hello, my name is jack jack";

	cout << "Input from 0 to " << hello.size() - 1 << endl;

	while (true)
	{
		int ix;
		cin >> ix;

		if (ix >= 0 && ix <= hello.size() - 1)
			cout << hello[ix] << endl;
		else
			cout << "Please try again" << endl;

	}

	return 0;
}