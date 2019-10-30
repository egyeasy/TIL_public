#include <iostream>
#include <bitset>

using namespace std;

int main()
{
	bool item1_flag = false;
	bool item2_flag = false;
	bool item3_flag = false;
	bool item4_flag = false;

	// flag�� ���� �ٲ㰡�鼭 �۾��ϱ⿡�� �������� ������. item Ȯ�强�� ������

	// ��Ʈ �÷���
	unsigned char items_flag = 0;
	cout << bitset<8>(items_flag) << endl;

	const unsigned char opt0 = 1 << 0;
	const unsigned char opt1 = 1 << 1;
	const unsigned char opt2 = 1 << 2;
	const unsigned char opt3 = 1 << 3; // ������ ����� ������ ��Ģ���� ���� 0 shift
	cout << bitset<8>(opt0) << endl;

	cout << "No item " << bitset<8>(items_flag) << endl;

	// item0 on
	items_flag |= opt0;
	cout << "Item0 obtained " << bitset<8>(items_flag) << endl;

	// item3 on
	items_flag |= opt3;
	cout << "Item3 obtained " << bitset<8>(items_flag) << endl;

	// item3 lost
	items_flag &= ~opt3;
	cout << "Item3 lost " << bitset<8>(items_flag) << endl;

	// has item1 ?
	if (items_flag & opt1) {
		cout << "Has item1 " << endl;
	}
	else {
		cout << "Not has item1" << endl;
	}

	// has item0 ?
	if (items_flag & opt0) { cout << "Has item0" << endl; }

	
	// obtain item 2, 3
	items_flag |= (opt2 | opt3);
	cout << bitset<8>(opt2 | opt3) << endl;
	cout << "Item2, 3 obtained " << bitset<8>(items_flag) << endl;

	// 2�� ���� �ְ� 1�� ���� ���� ���� ���
	if ((items_flag & opt2) && !(items_flag & opt1))
	{
		//items_flag ^= opt2; // ���¸� �ٲ��ִ� ����� XOR
		//items_flag ^= opt1;
		items_flag ^= (opt1 | opt2);
	}

	cout << bitset<8>(items_flag) << endl;

	
	// ��Ʈ ����ũ
	unsigned int pixel_color = 0xDAA520;
	cout << std::bitset<32>(pixel_color) << endl;

	// red(green, blue)�� �ش��ϴ� DA�� ����ϰ� �ʹٸ�?
	const unsigned int red_mask = 0xFF0000;
	const unsigned int green_mask = 0x00FF00;
	const unsigned int blue_mask = 0x0000FF;

	// blue�� �����غ���
	unsigned char blue = pixel_color & blue_mask;
	cout << "blue " << bitset<8>(blue) << " " << int(blue) << endl; // 00100000 32

	//unsigned char green = pixel_color & green_mask;
	unsigned int green = (pixel_color & green_mask) >> 8; // blue 8�ڸ����� ���� �����Ƿ� right shift�ؾ� green�� ���� ����
	cout << "green " << bitset<8>(green) << " " << int(green) << endl; // 00000000 ��µ�. char�� �޾Ƽ� size�� ������ ��.


	return 0;
}