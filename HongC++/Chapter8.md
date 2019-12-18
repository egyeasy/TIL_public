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





## 8.4 생성자 멤버 초기화 목록

```cpp
#include <iostream>
using namespace std;

class B
{
public:
	int m_b;

public:
	B(const int& m_b_in)
		: m_b(m_b_in)
	{}
};

class Something
{
private:
	int		m_i;
	float	m_d;
	char	m_c;
	int		m_arr[5]; // c++ 11 부터 가능
	B		m_b;

public:
	Something()
		: m_i(1), m_d(3.14), m_c('a'), m_arr{ 1, 2, 3, 4 ,5 }, m_b(m_i - 1) // 중괄호를 쓰면 형변환이 안된다(더 엄격하다)
	{
		/*m_i = 1;
		m_d = 3.14;
		m_c = 'a';*/
	}

	void print()
	{
		cout << m_i << " " << m_d << " " << m_c << endl;
	}

};
```





### 바로 초기화하기

```cpp
#include <iostream>
using namespace std;

class B
{
public:
	int m_b;

public:
	B(const int& m_b_in)
		: m_b(m_b_in)
	{}
};

class Something
{
private:
	int		m_i = 100;
	float	m_d = 100.0;
	char	m_c = 'F';
	int		m_arr[5] = { 100, 200, 300, 400, 500 }; // c++ 11 부터 가능
	B		m_b{ 1024 };

public:
	Something()
		: m_i(1), m_d(3.14), m_c('a'), m_arr{ 1, 2, 3, 4 ,5 }, m_b(m_i - 1) // 중괄호를 쓰면 형변환이 안된다(더 엄격하다)
	{
		/*m_i = 1;
		m_d = 3.14;
		m_c = 'a';*/
	}

	void print()
	{
		cout << m_i << " " << m_d << " " << m_c << endl;
	}

};
```

이 경우엔 생성자(아래에 있는 내용)가 더 우선이 된다. 그 아래에 주석된 부분은 더 나중에 실행됨. 위에서 아래 순이라고 보면 될듯.





## 8_5. 위임 생성자

생성자가 다른 생성자를 사용하는 것.

```cpp
#include <iostream>
#include <string>

using namespace std;

class Student
{
private:
	int		m_id;
	string	m_name;
public:
	Student(const int& id_in, const string& name_in)
		: m_id(id_in), m_name(name_in)
	{}

	void print()
	{
		cout << m_id << " " << m_name << endl;
	}

};

int main()
{
	Student man;
	
}
```



id_in에 디폴트 값을 넣어주고 싶다면?

```cpp
#include <iostream>
#include <string>

using namespace std;

class Student
{
private:
	int		m_id;
	string	m_name;
public:
	Student(const string& name_in)
		: m_id(0), m_name(name_in)
    {}
    
	Student(const int& id_in, const string& name_in)
		: m_id(id_in), m_name(name_in)
	{}

	void print()
	{
		cout << m_id << " " << m_name << endl;
	}

};

int main()
{
	Student man;
	
}
```

이것도 가능하지만 굉장히 귀찮아진다.

이 경우 생성자가 생성자를 가져다 쓰게 할 수 있다.



```cpp
public:
	Student(const string& name_in)
		//: m_id(0), m_name(name_in)
		: Student(0, name_in)
	{}

	Student(const int& id_in, const string& name_in)
		: m_id(id_in), m_name(name_in)
	{}
```



최근 방법으로는 별도의 생성자용 함수를 만들어서 가져다 쓰는 것이 있다.

```cpp
#include <iostream>
#include <string>

using namespace std;

class Student
{
private:
	int		m_id;
	string	m_name;
public:
	Student(const string& name_in)
		//: m_id(0), m_name(name_in)
	{
		init(0, name_in);
	}

	Student(const int& id_in, const string& name_in)
		//: m_id(id_in), m_name(name_in)
	{
		init(id_in, name_in);
	}
	
	void init(const int& id_in, const string& name_in)
	{
		m_id = id_in;
		m_name = name_in;
	}

	void print()
	{
		cout << m_id << " " << m_name << endl;
	}

};

int main()
{
	Student man;
	
}
```





## 8.6 소멸자 Destructor

```cpp
#include <iostream>
using namespace std;

class Simple
{
private:
	int m_id;

public:
	Simple(const int& id_in)
		: m_id(id_in)
	{
		cout << "Constructor " << m_id << endl;
	}

	~Simple()
	{
		cout << "Destructor " << m_id << endl;
	}
	
};

int main()
{
	Simple s1(0);
	Simple s2(1);

	return 0;
}
```



### new와 delete

```cpp
#include <iostream>
using namespace std;

class Simple
{
private:
	int m_id;

public:
	Simple(const int& id_in)
		: m_id(id_in)
	{
		cout << "Constructor " << m_id << endl;
	}

	~Simple()
	{
		cout << "Destructor " << m_id << endl;
	}
	
};

int main()
{
	//Simple s1(0);
	Simple* s1 = new Simple(0);
	Simple s2(1);

	delete s1;

	return 0;
}
```

