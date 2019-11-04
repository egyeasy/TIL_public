#include <iostream>
#include <string>

using namespace std;

// void printPerson(double height, float weight, ...) // 직접 다 넣기에는 부담.

struct Person
{
	double	height = 3.0;
	float	weight = 200.0;
	int		age = 100;
	string	name = "Mr. Incredible";

	void print()
	{
		cout << height << " " << weight << " " << age << " " << name;
		cout << endl;
	}
};

struct Family
{
	Person me, mom, dad;
};

Person getMe()
{
	Person me{ 2.0, 100.0, 20, "Jack Jack" };

	return me;
}

// Employee
struct Employee		// 2 + (2) + 4 + 8 = 16 bytes
{
	short	id;		// 2 bytes
	int		age;	// 4 bytes
	double	wage;	// 8 bytes
};

int main()
{
	double	height;
	float	weight;
	int		age;
	string	name;

	Person me{ 2.0, 100.0, 20, "Jack Jack" };
	// 이렇게 치기엔 부담스러움
	/*me.age = 20;
	me.name = "Jack Jack";
	me.height = 2.0;
	me.weight = 100.0;*/

	me.print();

	Person me2(me);
	me2.print();

	Person me3 = me;
	me3.print();

	Person me_from_func = getMe();
	me_from_func.print();

	cout << sizeof(Employee) << endl; // 16

	return 0;
}