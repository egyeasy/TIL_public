#include <iostream>
#include <bitset>

int main()
{
	using namespace std;

	unsigned int a = 3;

	// 어떻게 내부적으로 저장되는지 보고 싶다면
	cout << std::bitset<4>(a) << endl; // 0011

	unsigned int b = a << 1; // left shift

	cout << std::bitset<4>(b) << endl; // 0110
	
	b <<= 2; // * 2**2

	cout << b << endl;

	cout << (a << 1) << endl; // cout 내에서 shift 하려면 괄호 필요

	unsigned int c = 1024;

	cout << std::bitset<16>(c) << endl;

	// right shift
	cout << std::bitset<16>(c >> 1) << " " << (c >> 1) << endl; // 512
	cout << std::bitset<16>(c >> 2) << " " << (c >> 2) << endl; // 256
	cout << std::bitset<16>(c >> 3) << " " << (c >> 3) << endl; // 128
	cout << std::bitset<16>(c >> 4) << " " << (c >> 4) << endl; // 64

	// not
	cout << std::bitset<16>(~c) << " " << (~c) << endl; // 1 0이 뒤집혀서 나옴

	// 이진수 int
	unsigned int d = 0b1100;
	unsigned int e = 0b0110;

	// 이항 연산자
	cout << std::bitset<4>(a & b) << endl; // bitwise AND
	cout << std::bitset<4>(a | b) << endl; // bitwise OR
	cout << std::bitset<4>(a ^ b) << endl; // bitwise XOR

	a &= b; // 줄여쓸 수 있다.
	
	unsigned int f = 0b0110;
	cout << std::bitset<4>(f >> 2) << " " << (f >> 2) << endl;

	// Quiz
	// 0110 >> 2 -> decimal로 어떻게 될까 : 1
	// 5 | 12 : 0101 1100 : 1101
	// 5 & 12 : 0100
	// 5 ^ 12 : 1001

}