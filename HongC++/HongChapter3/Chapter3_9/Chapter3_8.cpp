#include <iostream>
#include <bitset>

using namespace std;

int main()
{
	bool item1_flag = false;
	bool item2_flag = false;
	bool item3_flag = false;
	bool item4_flag = false;

	// flag를 직접 바꿔가면서 작업하기에는 불편함이 따른다. item 확장성도 떨어짐

	// 비트 플래그
	unsigned char items_flag = 0;
	cout << bitset<8>(items_flag) << endl;

	const unsigned char opt0 = 1 << 0;
	const unsigned char opt1 = 1 << 1;
	const unsigned char opt2 = 1 << 2;
	const unsigned char opt3 = 1 << 3; // 실질적 계산은 없지만 규칙성을 위해 0 shift
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

	// 2를 갖고 있고 1을 갖고 있지 않을 경우
	if ((items_flag & opt2) && !(items_flag & opt1))
	{
		//items_flag ^= opt2; // 상태를 바꿔주는 명령은 XOR
		//items_flag ^= opt1;
		items_flag ^= (opt1 | opt2);
	}

	cout << bitset<8>(items_flag) << endl;

	
	// 비트 마스크
	unsigned int pixel_color = 0xDAA520;
	cout << std::bitset<32>(pixel_color) << endl;

	// red(green, blue)에 해당하는 DA만 출력하고 싶다면?
	const unsigned int red_mask = 0xFF0000;
	const unsigned int green_mask = 0x00FF00;
	const unsigned int blue_mask = 0x0000FF;

	// blue만 추출해보자
	unsigned char blue = pixel_color & blue_mask;
	cout << "blue " << bitset<8>(blue) << " " << int(blue) << endl; // 00100000 32

	//unsigned char green = pixel_color & green_mask;
	unsigned int green = (pixel_color & green_mask) >> 8; // blue 8자리까지 같이 나오므로 right shift해야 green만 추출 가능
	cout << "green " << bitset<8>(green) << " " << int(green) << endl; // 00000000 출력됨. char로 받아서 size가 부족한 것.


	return 0;
}