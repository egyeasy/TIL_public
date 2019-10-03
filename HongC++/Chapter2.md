## 2.1 기본 자료형 소개

변수의 주소는 계속 변한다. 어디로 할당될지 예측할 수 없다.

int : 4byte = 32bit -> int 변수를 하나 저장하는 데에 사용

char : 1byte = 8bit 사이즈

자료형의 종류마다 저장되는 형식, 용량이 다르다.



### 자료형 그룹

http://www.cplusplus.com/doc/tutorial/variables/

- Character types : char 등. 때에 따라 8비트가 아니라 16비트, 32비트로 쓰기도 함

- Integer types (signed) - signed char는 최소 8비트(문자여도 정수로 저장함. int를 저장할 수도 있다 -> int를 쓰고 있다면 출력할 때 int로 변환해서 출력해야 함) signed int는 최소 16비트. -> 최소 비트의 의미는 컴파일러에 따라서 용량을 다르게 설정 가능하다는 것.

- Integer types(unsigned) - 서로 저장하는 방식이 다름. unsigned가 특정 연산을 할 때 더 빠른 경우가 있음. unsigned 표시는 생략할 수 없음.
- Floating-point types - float, double, long double. 부동소숫점 표기 방식. 실수부와 지수부로 나누어서 저장. float는 32비트(4바이트)로 int와 같은 크기 사용.
- Boolean type - bool. True or False.
- Void type - void. storage가 없다. void pointer가 중요하게 사용됨.
- Null pointer



### 실습

- float은 숫자 뒤에 f를 붙여야 함 - f를 안 붙이면 double로 인식함. 더 정밀한 double을 float 변수에 할당하려고 하니까 truncated 된다고 warning이 뜸.
- float나 double은 생각보다 정밀하지 않다.
- 파이썬은 기본적으로 double을 씀. but 딥러닝은 float로 돈다 -> 오류가 생길 가능성 있음.
- modern c++에는 auto라는 게 생겼다. 



### auto

```cpp
auto aValue = 3.141592; // double로 자동 결정
auto aValue2 = 3.141592f; // float

cout << aValue << endl;
cout << aValue2 << endl;

cout << sizeof(aValue) << endl; // 8바이트
cout << sizeof(aValue) << endl; // 4바이트
```

sizeof의 파라미터에는 변수, 자료형 모두 넣을 수 있다.



### 초기화 방법 3가지

```cpp
bool bValue = false; // copy initialization
// 아래 두 개는 객체지향 때 중요
int a(123); // direct initialization
int b{ 123 }; // uniform initialization
```



```cpp
int i = 3.1415; // warning
int a(3.14); // warning
int b{4.5} // error
```



해결은 다음과 같이:

```cpp
// casting - 형 변환
int i = (int)3.1415;
int a((int)3.14);
int b{ 4 };
```



### 여러 개 동시 선언

```cpp
int k, l, m; // 같은 데이터형에서만 여러 개의 변수를 동시에 선언 가능
```

```cpp
int k = 0, l(456), m{ 123 };
```



예전의 C 컴파일러에서는 모든 변수를 제일 앞에서 선언했어야 했다.

최근에는 사용할 변수는 사용하기 직전에 사용하는 것을 선호 -> 코딩 스타일의 변화

사용하기 직전에 선언하면:

1. 디버깅을 하기가 좋다. 
2. refactoring하기가 편하다.





## 2.2 정수형, 코딩

char는 int는 문자열이든 1바이트 저장소.

integer short - 2바이트

int - 최소크기 2바이트. 대부분 4바이트를 사용

long - 4바이트

long long - 8바이트



### int

signed에서, 맨 처음 한 비트는 부호에 사용. unsigned integer는 항상 0 또는 양수



```cpp
#include <iostream>

int main(void)
{
	using namespace std;

	short	j = 1; // 2 bytes = 2 * 8 bits = 16 bits
	int		i = 1;
	long	l = 1;
	long long ll = 1;

	cout << sizeof(short) << endl;
	cout << sizeof(int) << endl;
	cout << sizeof(long) << endl;
	cout << sizeof(long long) << endl;

	// 표현할 수 있는 가장 큰 숫자
	cout << std::pow(2, sizeof(short) * 8 - 1) - 1 << endl; // 계산으로 구하기
	cout << std::numeric_limits<short>::max() << endl; // 존재하는 함수로 구하기
	cout << std::numeric_limits<short>::min() << endl;
	cout << std::numeric_limits<short>::lowest() << endl;
}
```



### overflow

범위에는 제한이 있고, 이를 넘어가면 문제가 발생한다.

```cpp
	short s = 32767;
	s = s + 1; // 32768을 기대

	cout << s << endl; // -32768을 출력
```

