## Chapter 9.1 산술 연산자 오버로딩 하기

``` cpp
#include <iostream>
using namespace std;

class Cents
{
private:
	int m_cents;
	
public:
	Cents(int cents = 0) {
		m_cents = cents;
	}
	int getCents() const {
		return m_cents;
	}
	int& getCents() { return m_cents; }

};

void add(const Cents& c1, const Cents& c2, Cents& c_out)
{
	c_out.getCents() = c1.getCents() + c2.getCents();
}

int main()
{
	Cents cents1(6);
	Cents cents2(8);

	Cents sum;
	add(cents1, cents2, sum);

	cout << sum.getCents() << endl;
}
```

이렇게 쓰면 불편하다.



좀 더 간편화해보면

```cpp
#include <iostream>
using namespace std;

class Cents
{
private:
	int m_cents;
	
public:
	Cents(int cents = 0) {
		m_cents = cents;
	}
	int getCents() const {
		return m_cents;
	}
	int& getCents() { return m_cents; }

};

Cents add(const Cents& c1, const Cents& c2)
{
	return Cents(c1.getCents() + c2.getCents());
}

int main()
{
	Cents cents1(6);
	Cents cents2(8);

	Cents sum;
	cout << add(cents1, cents2).getCents() << endl;

	
}
```



```cpp
#include <iostream>
using namespace std;

class Cents
{
private:
	int m_cents;
	
public:
	Cents(int cents = 0) {
		m_cents = cents;
	}
	int getCents() const {
		return m_cents;
	}
	int& getCents() { return m_cents; }

};

Cents operator + (const Cents& c1, const Cents& c2)
{
	return Cents(c1.getCents() + c2.getCents());
}

int main()
{
	Cents cents1(6);
	Cents cents2(8);

	Cents sum;

	cout << (cents1 + cents2).getCents() << endl;

	cout << (cents1 + cents2 + Cents(6)).getCents() << endl;
	
}
```





### friend로 더 간편하게

return문에서 private 변수에 접근가능해진다.

```cpp
class Cents
{
private:
	int m_cents;
	
public:
	Cents(int cents = 0) {
		m_cents = cents;
	}
	int getCents() const {
		return m_cents;
	}
	int& getCents() { return m_cents; }

	friend Cents operator + (const Cents& c1, const Cents& c2);


};
```





### 주의

삼항 연산자, Scope 연산자(`::`), sizeof, `.`, pointer 연산자에는 적용할 수 없다.

그리고 연산자 오버로딩을 해도 연산자 우선순위는 기존과 그대로 유지된다.

직관적으로 알 수 있는 경우에만 연산자 오버로딩을 사용할 것을 권장

또한 XOR 연산자 `^`는 연산자 우선순위가 아주 낮다. 하더라도 괄호로 싸서 써야 함.





### 연산자를 멤버 함수로 만들어보자

근데 멤버로 만들면 +에 인자가 2개 들어갈 수 없게 된다. 이건 한 인자가 this가 되기 때문.

```cpp
#include <iostream>
using namespace std;

class Cents
{
private:
	int m_cents;
	
public:
	Cents(int cents = 0) {
		m_cents = cents;
	}
	int getCents() const {
		return m_cents;
	}
	int& getCents() { return m_cents; }

	Cents operator + (const Cents& c2) {
		return Cents(this->getCents() + c2.getCents());
	}


};
```



### 주의사항 #2

멤버 함수로만 오버로딩 해야 하는 연산자들이 있다.

`=`(assignment), `[]`,  `()`,  `->`





## 9.2 입출력 연산자 오버로딩 하기

```cpp
#include <iostream>
using namespace std;

class Point
{
private:
	double m_x, m_y, m_z;

public:
	Point(double x = 0.0, double y = 0.0, double z = 0.0)
		: m_x(x), m_y(y), m_z(z)
	{}

	double getX() {
		return m_x;
	}

	double getY() {
		return m_y;
	}

	double getZ() {
		return m_z;
	}

	void print() {
		cout << m_x << " " << m_y << " " << m_z << endl;
	}
};

int main()
{
	Point p1(0.0, 0.1, 0.2), p2(3.4, 1.5, 2.0);

	p1.print();
	cout << endl;
	p2.print();
	cout << endl;

	return 0;
}
```

cout을 main에 한줄씩 써줘야하는게 불편하다.



### 연산자 오버로딩

규칙이 있다.

```cpp
	friend std::ostream& operator << (std::ostream& out, const Point& point)
	{
		out << m_x << " " << m_y << " " << m_z;

		return out; // chaining을 위함. 계속해서 출력하는 게 가능
	}
```

