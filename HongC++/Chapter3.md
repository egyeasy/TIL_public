## 3.1 연산자 우선순위와 결합법칙

### 위키피디아(영어) 연산자 우선순위 표

*, /, %는 level 5로 같은 우선순위. +와 -는 level 6. 5가 더 높은 걸로 인정된다.

`Left-to-right`은 우선순위가 같을 때 어떻게 처리할 것이냐 -> 좌에서 우 순을 말하는 것

linery plus/minus는 +3, -3과 같은 것. !(logically not), ~(bitwisely not)과 함께 level 3이다.

`=` : direct assignment

애매하면 괄호를 쳐서 우선순위를 명확하게 설정하자.





## 3.2 산술 연산자 arithmetic operator

```cpp
using namespace std;

int x = 1;
int y = -x; // 단항 연산자는 붙여서 쓰도록 하자
y = 1 - -x; 

return 0;
```



### 나누기와 나머지

정수 나머지, float 나머지가 다르다.

```cpp
int x = 7;
int y = 4;

cout << x / y << endl; // 1
cout << float(x) / y << endl; // 1.75
cout << x / float(y) << endl; // 1.75
cout << float(x) / float(y) << endl; // 1.75
```

나눗셈 둘 중 하나만 실수여도 결과는 실수다.



C++11부터는 -5 / 2를 버림해서 -2가 나오게 됨. 이전에는 어떻게 처리할지 애매했었다.

-5 % 2의 경우에도 왼쪽 숫자가 마이너스면 나머지도 마이너스, 플러스면 나머지도 플러스로 처리하기로.



```cpp
int x = 7;
int y = 4;

int z = x; // z = 7
z += y; // z = z + y;
```



## 3.3 증감 연산자 increment decrement operators

```cpp
using namespace std;

int x = 5;
int y = ++x;
int z = x--;

cout << y << endl; // 4
cout << z << endl; // 4

return 0;
```



다음부터가 중요한 얘기

```cpp
int x = 6, y = 6;
cout << x << " " << y << endl; // 6 6
// cout << ++x << " " << --y << endl; // 7 5
cout << x++ << " " << y-- << endl; // 6 6
cout << x << " " << y << endl; // 7 5
```

x++, y--는 출력한 다음에 연산을 적용하는 개념



부작용이 될 수 있는 경우를 알아보자

```cpp
int add(int a, int b)
{
    return a + b;
}

int main()
{
    using namespace std;
    
    int x = 1;
    int v = add(x, ++x); // do not use like this - 다른 변수 y를 만들어서 ++y로 넣는 것은 괜춘
    
    cout << v << endl;
    
    return 0;
}
```



```cpp
int main()
{
    using namespace std;
    
    int x = 1;
    // x = x++; // 결과가 명확하지 않다
    ++x;
    
    cout << x << endl;
    
    return 0;
}
```





## 3.4 sizeof 쉼표 연산자, 조건부 연산자

### sizeof

sizeof는 연산자에 해당. 함수가 아니다.

변수명과 함께 쓰일 때는 괄호가 없어도 작동 `sizeof a`

```cpp
	float a;

	sizeof(float);
	sizeof(a);

	sizeof a; // 괄호가 없어도 작동
```





### comma operator

앞에 것을 계산을 하고 뒤에 것도 계산한 다음 뒤의 것을 대입

```cpp
	// comma operator
	int x = 3;
	int y = 10;
	//int z = (++x, ++y);
	// 풀어서 쓰면
	++x;
	++y;
	int z = y;

	cout << x << " " << y << " " << z << endl;
```

for문에서 많이 사용.



```cpp
	int a = 1, b = 10; // 여기서는 comma 연산자가 아니라 둘을 구분하는 기호
	

	//z = a, b;

	cout << z << endl; // 1이 출력됨 -> 연산자의 우선순위가 대입 연산자(=)보다 낮기 때문. a가 들어가게 된다.
	
	z = (++a, b); // 뒤의 것을 출력하려면 싸줘야한다.
```





### 조건부 연산자(삼항 연산자) conditional operator

```cpp
	// conditional(arithmetric if)
	bool onSale = true;

	int price;

	if (onSale)
		price = 10;
	else
		price = 100;

	cout << price << endl;

	
	
```



price를 const int로 쓰고 싶다면?

```cpp
// conditional(arithmetric if)
	bool onSale = true;

	const int price = (onSale == true) ? 10 : 100;
	
	cout << price << endl;
```

if문에서 안 되는 것을 되게 할 수 있다.



함수를 짜서 표현한다면

```cpp
int getPrice(bool onSale)
{
	if (onSale)
		return 10;
	return 100;
}

// ... //
	const int price = getPrice(onSale);
```



```cpp
	int x1 = 5;

	cout << ((x1 % 2 == 0) ? "even" : "odd") << endl; // 연산자 우선순위 때문에 괄호로 감싸야 한다.
```





## 3.5 관계 연산자 Relational Poerators

