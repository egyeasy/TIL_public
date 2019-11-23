## 8.1 객체지향 프로그래밍과 클래스

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;


void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}

int main()
{
	string	name;
	string	address;
	int		age;
	double	height;
	double	weight;
}

```



### vector

벡터를 이용해 출력해보자

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;


void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}

int main()
{
	string	name;
	string	address;
	int		age;
	double	height;
	double	weight;

	vector<string>	name_vec;
	vector<string>	addr_vec;
	vector<int>		age_vec;
	vector<double>	height_vec;
	vector<double>	weight_vec;

	print(name_vec[0], addr_vec[0], age_vec[0], height_vec[0], weight_vec[0]);
}

```



### struct

안의 변수들을 멤버 변수라고 한다.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct Friend
{
	string	name;
	string	address;
	int		age;
	double	height;
	double	weight;
};

int main()
{
	//Friend jj{ "Jack Jack", 2, "Uptown", ... } // uniform initialization
	Friend jj;
	jj.name = "Jack Jack";
	jj.age = 2;

	print(jj.name, jj.address, jj.age, jj.height, jj.weight);
}

```



print 함수 매개변수를 struct 하나로 받아보자

```cpp
void print(const string& name, const string& address, const int& age,
	const double& height, const double& weight)
{
	cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
}


	print(jj);
```



fr.을 쓰는 것도 귀찮다면 print 함수를 struct의 멤버로 넣어줄 수 있다

```cpp
struct Friend
{
	string	name;
	string	address;
	int		age;
	double	height;
	double	weight;

	void print()
	{
		cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
	}
};


	jj.print();
```





### 클래스

데이터(변수)와 기능(함수)이 묶여있는 것을 오브젝트라고 한다. struct는 일반적으로 data를 넣을 때만 쓰고 기능까지 쓴다면 class를 쓴다. 

- 접근지정자(access specifier) - public, private, protected

```cpp
class Friend
{
public: // access specifier (public, private, protected)
	string	name;
	string	address;
	int		age;
	double	height;
	double	weight;

	void print()
	{
		cout << name << " " << address << " " << age << " " << height << " " << weight << endl;
	}
};

	Friend jj{ "Jack Jack", "Uptown", 20, 167, 57 }; // uniform initialization(instantiation), jj = instance
```



어떻게 편리하게 쓸 수 있을까?

```cpp
	// 친구가 여러 명이다
	vector<Friend> my_friends;
	my_friends.resize(2);

	//my_friends[0].print();
	//my_friends[1].print();
	
	for (auto& ele : my_friends)
		ele.print();
```



struct에는 access specifier가 들어가지 않는다. 





## 8.2 캡슐화, 접근 지정자, 접근 함수

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct Date
{
	int m_month;
	int m_day;
	int m_year;
};

int main()
{
	Date today{ 9, 4, 2025 };
	today.m_month = 8;
	today.m_day = 4;
	today.m_year = 2025;

	return 0;
}
```



struct를 class로 바꾸면 에러가 나게 된다. 클래스 내에서만 접근할 수 있도록 되어있기 때문(inaccessible)



```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Date
{
public:
	int m_month;
	int m_day;
	int m_year;
};

int main()
{
	Date today{ 9, 4, 2025 };
	today.m_month = 8;
	today.m_day = 4;
	today.m_year = 2025;

	return 0;
}
```

public을 써주면 가능하게 만들 수 있다.

private을 쓰면 다시 막히게 된다.(private이 default)



### private

그럼 밖에서 어떻게 private 변수에 접근하는가?

access 함수를 만들어야 한다.

```cpp
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Date
{
	int m_month;
	int m_day;
	int m_year;

public:
	void setDate(const int& month_input, const int& day_input, const int& year_input)
	{
		m_month = month_input;
		m_day = day_input;
		m_year = year_input;
	}
};

int main()
{
	Date today; // { 9, 4, 2025 };
	//today.m_month = 8;
	//today.m_day = 4;
	//today.m_year = 2025;

	today.setDate(8, 4, 2025);

	return 0;
}
```





### get, set

```cpp
class Date
{
	int m_month;
	int m_day;
	int m_year;

public:
	void setDate(const int& month_input, const int& day_input, const int& year_input)
	{
		m_month = month_input;
		m_day = day_input;
		m_year = year_input;
	}

	void setMonth(const int& month_input)
	{
		m_month = month_input;
	}

	// setDay, setYear ...

	const int& getDay() // get에서 day 를 바꾸지 못하도록
	{
		return m_day;
	}
};



	today.setDate(8, 4, 2025);
	today.setMonth(10);

	cout << today.getDay() << endl;
```





### 복사해오기

```cpp
	void copyFrom(const Date& original)
	{
		m_month = original.m_month;
		m_day = original.m_day;
		m_year = original.m_year;
	}
};

	Date copy;
	//copy.setDate(today.getMonth(), today.getDay(), today.getYear());
	// 이게 귀찮을 때
	copy.copyFrom(today);

```

