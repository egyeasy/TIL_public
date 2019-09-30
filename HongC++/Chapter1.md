# 1.1 프로그램의 구조

프로그램을 실행한다는 건 OS에 이걸 실행해달라고 요청하는 것.

요청하면 OS가 CPU와 메모리를 사용해서 프로그램을 실행하게 됨.

코드에는 함수가 있다 : 내부적으로 무언가를 해서 결과를 내놓는 것.

`main()`이라는 이름의 함수는 이름을 바꿀 수 없다 - OS가 프로그램을 실행할 때 main을 가장 먼저 찾는다. 기능을 수행하는 프로그램에 main은 반드시 있어야 함! 

빈 칸이나 빈 줄은 컴파일러가 무시한다. 사람이 편하려고 넣는 것.

함수 input의 `void`는 아무 것도 들어가지 않는 것을 의미.

- `return`(return statement)은 돌려주는 것을 의미. `return 0;` : OS에 0을 돌려준다.
- `;` (semi-colon)은 문장의 끝을 이걸로 표시. 반드시 있어야 함.



```cpp
int main(void)
{
	1 + 1; // expression

	int x; // integer라는 정수형의 데이터를 담을 수 있는 메모리 공간을 할당.

	return 0; // 명령문
}
```

`x`라는 이름으로 해당 메모리 공간을 사용할 수 있다.



```cpp
int main(void)
{
	1 + 1; // expression

	int x = 2; // integer라는 정수형의 데이터를 담을 수 있는 메모리 공간을 할당.
	x = 5;
	int y = x + 3;

	return 0;
}
```

2, 3, 5 등 변수에 대입하는 값을 **literal**이라고 부른다.



```cpp
include <iostream> // preprocessor directive(전처리기)

int main(void)
{
	1 + 1; // expression

	int x = 2; // integer라는 정수형의 데이터를 담을 수 있는 메모리 공간을 할당.
	x = 5;
	int y = x + 3;

	std::cout << y << std::endl;
	std::cout << 1 + 2 << std::endl;

	return 0;
}
```

std는 namespace. 여러 함수들을 묶어서 넣어놓음.

`<<`는 stream or output operator(연산자)라고 부른다.

std는 standard library. C++를 설치하면 자동으로 설치되게 된다. 마찬가지로 나만의 라이브러리를 만들어서 가져다 쓸 수 있다.





# 1.2 주석(Comments)

컴파일러 상에서 특정한 부분을 무시하게 만드는 것.



```cpp
#include <iostream> // preprocessor directive(전처리기)

int main(void)
{
	1 + 1; // expression

	int x = 2; // integer라는 정수형의 데이터를 담을 수 있는 메모리 공간을 할당.
	//x = 5;
	int y = x + 3;

	/*std::cout << y << std::endl;
	std::cout << 1 + 2 << std::endl; */

	return 0;
}
```

한줄만 / 영역 주석 처리 방법이 있다.

영역 주석 처리 시에 중복 범위 지정에 주의할 것.

* VS에서 `ctrl+k ctrl+c`로 주석처리 가능



```cpp
/*
	This is my program.
	Written by me
*/

#include <iostream> // preprocessor directive(전처리기)

int main(void)
{
}
```

와 같이 코드를 소개하는 주석을 달 수도 있다.



이틀만 지나도 자신이 쓴 코드를 잘 기억하지 못하게 됨. 이를 기억하기 위해 주석을 단다.

ex) 어떤 논문에서 가져왔다. 수학식은 ~~다. 등

```cpp
#include <iostream> // preprocessor directive(전처리기)

int main(void)
{
	1 + 1; // expression

	int x = 2; // integer라는 정수형의 데이터를 담을 수 있는 메모리 공간을 할당.
	//x = 5;
	int y = x + 3;
	
	// 1. ...
	// 2. ...
	std::cout << y << std::endl;
	std::cout << 1 + 2 << std::endl;

	return 0;
}
```

가독성을 위해 위에 다는 것을 추천.





# 1.3 변수와의 첫 만남

- 객체(objects) - 메모리에 담겨 있다.

- 변수(variables) - 객체가 메모리에 담겨 있는데, 변수를 통해 그 객체에 접근할 수 있다. 프로그래머가 숫자로 된 주소를 이해하기가 어렵기 때문에, 이름을 달아주는 것.
- Left-values / Right-values : 사용자가 메모리에 직접적으로 접근할 수 있느냐 / 없느냐가 가장 큰 차이 지점이 됨.