더하다가 최대범위를 넘어가면 가장 작은 숫자가 되어버림.



```cpp
	s = std::numeric_limits<short>::min();

	cout << "min() " << s << endl;

	s = s - 1;

	cout << " " << s << endl;
```

빼기도 마찬가지.



### unsigned integer

```cpp
	unsigned int i = -1;

	cout << i << endl;


	return 0;
```

엄청나게 큰 숫자가 나옴. 컴퓨터는 문제를 인지하지 못한다.



### 나눗셈

```cpp
	int k = 22 / 4;

	cout << k << endl;
```

5가 출력됨. 



```cpp
cout << 22 / 4 << endl;
cout << (float) 22 / 4 << endl; // 둘 중에 하나가 float이면 float로 계산하는 방법
```





## 2.3 C++ 11 고정 너비 정수 Fixed-width Integers

최소 사이즈만 규정하고 있기 때문에 컴파일러에 따라 자료형의 바이트가 다를 수 있다.

C++ 11부터는 어떤 플랫폼이든지 같은 양을 사용 - 고정 너비 정수



```cpp
#include <iostream>
//#include <cstdint> // iostream이 알아서 cstdint를 include함

int main(void)
{
	using namespace std;

	std::int16_t i(5); // 2바이트짜리 데이터타입으로 바꿔줌
	std:int8_t myint = 65; // 1바이트라서 integer가 아니라 char로 인식됨 -> 'A'가 출력된다.

	std::int_fast8_t fi(5); // 8비트 사이즈 중에 가장 빠른 데이터타입
	std::int_least64_t fl(5); // 적어도 8바이트를 갖는 데이터타입

	return 0;
}
```





## 2.4 무치형, 보이드, Void

```cpp

void my_function()
{

}

int main()
{
	// void my_void; // void는 메모리를 차지하지 않기 때문에 선언 불가
	int i = 123;
	float f = 123.456f;

	void* my_void; // 주소를 저장하는 것은 가능.

	my_void = (void*)&i;
	my_void = (void*)&f;

}
```

데이터 사이즈가 다르더라도, 저장하는 주소의 크기는 동일. 





## 2.5 부동소수점 수 Floating Point Numbers

1.0 x 10^2

### 부동소수점 Category

float - 4바이트

double - 8바이트

long double - 8, 12 or 16바이트



최근의 언어들은 double을 많이 사용함. but 숫자가 많을 경우엔 float을 씀. 파이썬은 기본적으로 double을 쓰지만 deep learning API는 float으로 짜여있을 수도.



- 부호(sign), 지수(exponent), 가수(maintissa)로 구성



### 실습

```cpp
#include <iostream>
#include <iomanip>

int main()
{
	using namespace std;

	float f;
	double d;
	long double ld;

	cout << sizeof(f) << endl; // 4
	cout << sizeof(d) << endl; // 8
	cout << sizeof(ld) << endl; // 8

	return 0;
}
```





```cpp
	cout << numeric_limits<float>::max() << endl;
	cout << numeric_limits<double>::max() << endl;
	cout << numeric_limits<long double>::max() << endl;


	cout << numeric_limits<float>::lowest() << endl;
	cout << numeric_limits<double>::lowest() << endl;
	cout << numeric_limits<long double>::lowest() << endl;
```

min() 대신에 lowest()를 써야 한다.



```cpp
	float f(3.141592f);
	double d(3.141592);
	long double ld(3.141592);

	cout << 3.14 << endl;
	cout << 31.4e-1 << endl;
	cout << 31.4e1 << endl;
```

숫자가 큰 경우에는 지수부를 따로 두는 것이 좋다.



```cpp
	cout << std::setprecision(16); // 16번째 자리 수까지 출력하도록 조절(iomanip library)
	cout << 1.0 / 3.0 << endl;
```



but 오차를 좀 다르게 처리하기 때문에 이상한 결과도 나옴

```cpp
	f = 123456789.0f;
	cout << f << endl;
```



double은 메모리에서 cpu로 보낼 때도 부담이 되는 등으로 꼭 이득인 것은 아니다. 장기적으로는 double로 가게 될 것 같다.



```cpp
	d = 0.1;
	cout << d << endl;
	cout << std::setprecision(17);
	cout << d << endl; // 마지막에 1이 붙음 - 완전히 정확하게 0.1을 표현할 수 없다.
```



```cpp
	double d1(1.0);
	double d2(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1);

	cout << setprecision(17);

	cout << d1 << endl; // 1
	cout << d2 << endl; // 0.99999999999999
```





