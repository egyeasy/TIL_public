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











































