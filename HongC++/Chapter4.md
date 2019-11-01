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





## 4.3 Using문과 모호성

```cpp
int main()
{
	//using namespace std;

	using std::cout; // namespace가 아니므로 표시해줄 필요가 없다.
	using std::endl;

	cout << "Hello " << endl;
	

	return 0;
}
```





```cpp
#include <iostream>

namespace a
{
	int my_var(10);
}

namespace b
{
	int my_var(20);
}


	using namespace a;
	using namespace b;

	cout << my_var << endl; // ambiguous 에러	
```



```cpp
	cout << a::my_var << endl;
	cout << b::my_var << endl;

	// 쓰지 않고 싶다면
	{
		using namespace a;
		cout << my_var << endl;
	}
	//cout << my_var << endl; // 이건 여전히 ambiguous
	{
		using namespace b;
		cout << my_var << endl;

	}
```

using namespace는 가급적 전역으로 하지 말 것. 나중에 프로젝트가 커지면 헷갈린다.

using namespace는 한번 선언하면 취소할 수 없을 것





## 4.4 auto 키워드와 자료형 추론 Type inference

자료형을 대입하는 값을 보고 알아서 넣어주는 키워드

```cpp
int main()
{
	using namespace std;

	auto a = 123;
	auto d = 123.0;
	auto c = 1 + 2;

	return 0;
}
```



```cpp
#include <iostream>

int add(int x, int y)
{
	return x + y;
}

int main()
{
	using namespace std;
    
	auto result = add(12, 2);

	return 0;
}
```



y를 double로 지정하면 함수의 return도 double로 바뀌게 됨

```cpp
#include <iostream>

int add(int x, int y)
{
	return x + (double)y;
}

int main()
{
	using namespace std;

	auto result = add(12, 2);

	return 0;
}
```

다만 함수의 인자로 auto를 정의할 수는 없다. 



```cpp
int add(int x, int y)
{
	return x + (double)y;
}

auto add(double x, double y)
{
	return x + y;
}
```

auto로는 쓸 수 없다. 개별적으로 정의해줘야 함. template에서 가능하지만 추후에 배울 것.

C++에서 여러 type의 return을 주는 것이 쉬워졌음.



### trailing return type

출력 타입을 표시해놓을 수도 있다

```cpp
auto add(int x, int y) -> int;
auto add(int x, int y) -> double;
```





## 4.5 형변환 Type conversion

```cpp
#include <iostream>
#include <typeinfo>

int main()
{
	using namespace std;

	int a = 123;
	cout << typeid(a).name() << endl; // int

	return 0;
}
```



### numeric promotion

```cpp

	float b = 1.0f;
	double d = b; // numeric promotion - 더 큰 type이 되면 문제가 없다.

	cout << typeid(a).name() << endl;

```



### numeric conversion

더 작은 size로 변환할 경우 문제가 발생할 수 있다.

```cpp
	int e = 30000;
	char f = e; // char에 들어가지 않는 큰 수 - signed면 127까지밖에 안됨.
	
	cout << static_cast<int>(f) << endl; // 48 이라는 엉뚱한 숫자 출력
```



```cpp
	double dd = 0.123456789;
	float f = dd;


	cout << std::setprecision(12) << f << endl; // 나름 최선을 다해 저장하지만 정밀도를 보장하지는 못한다.
```



### 암시적 형변환

float을 int로 바꿀 경우 버림을 한다.



```cpp
	cout << 5u - 10 << endl; // unsigned 5라는 뜻 - 엄청 큰 숫자가 뜸
```

우선순위 : int < unsigned int < long < unsigned long < long long < u long long < float < double < long double

-> unsigned int가 int로 안 바뀜



### 명시적 형변환(casting)

```cpp
	int ii = int(4.0); // c++ style. 
	ii = static_cast<int>(4.0); // c style
```





## 4.6 문자열 std string 소개

```cpp
#include <iostream>
#include <string>

using namespace std;

int main()
{
	const char my_strs[] = "Hello, World"; // 기본적인 방식. 한 글자가 배열의 한 칸
	//const string my_hello = "Hello, World"; // 편하라고 구현해낸 것. 사용자 정의 자료형
	const string my_hello{ "Hello, World" }; // 이렇게도 가능

	cout << "Hello, World" << endl;
    
	string my_ID = "123"; // 숫자는 이렇게
    
    

	return 0;
}
```



### 문자열 입력받기

```cpp
	cout << "Your name ? : ";
	std::string name;
	cin >> name;

	cout << "Your age ? : ";
	string age;
	cin >> age;

	cout << name << " " << age << endl;

```

