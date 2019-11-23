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
	add(3.0, 4.0); // 컴파일러가 알아서 해당하는 함수를 적용해서 컴파일한다.

	//print(0);
	//print('a'); // int로 인식. "a"라면 문자열이라 매치되는 게 없다고 나옴

	//print('a');
	//print(0);
	//print(3.14159); // 모호하다. 

	print((unsigned int)'a');
	print(0u);
	print(3.14159f);
	
	return 0;
}