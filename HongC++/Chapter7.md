## 7.1 매개변수와 실인자의 구분(parameter, argument)

매개변수는 함수가 어떤 일을 하는지를 바꿔주는 기능.

```cpp
#include <iostream>

using namespace std;

int foo(int x, int y); // x, y는 파라미터

int foo(int x, int y)
{
	return x + y;
} // x and y are destoryed here

int main()
{
	int x = 1, y = 2;

	foo(6, 7); // 6, 7 : arguments(actual parameters)
	foo(x, y + 1); // 6, 3이 argument

	return 0;
}
```

변수가 선언되는 것과 같은 방식으로 정의 됨 -> 함수가 끝남과 동시에 사라짐.





## 7.2 값에 의한 전달 Passing Arguments by value(call by value)

```cpp
#include <iostream>

using namespace std;

void doSomething(int y)
{
	cout << "In func " << y << " " << &y << endl;
}

int main()
{
	doSomething(5);

	int x = 6;

	cout << "In main " << x << " " << &x << endl;
}
```

5라는 값이 전달되는 경우 y를 5로 정의





```cpp
#include <iostream>

using namespace std;

void doSomething(int y)
{
	cout << "In func " << y << " " << &y << endl;
}

int main()
{
	doSomething(5);

	int x = 6;

	cout << "In main " << x << " " << &x << endl;

	doSomething(x);
	doSomething(x + 1);

	return 0;
}
```

변수에 의한 전달은 좀 다르다.

x를 넣었을 때 6이라는 값만 전달되는 것

x와 y의 출력되는 주소가 다른 것을 볼 수 있다.

x + 1도 값이기 때문에 변수로 전달될 수 없다.



값으로 전달되면 함수 외부에 영향을 미치지 못한다 -> 깔끔하다.





## 7.3 참조에 의한 인수 전달 call by reference

```cpp
#include <cmath>
#include <iostream>

using namespace std;

void addOne(int& y)
{
	cout << y << " " << &y << endl;
	y = y + 1;
}

int main()
{
	int x = 5;

	cout << x << " " << &x << endl;

	addOne(x);

	cout << x << " " << &x << endl;
}
```

참조에 의해 x라는 변수 자체가 넘어갔다고 보면 됨.

값이 변경되어서 나온다.

주소도 같다는 것을 볼 수 있다.

=> 이러한 성질을 함수의 출력을 갖고 오는 데에 사용하기도 함



```cpp
#include <cmath>
#include <iostream>

using namespace std;

void getSinCos(const double degree, double& sin_out, double& cos_out) // degree는 영향을 못 미치고, double은 함수를 호출한 곳에 영향을 미칠 수 있게 됨
{
	static const double pi = 3.141592;
	double radians = degree * pi / 180.0;
	sin_out = std::sin(radians);
	cos_out = std::cos(radians);
}

int main()
{
	double sin(0.0);
	double cos(0.0);

	getSinCos(30.0, sin, cos);

	cout << sin << " " << cos << endl;

	return 0;
}
```

입력으로만 쓰이는 것은 const로 박제할 수 있다.

출력으로 쓰이는 것을 레퍼런스로 대신할 수 있다.

degree도 레퍼런스로 만들면 더 좋다.



```cpp
void foo(int& x)
{
	cout << x << endl;
}

	// foo(6); // 주소가 없어서 에러가 남
```

이러면 어떻게 할까? 



1. 함수에서 &를 쓰지 않는다

2. const int &x를 쓴다(변경되지 않을 경우에만)

   ```cpp
   void foo(const int& x)
   {
   	cout << x << endl;
   }
   ```



최근

1. return value optimization이 잘 구현
2. 여러 개의 return type을 사용하는 게 어렵지 않게 됨.

그래서 매개변수를 `const int& x`로 쓰는 게 일반적



### 포인터에 대한 레퍼런스 보내기

```cpp
typedef int* pint;

void foo1(int*& ptr) // int* 대신 pint를 써도 됨
{
	cout << ptr << " " << &ptr << endl;
}


	int x1 = 5;
	int* ptr = &x1;

	// foo(ptr); // 에러
	foo1(ptr);
```



### array를 파라미터로 전달하는 방법

```cpp
void printElements(int (&arr)[4]) // 대괄호 안에 개수가 반드시 들어가야 함
{

}


	printElements(arr);
```

이렇게 잘 쓰지 않는다. 벡터로 보내는 것이 훨씬 편함



### vector

```cpp
void printElements(vector<int>& arr) // const가 들어가도 됨
{

}

	// int arr[]{ 1, 2, 3, 4 };
	vector<int> arr{ 1 , 2, 3, 4 };

	printElements(arr);
```





## 7.4 주소에 의한 인수 전달 Call by Address

```cpp
#include <iostream>

using namespace std;

void foo(int* ptr) // 주소만 input으로 들어갈 수 있다.
{
	cout << *ptr << " " << ptr << " " << &ptr << endl;
}

int main()
{
	int value = 5;

	cout << value << " " << &value << endl;

	int* ptr = &value;

	cout << &ptr << endl;

	foo(ptr);
	foo(&value);
	//foo(5); // 주소가 없어서 안됨. const int로도 안된다
}
```

main ptr의 주소와 foo 안의 ptr의 주소는 서로 다르다.(ptr 자체(*)는 같음. ptr의 주소(**)가 다르다는 것)

포인터도 하나의 변수이기 때문에 주소라는 값을 call by value한 것과 같다.

call by value의 일종인 것.



```cpp
void foo(const int* ptr)
{
	cout << *ptr << " " << ptr << " " << &ptr << endl;

	//*ptr = 10;
}
```

const int* 를 입력으로 받으면 deref 값을 변경할 수 없다.



### 주소로 값 변경하기

```cpp
void foo(double degree, double* sin_out, double* cos_out)
{
	*sin_out = 20;
	*cos_out = 30;
}

	double degree = 30;
	double sin, cos;
	foo(degree, &sin, &cos);
	
	cout << sin << ' ' << cos << endl;
```



### 배열

```cpp
void foo(int* arr, int length)
{
	for (int i = 0; i < length; ++i)
	{
		cout << arr[i] << endl;
	}
	
	arr[0] = 1.0; // 이것도 가능
}

```

`const int * arr`이라면 배열의 내용을 변경할 수 없다.



### 주소를 바꾸기

```cpp
void foo(const int * ptr, int* arr, int length)
{
	for (int i = 0; i < length; ++i)
	{
		cout << arr[i] << endl;
	}
	
	arr[0] = 1.0; // 이것도 가능

	int x = 1;

	ptr = &x;
}
```

주소 자체를 바꾸는 것은 가능. 못 바꾸게 하려면? `const int * const ptr`로 ptr 바로 앞에 const를 써줘야.

(`const int`는 주소 안의 값을 const로 설정하겠다는 뜻이고, const * ptr은 ptr 즉 주소를 const로 설정하겠다)





































