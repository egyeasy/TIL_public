## 5.1 제어 흐름 개요 Control flow

### 순서도 Flow Chart

제어 흐름을 나타낼 때 많이 사용

중단, 점프(Jump), 조건 분기, 반복, 예외 처리



### 중단

```cpp
#include <iostream>
#include <cstdlib>

int main()
{
	std::cout << "I love you " << std::endl;

	// return 0;
	
	exit(0); //  return보다 급하게 나가는 것. 코드에 어디에 있든지 정수 하나만 넣어주면 종료 가능. 프로그램이 절대로 무조건 종료되어야 할 경우.



	std::cout << "I love you, too" << std::endl;

	return 0;
}
```





## 5.2 조건문 if





## 5.3 switch-case

```cpp
#include <iostream>

using namespace std;

enum class Colors
{
	BLACK,
	WHITE,
	RED,
	GREEN,
	BLUE
};

void printColorName(Colors color)
{
	if (color == Colors::BLACK)
		cout << "Black" << endl;
	else if (color == Colors::WHITE)
		cout << "White" << endl;
	else if (color == Colors::RED)
		cout << "Red" << endl;
}
```

if문으로 쓰면 귀찮아진다



```cpp
int main()
{
	//printColorName(Colors::BLACK);

	int x;
	cin >> x;

	switch (x)
	{
	case 0:
		cout << "Zero";
	case 1:
		cout << "One";
	case 2:
		cout << "Two";
	}

	cout << endl;
}
```

0을 입력하면 zeroonetwo 모두 출력. 1을 입력하면 OneTwo

그래서 break를 쓰면 된다.



```cpp
int main()
{
	//printColorName(Colors::BLACK);

	int x;
	cin >> x;

	switch (x)
	{
	case 0:
		cout << "Zero";
		break;
	case 1:
		cout << "One";
		break;
	case 2:
		cout << "Two";
		break;
	}

	cout << endl;
}
```



printColor에 적용해보자.

```cpp
void printColorName(Colors color)
{
	switch (color)
	{
	case Colors::BLACK:
		cout << "Black";
		break;
	case Colors::WHITE:
		cout << "White";
		break;
	case Colors::RED:
		cout << "Red";
		break;
	}
}
```



일일이 컬러를 쓰기 귀찮다면

```cpp
	switch (static_cast<int>(color))
	{
	case 0:
		cout << "Black" << endl;
	case 1:
		cout << "White" << endl;
		break;
	case 2:
		cout << "Red" << endl;
		break;
	}
```



### 주의할 점

```cpp
	switch (x)
	{
		int a;		// 변수 선언을 할 수 있다.
		int b = 5;	// but case문 안에서는 변수 할당을 할 수 없다. 그 이후에는 가능.
	}

	switch (x)
	{
		int a;
	case 0:
		int y;
		break;

	case 1:
		y = 5;		// case 0을 지나지 않으면 선언이 되지 않는 것이 문제.
		cout << y << endl;
	}

	// 헷갈리면 case도 block으로 싸면 됨

	switch (x)
	{
	case 0:
	{
		int y = 5;
		y = y + x;
	}
    default:
		cout << "Undefined input" << x << endl;
	}
```

default문은 보통 맨 아래에 오므로 break가 필요하지 않다. 실수를 줄이려고 break를 쓰기도 함.





## 5.4 goto

```cpp
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
	double x;


tryAgain : // label - 이름표
	cout << "Enter a non-negative number" << endl;

	cin >> x;

	if (x < 0.0)
		goto tryAgain;

	cout << sqrt(x) << endl;

}
```

비쥬얼베이직에서는 goto를 많이 씀. goto문을 악마처럼 묘사하는 글들도 있음. 요즘 거의 안 쓰임.



```cpp
	goto skip;

	int x = 5;
skip:
	
	x += 3;
```

x를 선언하지 않고 뛰어넘어가서 에러 발생.



## 5.5 반복분 while



## 5.6 반복문 do while

한번은 꼭 실행하고 while

```cpp
#include <iostream>

using namespace std;

int main()
{
	int selection; 

	do
	{
		// int selection // do 안에 선언해버리면 while에서 접근 불가.
		cout << "1. add" << endl;
		cout << "2. sub" << endl;
		cout << "2. sub" << endl;
		cout << "2. sub" << endl;
		cin >> selection;
	} while (selection <= 0 || selection >= 5); // ; 필수

	cout << "You selected " << selection << endl;
}
```





## 5.7 반복문 for

```cpp
for (int i = 0, j = 0; (i + j) < 10; ++i, j += 2)
{
    cout << i << ' ' << j << endl;
}
```

변수 두 개를 쓸 수도 있다.





## 5.9 난수 만들기 random numbers

먼저 어떤 원리로 작동하는지 보자

```cpp
#include <iostream>

using namespace std;

unsigned int PRNG() // Pseudo Random number generator
{
	static unsigned int seed = 5523; // seed number

	seed = 8253729 * seed + 2396403; // 반복적으로 바꾸기 위해 static 변수 사용

	return seed % 32768;
}

int main()
{
	for (int count = 1; count <= 100; ++count)
	{
		cout << PRNG() << "\t";

		if (count % 5 == 0) cout << endl;

	}
}
```



### rand 라이브러리

```cpp
#include <cstdlib> // std::radn(), std::srand()


int main()
{
	for (int count = 1; count <= 100; ++count)
	{
		//cout << PRNG() << "\t";
		cout << std::rand() << "\t";

		if (count % 5 == 0) cout << endl;

	}
}
```





### time을 이용한 seed 주입

```cpp
#include <iostream>
#include <cstdlib> // std::radn(), std::srand()
#include <ctime> // std::time()

using namespace std;

unsigned int PRNG() // Pseudo Random number generator
{
	static unsigned int seed = 5523; // seed number

	seed = 8253729 * seed + 2396403; // 반복적으로 바꾸기 위해 static 변수 사용

	return seed % 32768;
}

int main()
{
	//std::srand(5323);
	std::srand(static_cast<unsigned int>(std::time(0)));
	for (int count = 1; count <= 100; ++count)
	{
		//cout << PRNG() << "\t";
		cout << std::rand() << "\t";

		if (count % 5 == 0) cout << endl;

	}
}
```





### 범위 사이의 정수

```
int getRandomeNumber(int min, int max)
{
	static const double fraction = 1.0 / (RAND_MAX + 1.0);

	return min + static_cast<int>((max - min + 1) * (std::rand() * fraction));
}

```



다음과 같이 할 수도 있다

```cpp
cout << rand() % 4 + 5 << "\t";
```

정밀하게 하고자 하는 경우 random library를 쓰는 게 좋다(C++)



### random 라이브러리 써서 범위 사이의 정수 표기

```cpp
	std::random_device rd;
	std::mt19937 mersenne(rd()); // create a mersenne twister - 숫자를 꼬아준다.
	std::uniform_int_distribution<> dice(1, 6); // 1~6까지 동일한 확률로 나온다.

	for (int count = 1; count <= 20; ++count)
	{
		cout << dice(mersenne) << endl;
	}
```

아까는 random number를 시간에 연동시켰는데 여기서는 별도의 device를 제공해줌.

mt19937 은 생성 알고리즘에 관련된 것





































