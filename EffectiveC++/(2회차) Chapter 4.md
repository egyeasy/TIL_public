# Chapter 4. Designs and Declarations

인터페이스를 디자인 하는 데 가장 중요한 가이드라인:

**정확하게 사용하기는 쉽고, 틀리게 사용하기는 어려워야 한다**

이 가이드라인을 토대로 정확성, 효율성, 캡슐화, 유지보수성, 확장성, 컨벤션 준수 등의 주제에 대한 논의가 가능해진다.

다음 논의들이 너가 알아야하는 모든 것은 아니지만 중요한 것들을 강조해서 알려준다.





## Item 18: 인터페이스를 올바르게 쓰기는 쉽게, 틀리게 쓰기는 어렵게 만들어라.

C++에는 함수 인터페이스, 클래스 인터페이스, 템플릿 인터페이스 등 인터페이스가 넘쳐난다.

클라이언트가 너가 만든 인터페이스를 잘못 쓴다면 너에게도 일정 부분 책임이 있다.

이상적으로는, 인터페이스를 잘못 쓸 경우 컴파일이 되지 않아야 한다.



예시를 살펴보자.

```c++
class Date {
  public:
    Date(int month, int day, int year);
};
```

여기서 나올 수 있는 실수는

1. 일/월 등의 날짜의 자리를 바꿔서 쓴다.
2. 월에 들어갈 수 없는 숫자를 쓴다.



### 타입 검증

많은 클라이언트 에러들은 새로운 타입을 도입함으로써 해결 가능하다.

```c++
struct Day {
  	explicit Day(int d)
        : val(d) {}
    int val;
};
```

와 같은 식으로 타입 정의하고

```c++
classs Date {
  public:
    Date(const Month& m, const Day& d, const Year& y);
};
```



이렇게 되면 다음과 같은 방식으로 써야 한다.

```c++
Date d(Month(3), Day(30), Year(1995));
```

encapsulated 데이터를 관리하는 클래스들의 기능을 좀 더 갖추면 좋겠지만(데이터의 유효성을 검증하는 기능 같은 걸 말하는 듯) 이 정도로도 인터페이스를 잘못 사용하는 에러를 어느 정도 막을 수 있다.



### 유효성 검증

이제 들어오는 값을 검증하는 방법을 살펴보자. enum을 쓰는 방법도 있지만,  enum은 int처럼 사용될 수 있으므로(item 2) type-safe하지 않다. 더 안전한 방법은 유효한 모든 Month들의 집합을 미리 정의하는 것이다.

```c++
class Month {
  public:
    static Month Jan() {return Month(1);}
    
  private:
    explicit Month(int m);
};

Date d(Month::Mar(), Day(30), Year(1995));
}
```

객체 대신에 함수를 쓰는 게 이상해보였다면, Item 4에서 non-local static object를 쓰는 것이 문제가 될 수 있다는 점을 상기해라.(초기화 순서가 정해지지 않아서 undefined behavior가 발생)



### 타입에 대한 제한

클라이언트 에러를 방지하는 또 다른 방법은 타입으로 할 수 있는 것을 제한하는 것이다.

일반적인 방식은 const를 달아서 user-defined type의 잘못된 사용을 막는 것이다.(item 3)

```c++
if (a * b = c)
```

이것은 또다른 가이드라인이기도 하다: **다른 좋은 이유가 없다면, 당신이 정의한 타입이 built-in 타입과 일관되게 작동하도록 만들어라.**

불필요한 비호환성을 피하는 진짜 이유는 인터페이스가 일관되게 작동하도록 만들기 위함이다.



### 사용자에게 무언가를 기억하도록 만들지 마라(shared_ptr)

```c++
Investment* createInvestment();
```

Item 13에서 이러한 팩토리 함수의 문제를 말한 바 있다. 1) delete pointer 하는 것을 까먹는 경우 2) 같은 포인터를 두 번 delete하는 경우



이를 대비해서 shared_ptr을 쓸 수 있지만 사용자가 그걸 쓰는 것을 까먹는다면? 애초에 그걸 방지하기 위해 shared_ptr을 return 하도록 선언하는 방법이 있다.

