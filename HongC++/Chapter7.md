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





## 7.6 인라인 함수

프로그램을 빠르게 만들려고 할 때 최적화를 하기 위

```cpp
#include <iostream>

using namespace std;

int min(int x, int y)
{
	return x > y ? y : x;
}

int main()
{

	cout << min(5, 6) << endl;
	cout << min(3, 2) << endl;
}
```

복사하는 등의 과정에서 시간이 많이 걸린다.



이럴 때 인라인 함수들을 이렇게 쓴다.

```cpp
#include <iostream>

using namespace std;

inline int min(int x, int y)
{
	return x > y ? y : x;
}

int main()
{

	cout << min(5, 6) << endl;
	cout << min(3, 2) << endl;

	cout << (5 > 6 ? 6 : 5) << endl;
	cout << (3 > 2 ? 2 : 3) << endl;
}
```

이렇게 쓴 효과와 같아진다. 이건 컴파일러에게 처리를 맡기는 것. inline 선언은 강제 의무가 아니라, 권장/권유이다. 가능하다면 적용해보는 것. 모든 함수를 inline으로 바꾼다고 빨라지는 것이 아니다. 또한 요즘 컴파일러는 인라인을 넣지 않아도 스스로 판단하여 성능이 빨라질 것 같으면 인라인을 적용한다. 따라서 요즘은 쓰든 안쓰든 속도의 보장이 없다는 게 대세다.

인라인과 같은 코딩 문법보다는 소프트웨어 구조, data driven(GPU 가속, 병렬처리 등)으로 성능을 개선하는 것을 권장.

인라인 함수를 많이 쓰게 되면 코드가 많이 커진다 -> 메모리에서 프로그램이 차지하는 용량이 많다 -> 더 효율적이라고 할 수가 없다.



## 함수 오버로딩 Function Overloading

```cpp
#include <iostream>
#include <string>
using namespace std;

int add(int x, int y)
{
	return x + y;
}

double add(double x, double y)
{
	return x + y;
}

int main()
{

}
```



```cpp
#include <iostream>
#include <string>
using namespace std;

int add(int x, int y)
{
	return x + y;
}

double add(double x, double y)
{
	return x + y;
}

int main()
{
	add(1, 2);
	add(3.0, 4.0); // 컴파일러가 알아서 해당하는 함수를 적용해서 컴파일한다.
}
```

컴파일러는 매개변수가 다르면 서로 다른 함수로 인식한다. 매개변수에 맞춰서 함수를 찾아 컴파일하는 것.

어느 add를 사용할 지는 컴파일 할 때 결정이 되어야 한다.

만약 이름과 매개변수 타입까지 같으면 에러가 발생한다. return type만 다르다고 다른 함수로 인식되지 않는다.



```cpp
//int getRandomValue() {}
void getRandom(int& x) {}

//double getRandomValue() {}
void getRandom(double& x) {}

	int x;
	getRandom(x);
```

아래 방법은 main에서 변수를 일일이 선언해줘야 함



```cpp
typedef int my_int;

void print(int x) {}

void print(my_int x) {}
```

my_int = int이기 때문에 컴파일 실패



```cpp
void print(char* value) {}
void print(int value) {}

	print(0);
	print('a'); // int로 인식. "a"라면 문자열이라 매치되는 게 없다고 나옴
```

잘 맞는 게 없어서 억지로 있는 것들 중에 갖다 맞춘다.



```cpp

void print(unsigned int value) {}
void print(float value) {}

	print('a');
	print(0);
	print(3.14159); // 모호하다. 
```



```cpp
	print((unsigned int)'a');
	print(0u); // unsigned int
	print(3.14159f);
```

이렇게 모호성을 해소할 수 있다.





## 매개변수의 기본값 Default Parameters

```cpp
#include <iostream>
using namespace std;

void print(int x = 0)
{
	cout << x << endl;
}

int main()
{
	print(10);
	print();

	return 0;
}
```



```cpp
void print(int x, int y = 20, int z = 30)
{
	cout << x << endl;
}

int main()
{
	//print(10);
	print();
	print(100);
	print(100, 200);

	return 0;
}
```

파라미터의 오른쪽부터 default 값을 채워줘야 한다.