```cpp
#include <iostream>

int main(void)
{
	// 1.3 변수와의 첫 만남
	int x = 123; // = : assignment operator
    
    std::cout << x << std::endl;

	return 0;
}
```

"x라는 이름을 가진 주소에 123을 저장한다."



`std::cout << &x << std::endl;` : 변수 x의 주소를 출력



```cpp
#include <iostream>

int main()
{
	int x = 123; // = : assignment operator
	x = x + 2; // x = 123 + 2;

	std::cout << &x << std::endl;
}
```

우측의 x는 123을 불러오고, 연산을 해서 x에 대입한다.



### Debug vs Release

Debug 모드에는 디버그에 필요한 요소들이 들어있음 -> 실행파일 용량이 크고 속도가 느림.

배포할 때는 반드시 release 모드를 쓸 것.



```cpp
#include <iostream>

int main()
{
	int x; // = : assignment operator

	std::cout << x << std::endl;

	return 0;
}
```

C++ runtime error : c++이 어렵다고 느끼게 만드는 가장 큰 이유 -> 메모리에 접근할려고 하는데 잘못 해서 OS에서 경고해주는 것.



```cpp
#include <iostream>

int main()
{
	int x; // = : assignment operator

	std::cout << x << std::endl;

	return 0;
}
```

(주의!) release 모드에서는 실행할 때 디버그 모드와 다르게 알아서 0을 대입해주는 등으로 컴파일러가 자의적으로 보충 작업을 수행하는 경우도 있음. 이렇게 쓸모 없게 대입된 값을 쓰레기(garbage) 값이라고 부른다.





### initialization vs assignment

`int x = 123` : initialization. x가 생길 때 바로 123을 넣어버린다. `int x(123)`도 거의 동일.

`x = 5` : assignment





# 1.4 입출력 스트림과의 첫 만남 cin, cout

### 출력

```cpp
#include <iostream>
#include <cstdio>

int main()
{
	int x = 1024;
	double pi = 3.141592;

	std::cout << "I love this lecture!";
	std::cout << "x is " << x << " pi is " << pi << std::endl;

	std::cout << "abc" << "\t" << "def" << std::endl;
	std::cout << "ab" << "\t" << "cdef" << std::endl;

	return 0;
}
```

`\t`는 글자 간 간격을 알아서 조절해주는 탭이다.

`\n`도 줄바꿈에 해당



`std::`를 쓰기 귀찮다면

```cpp
#include <iostream>
#include <cstdio>

int main()
{
	using namespace std;

```



다음은 오디오를 출력

```cpp
cout << "\a";
```





### 입력받기

입력받은 데이터를 저장할 수 있는 변수를 미리 선언해야 한다.





# 1.6 키워드와 식별자 이름짓기

cpp의 키워드 = 예약어(reserved)

변수명, 함수명을 지을 때 해당 이름을 사용하면 안 됨.

`n_apples`와 같이 언더스코어를 사용하여 단어끼리 분리하는 경우가 많다.





# 1.7  지역 범위

```cpp
#include <iostream>

int main()
{
	int x = 0;

	{
		int x = 1;
	}

	{
		int x = 2;
	}
}
```

이게 가능하다. main 함수 중괄호 안에 다른 중괄호가 있으면 서로 다른 공간이 됨 -> 다른 메모리에 대한 식별자.



```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 0;
	cout << x << " " << &x << endl;

	{
		int x = 1;
		cout << x << " " << &x << endl;
	}

	{
		int x = 2;
		cout << x << " " << &x << endl;
	}
}
```

첫번째 `&x`와 두번째 `&x`는 서로 다르다.



```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 0;

	cout << x << " " << &x << endl;

	{
		//int x = 1;
		x = 1;
		cout << x << " " << &x << endl;

	}

	cout << x << " " << &x << endl;

}
```

모두 같은 주소를 반환한다.





과제 : 다음 코드는 무엇을 반환하는가?

```cpp
#include <iostream>

using namespace std;

void doSomething(int x)
{
	x = 123;
	cout << x << endl; // #2
}


int main()
{
	int x = 0;

	cout << x << endl; // #1
	doSomething(x);
	cout << x << endl; // #3

	return 0;

}
```





# 1.8 연산자와의 첫 만남

