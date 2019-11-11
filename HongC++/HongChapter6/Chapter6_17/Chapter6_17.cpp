#include <iostream>
#include <limits>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	/*int fibonacci[] = { 0, 1, 1, 2, 3, 5, 8, 13,
							21, 34, 55, 89 };*/
	vector<int> fibonacci = { 0, 1, 1, 2, 3, 5, 8, 13,
							21, 34, 55, 89 };

	for (int number : fibonacci)
		cout << number << " ";
	cout << endl;

	// change
	for (int number : fibonacci)
		number = 10;


	for (int number : fibonacci)
		cout << number << " ";
	cout << endl;


	// change
	for (auto& number : fibonacci)
		number = 10;


	for (const auto number : fibonacci)
		cout << number << " ";
	cout << endl;

	cout << "¾ßÈ£" << endl;

	int max_number = std::numeric_limits<int>::lowest();

	for (const auto& n : fibonacci)
		max_number = std::max(max_number, n);

	cout << max_number << endl;
	

	
}