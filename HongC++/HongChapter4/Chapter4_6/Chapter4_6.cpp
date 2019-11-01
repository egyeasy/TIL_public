#include <iostream>
#include <string>
#include <limits>

using namespace std;

int main()
{
	const char my_strs[] = "Hello, World"; // �⺻���� ���. �� ���ڰ� �迭�� �� ĭ
	//const string my_hello = "Hello, World"; // ���϶�� �����س� ��. ����� ���� �ڷ���
	const string my_hello{ "Hello, World" }; // �̷��Ե� ����

	cout << "Hello, World" << endl;

	string my_ID = "123"; // ���ڴ� �̷���

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

	//std::cin.ignore(32767, '\n'); // 32767���� ���ڸ� �����ع�����. 2byte�� �Է°����� ���� �� ����
	std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');

	cout << name << " " << age << endl;


	string a("Hello, ");
	string b("World");

	string hw = a + b; // append - ���ڿ� �ڿ� ���ϱ�
	hw += "I'm good";

	cout << hw << endl;

	// ���� ����
	string c("Hell, World");

	cout << c.length() << endl;


	return 0;
}