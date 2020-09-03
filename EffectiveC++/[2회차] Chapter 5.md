# Chapter 5. Implementations

클래스의 적절한 정의, 함수의 적절한 선언은 가장 중요한 요소다.

그것만 잘하면 나머지 구현은 쉽다.

다만 그래도 주의할 점들이 많다.

1. 너무 일찍 변수를 정의하는 것은 성능 저하를 가져올 수 있다.
2. cast의 과도한 사용은 코드를 느리게 하고, 유지보수하기 어렵게 하고, 미묘한 버그들에 감염될 수 있다.
3. 객체의 internal에 대한 핸들을 리턴하는 것은 encapsulation을 좌절시키고 클라이언트들에게 dangling handle을 던져주게 될 수 있다.
4. exception의 영향을 생각하지 않으면 리소스 leak과 자료구조 corruption을 유발할 수 있다.
5. 과도한 inline 사용은 코드 양을 너무 불리게 될 수 있다.
6. 지나친 coupling은 지나치게 긴 빌드 타임을 초래할 수 있다.

앞으로 하나씩 알아보자.



## Item 26: 변수 정의를 가능한 한 뒤로 연기하라.

생성자나 소멸자가 있는 타입의 변수를 정의하게 되면, 변수를 정의할 때 생성 비용이 들게 되고, 변수가 scope 밖으로 벗어나면 소멸 비용이 든다.

쓰이지 않는 변수들에 대해서도 비용이 발생하므로 가능한 한 언제든 정의를 피하라.



너가 쓰이지 않는 변수를 정의하지 않는다고 생각하겠지만,

다음과 같은 예시를 생각해보라.

string encrypted를 정의한 후에 패스워드가 너무 짧아서 throw를 하게 되면 변수를 쓰지 않는 상황이 발생한다.

throw를 하게 되면 생성자와 소멸자에 대한 비용을 지불하게 된다.



따라서 필요할 때까지 encrypted의 정의를 연기하는 것이 좋다.

```cpp
	throw logic_error;
string encrypted;

return encrypted;
```

하지만 이것으로도 불충분하다.

encrypted는 argument 초기화 없이 정의되었기 때문이다.

item4에서 설명했듯이 지금 코드는 디폴트 생성자를 부르고 그 후에 값을 할당하는 것은 비효율적이다.



예를 들어 다음과 같이 encrypt가 수행된다고 하면:

```cpp
void encrypt(std::string& s);
```

다음과 같은 과정은 불필요하게 비효율적이다.

```cpp
{
    string encrypted;
    encrypted = password;
    ecrypt(password);
    return encrypted;
}
```

따라서 불필요하게 비용이 드는 기본 생성자를 부르지 않도록 하자.

```cpp
{
    string encrypted(password);
    
    encrypt(encrypted);
    return encrypted;
}
```

이것이 Item의 제목에서 "가능한 한 뒤로 연기하라"는 것의 진짜 의미다.

1. 변수를 쓰기 직전까지 변수의 정의를 연기해라.
2. 변수를 초기화하는 argument가 생길 때까지 변수의 정의를 연기해라.

이를 통해 불필요한 객체의 생성과 소멸을 피하고, 불필요한 기본 생성자를 피할 수 있다.

또한 변수들의 의미가 명확한 컨텍스트 속에서 변수를 초기화하는 목적을 문서화하기 쉽다.



### 루프의 경우는?

변수가 루프 안에서만 쓰이는 경우에 변수를 루프 안에서, 밖에서 중 어디서 정의할 것인가?

#### Approach A: outside

```cpp
Widget w;
for (int i = 0; i < n; ++i) {
    w = some value dependent on i;
}
```



#### Approach B: inside

```cpp
for (int i = 0; i < n; ++i) {
    Widget w(some value dependent on i);
}
```



두 접근법의 비용은 다음과 같다.

Approach A: 1 constructor + 1 destructor + n assignments

Approach B: n constructors + n destructors



assignment가 constructor&destructor pair보다 비용이 적게 들면 A가 효율적이다. 이는 주로 n이 큰 경우에 해당한다. 그렇지 않으면 B가 낫다.

게다가 A는 w를 larger scope에서도 보이게 하므로 이는 프로그램의 가독성과 유지보수성에 반한다.

결과적으로,

1. assignment가 constructor-destructor보다 비용이 싸고
2. 성능에 민감한 파트를 다룬다면

B를 쓰도록 하라.





## Item 27: 캐스팅을 최소화하라.

C++의 규칙은 타입 에러가 불가능한 것을 보장하도록 디자인되어있다.

이론적으로 네 프로그램이 정상적으로 컴파일 되면 그것은 어떤 객체에도 안전하지 않거나 비상식적인 연산을 시도하지 않는다.



불행하게도 캐스팅은 타입 시스템을 전복시키면서 알아차리기 쉬운, 또는 이상하고 미묘한 문제들을 낳는다.



일반적으로 같은 캐스팅을 수행하는 3가지 방법이 있다.

#### C-style

```c++
(T) expression
```

#### Function-style

```c++
T(expression)
```

#### new-style or C++-style