```cpp
	double zero = 0.0;
	double posinf = 5.0 / zero;
	double neginf = -5.0 / zero;
	double nan = zero / zero;

	cout << posinf << endl;
	cout << neginf << endl;
	cout << nan << endl; // ind는 indefinited - 정해지지 않았다.
```



### isnan

cmath include

계산하는 값이 infinite인지 아닌지 확인해보도록 하자.

```cpp
	cout << posinf << " " << std::isnan(posinf) << endl;
	cout << neginf << " " << std::isnan(neginf) << endl;
	cout << nan << " " << std::isnan(nan) << endl;
	cout << 1.0 << " " << std::isnan(1.0) << endl;
```





## 2.6 불리언 자료형과 조건문 if

```cpp
#include <iostream>

int main()
{
	using namespace std;

	bool b1 = true; // copy initialization
	bool b2(false); // direct
	bool b3{ true }; // uniform
	b3 = false;

	cout << b3 << endl;
	cout << b1 << endl;

	return 0;
}
```



```cpp
	cout << std::boolalpha;
	cout << b3 << endl;
	cout << b1 << endl;
```

true, false로 출력 가능



### not 연산자

```cpp
	cout << !true << endl;
	cout << !false << endl;
```



### 논리 연산자

기호 두 개 써야하는 거 명심할 것

```cpp
	cout << std::noboolalpha;
	cout << (true && true) << endl;
	cout << (true && false) << endl;
	cout << (false && true) << endl;
	cout << (false && false) << endl;

	cout << (true || true) << endl;
	cout << (true || false) << endl;
	cout << (false || true) << endl;
	cout << (false || false) << endl;
```



### 조건문

두 줄 이상일 때에는 중괄호로 싸야한다.

0이면 false, 나머지는 모두 true로 인식한다.

```cpp
	if (true)
		cout << "This is true " << endl;
	else
		cout << "This is false " << endl;
```



```cpp
bool isEqual(int a, int b)
{
	bool result = (a == b);

	return result;
}

	cout << std::boolalpha;
	cout << isEqual(1, 1) << endl;
	cout << isEqual(0, 3) << endl;
```



```cpp
	bool b;
	cin >> b;
	cout << std::boolalpha;
	cout << "Your input: " << b << endl;
```

컴파일러마다 결과가 다르게 나올 수도.



## 2.7 문자형 char type

- escape sequence

- 문자 하나를 표현할 때는 작은 따옴표, 열을 표현할 때는 큰 따옴표



```cpp
#include <iostream>

int main()
{
	using namespace std;

	char c1(65);
	char c2('A'); // "Hello, World"

	cout << c1 << " " << c2 << " " << int(c1) << " " << int(c2) << endl;
    
	return 0;
}
```



### casting

```cpp
	// c-style casting
	cout << (char)65 << endl;
	cout << (int)'A' << endl;

	// cpp style
	cout << char(65) << endl;
	cout << int('A') << endl;

	//static cast
	cout << static_cast<char>(65) << endl;
	cout << static_cast<int>('A') << endl;
```

두 번째 세 번째는 기능적으로 같다. static cast는 dynamic cast랑 대비되는 것.



static cast를 해도 원래 변수의 값이 변하지는 않는다

```cpp
	char ch(97);
	cout << ch << endl;
	cout << static_cast<int>(ch) << endl;
	cout << ch << endl;
```



문자를 쳐보면 해당하는 int 변환값을 알 수 있다.

```cpp
	cin >> c1;
	cout << c1 << " " << static_cast<int>(c1) << endl;

	cin >> c1;
	cout << c1 << " " << static_cast<int>(c1) << endl;
```

두 번 받았을 때 abc를 입력하면 a와 b가 하나씩 들어간다.



```cpp
	cout << sizeof(char) << endl;
	cout << std::numeric_limits<char>::max() << endl;
	cout << std::numeric_limits<char>::lowest() << endl;
```

이렇게 하면 콘솔창에서 출력할 수 없는 문자가 나옴. int로 바꿔서 표현해주자.



```cpp
	cout << sizeof(char) << endl;
	cout << (int)std::numeric_limits<char>::max() << endl;
	cout << (int)std::numeric_limits<char>::lowest() << endl;
```





### \n vs endl

\n은 그 다음 문자를 버퍼에 넣음. 혹시나 문자가 출력이 되지 않을 수 있다.

endl은 버퍼에 있는 것도 출력하라는 명령을 포함함. 이 점이 차이.

std::flush는 버퍼에 있는 걸 다 쏟고 줄바꿈은 하지 않음.

```cpp
	cout << int('\n') << endl;
	cout << "This is first line \nsecond line";
	cout << "This is first line " << endl;
	cout << "second line";
```



### 탭

