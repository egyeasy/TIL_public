#include <iostream>

using namespace std;

int main()
{
	int selection; 

	do
	{
		// int selection // do �ȿ� �����ع����� while���� ���� �Ұ�.
		cout << "1. add" << endl;
		cout << "2. sub" << endl;
		cout << "2. sub" << endl;
		cout << "2. sub" << endl;
		cin >> selection;
	} while (selection <= 0 || selection >= 5); // ; �ʼ�

	cout << "You selected " << selection << endl;
}