### 주의할 점 - 기본값 재정의

```cpp
void print(int x = 10, int y = 20, int z = 30); // in header

//void print(int x = 0)
//{
//	cout << x << endl;
//}

//void print(int x = 10, int y = 20, int z = 30)
void print(int x, int y, int z)
{
	cout << x << endl;
}
```

header에서 함수를 선언할 경우 한 군데에서만 default를 넣어줘야 한다.

보통은 헤더 파일에 디폴트를 넣는다.



```cpp
void print(std::string str) {}
void print(char ch = ' ') {}

	print(); // char 타입의 파라미터가 들어가는 함수로 인식될 것
```



좀 더 난감한 경우를 알아보자.

```cpp
void print(int x) {}
void print(int x, int y = 20) {}

	print(10); // ambiguous error
```

디폴트 값 때문에 앞의 매개변수 1개 함수를 오버로딩 할 수 없다.





## 7.9 함수 포인터

함수도 주소를 갖고 있다. 그래서 주소를 가지고 다른 것을 할 수 있다.

```cpp
#include <iostream>
using namespace std;

int func()
{
	return 5;
}

int main()
{

	cout << func << endl;
	
	int(*fcnptr)() = func;


	return 0;
}
```



```cpp
#include <iostream>
using namespace std;

int func()
{
	return 5;
}

int goo()
{
	return 10;
}

int main()
{

	cout << func << endl;
	
	int(*fcnptr)() = func; // func를 실행()시키지 않고 주소만 받는다.

	cout << fcnptr() << endl; // 괄호를 치면 실행이 됨

	fcnptr = goo;
	
	cout << fcnptr() << endl; // 10


	return 0;
}
```

  

매개변수 표시

```cpp
#include <iostream>
using namespace std;

int func(int x)
{
	return 5;
}

int goo()
{
	return 10;
}

int main()
{

	cout << func << endl;
	
	int(*fcnptr)(int) = func; // func를 실행()시키지 않고 주소만 받는다.

	cout << fcnptr() << endl; // 괄호를 치면 실행이 됨

	fcnptr = goo;
	
	cout << fcnptr() << endl; // 10




	return 0;
}
```

goo와는 매개변수 형식이 안맞아서 에러가 남.



```cpp

void printNumbers(const array<int, 10>& my_array, bool print_even)
{
	for (auto element : my_array)
	{
		if (print_even && element % 2 == 0) cout << element;
		if (!print_even && element % 2 == 1) cout << element;
	}
	cout << endl;

}



	std::array<int, 10> my_array = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

	for (auto element : my_array)
	{
		if (element % 2 == 0) cout << element;
	}
	cout << endl;

	printNumbers(my_array, true);
	printNumbers(my_array, false);

```



여기서 함수 포인터를 사용해보자.

```cpp
bool isEven(const int& number)
{
	if (number % 2 == 0) return true;
	else return false;
}

bool isOdd(const int& number)
{
	if (number % 2 != 0) return true;
	else return false;
}

void printNumbers(const array<int, 10>& my_array, bool (*check_fcn)(const int&))
{
	for (auto element : my_array)
	{
		if (check_fcn(element) == true) cout << element;
	}
	cout << endl;

}


	std::array<int, 10> my_array = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };

	printNumbers(my_array, isEven);
	printNumbers(my_array, isOdd);
```



기본값 부여도 가능

```cpp
void printNumbers(const array<int, 10>& my_array, bool (*check_fcn)(const int&) = isEven)
```



함수 포인터가 빈번하게 사용된다면 type define으로 줄일 수 있다.



### typedef

```cpp
typedef bool(*check_fcn_t)(const int&);

//void printNumbers(const array<int, 10>& my_array, bool (*check_fcn)(const int&) = isEven)
void printNumbers(const array<int, 10>& my_array, check_fcn_t check_fcn = isEven)
```



또는 앞에서 이렇게 선언

### using

```cpp
using check_fcn_t = bool(*)(const int&);
```



더 편한 것은(C++ 17)

### functional