여기서 스페이스바 등 빈칸을 넣어서 입력하면 나눠서 name, age에 들어감

이걸 막기 위해 getline을 쓸 수 있다.

```cpp
	cout << "Your name ? : ";
	std::string name;
	//cin >> name;
	std::getline(std::cin, name);

	cout << "Your age ? : ";
	string age;
	//cin >> age;
	std::getline(std::cin, age);

	cout << name << " " << age << endl;
```

\n이 나올 때까지 읽어들인다.



getline이 더 앞에 있는 것들까지 읽어들이게 될 수도 있다. 이 때는 앞에서 버퍼에 받아놨던 것을 날려줘야 함.

```cpp
	cout << "Your age ? : ";
	int age;
	cin >> age;

	std::cin.ignore(32767, '\n'); // 32767개의 글자를 무시해버려라. 2byte로 입력가능한 가장 긴 길이
```



32767을 직접 넣어주는 게 불편하다면

```cpp
#include <limits>

// ... //

std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
```



### 문자열 더하기

```cpp
	string a("Hello, ");
	string b("World");

	string hw = a + b; // append - 문자열 뒤에 더하기
	hw += "I'm good";

	cout << hw << endl;
```

더하기 연산자가 string 라이브러리에 제공되고 있어서 가능하다.



### 길이 측정

```cpp
	// 길이 측정
	string c("Hell, World");

	cout << c.length() << endl;
```





## 4.7 열거형 enumerated types

```cpp
#include <iostream>
#include <typeinfo>


int computeDamage(int weapon_id)
{
	if (weapon_id == 0) // sword
		return 1;

	if (weapon_id == 1) // hammer
	{
		return 2;
	}
}

int main()
{

	return 0;
}
```

이렇게 쓰면 무기마다 번호를 외우기가 쉽지 않다.



```cpp
enum Color
{
	COLOR_BLACK,
	COLOR_RED,
	COLOR_BLUE,
	COLOR_GREEN, // trailing comma 허용
}; // ; 필수

enum Feeling
{
	HAPPY,
	JOY,
	TIRED,
	BLUE, // 만약 위에서도 BLUE를 정의했으면 겹쳐서 컴파일 에러
};

int main()
{
	using namespace std;

	Color paint = COLOR_BLACK;
	Color house(COLOR_BLUE);
	Color apple{ COLOR_RED };

	cout << paint << ' ' << endl; // 0

	return 0;
}
```



값을 지정해줄 수도 있다. 오름차순으로 나머지는 설정됨

```cpp
enum Color
{
	COLOR_BLACK = -3,
	COLOR_RED,
	COLOR_BLUE = 5,
	COLOR_GREEN, // trailing comma 허용
}; // ; 필수


	cout << COLOR_BLACK << endl; // -3
	cout << COLOR_RED << endl; // -2
	cout << COLOR_BLUE << endl; // 5
	cout << COLOR_GREEN << endl; // 6
```

숫자 겹치게 설정하지 않도록 주의.



`int color_id = COLOR_RED` 가능하다.

`Color my_color = color_id`는 안된다. 변수를 쓰게 하도록 만들어져있지 않기 때문.

대신 `static_cast<Color>(3);`으로 하면 된다.



```cpp
	//cin >> my_color; // 안 된다
	int in_number;
	cin >> in_number;

	if (in_number == 0) my_color = COLOR_BLACK;
```



### string으로 입력받기

```cpp
	string str_input;

	std::getline(cin, str_input);

	if (str_input == "COLOR_BLACK") 
```





## 4.8 영역 제한 열거형(열거형 클래스) enum Class

```cpp
#include <iostream>

int main()
{
	using namespace std;

	enum Color
	{
		RED,
		BLUE
	};

	enum Fruit
	{
		BANANA,
		APPLE
	};

	Color color = RED;
	Fruit fruit = BANANA;

	cout << (color == fruit) << endl;

	return 0;
}
```



비교가 안 되게 막을 수 있다.

```cpp
int main()
{
	using namespace std;

	enum class Color
	{
		RED,
		BLUE
	};

	enum class Fruit
	{
		BANANA,
		APPLE
	};

	Color color1 = Color::RED;
	Color color2 = Color::BLUE;
	Fruit fruit = Fruit::BANANA;

	//cout << (color == fruit) << endl;
	cout << (color1 == color2) << endl;
	

	return 0;
}
```

static_cast로 int로 강제변환해서 비교할 수는 있다.

















