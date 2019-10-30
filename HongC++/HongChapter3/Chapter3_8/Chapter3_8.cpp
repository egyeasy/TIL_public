#include <iostream>
#include <bitset>

int main()
{
	using namespace std;

	unsigned int a = 3;

	// ��� ���������� ����Ǵ��� ���� �ʹٸ�
	cout << std::bitset<4>(a) << endl; // 0011

	unsigned int b = a << 1; // left shift

	cout << std::bitset<4>(b) << endl; // 0110
	
	b <<= 2; // * 2**2

	cout << b << endl;

	cout << (a << 1) << endl; // cout ������ shift �Ϸ��� ��ȣ �ʿ�

	unsigned int c = 1024;

	cout << std::bitset<16>(c) << endl;

	// right shift
	cout << std::bitset<16>(c >> 1) << " " << (c >> 1) << endl; // 512
	cout << std::bitset<16>(c >> 2) << " " << (c >> 2) << endl; // 256
	cout << std::bitset<16>(c >> 3) << " " << (c >> 3) << endl; // 128
	cout << std::bitset<16>(c >> 4) << " " << (c >> 4) << endl; // 64

	// not
	cout << std::bitset<16>(~c) << " " << (~c) << endl; // 1 0�� �������� ����

	// ������ int
	unsigned int d = 0b1100;
	unsigned int e = 0b0110;

	// ���� ������
	cout << std::bitset<4>(a & b) << endl; // bitwise AND
	cout << std::bitset<4>(a | b) << endl; // bitwise OR
	cout << std::bitset<4>(a ^ b) << endl; // bitwise XOR

	a &= b; // �ٿ��� �� �ִ�.
	
	unsigned int f = 0b0110;
	cout << std::bitset<4>(f >> 2) << " " << (f >> 2) << endl;

	// Quiz
	// 0110 >> 2 -> decimal�� ��� �ɱ� : 1
	// 5 | 12 : 0101 1100 : 1101
	// 5 & 12 : 0100
	// 5 ^ 12 : 1001

}