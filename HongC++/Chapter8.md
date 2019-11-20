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























