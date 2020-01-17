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





















