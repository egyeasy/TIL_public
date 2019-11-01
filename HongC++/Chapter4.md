## 4.1 지역 변수, 범위, 지속기간

- 범위(scope)
- 지속기간(duration)



```cpp
#include <iostream>

int main()
{
	using namespace std;

	int apple = 5;

	cout << apple << endl; // 5

	{
		int apple = 1;
		cout << apple << endl; // 1
	}

	cout << apple << endl; // 5
}
```

같은 영역 안에서는 중복 정의 불가능. 중괄호로 구분된 영역에서는 가능



### namespace

```cpp
#include <iostream>

namespace work1
{
	int a = 1;

	void doSomething()
	{
		a += 3;
	}

}

namespace work2
{
	int a = 2;
	void doSomething()
	{
		a += 5;
	}
}

// ... //

	work1::a;
	work1::doSomething();

	work2::a;
	work2::doSomething();
```



`::` : scope resolution operator. 영역 충돌이 일어났을 때 해결해줌



### nested namespace

c++17에 추가된 기능



```cpp
namespace work1::work11::work111
{
	int a = 1;
	void doSomething()
	{
		a += 3;
	}

}

// ... //

	work1::work11::work111::doSomething();
```

work1 안에 work11을 만들고, 그 안에 work111을 또 만들어야 하는 수고를 덜 수 있다.

단 컴파일 버전 설정을 바꿔줘야 함 -> project properties -> C/C++ -> language -> C++17로 바꿔주기





## 4.2 전역 변수, 정적 변수, 내부연결, 외부연결

### 전역 변수, 지역 변수

```cpp
#include <iostream>

using namespace std;

int value = 123; // 전역 변수

int main()
{
	cout << value << endl; // 123
	int value = 1; // name hiding(shadowing)이 작동하여 전역 변수와 겹치지 않게 함
	cout << value << endl; // 1

	// 전역 영역 연산자
	cout << ::value << endl;

	return 0;
}
```



### 정적 변수 static variable

```cpp
void doSomething()
{
	int a = 1;
	++a;
	cout << a << endl;
}

```

계속 2를 출력



```cpp
int a = 1;

void doSomething()
{
	static int a = 1; // a = 1 value 할당 작업을 반복하지 않는다. but 맨 처음 초기화는 반드시 필요.
	++a;
	cout << a << endl;
}

```

전역 변수로 설정하거나, static으로 설정하면 2, 3, 4, 5로 늘어나는 것을 볼 수 있다.

static의 의미: 해당 변수가 메모리로부터 받은 주소가 static(정적)이라는 것. 함수 내의 지역 변수는 일반적으로 메모리 주소를 할당 받았다가 사라짐. static은 초기화를 한 번 밖에 안함. 계속 그 주소를 쓰는 것. 디버깅할 때 유용하다. 함수가 얼마나 호출되는지 출력할 때 좋다.

전역변수는 어디서나 값을 바꿀 수 있다. 여러 파일들에서 전역 변수에 접근한다면 관리를 하기 힘들다. 따라서 함수에 인자로 전역 변수를 전달해주든지, 전역 변수를 `g_a`등으로 지역 변수와 구분되게 명명하든지 해야 한다.

linking 단계에서 local variable끼리 연결해줄 필요는 없다. local variable은 해당 obj 파일 내에서만 사용되기 때문. 다른 파일에서 scope에 접근할 수 없다. -> local variable은 linkage가 없다.



### internal linkage

안에서 어디에서나 쓸 수 있음. 

```cpp
#include <iostream>

using namespace std;

static int g_a = 1;
```



### external linkage

전역 변수를 외부에서도 쓸 수 있게

일단 함수를 가져와서 쓰는 법을 보자.



#### test.cpp

```cpp
#include <iostream>

int b = 123;

void doSomething()
{
	using namespace std;

	cout << "Hello " << endl;
}
```



#### Chapter4_2.cpp

```cpp
//#include "test.cpp" // 가급적 사용하지 않음

// forward declaration
extern int b;
extern void doSomething(); // extern은 생략 가능. 어딘가 다른 파일에 있다는 것을 알려준다.
```

여기서도 `b=456` 등을 해버리면 multiply defined symbols 에러. 여러 번 정의한 것으로 인식된다.



헤더를 생성해보자.



#### MyConstants.h

```h
#pragma once // 이 header 파일을 중복으로 include 한 경우의 충돌을 막아줌

namespace Constants
{
	const double pi(3.141592);
	const double gravity(9.8);

}
```



#### main

```cpp
	cout << "In main.cpp file " << Constants::pi << " " << &Constants::pi << endl;
```



#### test

```cpp
	cout << "In test.cpp file " << Constants::pi << " " << &Constants::pi << endl; // 주소까지 출력
```

희한하게도 main과 test에서 주소가 다르게 나온다. 파일마다 다른 주소를 할당하면 낭비가 발생할 수 있음.



그렇다면 한 주소로 쓸 수 있게 해주자. cpp 파일을 생성

#### MyConstants.cpp

```cpp
namespace Constants
{
	extern const double pi(3.141592);
	extern const double gravity(9.8);
}
```



#### MyConstants.h

```h
#pragma once // 이 header 파일을 중복으로 include 한 경우의 충돌을 막아줌

namespace Constants
{
	// 헤더에서는 선언만 함
	extern const double pi;
	extern const double gravity;
}
```



이렇게 되면 같은 주소로 출력됨을 알 수 있다.



### 정리

```cpp
int g_x; // external linkage - 여러 개의 파일에서 접근 가능
static int g_x; // internal linkage - 다른 cpp 파일에서 접근이 불가능
const int g_x; // 이렇게 쓰면 안됨

extern int g_z;
extern const int g_z;

// 초기화까지 하는 경우
int g_y(1);
static int g_y(1);
const int g_y(1); // 외부에서 접근 불가능

extern int g_w(1);
extern const int g_w(1); // 외부에서도 접근 가능
```



- extern, static 헷갈리는 부분 다음 참조

  https://ccode.tistory.com/114