```c++
std::shared_ptr<Investment> createInvestment();
```



게다가 item 14가 설명하듯이 shared_ptr을 반환하는 방법에서 deleter를 resource-release function으로 지정해줄 수도 있으므로 리소스 해제와 관련한 클라이언트 에러도 방지할 수 있다.

resource-destruction 메커니즘을 getRidOfInvestment로 만들어놨는데 사용자가 delete를 쓰는 것을 방지하도록 하려면 어떻게 해야할까? 해당 해제 함수를 deleter로 지정을 해주면 된다.

``` c++
std::shared_ptr<Investment> plnv(0, getRidOfInvestment); // 컴파일 오류
```

첫 번째 인자가 포인터여야 하므로 위와 같이 쓰면 안 된다.

```c++
std::shared_ptr<Investment> plnv(static_cast<Investment*>(0), getRidOfInvestment); // 컴파일 성공
```

물론 null로 초기화 후에 값을 할당하는 것보다 곧바로 retVal의 생성자에 raw pointer를 할당하는 것이 더 좋다(Item 26 참고)



shared_ptr의 좋은 기능은 "cross_DLL problem"이라는 잠재적인 클라이언트 에러를 제거해준다는 것이다. 서로 다른 DLL에서 각자 new/delete를 맡아서 하게 되면 런타임 에러를 발생시킬 수 있다. 하지만 shared_ptr의 default deleter는 shared_ptr이 create된 DLL의 delete를 쓰기 때문에 그 문제를 피할 수 있따.



이번 아이템은 shared_ptr에 관한 것은 아니라, 인터페이스를 올바르게 쓰기 쉽게 하고 잘못 쓰기 어렵게 만드는 것이지만, shared_ptr은 대표적인 좋은 방안이다.

boost의 shared_ptr은 raw pointer의 두 배 크기지만 다양한 유용한 기능을 제공한다. 많은 어플리케이션에서 그 추가적인 런타임 코스트는 알아차리기 어렵지만 클라이언트 에러의 감소는 눈에 띌 것이다.







## Item 19: 클래스 디자인을 타입 디자인처럼 취급해라.

다른 OOP 언어에서와 같이, C++에서도 클래스를 정의하는 것은 새로운 타입을 정의하는 것이다. 따라서 built-in type을 디자인하는 데 쓰는 노력 만큼이나 조심스러운 접근을 클래스 디자인할 때에도 해야 한다.

좋은 타입을 디자인하는 것이 어렵기 때문에 좋은 클래스를 디자인하는 것도 어렵다.

좋은 클래스나 타입은 자연스러운 syntax, 직관적인 의미, 그리고 하나 또는 그 이상의 효율적인 구현체들을 가지고 있어야 한다.

효율적인 클래스를 디자인하기 위해 당신이 직면하는 이슈를 이해해야 한다:

- **new type이 어떻게 생성되고 소멸되어야 하는가?**

  constructor, destructor, 메모리 할당과 해제

- **객체 초기화가 객체 할당과 어떻게 달라야 하는가?**

  constructor, 할당 연산자들 간의 작동과 차이점을 결정한다.

- **객체가 pass-by-value되는 것은 무엇을 뜻하는가?**

  copy constructor가 불린다.

- **새로운 타입에 대한 적합한 value에 대한 제약이 무엇인가?**

  데이터 멤버들은 특정 조합의 값을 가지고 있어야만 유효하다. 이 조합은 클래스가 가지고 있어야 할 불변 요소들을 결정한다. 불변 요소들은 에러 체킹을 결정한다.

- **타입이 상속 그래프에 적절하게 들어맞는가?**

  존재하는 클래스를 상속받을 때 함수가 virtual인지 아닌지에 영향을 받게 된다. 특히 desctructor에 신경을 써라.

- **타입에 대해서 어떤 타입 변환이 허용되는가?**

  T1에서 T2로 implicit한 타입 변환을 원한다면 T1 클래스 내에 operator T2와 같은 타입 변환 함수를 작성하거나, T2의 (하나의 argument로 호출할 수 있는) non-explicit constructor를 호출함으로써 가능하다.

  explicit 버전만 원한다면 type conversion operator와 non-explicit constructor with one argument는 피해야 한다.