```cpp
void printNumbers(const array<int, 10>& my_array, std::function<bool(const int&)> check_fcn = isEven)
    
    std::function<bool(const int&)> fcnptr1 = isEven;

	printNumbers(my_array, isEven);
	printNumbers(my_array, isOdd);

	fcnptr1 = isOdd;

	printNumbers(my_array, fcnptr1);
```





## 7.10 스택과 힙

메모리의 각 부분을 세그먼트라고 함



### 각 세그먼트

힙

스택

data : 초기화된 전역 및 static variables

BSS(uninitialized data segment) : 0으로 초기화된 static variables

code segment : 작성한 코드



### 스택 stack

함수가 다른 호출하며 깊이 들어가면서 stack에 함수 및 지역변수들을 쌓는다. 함수가 끝나면 그것을 위에서 제거한다.

스택의 단점 : 빠르지만 크기가 작다. `array[1000000]`를 할당하지 못한다(**stack** **overflow**)



### 힙 heap

스택을 보완하기 위해 힙 메모리를 추가로 사용.

```cpp
int main()
{
    int *ptr = nullptr;
    ptr = new int[1000000];
    
    delete[] ptr;
    
    ptr = nullptr;
    
    return 0;
}
```



`ptr = new int[1000000];` 동적메모리를 할당하면 이 만큼의 공간을 할당함. but 어디에 생기는지는 알기 힘들다(스택은 순차적으로 쌓이지만, 힙에는 순서가 없다) 큰 데이터가 일련으로 들어갈 수 있는 공간을 마련해야 할 경우 OS가 가장 적당한 곳을 지정해서 들어가기 때문.

`delete[] ptr` : heap에 할당된 메모리를 회수해감. 단, 스택 상에는 ptr이 남아있다. 이 변수를 따라가면 이상한 값이 있을 것. 이를 방지하기 위해 `ptr = nullptr;`



```cpp
void initArray()
{
    int *ptr2 = new int[1000];
    // delete[] ptr2; // delete 하지 않는다면?
}

int main()
{
    initArray();
    
    return 0;
}
```

initArray() 함수가 끝나고 나가는데 ptr2를 heap 상에서 지우지 않았다. 이럴 경우 ptr2의 내용을 가리키는 변수가 없어진다 -> 메모리 누수 -> 다른 프로그램이 사용할 메모리를 잠식하게 됨.





## 7.11 std::vector를 스택처럼 사용하기

vector에는 size, capacity가 있다.

new와 delete은 많이 느리다.

벡터는 new와 delete을 사용하여 공간을 늘리기도, 줄이기도 하는 건데,

어떻게 하면 new와 delete이 적게 호출될 지를 따지면서 짜야 효율성을 향상시킬 수 있다.

- capacity : 프로그램 내부에서는 capacity 개수 만큼 메모리를 가지고 있다
- size : 그 중 일부만 사용하는데 그 크기임.



```cpp
#include <iostream>
#include <vector>

using namespace std;

int main()
{
	// int *v_ptr = new int[3]{1, 2, 3};

	std::vector<int> v{ 1, 2, 3 };

	// size, capacity(용량)
	
	for (auto& e : v)
		cout << e << " ";
	cout << endl;

	return 0;
}
```



```cpp
	cout << v.size() << " " << v.capacity() << endl; // 3
	
	v.resize(10);

	cout << v.size() << " " << v.capacity() << endl;

	for (auto& e : v)
		cout << e << " ";
	cout << endl;

	v.resize(2);

	for (auto& e : v)
		cout << e << " ";
	cout << endl;
```

사이즈를 늘릴 때는 size, capacity가 늘어나지만, 사이즈를 줄이면 capacity는 줄어들지 않는다.

사이즈를 2까지 줄인 다음에 `v.at(2)`으로 강제로 불러보면 runtime error가 발생

강제로 포인터를 가져와보자

```cpp
int *ptr = v.data();

cout << ptr[2] << endl; // 3
```

억지로 가지고 와진다.



2개로 작게 resize를 했을 때 전체 갯수 중에 복사한 다음 뒷 부분을 지우면 메모리를 더 잘 쓸 수 있을 것. 하지만 vector는 속도를 위해 메모리를 희생했다. 그러므로 리사이즈 해도 원래의 element를 가지고 있는 것. size는 변하지만 capacity는 변하지 않는다는 점에서도 확인할 수 있다.