```cpp
	int x, y;
	cin >> x >> y;
	cout << "Your input values are : " << x << " " << y << endl;

	if (x == y)
		cout << "equal" << endl;
	if (x != y)
		cout << "Not equal" << endl;
	if (x > y)
		cout << "x is greater than y" << endl;
```



### 주의사항 - 부동소숫점끼리의 비교

```cpp
	double d1(100 - 99.99);  // 0.001
	double d2(10 - 9.99); // 0.001

	if (d1 == d2)
		cout << "equal" << endl;
	else
	{
		cout << "Not equal" << endl;

		if (d1 > d2) cout << "d1 > d2" << endl;
		else //if(d1 < d2)
			cout << "d1 < d2" << endl;
	}

	cout << std::abs(d1 - d2) << endl; // 5.32907e-15
```



오차의 한계를 정의할 수 있다.

```cpp
	const double epsilon = 1e-10;

	if (std::abs(d1 - d2) < epsilon)
		cout << "Approximately equal" << endl;
	else
		cout << "Not equal" << endl;
```





## 3.6 논리 연산자 logical operators

```cpp
	// logical NOT
	bool x = true;
	bool y = false;

	cout << !x << endl;
	

	// logical AND
	cout << (x && y) << endl; // 반드시 2개를 써줘야 함. &는 bitwise operator
```



```cpp
	bool hit = true;
	int health = 10;

	if (hit == true && health < 20) // hit == true 대신 hit만 써도 됨
	{
		cout << "die" << endl;
	}
	else
		health -= 20;
```



### logical OR

```cpp
	// logical OR ||
	x = true;
	y = false;

	cout << (x || y) << endl;
```





### 실수하기 쉬운 예제

```cpp
	int x1 = 5;
	int y1 = 7;

	if (!x1 == y1) // false true(형변환)를 비교하게 됨
	{
		cout << " x does not equal y" << endl;
	}
	else
		cout << " x equals y" << endl;
```

괄호로 잘 싸주는 게 좋다.



### logical OR 예제

```cpp
	int v = 1;

	if (v == 0 || v == 1)
		cout << "v is 0 or 1" << endl;
```





### short circuit evaluation

```cpp
	// short circuit evaluation
	int x2 = 2;
	int y2 = 2;

	if (x2 == 1 && y2++ == 2)
	{
		// do something
	}

	cout << y2 << endl;
```

`x2 == 1`가 틀리게 되면 뒤를 안 봐도 알 수 있어서 `y2++`를 실행시키지 않게 된다.





### De Morgan's Law

분배법칙이 성립하지 않는다.

```cpp
	bool x3 = true;
	bool y3 = false;

	!(x && y);
	!x || !y;
```



### XOR

```cpp
	// XOR
	// false false -> false
	// false true true
	// true false true
	// true true false

	// but c++에는 연산자가 없다. 그래서 아래와 같이 씀
	if (x3 != y3)
	{
		// do something
	}
```





### AND와 OR

```cpp
	bool v1 = true;
	bool v2 = false;
	bool v3 = false;

	bool r1 = v1 || v2 && v3; // &&가 ||보다 우선순위가 높다.
	bool r2 = (v1 || v2) && v3;
	bool r3 = v1 || (v2 && v3); // 이렇게 쓰는 게 바람직

	cout << r1 << endl;
	cout << r2 << endl;
```





## 3.7 이진수 Binary Numbers

### binary to decimal

### decimal to binary

방법 1: 2로 계속 나눠서 나머지를 추려낸다.

방법 2: 1 2 4 8 ... 중에서 N보다 작거나 같은 수 중에 가장 큰 수를 N에서 빼가면서 자릿수를 구한다.

### 이진수 덧셈

### 음의 정수를 이진수로 어떻게 바꿀까

- -5를 바꿔보자

1. 5의 이진수는 0000 0101
2. 보수(complement) : 1111 1010
3. 1을 더한다 : 1111 1011

맨앞자릿 수는 +인지 -인지를 나타냄.



- 1001 1110(-98)을 바꿔보자

1. 0110 0001
2. 0110 0010 -> 98



### signed vs unsigned

1001 1110 = 128 + 16 + 8 + 4 + 2 (unsigned)

​					 -128 + 16 + 8 + 4 + 2 (signed)





## 3.8 비트단위 연산자 Bitwise Operators 컴퓨터 작동원리

메모리의 주소를 줄 수 있는 단위가 바이트 단위.

메모리 주소 하나는 최소 1바이트다.

1. 데이터를 꽉꽉 채워넣기 위해 사용.

2. 계산 속도가 빠름



// << left shift
// >> right shift
// ~, &, |, ^ bitwise not, and, or, xor



비트마스크, 게임 프로그래밍 등 빠른 프로그래밍을 할 때 필수적임.



```cpp
#include <iostream>
#include <bitset>

int main()
{
	using namespace std;

	unsigned int a = 3;

	// 어떻게 내부적으로 저장되는지 보고 싶다면
	cout << std::bitset<4>(a) << endl; // 0011

	unsigned int b = a << 1; // left shift

	cout << std::bitset<4>(b) << endl; // 0110
}
```