- **타입에 대한 연산자와 함수로 무엇이 적절한가?**

  클래스에서 선언하는 멤버, non-멤버 함수가 무엇일지를 결정한다.

- **어떤 표준 함수가 불허용되어야 하는가?**

  private될 함수가 무엇인지를 결정한다.

- **타입의 멤버에 누가 접근 권한을 갖는가?**

  public, private, protected, friends, nest class

- **타입의 "선언되지 않은 인터페이스"가 무엇인가?**

  성능, exception safety, 리소스 사용과 관련해서 보장을 해주고 있는가? 이러한 보장을 해주려고 한다면 클래스 구현에 제약이 가해질 것이다.

- **타입이 얼마나 일반적인가?**

  사실은 타입의 패밀리를 정의하고 있는 상황일 수도 있다. 그 때는 class template을 정의해야 한다.

- **새로운 타입이 정말로 필요로 하는 것인가?**

  존재하는 클래스에 functionality를 추가하는 것이라면, non-member function과 template을 정의하는 것만으로도 가능하다.

이 질문들은 답하기 어렵고, 그래서 효율적인 클래스 정의가 어렵다. 잘만 되면 그러한 노력은 투자할 가치가 있다.





## Item 20: pass-by-value보다 pass-by-reference-to-const를 선호하라.

### pass-by-value의 문제

C++은 default로 함수를 통해 값을 전달할 때 pass-by-value를 사용한다.

따라서 다른 설정을 해주지 않으면 function의 파라미터들은 전달된 argument들의 copy로 초기화된다.

함수의 caller들 또한 function에서 리턴된 값의 'copy'를 전달받게 된다.

이러한 copy들은 객체의 copy constructor들에 의해 생성되고, 이는 pass-by-value를 비용이 많이 드는 연산으로 만들게 된다.

그 과정을 좀 자세히 살펴보면:

1. 실제로 함수 내부에서 pass-by-value로 던져진 파라미터를 사용할 때 객체의 contructor와 destructor가 모두 불리게 된다.
2. 그 뿐만이 아니다. 객체 안에는 멤버 변수들이 있으므로 멤버들의 constructor가 불려야 하고, 상속을 받고 있다면 부모 객체의 constructor, 부모 객체의 멤버들의 constructor도 불려야 한다. 
3. destructor의 경우도 마찬가지다.



### pass-by-reference-to-const

이러한 construction과 destruction을 피해갈 수 있는 방법이 있다 => **pass by reference-to-const**

```c++
bool validateStudent(const Student& s);
```

이 때 const를 붙이는 이유는,

pass-by-value 방식에서는 함수 내부에서 객체의 copy를 사용하기 때문에 caller가 객체에 변경이 가해질 것을 걱정하지 않아도 됐다.

하지만 reference로 던져줄 경우 변경을 우려해야하기 때문에, 그 걱정을 하지 않게 const로 전달해주는 것이다.



### slice problem 또한 회피 가능함

derived 클래스 객체가 pass-by-value를 통해 base class 객체로 전달될 경우 base class constructor로 초기화되고, 그래서 derived 부분은 잘려나간다.(sliced) 

따라서 파라미터의 virtual 메소드를 실행하더라도 이는 base class의 메소드를 실행하게 될 것이다.

그러한 문제 또한 reference-to-const로 해결할 수 있다.

```c++
void printNameAndDisplay(const Window& w) {
	std::out << w.name();
  w.display();
}
```

이제 파라미터는 어떤 타입으로 전달되었는지와 상관없이 실제 타입대로 작동하게 된다.



c++ 컴파일러에서 레퍼런스는 포인터와 유사하게 구현되어 있다. 그렇기에 레퍼런스로 전달하는 것은 포인터를 전달하는 것과 같다.

다만 빌트인 타입, iterator, fuction object의 경우 pass-by-value가 더 빠르게 되도록 구현되어 있고, slicing problem을 겪지 않는다.



### 작은 객체라고 pass-by-value해서는 안 된다.

