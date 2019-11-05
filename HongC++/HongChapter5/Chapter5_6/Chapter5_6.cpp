#include <iostream>

using namespace std;

int main()
{
	int selection; 

	do
	{
		// int selection // do 안에 선언해버리면 while에서 접근 불가.
		cout << "1. add" << endl;
		cout << "2. sub" << endl;
		cout << "2. sub" << endl;
		cout << "2. sub" << endl;
		cin >> selection;
	} while (selection <= 0 || selection >= 5); // ; 필수

	cout << "You selected " << selection << endl;
}