의문사항은, 클래스 함수 내에서 다른 인스턴스의 멤버변수에 직접 접근하고 있다는 것이다. 같은 클래스로 정의되어있으면 private에 접근할 수 있다.



### getter, setter를 하는 이유 중 1

```cppcopy.m_day = 123;
	copy.m_day = 123;
	today.m_month = 45;

```

이렇게 된 상태에서 멤버 변수 이름이 바뀌게 되면 바깥 단의 변수 이름도 바꿔줘야 한다. access function만 접근할 수 있게 해놓으면 클래스 안에서 다 해결이 가능하다. visual studio의 rename 기능도 소스가 커지면 제대로 작동하지 않을 수 있음.





## 8.3 생성자 Constructors

```cpp
#include <iostream>

using namespace std;

class Fraction
{
private:
	int m_numerator;
	int m_denominator;

public:
	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};

int main()
{
	Fraction frac;

	frac.print();

	return 0;
}

```

이렇게 쓰면 이상한 숫자가 출력된다. 이것은 멤버변수를 초기화해주지 않았기 때문.



encapsulation을 유지하면서 값을 대입할 수 없을까?

### 기본값 설정

```cpp
class Fraction
{
private:
	int m_numerator = 0;
	int m_denominator = 1;

public:
	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};
```



### 생성자 기본값

```cpp
#include <iostream>

using namespace std;

class Fraction
{
private:
	int m_numerator = 0;
	int m_denominator = 1;

public:
	Fraction()
	{
		m_numerator = 0;
		m_denominator = 1;

		cout << "Fraction() Constructor" << endl;
	}
	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};

int main()
{
	Fraction frac; // 생성자가 하나도 없을 때 반드시 괄호를 빼야함


	frac.print();

	return 0;
}

```





### 생성자 값 넣어주기

```cpp
#include <iostream>

using namespace std;

class Fraction
{
private:
	int m_numerator = 0;
	int m_denominator = 1;

public:
	Fraction(const int& num_in, const int& denom_in = 1) // default 설정 가능
	{
		m_numerator = num_in;
		m_denominator = denom_in;

		cout << "Fraction() Constructor" << endl;
	}
	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};

int main()
{//Fraction frac; // 생성자가 하나도 없을 때 반드시 괄호를 빼야함(function과 구분이 잘 안가기 때문)
	Fraction one_thirds(1, 3);
	one_thirds.print();


	//frac.print();

	return 0;
}

```



```cpp
#include <iostream>

using namespace std;

class Fraction
{
private:
	int m_numerator;
	int m_denominator;

public:
	//Fraction(const int& num_in, const int& denom_in)
	//{
	//	m_numerator = num_in;
	//	m_denominator = denom_in;

	//	cout << "Fraction() Constructor" << endl;
	//}
	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};
```

이렇게 돼도 클래스를 만들 수는 있다. 이 경우 디폴트 생성자가 적용된다. 그러면 멤버 변수에는 쓰레기 값이 들어가게 된다.

생성자 하나만이라도 정의를 하면 기본 생성자가 설정되지 않는다.

변수를 안 받고 싶다면 파라미터 없이 만드는 생성자를 정의 직접 해줘야함.

```cpp
class Fraction
{
private:
	int m_numerator = 0;
	int m_denominator = 1;

public:
	Fraction()
	{
		m_numerator = 1;
		m_denominator = 1;
	}
	Fraction(const int& num_in, const int& denom_in)
	{
		m_numerator = num_in;
		m_denominator = denom_in;

		cout << "Fraction() Constructor" << endl;
	}
	void print()
	{
		cout << m_numerator << " / " << m_denominator << endl;
	}
};

int main()
{
	//Fraction frac; // 생성자가 하나도 없을 때 반드시 괄호를 빼야함
	Fraction one_thirds(1, 3);
	one_thirds.print();

	Fraction one;
	one.print();

```

아래의 생성자에 두 파라미터 모두 기본값을 생성하면 Fraction one이 안 만들어진다.



### Copy initialization

```cpp
Fraction one_thirds = Fraction{ 1, 3 };
```

아래를 더 권장

```cpp
Fraction one_thirds{ 1, 3 };
```

위 방식(uniform initialization)은 타입 변환을 허용하지 않는다. 

```cpp
Fraction one_thirds(1, 3);
```

이건 warning만 뜨고 되긴 된다.





### 클래스 안의 클래스

```cpp
class Second
{
public:
	Second()
	{
		cout << "class Second constructor()" << endl;
	}
};

class First
{
	Second sec;
public:
	First()
	{
		cout << "class First constructor()" << endl;
	}
};


	First fir;
```

Second가 먼저 만들어지고 First가 만들어진다. Second가 만들어져 있어야 Frist가 Second를 가지고 작업을 할 수 있기 때문.



### private 생성자

생성자를 private으로 하는 건 말도 안되지만 이걸 쓰는 프로그래밍 기법이 따로 있음.

























