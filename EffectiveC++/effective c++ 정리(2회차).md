# Introduction

### 함수 declaration과 definition

함수 선언 : 함수 시그니처를 표시(파라미터, 리턴 값)

함수 정의 : 몸체 등 구체적으로 표시



### 생성자

default constructor

copy constructor

copy assignment operator

```cpp
class Widget{
 public:
  Widget();								// default constructor
  Widget(const Widget& rhs);			// copy constructor
  Widget& operator=(const Widget& rhs);	// copy assignment operator
}

Widget w1;								// invoke default constructor

Widget w2(w1);							// invoke copy constructor
Widget w3 = w2;							// invoke copy constructor
bool hasAcceptableQuality(Widget w);	// invoke copy constructor(pass-by-value)

w1 = w2;								// invoke copy assignment operator
```





### undefined behavior

런타임에 무슨 일이 일어날지 몰라 발생하는 에러

프로그램이 정상적으로 작동할 수도, 이상한 값을 뱉을 수도 있다.





# Chapter 1. Accustoming Yourself to C++



## Item 1: C++을 언어들의 연합체로 봐라

오늘날 C++은 멀티패러다임 프로그래밍 언어다: 절차적, 객체지향적, 함수적, generic, 메타프로그래밍 특징들을 모두 갖고 있다.

- C
- Object-Oriented C++ : 클래스, 상속, encapsulation, 다형성, 가상함수
- Template C++ : generic 프로그래밍스러운 부분.
- STL



### 특이사항

- C에서는 pass-by-value보다 pass-by-ref가 더 효율적이다.
  OOC++에서 사용자 정의 ctor, dtor의 경우에는 pass-by-reference-to-const가 보통 더 빠르다.
  Template에서도 타입을 모르고 짜기 때문에 또 그렇다.
  STL은 C의 pointer에 기초해서 오브젝트들이 만들어지기 때문에 pass-by-value가 빠르다.



## Item 2: `#define`보다 `const`, `enum`, `inline`을 선호하라.

= 전처리기보다 컴파일러를 선호하라.

#define은 언어의 부분이라고 할 수 없다.



#define의 symbolic name은 컴파일러에게 보이지 않는다. -> symbol table에 들어가지 않는다.

#define은 scope를 가리지 않기 때문에 클래스 specific한 constant를 만들 수 없다.



### static class integral member variable

static, integral type(int, char, bool)의 class-specific constant는 선언할 때 정의를 하지 않아도 된다.(값을 주지 않아도 된다)

헤더파일에서:

```cpp
class GamePlayer {
    private:
    static const int NumTurns = 5;
    int scores[NumTurns];
}
```



그럼 impl. 파일에서 다음과 같이 정의해야 한다:

```cpp
const int GamePlayer::NumTurns;
```

단, 이미 값을 초기화했기 때문에 초기화는 허용되지 않는다.



클래스 선언에서 초기화를 허용하지 않는 컴파일러도 있다.

그럴 때는 다음과 같이 짤 수 있다:

```cpp
class CostEstimate {
    private:
    static const double FudgeFactor;			// declaration; header file
};

const double CostEstimate::FudgeFactor = 1.35;	// definition; imple. file
```



#### cf. integral type

bool, char, int -> **통합 정수 타입(integral type)**. 정수로 치부될 수 있는 타입들. 유사하기 때문에 bool, char, short와 같은 타입은 int로 타입 승격(promotion)이 되기도 한다.

통합 정수 타입 + double(부동소숫점 타입) -> 산술가능 타입(arithmetic type)

float + double -> 실수 타입



### enum hack

하지만 클래스 선언에서 초기화를 해주지 않는 방법의 경우에, GamePlayer::scores[NumTurns]에서와 같이 클래스 컴파일 중에 배열의 크기를 알아야 하는 예외적인 상황이 있을 수 있다.

그럴 땐 enum을 쓴다. 이는 enum이 정수로 쓰일 수 있다는 점을 활용한다.

```cpp
class GamePlayer {
    private:
    enum { NumTurns = 5 };
    
    int scores[NumTurns];
}
```