어떤 이들은 빌트인 타입이 작기 때문에, 작은 타입들은 pass-by-value로 넘겨줘야한다고 생각하는데 이는 근거없다. 하지만 객체가 작다는 것이 copy constructor를 호출하는 비용이 싸다는 것을 의미하는 것은 아니다. ex) STL 컨테이너와 같은 객체들은 포인터 말고는 더 가진 것이 거의 없지만 가지고 있는 것을 복사하는 데는 비용이 매우 많이 든다. 

작은 객체들이 비용이 적은 constructor를 가지고 있을 경우에도 **성능 문제**가 발생할 수 있다. 어떤 컴파일러들은 user-defined와 빌트인 타입이 실질적으로 같은 representation을 가지고 있더라도 다르게 취급한다. ex) 어떤 컴파일러들은 double을 레지스터 하나에 넣으면서 double만으로 이뤄져있는 객체를 넣는 것은 거부한다. 이 경우에는 레퍼런스로 전달한다면 컴파일러들이 포인터를 레지스터에 넣을 것이므로 해결될 것이다. 

pass-by-value에 있어 또다른 문제는 user-defined에서 **사이즈가 변할 수 있다**는 것이다. 초기엔 작았던 객체가 구현을 함에 따라 커질 수도 있다. 심지어 다른 C++ 구현을 쓰게 되면 또 달라진다. string 타입의 크기가 다른 라이브러리 구현체보다 7배 큰 구현체도 있다.





## Item 21: 객체를 리턴해야할 때 레퍼런스를 리턴하지 마라.

만약 pass-by-reference의 장점을 알아서 계속해서 그것만을 쓰려고 하면 문제가 생길 수 있다 -> 존재하지 않는 객체의 레퍼런스를 pass하려고 할 때이다.

레퍼런스는 하나의 name이고, name은 **존재하는 객체**를 위한 것이다. 그렇다면 그 객체를 위한 다른 이름 또한 존재해야 한다. 그러려면 이미 존재하는 객체여야 한다.

하지만 곱셈에 있어서 그러한 객체가 미리 존재한다는 보장이 없다.

```c++
Rational a(1, 2);
Rational b(3, 5);

Rational c = a * b; // 3/10
```

3/10이라는 Rational이 미리 존재한다는 것은 비합리적이어보인다. 그렇기 때문에 연산자가 스스로 reference를 가질 객체를 생성해야 한다.



1. stack에 객체를 생성하기

지역 변수를 선언함으로써 스택에 생성하는 것이 가능하다.

```c++
const Rational& operator*(const Rational& lhs, const Rational& rhs)
{
    Rational result();
    return result;
}
```

목표는 constructor를 부르지 않는 것이었기 때문에, local 객체를 생성하는 것이 못마땅할 수 있다.

더 심각한 문제는 local 객체는 함수를 나가면서 소멸되는데, **소멸된 객체에 대한 레퍼런스를 반환한다**는 것이다.

이는 undefined behavior로 이어진다.



2. heap에 객체 생성하기

new를 사용하는 방법이다.

```c++
const Rational& operator*(const Rational& lhs, const Rational& rhs)
{
    Rational *result = new Rational(lhs.n * rhs.h, lhs.d * rhs.d);
    return *result;
}
```

여기서도 여전히 constructor call이 불린다는 점에는 비용을 지불해야 한다.

하지만 또다른 문제가 존재한다: **누가 delete를 부를 것인가?**

이 같은 방식으로 할 때 이 경우에는 delete를 해줄 수 없는 문제가 발생한다.

```c++
Rational w, x, y, z;
w = x * y * z;
```

여기서 *를 통해 반환되는 포인터는 숨겨지기 때문에 delete를 부를 수가 없어진다.



3. static 객체 선언

여기서 두 방식 다 constructor를 호출하게 된다는 것을 알았을 것이다. 또한 우리의 처음 목표는 constructor 호출을 피하는 것이었다. 이에 따라 새로운 방식을 떠올리게 될 수 있는데, 이는 **함수 안에서 선언한 static 객체의 레퍼런스를 리턴하는 것**이다.

```c++
const Rational& operator*() // 생략
{
    static Rational result;
    
    result = ...;
    
    return result;
}
```