이렇게 짜면 안된다. 멤버 function인 것처럼 짜서 멤버 변수에 직접 접근하고 있는데, 첫번째 인자가 output stream이라 그게 불가능함.(클래스여야 한다는 말인 것 같다)



```cpp
	friend std::ostream& operator << (std::ostream& out, const Point& point)
	{
		out << point.m_x << " " << point.m_y << " " << point.m_z;

		return out; // chaining을 위함. 계속해서 출력하는 게 가능
	}
};

int main()
{
	Point p1(0.0, 0.1, 0.2), p2(3.4, 1.5, 2.0);

	cout << p1 << " " << p2;

	return 0;
}
```



output stream의 장점은 file 출력을 할 수 있다는 것이다.



### file 출력

```cpp
#include <fstream>

int main()
{
	ofstream of("out.txt"); // 출력할 파일 이름

	Point p1(0.0, 0.1, 0.2), p2(3.4, 1.5, 2.0);

	//p1.print();
	//cout << endl;
	//p2.print();
	//cout << endl;

	cout << p1 << " " << p2;

	of << p1 << " " << p2 << endl;

	of.close();

	return 0;
}
```

같은 위치에 out.txt가 만들어진 것을 볼 수 있다.





### cin 오버로딩

```cpp

	friend std::istream& operator >> (std::istream& in, const Point& point)
	{
		in << point.m_x << point.m_y << point.m_z;

		return in; // chaining을 위함. 계속해서 출력하는 게 가능
	}
```

인자 클래스를 const로 하면 안됨. 우리가 멤버 변수를 바꿔줄 것이기 때문



```cpp
	friend std::istream& operator >> (std::istream& in, Point& point)
	{
		in >> point.m_x >> point.m_y >> point.m_z;

		return in; // chaining을 위함. 계속해서 출력하는 게 가능
	}

int main()
{
	Point p1, p2;

	cin >> p1 >> p2;
```





## 9.3 단항 연산자 오버로딩 하기

```cpp
#include <iostream>
using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }

	// 단항 연산자
	Cents operator - () const
	{
		return Cents(-m_cents);
	}

	friend std::ostream& operator << (std::ostream& out, const Cents& cents)
	{
		out << cents.m_cents;
		return out;
	}
};

int main()
{
	Cents cents1(6);
	Cents cents2(0);

	int a = 3;

	// 단항 연산자
	cout << -a << endl;
	cout << !a << endl;

	cout << cents1 << endl;
	cout << -cents1 << endl;
	cout << -Cents(-10) << endl;

	return 0;
}

```



### Not operator !

```cpp
	bool operator ! () const
	{
		// !Cents(...)
		return (m_cents == 0) ? true : false;
	}

int main()
{
	Cents cents1(6);
	Cents cents2(0);

	// not operator
	cout << endl;
	auto temp = !cents1; // temp는 bool type

	cout << !cents1 << " " << !cents2 << endl;

	return 0;
}

```





## 9.4 비교 연산자 오버로딩 하기

std sort를 사용하려면 크기 비교 연산자가 구현돼 있어야 함.

if 문 안에서 쓰려고 해도 필요

```cpp
#include <iostream>
using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	int& getCents() { return m_cents; }

	friend bool operator == (const Cents& c1, const Cents& c2)
	{
		return c1.m_cents == c2.m_cents;
	}

	friend std::ostream& operator << (std::ostream& out, const Cents& cents)
	{
		out << cents.m_cents;
		return out;
	}
};

int main()
{
	int a = 3, b = 3;
	if (a == b)
		cout << "Equal " << endl;

	Cents cents1(6);
	Cents cents2(6);

	if (cents1 == cents2)
		cout << "Equal " << endl;

	cout << std::boolalpha;
}
```



### sorting

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


	vector<Cents> arr(20);
	for (unsigned i = 0; i < 20; ++i)
		arr[i].getCents() = i;

	std::random_shuffle(begin(arr), end(arr));

	for (auto& e : arr)
		cout << e << " ";
	cout << endl;

	std::sort(begin(arr), end(arr));

	for (auto& e : arr)
		cout << e << " ";
	cout << endl;

```

숫자 뒤섞은 다음 sort해서 보여주기

이를 위해 크기 비교 연산자를 오버로딩 해줘야 함



**왼쪽이 더 작은지를 비교하는 연산자 (<)를 정의해야 함**

```cpp
	friend bool operator < (const Cents& c1, const Cents& c2)
	{
		return c1.m_cents < c2.m_cents;
	}
```





## 9.5 증감 연산자 오버로딩 하기

++, --

전위형이냐, 후위형이냐에 따라 성질이 다르다(앞에 오냐 뒤에 오냐)

```cpp
#include <iostream>
using namespace std;

