#include <iostream>
#include <cstring>

using namespace std;

int main()
{
	char myString[] = "string";

	for (int i = 0; i < 7; ++i)
	{
		cout << (int)myString[i] << endl; // ASCII ���

		
	}

	cout << sizeof(myString) / sizeof(myString[0]) << endl;


	char string[255];

	//cin >> string;
	cin.getline(string, 255);

	string[0] = 'A';
	//string[4] = '\0';

	cout << string << endl;

	int ix = 0;
	while (true)
	{
		if (string[ix] == '\0') break;

		cout << string[ix] << " " << (int)string[ix] << endl;
		++ix;
	}


	// string copy
	char source[] = "Copy this!";
	char dest[50];
	//strcpy(dest, source); // source�� dest�� ����
	strcpy_s(dest, 50, source);

	cout << source << endl;
	cout << dest << endl;

	// strcat() - �� ���ڿ� �ڿ� �ٸ� ���ڿ� ���̱�
	// strcmp() - �� ���ڿ� �������� ��

	//strcat_s(dest, source);

	cout << source << endl;
	cout << dest << endl;

	cout << strcmp(source, dest) << endl;

	return 0;
}