```cpp
#include <iostream>

using namespace std;

int main()
{
	int x = 2;  // x is a variable, 2 is a literal.

	cout << x + 2 << endl; // + is an operator, x and 2 are 피연산자

	cout << "adfewf" << endl;

	return 0;
}
```



단항 연산자: `-x`, `-2`

이항 연산자: `1 + 2`

삼항 연산자 - 조건 연산자로, C++ 언어의 유일한 삼항 연산자.

```cpp
int y = (x > 0) ? 1 : 2;
```

참이면 왼쪽, 거짓이면 오른쪽





# 1.9 기본적인 서식 맞추기

- 코드 정리는 프로그래머의 효율을 위해서 하는 것. 컴퓨터는 여백을 인식하지 않는다.
- 다닥다닥 붙어있는 코드를 잘라내기해서 붙여넣기 하면 VS가 알아서 고쳐준다.







# 1.10 선언과 정의의 분리

 함수가 있다는 것을 main 함수 상단에서 미리 알려준다.

```cpp
#include <iostream>

using namespace std;

int add(int a, int b); // forward declaration
int multiply(int a, int b);
int subtract(int a, int b);

int main()
{
	cout << add(1, 2) << endl;

	return 0;
}


// definition
int add(int a, int b)
{
	return a + b;
}

int mulitply(int a, int b)
{
	return a * b;
}

int subtract(int a, int b)
{
	return a - b;
}
```





# 1.11 헤더파일 만들기

## 방법 1

### main.cpp

```cpp
#include <iostream>

using namespace std;

int add(int a, int b);

int main()
{
	cout << add(1, 2) << endl;

	return 0;
}

```



### add.cpp

```cpp

int add(int a, int b)
{
	return a + b;
}
```





## 방법 2

Header 파일 `add.h` 추가

### main.cpp

```cpp
#include <iostream>
#include "add.h"

using namespace std;

int main()
{
	cout << add(1, 2) << endl;

	return 0;
}
```



### add.h

```h
#pragma once

int add(int a, int b);
```



### add.cpp

```cpp
int add(int a, int b)
{
	return a + b;
}
```



Header를 다른 데로 옮기고 싶다면?

MyHeaders 폴더를 만들어서 add.h를 그 안으로 옮긴다면

### main.cpp

```cpp
#include "MyHeaders/add.h"
```

로 include 하면 된다.



### Linking 에러

VS에서 remove 명령어는 디렉토리에서 삭제하지 않지만 VS에게 인식하지 못하게 하는 것.

add.h를 remove 하면 Linking error가 발생하게 된다.(`unresolved external symbol`)

declaration과 definition을 분리했기 때문에 이런 에러가 발생한다.





# 1.12 헤더 가드가 필요한 이유

헤더 파일의 `#pragma once`가 헤더 가드.

예제에서는 헤더파일에 정의까지 집어넣도록 해보자 -> 이럴 때 문제가 발생하는데 헤더가드가 그 문제를 방지해줌.



### add.h

```h
//#pragma once

int add(int a, int b)
{
	return a + b;
}
```



### my_work.h

```h
//#pragma once

#include "add.h"

void doSomething()
{
	add(1, 2);
}
```



### main.cpp

```cpp
#include <iostream>
#include "my_work.h"
#include "add.h"

using namespace std;

int main()
{
	doSomething();

	return 0;
}
```



위와 같이 두 번 add.h를 불러왔을 때 컴파일 에러가 발생한다 -> 중복 되면 한 번만 불러오도록 설정해보자



### add.h

```h
//#pragma once

#ifndef MY_ADD
#define MY_ADD

int add(int a, int b)
{
	return a + b;
}

#endif
```



### add.h

이게 번거롭다면 pragma once를 사용

똑같이 작동한다.



```h
#pragma once

//#ifndef MY_ADD
//#define MY_ADD

int add(int a, int b)
{
	return a + b;
}

//#endif
```





# 1.13 네임스페이스 명칭 공간

### main.cpp

```cpp
#include <iostream>

int doSomething(int a, int b)
{
	return a + b;
}

int doSomething(int a, int b)
{
	return a * b;
}

int main(void)
{

	return 0;
}
```

이는 컴파일 에러 발생. namespace로 구분해보자.



```cpp
#include <iostream>

namespace MySpace1
{
	int doSomething(int a, int b)
	{
		return a + b;
	}
}

int doSomething(int a, int b)
{
	return a * b;
}

using namespace std;

int main(void)
{
	cout << MySpace1::doSomething(3, 4) << endl;
	cout << doSomething(3, 4) << endl;

	return 0;
}
```



