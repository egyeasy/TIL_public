#include <iostream>
#include <string>

using namespace std;


//void print(int x = 10, int y = 20, int z = 30); // in header

//void print(int x = 0)
//{
//	cout << x << endl;
//}

//void print(int x = 10, int y = 20, int z = 30)
//void print(int x, int y, int z)
//{
//	cout << x << endl;
//}

//void print(std::string str) {}
//void print(char ch = ' ') {}

void print(int x) {}
void print(int x, int y = 20) {}

int main()
{
	//print(10);
	
	/*print();
	print(100);
	print(100, 200);*/

	//print(); // char Ÿ���� �Ķ���Ͱ� ���� �Լ��� �νĵ� ��

	print(10); // ambiguous


	return 0;
}