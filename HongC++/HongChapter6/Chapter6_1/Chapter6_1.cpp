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


	int num_students = 0; // const int�� �����ϸ� �迭 ������� ���� ����
	cin >> num_students; // ��Ÿ�ӿ� �����ȴ� = ������ �ϴ� ���� ���� ��������. 

	// int students_scores[num_students]; // ���� ��

	

	return 0;

}