class Digit
{
private:
	int m_digit;

public:
	Digit(int cents = 0) { m_digit = cents; }
	int getCents() const { return m_digit; }
	int& getCents() { return m_digit; }

	// prefix(전위형)
	Digit& operator ++ ()
	{
		++m_digit;
		
		return *this; // 자기 자신(의 레퍼런스를 deref한 것) 리턴
	}

	// postfix(후위형)
	Digit operator ++ (int) // Dummy를 넣어서 postfix를 정의한다
	{
		Digit temp(m_digit);

		++(*this); // 또는 ++m_digit. 위의 오버로딩 함수를 사용.
		return temp;
	}

	friend std::ostream& operator << (std::ostream& out, const Digit& d)
	{
		out << d.m_digit;
		return out;
	}
};

int main()
{
	Digit d(5);

	cout << ++d << endl;
	cout << d << endl;

	cout << d++ << endl;
	cout << d << endl;

	return 0;

}
```





## 9.6 첨자 연산자 오버로딩 하기

```cpp
#include <iostream>
using namespace std;

class IntList
{
private:
	int m_list[10];

public:
	void setItem(int index, int value)
	{
		m_list[index] = value;
	}

	int getItem(int index)
	{
		return m_list[index];
	}
};

int main()
{
	IntList my_list;
	my_list.setItem(3, 1);
	cout << my_list.getItem(3) << endl;
}
```



리스트를 반환하는 것도 가능하다

```cpp
	int* getList()
	{
		return m_list;
	}


	my_list.getList()[3] = 10;
	cout << my_list.getList()[3] << endl;
```



### 첨자 연산자 오버로딩

```cpp
	int& operator [] (const int index)
	{
		return m_list[index];
	}


	my_list[3] = 10;
	cout << my_list[3] << endl;
```



### const IntList의 경우에는?

```cpp
	const int& operator [] (const int index) const
	{
		return m_list[index];
	}
```



### assert로 index 잘못 들어오는 것 막기

연산자는 많이 사용하기 때문에 if문보다는 assert를 쓰는 것이 빠르게 쓰기에 좋다.

```cpp
	int& operator [] (const int index)
	{
		assert(index >= 0);
		assert(index < 10);

		return m_list[index];
	}
```



### 참고

```cpp
	IntList* list = new IntList;
	// list[3] 이렇게 하면 안됨
	(*list)[3] = 10; // OK (dereference)
```





##  9.7 괄호 연산자 오버로딩과 함수 객체

함수가 객체인 것처럼 사용할 수 있다.

```cpp
#include <iostream>
using namespace std;

class Accumulator
{
private:
	int m_counter = 0;

public:
	int operator()(int i) { return (m_counter += i); }
};

int main()
{
	Accumulator acc;
	cout << acc(10) << endl; // 현재 있는 값에 10을 더함
	cout << acc(20) << endl; // 10 + 20

	return 0;
}
```





## 9.8 형변환을 오버로딩 하기

type cast를 오버로딩

```cpp
#include <iostream>
using namespace std;

class Cents
{
private:
	int m_cents;

public:
	Cents(int cents = 0) { m_cents = cents; }
	int getCents() const { return m_cents; }
	void setCents(int cents) {
		m_cents = cents;
	}

	operator int()
	{
		cout << "cast here" << endl;
		return m_cents;
	}

};

void printInt(const int& value)
{
	cout << value << endl;
}

int main()
{
	Cents cents(7);

	printInt(cents);

	return 0;
}
```



```cpp
	int value = (int)cents;
	value = int(cents);
	value = static_cast<int>(cents);
```

다 같은 것이다.



### 달러를 센트로 변환

```cpp
class Dollar
{
private:
	int m_dollars = 0;

public:
	Dollar(const int& input) : m_dollars(input) {}

	operator Cents()
	{
		return Cents(m_dollars * 100);
	}
};


	Dollar dol(2);
	Cents cents2 = dol;
	printInt(cents2);
```





## 9.9 복사 생성자, 복사 초기화 반환값 최적화

```cpp
#include <iostream>
#include <cassert>
using namespace std;

class Fraction
{
private:
	int m_numerator;
	int m_denominator;

public:
	Fraction(int num = 0, int den = 1)
		: m_numerator(num), m_denominator(den)
	{
		assert(den != 0);
	}

	Fraction(const Fraction& fraction) // copy constructor
		: m_numerator(fraction.m_numerator), m_denominator(fraction.m_denominator)
	{
		cout << "Copy constructor called" << endl;
	}

	friend std::ostream& operator << (std::ostream& out, const Fraction& f)
	{
		out << f.m_numerator << " / " << f.m_denominator << endl;

		return out;
	}
};