하지만 static 객체를 쓰는 모든 디자인에서와 같이 이는 **thread-safety** 문제가 존재한다.

게다가 더 파고들게 되면, 다음과 같은 문제가 발생한다.

```c++
Rational a, b, c, d;

if((a * b) == (c * d)) {
    // do sth
} else {
    // do other sth
}
```

여기서 a, b, c, d의 값에 상관없이 항상 ==이 성립하는 문제가 발생한다.

이는 연산자 *의 결과값이 항상 같은 객체의 레퍼런스를 반환하기 때문이다.



4. static array 쓰기

이 정도로 충분할텐데도 또다른 방법을 강구하는 이가 있을 수 있다.

이것의 문제를 짚어보자면,

1) n을 정하는 문제. n이 너무 작으면 리턴할 value를 담을 칸이 부족할 것이다. n이 너무 크면 function이 불리는 첫 번째에 n개의 모든 constructor가 불리게 된다. 나중엔 n개의 dtor가 불리게 될 것이다.

2) array의 객체에 값을 할당하는 문제에도 cost가 든다. 할당에는 dtor(원래 값을 소멸)와 ctor(새 값을 복사)하는 비용이 드는데, 우리의 목표는 ctor와 dtor를 피하는 것이었다!

vector를 쓰는 것도 그닥 더 좋지 않다.



새로운 객체를 리턴하는 함수를 쓰는 법은 **새로운 객체를 리턴**하도록 하는 것이다.

```c++
inline const Rational operator*(const Rational& lhs, const Rational& rhs)
{
    return Rational(lhs.n * rhs.n, lhs.d * rhs.d);
}
```

return value의 ctor와 dtor를 부르면서 비용이 발생하지만, 길게 보면 이것은 정확한 동작을 위한 작은 비용이다.

또한 컴파일러가 때때로 behavior가 바뀌지 않는 선에서 효율성을 위해서 constrction과 destruction을 없애줄 수도 있기 때문에 걱정하는 ctor/dtor 비용이 발생하지 않을 수도 있다.

너는 따라서 return을 할때 정확한 동작이 무엇인지에 따라 선택만 하면 된다. 나머지는 컴파일러 판매업자들이 고민해서 비용을 최소화해줄 것이다.





## Item 22: data 멤버를 private으로 선언해라.

여기서는 먼저 data member가 public이 되면 안 되는 이유를 살펴보고, 다음으로 public이 되면 안 된다는 논의가 protected에도 똑같이 적용된다는 점을 밝힐 것이다. 따라서 데이터 멤버들이 private이 되어야 한다는 결론을 이끌어낼 것이다.



### 문장 일관성(syntactic consistency)

데이터 멤버가 public이 아니면 클라이언트가 객체에 접근하는 방법은 멤버 함수밖에 없다. 그렇다면 사용자는 클래스의 멤버에 접근하기 위해 괄호를 써야할지 말아야할지 머리를 긁적이게 되는 경우가 없을 것이고, 이는 비용을 상당히 줄여준다.



### 접근 통제(control over accessibility)

data를 public으로 두면 누구나 read-write 엑세스를 갖게 된다. 하지만 값에 대한 getter/setter를 이용하면 no access/read-only access/read-write access를 원하는 대로 구현할 수 있다.

접근 통제를 잘게 쪼개어서 할 수 있다는 것은 중요하다. data member는 숨겨져 있어야 하기 때문이다. 모든 데이터들이 getter/setter를 필요로 하는 경우는 거의 없다.



### 캡슐화(encapsulation)

함수를 통해 데이터 멤버에 접근하도록 만들어놨으면, 너가 나중에 데이터 멤버를 바꿔놓아도 클래스를 쓰는 사람은 전혀 알아차리지 못한다.

예시를 들어 설명하면,

```c++
class SpeedDataCollection {
  public:
    void addValue(int speed);
    double averageSoFar() const;
}
```

여기서 averageSoFar() 함수를 구현하는 방법이 두 가지가 있다.

1. 현재까지의 평균 속도를 데이터 멤버로 두는 것. 함수는 그 값을 리턴하기만 하면 된다.
2. 함수가 호출될 때마다 매번 값을 새롭게 계산하는 것.

