#include <iostream>

using namespace std;

struct Rectangle
{
	int length;
	int width;
};

enum StudentName
{
	JACKJACK,	// = 0
	DASH,		// = 1
	VIOLET,		// = 2
	NUM_STUDENTS, // = 3
};

int main()
{
	cout << sizeof(Rectangle) << endl; // 8

	Rectangle rect_arr[10];

	cout << sizeof(rect_arr) << endl;  // 8 * 10 = 80


	//int my_array[5] = { 1, 2, 3, 4, 5 };
	int my_array[]{ 1, 2, 3, 4, 5 }; // C++ 17

	cout << my_array[JACKJACK] << endl;
	cout << my_array[VIOLET] << endl;
	cout << my_array[4] << endl;

	int students_scores[NUM_STUDENTS];


	int num_students = 0; // const int로 선언하면 배열 사이즈로 선언 가능
	cin >> num_students; // 런타임에 결정된다 = 실행을 하는 때에 값이 정해진다. 

	// int students_scores[num_students]; // 빨간 줄

	

	return 0;

}