```cpp
	b <<= 2; // * 2**2

	cout << b << endl;

	cout << (a << 1) << endl; // cout 내에서 shift 하려면 괄호 필요
```



2의 n제곱을 계산할 때 power보다 훨씬 빠르다.



### Right shift

```cpp
	unsigned int c = 1024;

	cout << std::bitset<16>(c) << endl;

	// right shift
	cout << std::bitset<16>(c >> 1) << " " << (c >> 1) << endl; // 512
	cout << std::bitset<16>(c >> 2) << " " << (c >> 2) << endl; // 256
	cout << std::bitset<16>(c >> 3) << " " << (c >> 3) << endl; // 128
	cout << std::bitset<16>(c >> 4) << " " << (c >> 4) << endl; // 64

	// not
	cout << std::bitset<16>(~c) << " " << (~c) << endl; // 1 0이 뒤집혀서 나옴
```



### 이항 연산자 AND, OR, XOR

```cpp
	// 이진수 int
	unsigned int d = 0b1100;
	unsigned int e = 0b0110;

	cout << std::bitset<4>(a & b) << endl; // bitwise AND
	cout << std::bitset<4>(a | b) << endl; // bitwise OR
	cout << std::bitset<4>(a ^ b) << endl; // bitwise XOR
```





## 3.9 비트 플래그, 비트 마스크 사용법 Bit Flags, Bit masks

```cpp
#include <iostream>

using namespace std;

int main()
{
	bool item1_flag = false;
	bool item2_flag = false;
	bool item3_flag = false;
	bool item4_flag = false;

	

	return 0;
}
```

flag를 직접 바꿔가면서 작업하기에는 불편함이 따른다. item 확장성도 떨어짐



### 비트 플래그

변수 하나만 써서 flag들을 조정해보자.



```cpp
#include <iostream>
#include <bitset>

using namespace std;

int main()
{
	// 비트 플래그
	unsigned char items_flag = 0;

	cout << bitset<8>(items_flag) << endl;

	return 0;
}
```



```cpp
	// 비트 플래그
	unsigned char items_flag = 0;
	cout << bitset<8>(items_flag) << endl;

	const unsigned char opt0 = 1 << 0;
	const unsigned char opt1 = 1 << 1;
	const unsigned char opt2 = 1 << 2;
	const unsigned char opt3 = 1 << 3; // 실질적 계산은 없지만 규칙성을 위해 0 shift
	cout << bitset<8>(opt0) << endl;

	cout << "No item " << bitset<8>(items_flag) << endl;

	// item0 on
	items_flag |= opt0;
	cout << "Item0 obtained " << bitset<8>(items_flag) << endl;

	// item3 on
	items_flag |= opt3;
	cout << "Item3 obtained " << bitset<8>(items_flag) << endl;

	// item3 lost
	items_flag &= ~opt3;
	cout << "Item3 lost " << bitset<8>(items_flag) << endl;

	// has item1 ?
	if (items_flag & opt1) {
		cout << "Has item1 " << endl;
	}
	else {
		cout << "Not has item1" << endl;
	}

	// has item0 ?
	if (items_flag & opt0) { cout << "Has item0" << endl; }

	// obtain item 2, 3
	items_flag |= (opt2 | opt3);
	cout << bitset<8>(opt2 | opt3) << endl;
	cout << "Item2, 3 obtained " << bitset<8>(items_flag) << endl;


	// 2를 갖고 있고 1을 갖고 있지 않을 경우
	if ((items_flag & opt2) && !(items_flag & opt1))
	{
		//items_flag ^= opt2; // 상태를 바꿔주는 명령은 XOR
		//items_flag ^= opt1;
		items_flag ^= (opt1 | opt2);
	}

	cout << bitset<8>(items_flag) << endl;
```

OpenGL 등의 변수에서 비트 플래그를 쓰면 편하다.





### 비트 마스크

컬러맵을 예시로 보자.

```cpp
	unsigned int pixel_color = 0xDAA520;
	cout << std::bitset<32>(pixel_color) << endl;

	// red(green, blue)에 해당하는 DA만 출력하고 싶다면?
	const unsigned int red_mask = 0xFF0000;
	const unsigned int green_mask = 0x00FF00;
	const unsigned int blue_mask = 0x0000FF;

	// blue만 추출해보자
	unsigned char blue = pixel_color & blue_mask;
	cout << "blue " << bitset<8>(blue) << " " << int(blue) << endl; // 00100000 32

	//unsigned char green = pixel_color & green_mask;
	unsigned int green = (pixel_color & green_mask) >> 8; // blue 8자리까지 같이 나오므로 right shift해야 green만 추출 가능
	cout << "green " << bitset<8>(green) << " " << int(green) << endl; // 00000000 출력됨. char로 받아서 size가 부족한 것.
```

















