1번 접근은 객체의 크기를 **크게** 만든다. 평균, 총 누적, 데이터 개수와 같은 멤버 변수들을 위한 공간을 할당해야 하기 때문이다. 하지만 함수의 구현이 굉장히 간단하고, 속도가 빠르다.

2번 접근은 객체의 크기가 작지만, 함수가 호출될 때마다 계산해야 하므로 느리다.

메모리가 타이트한 기계에서는, 그리고 평균을 자주 호출하지 않아도 되는 어플리케이션에서는 2번 접근이 적절할 것이다.

평균이 자주 호출되는 경우, 그리고 속도가 중요한 경우, 메모리가 이슈가 되지 않는 경우에는 1번 접근이 적절할 것이다.

멤버를 함수로만 접근하게 캡슐화 함으로써 얻는 이점은,

너가 **인터페이스를 구현할 때 앞의 접근 방식을 마음대로 바꿔가면서 구현할 수 있다는 것**이다.

사용자는 다시 컴파일하기만 하면 된다.



### 캡슐화의 유연성(flexibility)

데이터 멤버를 캡슐화를 함으로써 구현 유연성을 얻을 수 있다. 그 예로, 데이터 멤버가 언제 read/write 되는지 쉽게 알 수 있고, 클래스 invariant와 함수의 pre/postcondition을 알 수 있고, 멀티스레드 환경에서 동기화를 수행할 수 있다.

캡슐화는 처음에 보기보다 더 중요한데, 데이터 멤버를 사용자에게서 숨기면 클래스 invariant들이 항상 유지됨을 보장할 수 있고(멤버 함수만 그들에게 영향을 줄 수 있기 때문에), 나중에 구현을 바꿀 수도 있다. 구현 사항을 public으로 공개해놓으면 수정할 수 있는 범위가 현저하게 제한 받는다. 너무 많은 클라이언트 코드가 broken 될 것이기 때문이다. 따라서 public은 unchangeable하다고 이해하는 것이 좋다(특히 광범위하게 사용되는 클래스는 더 그렇다). 하지만 광범위하게 사용되는 클래스는 구현을 더 나은 구현으로 대체함으로써 얻는 이점이 크기 때문에, 가장 캡슐화가 필요한 대상이기도 하다.



### protected에도 유사한 논의 적용 가능

public에서 문장 일관성(syntactic consistency), 잘개 쪼개어진 접근 제어(access control)에 대해 나눴던 논의는 쉽게 protected에도 적용된다.

그렇다면 캡슐화는 어떨까? 결론적으로 말해서 protected 데이터 멤버가 public에서보다 더 캡슐화되어 있다고 할 수 없다.

Item 23에서는 어떤 것의 캡슐화는 그것이 변화했을 때 코드가 broken 되는 양에 반비례한다고 설명한다. 따라서 데이터 멤버의 캡슐화는 그 데이터 멤버가 바뀌었을 때 broken 되는 코드의 양에 반비례 한다.

**public** 데이터 멤버를 삭제할 경우 그것을 사용하는 클라이언트 코드들이 broken된다. 이는 알 수 없을 정도로 많은 양이다. 따라서 public 데이터 멤버는 캡슐화되어야 한다.

**protected** 데이터 멤버를 삭제할 경우 이것을 쓰는 모든 derived class의 코드가 broken 된다. 따라서 이것 또한 알 수 없을 정도로 많은 양이다. 따라서 protected 또한 public과 비슷한 정도로 캡슐화되어있지 않은 것이다.

이는 비직관적이지만 숙련된 라이브러리 구현자들은 그것이 상당히 사실이라고 말할 것이다. 어떤 데이터 멤버를 public/protected로 선언하고 클라이언트가 그걸 쓰기 시작하면 그걸 바꾸기 무척 어렵다. 많은 코드들이 다시 쓰여지고, 다시 테스트 되고, 다시 문서화, 다시 컴파일되어야 한다.

따라서 캡슐화의 관점에서는 두 가지의 엑세스 레벨만 존재한다: private(캡슐화 제공), 나머지 전부(제공하지 않음)















