### 원래 벡터를 출력하는 방법

```cpp
for (unsigned int i = 0; i < v.size(); ++i)
    cout << v[i] << " ";
cout << endl;
```



### reserve

```cpp
	v.reserve(1024);
```

size는 그대로, capacity를 1024로 늘리는 작업 -> 나중에 동적으로 element를 추가할 때 추가하는 속도가 빨라짐



### stack with vector

재귀호출을 할 때 stack overflow가 나면 -> vector를 stack으로 사용하는 경우가 있다.

```cpp
void printStack(const std::vector<int>& stack)
{
	for (auto& e : stack)
		cout << e << " ";
	cout << endl;
}


	// 스택
	std::vector<int> stack;

	stack.push_back(3);
	printStack(stack);

	stack.push_back(5);
	printStack(stack);
	
	stack.push_back(7);
	printStack(stack);
	
	stack.pop_back();
	printStack(stack);
	
	stack.pop_back();
	printStack(stack);
```

미리 reserve를 해두면 push_back 할 때 속도가 빠르다.

pop은 capacity를 유지한 채로 size만 줄인다 -> 빠를 것





## 7.12 재귀적 함수 호출

```cpp
#include <iostream>
using namespace std;

void countDown(int count)
{
	cout << count << endl;
	countDown(count - 1);
}

int main()
{
	countDown(5);

	return 0;
}
```

코드는 다른 곳에 저장돼있고, 주소를 보고 그 코드를 찾아간다.



무한 호출을 막기 위해 중단 조건을 설정하자.

```cpp
#include <iostream>
using namespace std;

void countDown(int count)
{
	cout << count << endl;

	if(count > 0)
		countDown(count - 1);
}

int main()
{
	countDown(5);

	return 0;
}
```



1부터 N까지의 합을 구하는 재귀 함수

```cpp
#include <iostream>
using namespace std;


int sumTo(int sumto)
{
	if (sumto <= 0)
		return 0;
	else if (sumto <= 1)
		return 1;
	else
		return sumTo(sumto - 1) + sumto;
}

int main()
{
	cout << sumTo(4) << endl;

	return 0;
}
```





### 피보나치 수열

```cpp
int sumTo(int sumto)
{
	if (sumto <= 0)
		return 0;
	else if (sumto <= 1)
		return 1;
	else
		return sumTo(sumto - 1) + sumto;
}
```



recursion의 depth에 한계가 있고, performance 가 중요할 때 별로 사용하지 않는 듯하다. 실전에서는 iteration을 많이 사용한다.





## 7.13 방어적 프로그래밍의 개념

많은 사람들이 사용할 때 에러가 나지 않도록 만드는 게 방어적 프로그래밍.

요즘은 컴파일러가 잘 돼있어서 컴파일러가 미리 잡아낼 수 있도록 짜는 것도 좋다.

그것보다 문제가 되는 것은 semantic errors



### sematic erros

```cpp
#include <iostream>

using namespace std;

int main()
{
	// semantic errors

	int x;
	cin >> x;

	if (x >= 5)
		cout << "x is greater than 5" << endl;

	return 0;
}
```

x가 5와 같을 경우를 포함하고 있다 -> **논리** **오류**

이건 설계자가 아니면 알기 쉽지 않다.



### violated assumption

사용자가 내가 작성한 방식과는 전혀 다른 방식으로 사용한다.

```cpp
	// violated assumption

	string hello = "Hello, my name is jack jack";

	int ix;
	cin >> ix;

	cout << hello[ix] << endl;
```

ix에 string 길이보다 큰 값을 넣으면 런타임 에러가 뜬다. 이걸 미리 막을 수 있는 것이 방어적 프로그래밍.



```cpp
	string hello = "Hello, my name is jack jack";

	cout << "Input from 0 to " << hello.size() - 1 << endl;

	while (true)
	{
		int ix;
		cin >> ix;

		if (ix >= 0 && ix <= hello.size() - 1)
			cout << hello[ix] << endl;
		else
			cout << "Please try again" << endl;

	}
```

결국 이런 것은 경험과 관련이 있다. 실패의 시간을 가져봐야 한다. 





