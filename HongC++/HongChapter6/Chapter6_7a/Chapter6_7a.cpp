#include <iostream>
#include <cstddef>

void doSomething(double* ptr)
{
	std::cout << "address of pointer variable in function: " << &ptr << std::endl;

	if (ptr != nullptr)
	{
		// do something useful
		std::cout << *ptr << std::endl;
	}
	else
	{
		// do nothing with ptr
		std::cout << "Null ptr, do nothing" << std::endl;
	}

}

int main()
{
	double* ptr = 0; // c-style
	double* ptr2 = NULL;
	double* ptr3 = nullptr; // modern c++
	// double *ptr{ nullptr } // uniform initialization 가능

	if (ptr3 != nullptr)
	{
		// do something useful
	}
	else
	{
		// do nothing with ptr
	}

	doSomething(ptr3);
	doSomething(nullptr);

	double d = 123.4;
	doSomething(&d);

	ptr = &d;

	doSomething(ptr);

	std::nullptr_t nptr; // null pointer밖에 못넣는다.

	std::cout << "address of pointer variable in main: " << &ptr3 << std::endl;

	return 0;

}