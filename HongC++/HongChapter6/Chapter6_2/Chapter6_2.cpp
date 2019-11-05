#include <iostream>

using namespace std;

void doSomething(int students_scores[]) // size 표시하지 않아도 됨
{
	cout << students_scores[0] << endl;
	cout << students_scores[1] << endl;
	cout << students_scores[2] << endl;

	cout << (int)&students_scores << endl;
	cout << "size: " << sizeof(students_scores) << endl;
}

int main()
{
	const int num_students = 20;

	int students_scores[num_students] = { 1, 2, 3, 4, 5 };

	cout << (int)&students_scores << endl;			// +0
	cout << (int) & (students_scores[0]) << endl;	// +0
	cout << (int) & (students_scores[1]) << endl;	// +4
	cout << (int) & (students_scores[2]) << endl;	// +8
	cout << (int) & (students_scores[3]) << endl;	// +12

	cout << "size: " << sizeof(students_scores) << endl;

	doSomething(students_scores); // 함수의 인자로 전달 가능

	return 0;
}