```cpp
	cout << int('\t') << endl;
	cout << "This is first line \tsecond line ";
```



### 큰 따옴표

```cpp
	cout << "This is first line \tsecond line \"";
```



### 사운드

`\a`



### wchar_t

윈도우 프로그램에서 씀. 골치아픈 점이 있다.



### char32_t

이모티콘 등 유니코드의 문자들을 쓸 수 있음.





## 2.8 리터럴 상수 literal constants

```cpp
#include <iostream>

int main()
{
	using namespace std;

	float pi = 3.14f; // long double일 경우에는 l을 씀
	int i = 12324u;

	return 0;
}
```

접미사는 f, l, u 등이 있다. u는 unsigned

`(unsigned int) 12342`라고 명시하는 방법도 있다.



```cpp
	unsigned int n = 5u;
	long n2 = 5L;
	double d = 6.0e-10;
```



### 팔진수

Octal : 0 1 2 3 4 5 6 7 10 11 12 13

Hexa : 0 1 2 3 4 5 6 7 8 9 A B C D E F 10 11 12 13



팔진수는 앞에 0을 붙여서 표기.

```cpp
	int x = 012; // 8진수를 의미
	cout << x << endl;
```



16진수는 0x를 붙인다.

```cpp
	x = 0xF;
	cout << x << endl;
```



이진수가 0011 1010 1111 1111 등으로 나열되어 있으면 읽기 불편

이를 16진수로 압축해서 표현



C++14부터 binary literal이 가능해짐

```cpp
	x = 0b1010;
	cout << x << endl;

	x = 0b'1010;
	cout << x << endl;

	x = 0b1010'1111; // 구분자로 '를 쓰는 것을 허용(컴파일러가 무시)
	cout << x << endl;
```



리터럴 상수를 코드에 넣어놓는 경우가 있다.

```cpp
int num_items = 123;
int price = num_items * 10;
```

magic number 10이 눈에 잘 안들어옴. 반복해서 써야할 수도.



따라서 symbolic 상수를 사용함

```cpp
	const int price_per_item = 10;

	int num_items = 123;
	int price = num_items * price_per_item;
```





## 2.9 심볼릭 상수 symbolic constants

나중에 값을 바꿀 수 없도록 고정시켜놓는 역할.

순서는 상관없지만 const를 자료형보다 앞에 붙이는 편.

const는 처음에 값을 반드시 넣어줘야 함.

```cpp
#include <iostream>

int main()
{
	using namespace std;

	const double gravity{ 9.8 };

	// gravity = 1.2; // 값을 바꿀 수 없다.

	return 0;
}
```





### const parameter

```cpp
void printNumber(const int my_number)
{
	// my_number = 456; // 입출력을 알아보기 힘들게 만드므로 방지하는 편
	int n = my_number; // 변경하고자 한다면 복사해서 쓴다.

	cout << my_number << endl;
}


	printNumber(123);
```



### 컴파일 타임 vs 런타임

```cpp
	const int my_const(123); // 컴파일 타임 상수
	
	int number;
	cin >> number;

	const int special_number(number); // 런타임 상수 - 실행이 되어야 정해짐
```



### constexpr

컴파일 타임에 결정되는 것을 명시해주는 새로운 문법

```cpp
	const int my_const(123); // 컴파일 타임 상수
	constexpr int my_const2(123);

	int number;
	cin >> number;

	const int special_number(number); // 런타임 상수 - 실행이 되어야 정해짐
	// constexpr int special_number(number); // 이렇게 쓸 수 없다
```



### 상수 매크로

```cpp
#define PRICE_PER_ITEM 30

// 밑에서 사용
```

C++에서는 이런 방식으로 상수를 쓰지 않음. C의 잔재

1. 디버깅이 힘들다.
2. 상수의 적용 범위가 너무 넓다.



```cpp
	const int price_per_item = 30;

	int num_item = 123;
	int price = num_item * price_per_item;
```

이렇게 쓰는 것이 바람직.



### MY_CONSTANTS.h

나중엔 price_per_item이 변화해야할 수도 있다. 대문자로 바꿔놓으면 나중에 헷갈린다. 이를 처리하는 방법

```h
#pragma once

namespace constants
{
	constexpr double pi(3.141592);
	constexpr double avogadro(6.0221413e23);
	constexpr double moon_gravity(9.8 / 6.0);
}

```

이렇게 상수 헤더 파일을 만들고 모아놓는 것이 좋다.



```cpp
#include <iostream>
#include "MY_CONSTANTS.h"


	double radius;
	cin >> radius;

	double circumference = 2.0 * radius * constants::pi;
```

헤더 파일은 다른 곳에서도 쓸 수 있으므로 재사용성이 좋아진다.