int main()
{
	Fraction frac(3, 5);

	Fraction fr_copy(frac); // 복사

	cout << frac << fr_copy << endl;

	return 0;
}
```

결과가 똑같이 나오는 것을 볼 수 있다.



### copy initialization

```cpp
	Fraction fr_copy = frac; // copy initialization
```

이 경우에도 위와 같음



### 복사를 막고 싶다면

copy constructor를 private으로 옮기면 된다.



### 이 경우에는?

```cpp
	Fraction fr_copy(Fraction(3, 10));
```

컴파일러가 알아서 Fraction부분을 생략하고 3, 10만 넣는다.



### 함수로 받기

```cpp
Fraction doSomething()
{
	Fraction temp(1, 2);

	return temp;
}

	Fraction result = doSomething();
	cout << result << endl;
```

디버그 모드에서는 카피 컨스트럭터가 쓰임(copy initialization - 두 개가 서로 다른 주소. 복사를 해서 씀)

릴리즈 모드에서는 안쓰이고 오브젝트를 그냥 그대로 받아서 씀(**반환값 최적화** - 같은 주소의 객체를 넘겨받음)





## 9.10 변환 생성자, explicit, delete

메모리 할당 해제할 때의 delete와는 다른 것.



### 변환 생성자(converting constructor)

함수에 인자로 대충 넣어도 클래스를 만들어서 전달해주는 것

```cpp
void doSomething(Fraction frac) {
    
}

int main()
{
    doSomething(7);
}
```

생성자에 모든 인자를 전달하지 않았다면 기본값을 사용해서 만들어준다.



### explicit

생성자에 explicit 선언하면 위의 방법이 막히게 된다. 

```cpp
explicit Fraction(int num = 0, int den = 1)

doSomething(frac);
```



### delete

버전업을 해서 못쓰게 만들고 싶을 때 강력하게 막아놓으려고 쓴다.

```cpp
public:
Fraction(char) = delete;

Fraction frac2('c'); // error
```





## 9.11 대입 연산자 오버로딩, 깊은 복사, 얕은 복사



### 얕은 복사

```cpp
MySTring hello("Hello");

cout << (int*)hello.m_data << endl;
cout << hello.getString() << endl;

{
    MyString copy = hello; // 복사 생성자 호출
    cout << (int*)copy.m_data << endl;
    cout << copy.getString() << endl;
} // scope가 끝나면 복사된 객체는 사라진다.
```

지금은 복사 생성자를 정의하지 않았기 때문에 디폴트 복사 생성자가 쓰인다.

멤버를 그냥 복사해서 준다.



그 다음 main에서 string을 부르면

```cpp
cout << hello.getString() << endl;
```

이미 copy가 지워지면서 m_data 포인터를 delete해버림 -> hello의 m_data까지 delete 되어 버린다.

이상한 값이 나와버리게 된다.



### copy constructor - 깊은 복사를 구현해보자

```cpp
MyString(const MyString &source)
{
    cout << "Copy Constructor " << endl;
    
    m_length = source.m_length;
    
    if (source.m_data != nullptr)
    {
        m_data = new char[m_length];
        
        for (int i = 0; i < m_length; ++i)
            m_data[i] = source.m_data[i];
    }
    else
        m_data = nullptr;
}
```



### 대입 연산자

```cpp
MyString& operator = (const MyString &source)
{
    // shallow copy
    //this->m_data = source.m_data;
    //this->m_length = source.m_length;
    
    // 주소 비교해서 같다면 끝내버림
    if (this == &source) // 자기가 자기 자신에게 할당하는 경우(hello = hello)
        return *this;
    
    delete[] m_data; // 갖고 있던 것을 지워버림(할당이기 때문에 이전에 멤버가 있었을 것)
    
    m_length = source.m_length;
    
    if (source.m_data != nullptr)
    {
        m_data = new char[m_length];
        
        for (int i = 0; i < m_length; ++i)
            m_data[i] = source.m_data[i];
    }
    else
        m_data = nullptr;
    
   	return *this;
}
```



### 복사 생성자 사용

```cpp
MyString hello("Hello");

{
    MyString copy = hello;
}
```



### 대입 연산자 사용

```cpp
MyString str1 = hello; // 복사 생성자 호출(방법 1)
MyString str1(hello); // 복사 생성자 호출(방법 2) - 이게 더 구분이 되므로 추천

MyString str2;
str2 = hello; // 대입 연산자 호출
```



### 복사 생성자 구현하지는 않고 얕은 복사를 막는 법

직접 구현하기 귀찮다면

아예 얕은 복사를 막아버리는 delete를 쓸 수 있다.

```cpp
MyString(const MyString &source) = delete;
```





















