```c++
const_cast<T>(expression)
dynamic_cast<T>(expression)
reinterpret_cast<T>(expression)
static_cast<T>(expression)
```

const_cast : 객체의 const성을 던져버리기 위해 쓰임

dynamic_cast : 안전한 downcasting을 하기 위해 쓰임. old-style syntax로 수행될 수 없음. 많은 런타임 코스트

reinterpret_cast : 구현에 의존적인 결과(포인터를 int로 casting하는 것 같은)를 만들어내기 위한 low-level cast에 쓰임. low-level 밖에서는 거의 쓰이면 안됨.

static_cast : implicit conversion을 강제하기 위해 쓰임. 그 반대의 경우도 쓰임.(const -> non-const는 불가)



old-style도 여전히 합법적이지만, new style이 더 선호할만하다.

그 이유는

1. 코드에서 알아보기가 훨씬 쉽다.
2. 각 cast의 목적을 좁게 구체화함으로써 컴파일러가 에러를 진단하기 쉽게 만든다.



old-style을 쓰는 유일한 순간은 함수에 객체를 전달하기 위해 explicit 생성자를 호출할 때이다.

```c++
class Widget {
  public:
    explicit Widget(int size);
};
void doSomeWork(const Widget& w);
doSomeWork(Widget(15));					// function-style

doSomeWork(static_cast<Widget>(15));	// C++-style
```

객체 생성은 cast처럼 느껴지지 않기 때문에 나는 아마 function-style을 선호할 것이다.

(실제로 둘은 같은 기능을 하고 있다 - doSomeWork에 전달할 임시적인 Widget 객체를 생성)

하지만 core dump로 이어지는 코드의 경우에도 너가 작성할 때는 상당히 합리적이라고 느낀다.

그러니까 그 느낌을 무시하고 new-style cast를 항상 쓰는 게 낫다.



### cast는 의외의 기능을 수행한다

많은 프로그래머들이 캐스트가 컴파일러에게 한 타입을 다른 타입으로 다루라는 것밖에 안 시키는 걸로 알고 있다.

하지만 이는 오해다.

어떤 종류의 타입 변환이든 종종 런타임에 실행되는 (추가적인) 코드를 만들어내게 되는데,

```c++
int x, y;
...
double d = static_cast<double>(x) / y; // x를 y로 나눔. floating point division을 씀
```

int x를 double로 cast하는 것은 (추가적인) 코드를 만들어내게 된다.

이것은 많은 아키텍쳐에서 int의 표현과 double의 표현이 다르기 때문이다.

-> 그러니까 단순히 다른 타입으로 취급하는 것이 아니라 새로운 연산을 추가하는 것이다.



```c++
class Base {...};
class Derived: public Base {...};
derived d;
Base *pb = &d;
```

*pb와 &d 두 포인터는 같지 않을 수도 있다.

같지 않을 경우 런타임에 Derived* 포인터에 offset이 적용돼서 정확한 Base* 포인터 값이 가져와진다.

이 예는 하나의 객체가 여러 주소를 가질 수 있다는 것을 보여준다. 이것은 C++에서만 일어나는 일이다.

다중 상속을 쓰고 있을 경우엔 거의 항상 일어나고, 단일 상속에서도 일어날 수 있다.

따라서 C++에서 무언가가 어떻게 이뤄져있는지 함부로 가정하고 써서는 안 된다.



하지만 offset이 항상 쓰이는 것은 아니다.

객체가 lay out 되고 주소가 계산되는 방식은 컴파일러마다 다르다.

그것은 너가 어떻게 작동하는지를 알고 있는 cast가 다른 플랫폼에서는 작동하지 않을 수도 있다는 것을 의미한다





## Item 28: 객체 내부에 대한 "핸들"을 리턴하는 것을 피하라.

사각형과 관련된 어플리케이션을 다루고 있다고 가정하자.

사각형은 UpperLeft corner와 LowerRight corner로 표현될 수 있다.

Rectangle 객체를 작게 유지하기 위해 Point들을 struct에 담고, Rectangle은 그 struct의 포인터를 갖고 있게 했다고 하자.



```c++
class Point {
  public:
    Point(int x, int y);
    
    void setX(int newVal);
    void setY(int newVal);
};

struct RectData {
    Point ulhc;
    Point lrhc;
};

class Rectangle {
  private:
    std::shared_ptr<RectData> pData;
};
```

Rectangle 클라이언트는 Rectangle의 크기를 설정할 필요가 있을 수 있기 때문에

클래스는 upperLeft, lowerRight 함수를 제공하기로 한다.

하지만 Item 20에서 봤던 대로 `Point`는 user-defined type이므로 value로 전달하는 것보다 **reference로 전달하는 것이 빠르다.**

그래서 이 함수들을 reference로 리턴하게 만들었다고 해보자.

```c++
class Rectangle {
  public:
    Point& upperLeft() const { return pData->ulhc; }
    Point& lowerRight() const { return pData->lrhc; }
};
```

이것은 컴파일되긴 하지만 틀렸다. 자기모순이다.