소멸자는 instance가 메모리에서 해제될 때 내부에서 자동으로 호출됨. 동적할당으로 만들어진 경우에는 영역을 벗어나도 자동으로 메모리가 해제되지 않기 때문에 delete로 메모리를 해제할 때에만 소멸자가 호출됨.

소멸자를 프로그래머가 직접 호출하는 것은 대부분의 경우 권장하지 않음.



```cpp
class IntArray
{
private:
	int* m_arr = nullptr;
	int m_length = 0;

public:
	IntArray(const int length_in)
	{
		m_length = length_in;
		m_arr = new int[m_length];

		cout << "Constructor " << endl;
	}

	~IntArray()
	{
		if(m_arr != nullptr) // 안전장치
			delete[] m_arr; // 소멸자를 쓰면 간편하게 메모리를 지우고 사라질 수 있다.
	}

	int getLength() { return m_length; }
};

int main()
{
	while (true)
	{
		IntArray my_int_arr(10000); // 메모리 leak이 발생한다.
		//delete[] my_int_arr.m_arr; // 이건 접근이 불가하다.
		
	}

	return 0;
}
```

이렇게 소멸자를 통해 new한 것을 소멸자에서 delete해주면 된다.

array 대신에 vector를 쓰면 알아서 소멸자 메커니즘이 적용돼 있기 때문에 delete 까먹는 걸 걱정하지 않아도 된다.





## 8.7 this 포인터와 연쇄 호출 Chaining Member Functions

서로 다른 인스턴스를 어떻게 구분할까

```cpp
#include <iostream>
using namespace std;

class Simple
{
private:
	int m_id;

public:
	Simple(int id)
	{
		setId(id);

		cout << this << endl;
	}

	void setId(int id) { m_id = id; }
	int	 getId() { return m_id; }
};


int main()
{
	Simple s1(1), s2(2);
	s1.setId(2);
	s2.setId(4);

	cout << &s1 << " " << &s2;

}
```





### this는 멤버 function에서 생략된다

```cpp
#include <iostream>
using namespace std;

class Simple
{
private:
	int m_id;

public:
	Simple(int id)
	{
		this->setId(id); //  일반적으로 this->가 생략돼있는 것
		//(*this).setId(id); // 이것도 가능

		cout << this << endl;
	}

	void setId(int id) { m_id = id; }
	int	 getId() { return m_id; }
};


int main()
{
	Simple s1(1), s2(2);
	s1.setId(2);
	s2.setId(4);

	cout << &s1 << " " << &s2;

}
```



main에서는 `Simple::setId(&s2, 4);`와 같은 방식으로 함수를 한 곳에 저장해두고 인스턴스 주소를 함께 넘겨줘서 실행한다.



### chaining member function

```cpp

class Calc
{
private:
	int m_value;

public:
	Calc(int init_value)
		: m_value(init_value)
	{}

	void add(int value) { m_value += value; }
	void sub(int value) { m_value -= value; }
	void mult(int value) { m_value *= value; }

	void print()
	{
		cout << m_value << endl;
	}
};

	Calc cal(10);
	cal.add(10);
	cal.sub(1);
	cal.mult(2);
	cal.print();
}
```



이게 좀 귀찮다면

```cpp
class Calc
{
private:
	int m_value;

public:
	Calc(int init_value)
		: m_value(init_value)
	{}

	Calc& add(int value) { m_value += value; return *this; }
	Calc& sub(int value) { m_value -= value; return *this; }
	Calc& mult(int value) { m_value *= value; return *this; }

	void print()
	{
		cout << m_value << endl;
	}
};



	Calc cal(10);
	cal.add(10).sub(1).mult(2).print();
```



```cpp
Calc cal(10);
Calc &temp1 = cal.add(10);
Calc &temp2 = temp1.sub(1);
Calc &temp3 = temp2.mult(2);
temp3.print();
```





## 8.8 클래스 코드와 헤더 파일



헤더에서는 using namespace std를 안 쓰는 것이 좋다.



### main.cpp

```cpp
#include "Calc.h"

int main()
{

	Calc cal(10);
	cal.add(10).sub(1).mult(2).print();
}
```





### Calc.h

```cpp
#pragma once

#include <iostream>


class Calc
{
private:
	int m_value;

public:
	Calc(int init_value)
		: m_value(init_value)
	{}

	Calc& add(int value);
	Calc& sub(int value);
	Calc& mult(int value);

	void print();
};

```

어떤 경우엔 정의를 헤더에 넣는 걸 권장하는 경우가 있다. template로 구현된 body를 소스에서 구현하기에 번잡할 수도 있음. 



### Calc.cpp

```cpp
#include "Calc.h"


Calc& Calc::add(int value) { m_value += value; return *this; }
Calc& Calc::sub(int value) { m_value -= value; return *this; }
Calc& Calc::mult(int value) { m_value *= value; return *this; }

void Calc::print()
{
	using namespace std;
	cout << m_value << endl;
}
```