### 매크로 함수

매크로 함수의 비정상적인 작동을 주의해라. 대신 inline function template을 쓸 수 있다.

```cpp
template<typename T>
inline void callWithMax(const T& a, const T& b) // T가 무엇인지 모르기 때문에
{												// reference-to-const로 전달
    f(a > b ? a : b);
}
```

이러한 방식으로는 scope와 access rule도 지킬 수 있다.(class private member 등에서 특히 필요)



#### cf. inline function이란?

성능 향상을 위해 코드에 함수의 body를 그대로 넣어서 컴파일하는 것이라고 이해하면 될 듯.

- 장점(매크로와 대비해서)
  1. 전달인자에서 데이터형 체크 가능(매크로에서는 파라미터와 리턴 타입을 명시할 수 없음)
  2. 일반 함수처럼 사용 가능(매크로에서는 변수를 넘겨줄 경우에 이상한 값이 나오기도)
  3. 디버깅 가능
- 단점
  1. 실행 코드가 커진다.
  2. 구현을 짧게 작성해야 한다. 길어진다면 컴파일러는 인라인 함수를 일반 함수로 취급하게 된다.





## Item 3: 언제나 가능하다면 `const`를 써라.

컴파일러에게 변하지 말아야 할 변수들을 알려줄 수 있으며, 굉장히 다양한 곳에 쓸 수 있다.



```cpp
const char * const p = greeting;
```

\* 기준 좌측은 포인터의 대상이 const라는 것(type과 const의 순서는 바뀌어도 됨),

우측은 포인터 자체가 const라는 것을 의미



### iterator

iterator 자체가 포인터에 해당하고, 법칙은 위와 반대로 생각해야 한다.

```cpp
const std::vector<int>::iterator iter 	// 포인터 자체가 const
std::vector<int>::const_iterator cIter  // 가리키는 대상이 const
```



### 함수 const

파라미터, return값, member function, 그 function 전체에도 const를 붙일 수 있다.



return에 const를 왜 쓰냐고 할 수도 있겠지만, typo error를 방지해주는 효과도 있다.

```cpp
class Rational {...};
const Rational operator*(const Rational& lhs, const Rational& rhs);

// ... //

Rational a, b, c;

(a * b = c;)		// 비교를 하려다 실수로 할당을 한 경우
					// a * b의 결과값이 const라서 c를 할당할 수 없게 된다.
```



#### const 멤버 함수

const 오브젝트에서 호출할 수 있는 함수가 무엇인지 구분하기 위함.

이점은:

1. object를 수정해도 되는 함수가 무엇인지 파악하기 쉽다.
2. 코드 효율성 향상 - by-referece-to-const를 통해 효율성 향상이 가능한데, 이 때 object 전달 및 사용이 가능하려면 const 멤버 함수를 써야 한다.



cf. const 객체 - 멤버 변수를 초기화한 이후엔 변경할 수 없는 객체



**예제**

```cpp
char& operator[](std::size_t position)
{ return text[position]; }
```

non-const operator[]의 리턴 타입은 refererence to a char임 -> 실제로 변경이 가능함



#### member function이 const라는 것의 의미는 무엇일까?

1. **bitwise constness(physical constness)**

   멤버 함수가 멤버를 변경시킬 수 없는 경우에만 const를 붙인다.

   이는 c++의 constness 정의와도 같지만, 실제로 이 의미대로 구현돼도 const하게 작동하지 않는 경우들이 있다. 

   ```cpp
   class CTextBlock {
       public:
       ...
       char& operator[](std::size_t position) const
       { return pText[position]; }
       
       private:
       char *pText;
   }
   
   const CTextBlock cctb("Hello");
   char *pc = &cctb[0];
   
   *pc = 'J';		// reference를 받아왔기 때문에 변경이 가능하다
   ```

   

