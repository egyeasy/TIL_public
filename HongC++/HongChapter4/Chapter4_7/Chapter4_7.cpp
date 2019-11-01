#include <iostream>
#include <typeinfo>


int computeDamage(int weapon_id)
{
	if (weapon_id == 0) // sword
		return 1;

	if (weapon_id == 1) // hammer
	{
		return 2;
	}
}

enum Color
{
	COLOR_BLACK = -3,
	COLOR_RED,
	COLOR_BLUE = 5,
	COLOR_GREEN, // trailing comma 허용
}; // ; 필수

enum Feeling
{
	HAPPY,
	JOY,
	TIRED,
	BLUE, // 만약 위에서도 BLUE를 정의했으면 겹쳐서 컴파일 에러
};

int main()
{
	using namespace std;

	Color paint = COLOR_BLACK;
	Color house(COLOR_BLUE);
	Color apple{ COLOR_RED };

	cout << paint << ' ' << endl; // 0

	cout << COLOR_BLACK << endl; // -3
	cout << COLOR_RED << endl; // -2
	cout << COLOR_BLUE << endl; // 5
	cout << COLOR_GREEN << endl; // 6

	//cin >> my_color; // 안 된다
	int in_number;
	cin >> in_number;

	//if (in_number == 0) my_color = COLOR_BLACK;

	string str_input;

	std::getline(cin, str_input);

	if (str_input == "COLOR_BLACK") // doSomething

	 

	return 0;
}