#include <iostream>
#include <string>
using namespace std;

int add(int x, int y)
{
	return x + y;
}

double add(double x, double y)
{
	return x + y;
}

//int getRandomValue() {}
void getRandom(int& x) {}

//double getRandomValue() {}
void getRandom(double& x) {}

typedef int my_int;

// void print(int x) {}

// void print(my_int x) {}


//void print(char* value) {}
//void print(int value) {}

void print(unsigned int value) { cout << value << endl; }
void print(float value) {}


int main()
{
	add(1, 2);
	add(3.0, 4.0); // �����Ϸ��� �˾Ƽ� �ش��ϴ� �Լ��� �����ؼ� �������Ѵ�.

	//print(0);
	//print('a'); // int�� �ν�. "a"��� ���ڿ��̶� ��ġ�Ǵ� �� ���ٰ� ����

	//print('a');
	//print(0);
	//print(3.14159); // ��ȣ�ϴ�. 

	print((unsigned int)'a');
	print(0u);
	print(3.14159f);
	
	return 0;
}