1. 한편으로는 upperLeft와 lowerRight가 **const 멤버 함수**로 선언이 되어있다

   Rectangle 클라이언트들에게 Point가 무엇인지 알려주는 것까지만 제공하기 위해서이다.(변경은 불가하도록)

2. 다른 한편, 두 함수는 **private internal data에 대한 reference**를 리턴한다.

   호출자가 internal data를 변경할 수 있게 된다.

예를 들어:

```c++
Point coord1(0, 0);
Point coord2(100, 100);

const Rectangle rec(coord1, coord2);

rec.upperLeft().setX(50);
```

rec이 const임에도 Point들을 변경하는 것이 가능하다.



이는 두 가지 가르침을 준다.

1. 데이터 멤버는 그 멤버에 대한 **reference를 리턴하는 가장 접근성이 높은 함수** 만큼만 캡슐화 되어있다.

   upperLeft, lowerRight public 함수가 Point에 대한 reference를 제공하므로 Point는 사실상 public data member이다.

2. const 멤버 함수가 객체(Rectangle)의 밖에 저장되어 있는 데이터(Point)의 reference를 리턴하면, 함수의 호출자는 데이터(Point)를 변경할 수 있다.
   (이것은 bitwise constness의 단점이다 - Item 3)



여기서는 멤버 함수가 레퍼런스를 리턴했지만, pointer나 iterator를 리턴했어도 같은 이유로 같은 문제가 발생한다.

Reference, Pointer, Iterator는 모두 **handle**(다른 객체를 얻을 수 있는 수단)이다.

객체 내부에 대한 handle을 리턴한는 것은 객체의 캡슐화와 상충하는 리스크가 있다.

앞에서와 봤던대로, const 멤버 함수가 객체의 상태를 바꾸게 될 수도 있는 것이다.



### 멤버 함수에 대한 접근성

우리는 주로 객체의 "내부(internal)"를 data member라고 인식하지만,

public이 아닌 **멤버 함수**도 객체의 내부에 포함된다.

따라서 멤버 함수에 대한 handle을 리턴하지 않는 것도 중요하다.

즉 어떤 멤버 함수가 자신보다 접근성이 더 낮은 멤버 함수의 포인터를 리턴하는 일이 없어야 한다는 것이다.



### 해결책

앞에서 봤던 Rectangle 문제로 돌아오자.

upperLeft, lowerRight와 관렪된 문제에서 해결책은 리턴 타입에 const를 붙이는 것이다.

```c++
class Rectangle {
  public:
    const Point& upperLeft() const {...}
    const Point& lowerRight() const {...}
};
```

이런 디자인에서 클라이언트는 rectangle을 정의하는 **Point를 읽을 수 있지만 변경할 수는 없다**. -> upperLeft, lowerRight를 const로 선언하는 것이 거짓말이 아니게 된다.

객체의 **캡슐화** 문제와 관련하여서는, Rectangle을 이루고 있는 Point가 무엇인지 클라이언트들이 볼 수 있게 해놓았다 -> **캡슐화의 완화**라고 할 수 있다.

하지만 write access는 금지되어 있다 -> **제한된 완화**에 해당한다.



### dangling handle 문제

upperLeft, lowerRight는 여전히 객체 내부에 대한 handle을 리턴하고 있긴 하다.

이것은 dangling handle이라는 문제로 이어질 수 있다. -> handle이 더 이상 존재하지 않는 객체의 부분을 참조하는 것이다.

그렇게 사라지는 개체의 가장 흔한 케이스는 함수 리턴 value이다.

```c++
const Rectangle boundingBox(const GUIObject& obj);

GUIObject* pgo;
const Point* pUpperLeft = &(boundingBox(*pgo).upperLeft());
```

boundingBox에 대한 호출은 새로운, **임시적인** Rectangle 객체를 리턴할 것이다.

그 객체는 이름이 없으므로 temp라고 부르자.

temp에 대한 upperLeft가 호출되면, upperLeft는 temp의 내부에 대한 reference를 리턴한다.

문장의 끝에서 temp는 destroy 된다 -> temp의 Point들도 destroy된다. -> pUpperLeft는 존재하지 않는 객체를 가리키고 있게 된다.(dangling)



이것이 객체 내부에 대한 handle을 리턴하는 함수가 위험한 이유이다.

(이 문제에 있어서는) handle이 포인터인지, 레퍼런스인지, iterator인지는 중요하지 않고,

멤버 함수가 const 멤버 함수인지도 중요하지 않고,

멤버 함수가 const한 handle을 반환하고 있는지도 중요하지 않다.

중요한 것은 **handle이 리턴되고 있다**는 것이다. -> handle이 참조하고 있는 객체보다 handle 자신이 더 오래 살아남게 되는(dangle하게 되는) 리스크가 존재하게 된다.



그렇다고 handle을 리턴하는 멤버 함수를 절대로 쓰면 안 된다는 것은 아니다.

가끔은 써야 하는 예외가 있다.

operator[]는 string과 vector에 대한 individual element를 꺼낼 수 있게 하고,

operator[]는 컨테이너 안의 데이터에 대한 reference를 리턴하는 방식으로 작동한다.

컨테이너가 소멸되면 데이터도 소멸된다.



















