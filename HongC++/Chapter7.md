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





## 7.5 다양한 반환 값들(값, 참조, 주소, 구조체, 튜플)

### return by value

```cpp
#include <iostream>

using namespace std;

int getValue(int x)
{
	int value = x * 2;
	return value;
}

int main()
{
	int value = getValue(3);

	return 0;
}
```

값이 복사해서 들어가게 된다. 하지만 변수의 생성, 복사 때문에 속도가 떨어질 것. 간단한 경우에는 문제가 되지 않으나 데이터가 엄청나게 많다면 문제가 된다. 



### 주소로 돌려받기(return by address)

1. dereference해서 받기(`int value = *getValue(3);`)

   권장하지 않는다. 함수 영역을 벗어남과 동시에 사라지게 되는데 이걸 반환하는 것이 좋지는 않다.

2. 주소를 받기

   ```cpp
   #include <iostream>
   
   using namespace std;
   
   int* getValue(int x)
   {
   	int value = x * 2;
   	return &value;
   }
   
   int main()
   {
   	int *value = getValue(3); // 
   
   	return 0;
   }
   ```

   이건 더 위험하다. 함수를 벗어나면서 변수는 사라졌는데 주소만 쥐고 있으면서 전달하면 그 안에 뭐가 있는지 모른다. main dereference 하면 제대로 나오긴 할 수 있으나 권장하지 않는다.



특이한 방식으로 return by address 하기도 한다.

```cpp
int* allocateMemory(int size)
{
	return new int[size];
}

	//int* array = new int[10];
	int* array = allocateMemory(1024);
	delete[] array;

```

이것의 위험은 new와 대응되는 delete이 있어야 한다는 것. main에 delete을 두면 new랑 층위가 달라서 어려워질 수 있다.



### return by reference

```cpp
int& getVal(int x)
{
	int value = x * 2;
	return value;
}

	int &val = getVal(5);

	cout << val << endl;
	cout << val << endl;
```

작동하긴 하지만 위험하다. 이미 사라지는 애의 reference를 받는 것.

두 번째 출력할 때 이상한 값이 나온다. 임시로 잡아두다가 값이 사라진 것 -> 쓰레기 값이 출력된다.



쓸모가 없냐하면 그런 건 아니다. 편하게 쓸 수 있는 경우가 있다.

```cpp
int& get(std::array<int, 100>& my_array, int ix) // 여기서 &로 받는다.
{
	return my_array[ix];
}

	std::array<int, 100> my_array;
	my_array[30] = 10;
	
	// 데이터 일부를 고치고 싶다.
	get(my_array, 30) = 1024;

	cout << my_array[30] << endl;
```

array 주소는 확실하게 main에 잡아둔 상태에서 한 인자를 얻고 싶을 때 사용.



### 여러 개의 값 리턴

1. struct로 받는 게 일반적인 방법

```cpp
struct S
{
	int a, b, c, d;
};

S getStruct()
{
	S my_s{ 1, 2, 3, 4 };
	return my_s;
}


	S my_s = getStruct();
	cout << my_s.a << endl;
```

​	c 스타일이라면 이걸 사용하지만 불편하다. 속도는 더 빠르다.



2. tuple 사용

   ```cpp
   #include <tuple>
   
   using namespace std;
   
   std::tuple<int, double> getTuple()
   {
   	double a = 10;
   	double d = 3.14;
   	return std::make_tuple(a, d);
   }
   
   	// tuple
   	std::tuple<int, double> my_tp = getTuple();
   	cout << std::get<0>(my_tp) << endl; // a
   	cout << std::get<1>(my_tp) << endl; // d
   
   ```

   이것도 여전히 불편하긴 하다. 받는 쪽에서 tuple을 선언해야 함



3. C++ 17

   ```cpp
   	auto [a, d] = getTuple();
   	cout << a << endl;
   	cout << d << endl;
   ```

   a, d 변수를 선언함과 동시에 받아주는 것.















