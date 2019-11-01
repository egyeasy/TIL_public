#include <iostream>
#include <string>
#include <limits>

using namespace std;

int main()
{
	const char my_strs[] = "Hello, World"; // 기본적인 방식. 한 글자가 배열의 한 칸
	//const string my_hello = "Hello, World"; // 편하라고 구현해낸 것. 사용자 정의 자료형
	const string my_hello{ "Hello, World" }; // 이렇게도 가능

	cout << "Hello, World" << endl;

	string my_ID = "123"; // 숫자는 이렇게

	cout << "Your name ? : ";
	std::string name;
	//cin >> name;
	//std::getline(std::cin, name);

	cout << "Your age ? : ";
	//string age;
	//cin >> age;
	//std::getline(std::cin, age);
	int age;
	cin >> age;

	//std::cin.ignore(32767, '\n'); // 32767개의 글자를 무시해버려라. 2byte로 입력가능한 가장 긴 길이
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	cout << name << " " << age << endl;


	string a("Hello, ");
	string b("World");

	string hw = a + b; // append - 문자열 뒤에 더하기
	hw += "I'm good";

	cout << hw << endl;

	// 길이 측정
	string c("Hell, World");

	cout << c.length() << endl;


	return 0;
}