2. **logical constness** - 이걸 따르길 권장

   const 멤버 함수가 오브젝트의 멤버를 약간씩 변경시킬 수 있다 ㅡ 단 클라이언트가 감지하지 못하는 경우에만

   근데 컴파일러는 bitwise const 법칙을 따르고, 함수 내에서 멤버를 변경시킬 수 없게 하는데 어떻게 하지?

   -> **mutable**을 쓴다 : mutable은 데이터 멤버를 bitwise constness로부터 해방되게 만든다.

   ```cpp
   class CTextBlock {
     public:
       std::size_t length() const;
       
     private:
       char *pText;
       mutable std::size_t textLength;
       mutable bool lenthIsValid;
   };
   
   std::size_t CTextBlock::length() const
   {
       if (!lengthIsValid) {
           textLength = std::strlen(pText);
           lengthIsValid = true;
       }
       
       return textLength;
   }
   ```

   

내가 이해하기로 1. bitwise constness는 애초에 class의 문법적 한계 때문에 지켜질 수 없는 법칙이므로, 차라리 이를 좀 더 완화시켜서(이해하는 김에 우리가 실제로 사용하는 양태에 적합한 형태로) 이해하는 것이 2. logical constness이다.





## Item 4: 오브젝트를 사용하기 전에 초기화해라.

초기화가 알아서 수행될지는 경우마다 다 다르다.

C++의 C 파트의 경우 초기화는 런타임 cost를 발생시키지만, 일어날 것이라는 보장이 없다.

-> 항상 오브젝트를 쓰기 전에 초기화 하라.



클래스의 경우 할당(assignment)과 초기화(initiaialization)를 혼동하지 말 것.

빌트인 타입(e.g. int)의 경우 할당 이전에 초기화가 될 것이라는 보장이 없다.



할당 방식은 빌트인 타입이 아닌 user defined 멤버 변수들에 값을 할당할 때 default constructor를 부른 다음 값을 할당하지만, 

초기화 방식은 복사 생성자를 사용한다 -> 더 효율적.

빌트인 타입의 경우에는 초기화 방식, 할당 방식의 비용에 차이가 없다. 하지만 일관성을 위해 초기화해주자.(초기화 하지 않으면 undefined behavior로 읻어질 수 있다)



user defined 변수들의 경우 default constructor로 초기화해주는 방법도 있다.

```cpp
ABEntry::ABEntry()
: theName(),		// 이 부분을 member initialization list라고 부름
  theAddress(),
  thePhones(),
  numTimesConsulted(0)
  {}
```



멤버변수는 선언된 순으로 초기화된다.



### 다른 translation unit에서 정의된 non-local static 오브젝트의 초기화 순서

static object - stack, heap object는 제외, global object, namespace scope object, class 안에서 static으로 선언된 obejct, function 안에서 static 선언 obejct, **file scope**에서 static 선언 obejct가 포함됨.

local static object - 함수 안에 선언된 static object

non-local - 나머지 전부.

static object는 main이 실행이 끝날 때 destructor가 불린다.



**translation unit** - single object file을 만들어주는 소스 코드. 보통 inlcude된 파일들과 하나의 소스 파일을 가리킨다.



다른 translation unit에 있는 non static object가 초기화 때 다른 상대편을 사용한다면 순서가 정의되어있지 않아 문제가 된다.



```cpp
class FileSystem {
    public:
    std::size_t numDisks() const;
    
};
extern FileSystem tfs;	// client들에게 쓰라고 object를 선언(정의는 라이브러리 cpp 파일 내에)
}
```

FileSystem object는 **non-trivial**이다 -> construct 되기 전에 쓰는 것은 재앙이다.



해결책은,

함수 내에서 static으로 선언하여 local static object로 만드는 것이다.

함수는 해당 변수의 reference를 반환하도록 한다 -> **Singleton**

해당 함수를 부르지 않으면 object를 constr/destr하는 비용도 생기지 않는다.



### 멀티스레드

멀티스레드 환경에서는 non-const static object(local이든 non-local이든)는 멀티스레드에서 문제를 일으킬 가능성이 있다.

-> 프로그램 시작하는 부분의 single thread 로직에서 모든 reference-returning 함수를 직접 호출하도록 하면 된다. -> race condition을 피할 수 있다.









