## 7.14 단언하기 assert

컴파일러 도움을 받기.

```cpp
#include <cassert> // assert.h

int main()
{
	assert(false);

	return 0;
}
```

디버그 모드일 때만 작동한다. 프로젝트 설정 > C/C++ > Preprocessor에 들어가면 NDebug 설정이 되어있는 것을 볼 수 있다. 여기서는 안 되는 것.

릴리즈 모드에서는 프로그램이 빠르게 돌아야하기 때문에 assert를 빼버린다.



```cpp
#include <cassert> // assert.h

int main()
{
	//assert(false);


	int number = 5;
	 
	/// ...

	assert(number = 5);
	

	return 0;
}
```



다른 예제를 보자

```cpp
#include <cassert> // assert.h
#include <array>
#include <iostream>

using namespace std;

void printValue(const std::array<int, 5>& my_array, const int& ix)
{
	assert(ix >= 0);
	assert(ix <= my_array.size() - 1);

	cout << my_array[ix] << std::endl;
}

int main()
{

	std::array<int, 5> my_array{ 1, 2, 3, 4, 5 };

	printValue(my_array, 100);

	return 0;
}
```

런타임 에러가 나긴 하지만 어디서 틀렸는지를 assert를 통해 알 수 있다. 다른 프로그래머는 런타임에 assert를 통해 알 수 있는 것.

assert 내부에 && 문을 써줄 수도 있음.



### static assert

컴파일 타임에 결정이 되는 경우에만 쓸 수 있다.

`static_assert(x == 5)`에서 x가 const가 아니면 쓸 수 없다.

인자로 에러 메시지를 남길 수도 있다.

```cpp
	// static assert
	const int x = 10;
	assert(x == 5);

	static_assert(x == 5, "x should be 5");
```





## 7.15 명령줄 인수 command line arguments

main 함수 괄호 안에 매개변수 집어넣는 법

파라미터를 두 가지를 넣을 수 있다.

```cpp
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) // 개수, 내용
{
	for (int count = 0; count < argc; ++count)
	{
		cout << argv[count] << endl; // 실행파일 경로(이름) 출력
	}
	


	return 0;
}
```

1. x86 native tools command prompt에서 해당 프로그램을 실행할 수도 있다. 프로그램 경로 + "출력할 명령어"를 띄어쓰기 구분으로 써준다.
2. 다른 방법은 프로젝트 설정 > debugging >  command arguments에 my_program '100 1024 3.14' 입력



### string으로 처리하기

```cpp
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[]) // 개수, 내용
{
	for (int count = 0; count < argc; ++count)
	{
		std::string argv_single = argv[count];

		if (count == 1) // 0번은 실행파일 path
		{
			int input_number = std::stoi(argv_single); // 정수로 바꿔주기
			cout << input_number + 1 << endl;
		}
		cout << argv[count] << endl; // 실행파일 경로(이름) 출력
	}
	


	return 0;
}
```



### boost library - commandline options

커맨드라인을 좀 더 편하게 쓸 수 있다.





## 7.16 생략부호 Ellipsis

함수의 인자로 개수를 정해서 받고 싶지 않을 때

```cpp
#include <iostream>
#include <cstdarg> // for ellipsis
using namespace std;

double findAverage(int count, ...)
{
	double sum = 0;

	va_list list; // 문자열로 받는다.

	va_start(list, count); // 두 번째 인자로 들어오는 arg의 개수를 알려준다

	for (int arg = 0; arg < count; ++arg)
		sum += va_arg(list, int);

	va_end(list);

	return sum / count;
}

int main()
{
	cout << findAverage(1, 1, 2, 3, "Hello", 'c') << endl; // 1개만 되고 나머지는 무시됨
	cout << findAverage(3, 1, 2, 3) << endl;
	cout << findAverage(5, 1, 2, 3, 4, 5) << endl;
	cout << findAverage(10, 1, 2, 3, 4, 5) << endl; // 이상한 숫자가 도출
}
```

but 디버깅하기 힘들고 런타임에서 오류가 나면 막막할 때가 있어서 쉽지 않다.

최근에는 모던 C++ 문법을 사용해서 하려고 노력함.



