다음과 같이 namespace를 생략할 수 있다.

```cpp
#include <iostream>

namespace MySpace1
{
	int doSomething(int a, int b)
	{
		return a + b;
	}
}

namespace MySpace2
{
	int doSomething(int a, int b)
	{
		return a * b;
	}
}

using namespace std;

int main(void)
{
	using namespace MySpace1;

	doSomething(3, 4);

	//cout << MySpace1::doSomething(3, 4) << endl;
	//cout << MySpace2::doSomething(3, 4) << endl;

	return 0;
}
```



namespace 중복도 가능

```cpp
#include <iostream>

namespace MySpace1
{
	namespace InnerSpace
	{
		int doSomething(int a, int b)
		{
			return a + b;
		}
	}
}

namespace MySpace2
{
	int doSomething(int a, int b)
	{
		return a * b;
	}
}

using namespace std;

int main(void)
{
	using namespace MySpace1::InnerSpace;

	//cout << MySpace1::doSomething(3, 4) << endl;
	//cout << MySpace2::doSomething(3, 4) << endl;

	doSomething(3, 4);


	return 0;
}
```





# 1.14 전처리기와의 첫 만남

define - 전처리기. 미리 정의해서 쓸 수 있는 일종의 매크로

```cpp
#include <iostream>
using namespace std;

#define MY_NUMBER 333

int main()
{
	cout << MY_NUMBER << endl;

	return 0;
}
```



```cpp
#include <iostream>
using namespace std;

#define MY_NUMBER 333
#define MAX(a, b) ((a>b) ? a : b) // 괄호로 싸야 한다.

int main()
{
	cout << MY_NUMBER << endl;
	
	cout << MAX(1, 2) << endl;


	return 0;
}
```



이렇게 하는 걸 추천

```cpp
#include <iostream>
using namespace std;

#define MY_NUMBER 333
#define MAX(a, b) (((a)>(b)) ? (a) : (b)) // 괄호로 싸야 한다.

int main()
{
	cout << MY_NUMBER << endl;
	
	cout << MAX(1 + 3, 2) << endl;


	return 0;
}
```



라이브러리를 써서 max를 표현할 수도 있다.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

#define MY_NUMBER 333
#define MAX(a, b) (((a)>(b)) ? (a) : (b)) // 괄호로 싸야 한다.

int main()
{
	cout << MY_NUMBER << endl;
	
	cout << MAX(1 + 3, 2) << endl;
	cout << max(1 + 3, 2) << endl;


	return 0;
}
```





### Conditional Compilation

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

#define MY_NUMBER 333
#define MAX(a, b) (((a)>(b)) ? (a) : (b)) // 괄호로 싸야 한다.

#define LIKE_APPLE

int main()
{
	cout << MY_NUMBER << endl;
	
	cout << MAX(1 + 3, 2) << endl;
	cout << max(1 + 3, 2) << endl;

#ifdef LIKE_APPLE
	cout << "Apple " << endl;
#endif

#ifndef LIKE_APPLE
	cout << "Orange " << endl;
#endif

	return 0;
}
```

VS가 LIKE_APPLE이 정의되어있는 것을 인식하고 ifndef 부분을 흐리게 표시해준다. 빌드할 때부터 이 여부를 인식해서 빌드 -> windows인지 linux인지 인지하고 컴파일을 해야할 때 자주 쓰게 됨



define의 효력은 해당 파일 안에서만 적용됨.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

#define MY_NUMBER 333
#define MAX(a, b) (((a)>(b)) ? (a) : (b)) // 괄호로 싸야 한다.

#define LIKE_APPLE

void doSomething()
{
#ifdef LIKE_APPLE
	cout << "Apple " << endl;
#endif

#ifndef LIKE_APPLE
	cout << "Orange " << endl;
#endif
}

int main()
{
	cout << MY_NUMBER << endl;
	
	cout << MAX(1 + 3, 2) << endl;
	cout << max(1 + 3, 2) << endl;

	doSomething();

	return 0;
}
```



doSomething 함수를 다른 파일로 옮기면 Orange가 출력되게 된다. APPLE 정의가 main 함수 안에서만 효력이 있기 때문.

* using namespace std는 개별 함수 안에서 불러주는 것을 추천

















