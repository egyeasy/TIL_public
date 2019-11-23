#include <iostream>

struct Person
{
	int age;
	double weight;

};

int main()
{
	Person person;

	person.age = 5;
	person.weight = 30;

	Person& ref = person;
	ref.age = 15;
	
	// 포인터는 좀 다르다
	Person* ptr = &person;
	ptr->age = 30;
	(*ptr).age = 20; // dereference를 쓰면 점으로 접근 가능
	
	Person& ref2 = *ptr;
	ref2.age = 45;

	std::cout << &person << std::endl;
	std::cout << &ref2 << std::endl;

	return 0;
}