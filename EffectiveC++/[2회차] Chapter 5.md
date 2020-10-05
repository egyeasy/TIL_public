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

그것은 너가 어떻게 작동하는지를 알고 있는 cast가 다른 플랫폼에서는 작동하지 않을 수도 있다는 것을 의미한다.



캐스트의 흥미로운 점 중 하나는, 겉보기에는 맞는 것처럼 쓰기는 쉽지만 실제로는 틀릴 수 있다는 점이다.

많은 어플리케이션 프레임워크에서 derived class의 virtual 멤버 함수의 구현체는 base class 함수를 먼저 호출한다.





우리가 Window base class와 SpecialWindow derived class를 가지고 있다고 해보자.

둘 다 `onResize` 함수를 정의하고 있다.

게다가 SpecialWindow는 Window의 onResize를 먼저 호출하도록 기대된다고 하자.

다음과 같이 작성했을 때 맞는 것처럼 보이지만 실제로는 틀리다.

```c++
class Window {
  public:
    virtual void onResize() {...}
};

class SpecialWindow: public Window {
  public:
    virtual void onResize() {
      static_cast<Window>(*this).onResize();
    }
};
```

(old-style cast를 써도 결과는 같다)

결과적으로 Window::onResize가 호출된다.

하지만 너의 예상과는 다르게, **현재의 객체에 Window::onResize가 호출되지는 않는다!**

대신에 *this의 base class part가 **일시적으로 copy되어 생성되고** 이것에 대해 onResize가 호출되게 된다.

Window::onResize가 객체를 변경하는 로직을 수행한다면, 복사된 객체가 변경되게 된다.

SpecialWindow::onResize가 그 이후의 로직에서 변경을 수행한다면, 객체는 invalid한 상태로 변화하게 된다.



따라서,

컴파일러가 *this를 base class object로 다루지 않도록, 현재의 객체에 대해 base class version의 onResize 함수가 불리도록 하려면:

```c++
class SpecialWindow: public Window {
  public:
    virtual void onResize() {
        Window::onResize();
    }
};
```



### dynamic_cast

이러한 예제에서 또한 알 수 있는 것은

너가 cast를 하려고 할 때, 잘못된 접근을 하고 있을 수도 있다는 것이다.

이 상황에서는 dynamic_cast를 썼어야 했다.



주의할 점 : **dynamic_cast**는 상당히 느리다.

최소한 하나의 흔한 구현에서 클래스의 이름을 비교하는 방식으로 cast가 이루어진다.

이런 식으로 구현된 데는 특정한 이유가 있지만(dynamic linking 지원 관련)

아무튼 performance에 민감한 코드에서는 dynamic_cast에 유의해야 한다.



dynamic_cast를 쓰는 일반적인 목적은,

**객체를 다루기 위해 base class에 대한 pointer나 reference만 가지고 있는 상황에서**

**derived class로 여겨지는 객체에 대해 derived class operation을 수행**하기 위해서이다.

이러한 문제를 피하기 위해 두 가지 일반적인 방법이 있다.



1. **derived class를 직접적으로 가리키는 포인터를 담고 있는 컨테이너를 써라.**

   그렇게 함으로써 base class interface를 통해 객체를 다뤄야 하는 상황을 없애라.

   Window와는 다르게 SpecialWindow만이 blink() 함수를 가지고 있다면,

   다음과 같이 하는 대신에:

   ```c++
   typedef
       std::vector<std::shared_ptr<Window>>VPW;
   VPW winPtrs;
   
   for (VPW::iterator iter = winPtrs.begin();
        iter != winPtrs.end();
        ++iter) {
     if (SpecialWindow *psw = dynamic_cast<SpecialWindow*>(iter->get()))
         psw->blink();
   }
   ```

   다음과 같이 해라:

   ```c++
   typedef std::vector<std::shared_ptr<SpecialWindow>> VPSW;
   VPSW winPtrs;
   
   for (VPSW::iterator iter = winPtrs.begin();
        iter != winPtrs.end();
        ++iter)
     (*iter)->blink();
   ```

   물론 이러한 접근에서는 같은 컨테이너의 여러 종류의 Window 파생 클래스를 담을 수 없다.

   여러 Window type을 다루기 위해서는 여러 종류의 type-safe 컨테이너가 필요해진다.



2. **base class interface를 통해 쓸 법한 Window 파생 클래스의 기능들을 모두 base class의 virtual function으로 제공하라.**

   SpecialWindow만 blink할 수 있더라도 base class에도 해당 함수를 선언하는 것이다.

   ```c++
   class Window {
     public:
       virtual void blink() {}
   };
   
   // Window를 담은 container의 item들에 대해 blink() 호출
   ```



위의 2가지 방법 모두 보편적으로 적용 가능한 것은 아니지만 많은 경우에 있어 dynamic_casting의 대안을 제공해준다.

반드시 너가 피해야 하는 디자인은 cascading dynamic_cast이다.

(if, else if 마다 dynamic_cast를 통해 어떤 파생클래스인지를 비교)

이러한 코드는 크고 느리고, 보기에도 이상하다(Window class의 hierarchy가 바뀌면 저 코드도 바꿔야 하는 상황이 생긴다)

저런 코드는 virtual function을 호출하는 방식에 기반하여 대체되어야 한다.



좋은 c++ 코드는 cast를 거의 사용하지 않지만, cast를 모두 제거하는 것은 일반적으로 실용적이지 않다.

int to double cast를 cast를 쓰기에 합리적이지만, 꼭 필요한 상황이 아니기도 하다.

cast는 최대한 고립되어야 한다 -> interface가 내부적으로 지저분한 일들을 처리해줌으로써 client를 보호해야 한다.









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









## Item 29: exception-safe한 code를 위해 노력하라.

배경 이미지를 가지고 있는 GUI 메뉴를 표현하는 클래스를 가지고 있다고 해보자.

클래스는 thread 환경에서 사용될 수 있도록 디자인 되어서, 병행성 컨트롤을 위해 mutex를 가지고 있다.



```c++
void PrettyMenu::changeBackground(std::istream& imgSrc) {
  	lock(&mutex);
    
  	delete bgImage;
  	++imageChanges;
    bgImage = new Image(imagSrc);
    
    unlock(&mutex);
}
```

exception safety 관점에서 이 함수는 정말 나쁘다.

exception safety의 두 요건은 다음과 같다.

1. **리소스를 leak하지 않는다.**

   위 코드는 new Image가 exception을 뱉었을 때 unlock이 실행되지 않고, mutex를 영원히 갖고 있게 된다.

2. **자료구조가 corrupted되지 않는다.**

   new Image가 throw하면 gmImage는 delete된 객체를 가리키고 있게 된다.

   게다가 new image가 할당되지 않았음에도 imageChanges는 증가되었다.



1. 리소스 leak 문제 대응

   리소스 이슈에 대한 대처는 간단하다. Item 13, 14를 참고하여 적절한 방식으로 mutex가 해제되도록 만들 수 있다.

```c++
{
    Lock ml(&mutex);
    
    delete bgImage;
    ...
}
```

​	Lock과 같은 리소스 매니징 클래스의 장점은 함수를 짧게 만든다는 점이다.

​	unlock이 더이상 필요하지 않게 된다. 따라서 이해하기도 더 쉽다.



2. 자료구조 corruption 문제 대응

   exception-safe한 함수를 만들기 위해 세 가지 종류의 guarantee들 중에서 선택해야 한다:

   1) **the basic guarantee**

   exception throw가 발생하더라도 프로그램의 모든 것이 valid 상태에 있는 것.

   모든 객체나 자료구조가 corrupt되지 않고, 모든 객체가 내적으로 일관된 상태에 있는 것이다.

   하지만 프로그램의 정확한 상태는 예측 불가능하다.

   changeBackground 함수 도중에 exception이 발생하면 객체는 이전의 배경이미지를 가지고 있을 수도, default 배경 이미지를 가지고 있을 수도 있다.

   클라이언트는 그것을 예측할 수 없다.(알아내려면 멤버 함수를 불러서 확인해봐야 한다)

   

   2) **the strong guarantee**

   exception이 throw 됐을 때 프로그램의 상태가 변하지 않는 것을 보장한다.

   이러한 함수의 호출은 '원자적'이어서 성공하면 완전히 성공하고, 실패하면, 프로그램 상태는 함수가 호출되지 않았던 것처럼 된다.

   ​	

   strong guarantee를 보장하는 함수를 쓰는 것이 더 쉽다.

   strong에서는 오직 두 가지의 프로그램 상태만 존재하지 때문이다: 예상되는 성공적인 함수 실행 or 함수가 실행되었을 때의 프로그램 상태

   basic에서는 exception이 발생했을 때 프로그램은 어떤 유효한 상태로도 변할 수 있다.

   

   3) **the nothrow guarantee**

   exception을 throw하지 않을 것을 보장한다.

   모든 빌트인 타입에 대한 연산은 no-throw이다. -> exception-safe 코드를 작성하는 데 중요하다.

   #### empty exception specification

   ```c++
   int doSomething() throw(); // note empty exception spec.
   ```

   위의 spec.은 doSomething이 never throw라고 말해주지는 않는다.

   대신 doSomething이 exception을 던지면 그것은 심각한 에러이고, unexpected 함수가 불려야 한다는 것을 의미한다.

   이것은 사실 exception guarantee를 전혀 제공하지 않고 있는 것이다.

   함수의 선언만으로는 그 함수가 옳은지, 이식 가능한지, 효율적인지에 대해 알 수가 없으며 마찬가지로 exception safety를 보장하는지도 알 수 없다.

   그 모든 특징들은 함수의 정의에 의해 결정된다.



exception-safe한 코드는 위의 3가지 guarantee 중 하나를 반드시 제공해야 한다.

일반적인 규칙으로서 너는 가장 강한 guarantee를 제공하고 싶을 것이다.

nothrow 함수는 정말 멋지지만, C++의 C part가 아닌 부분에서 throw하지 않는 함수만 쓰기는 어렵다.

STL container와 같은 동적으로 할당되는 메모리는 충분한 메모리를 찾지 못하면 전형적으로 bad_alloc exception을 발생시킨다.

**그러니 만약 가능하다면 nothrow를 제공하고, 대부분의 함수에서는 basic과 strong guarantee 중에서 선택해야 한다.**



changeBackground 예제에서 strong gurantee를 제공하는 것은 **거의** 가능하다.

1. `bgImage` data member를 built-in Image* 포인터에서 shared_ptr로 바꾼다.(Item 13 참고)

   smart resource-managing pointer가 strong exception safety를 제공한다는 점은,

   Item 13에서 이것을 쓰는 것이 좋은 설계의 기초라고 했던 주장을 뒷받침해준다.

   

2. 문장의 순서를 바꿔서 image가 바뀌기 전에는 `imageChanges`를 증가시키지 않는다.

   어떤 일이 실제로 일어나기 전에 객체의 상태를 변경하지 않는 것이 좋은 정책이다.





이제 너가 직접 old image를 delete할 필요가 없다.

smart pointer 안에서 알아서 해주기 때문이다.

게다가 reset 함수는 그 인자(new Image()의 결과)가 성공적으로 생성되었을 때에만 호출된다.

함수에 진입하지 않으면 delete도 호출되지 않는다.

또한 리소스 관리를 위한 객체의 사용이 함수 정의의 길이를 줄여주기도 했다.



### strong guarantee를 제공하지 못하게 하는 옥의 티

앞서 말했듯이 위의 2가지 변경을 통해 strong guarantee를 제공하는 것이 **거의** 가능한데,

무엇이 옥의 티일까?

`imgSrc`라는 파라미터이다.

Image constructor가 throw exception하면 input stream에 대한 read marker는 이미 움직였을 가능성이 있고,

그런 움직임은 프로그램의 다른 부분에서 발견할 수 있는 상태 변화에 해당할 수 있다.

이 이슈를 처리하지 않으면 위의 예제는 basic exception safety guarantee에 머물게 된다.



### copy and swap

옥의 티는 제쳐두고 changeBackground가 strong guarantee를 제공한다고 가정해보자.

strong guarantee를 만들어낼 수 있는 전형적인 디자인 전략이 있으므로, 그것에 친숙해지자.

그것은 **copy and swap**이다.

1. 변경을 원하는 객체의 복사본을 만들고, 복사에 변경 사항을 반영한다.
2. 변경 연산 중 하나라도 exception을 발생시키면 원래의 객체는 변경되지 않은 상태로 남아있게 된다.
3. 모든 변경 사항이 반영되면 original과 copy를 non-throwing 연산을 통해 swap 한다.



### pimpl idiom

copy and swap은 일반적으로 pimpl idiom이라는 방식으로 구현된다.

이것은 진짜 객체의 (변경되어야 하는) 데이터를 분리된 구현 객체(여기서는 struct)에 넣고,

이 구현 객체에 대한 포인터를 진짜 객체가 가지고 있게 하는 것이다.

```c++
struct PMImpl {
  std::shared_ptr<Image> bgImage;
  int imageChanges;
};

class PrettyMenu {
  private:
    Mutex mutex;
    std::shared_ptr<PMImpl> pImpl;
};

void PrettyMenu::changeBackground(std::istream& imgSrc) {
    using std::swap;
    Lock ml(&mutex);
    std::shared_ptr<PMImpl> pNew(new PMImpl(*pImpl));
    pNew->bgImage.reset(new Image(imgSrc));
    ++pNew->imageChanges;
    swap(pImpl, pNew);
}
```

위 예제에서 PMImpl을 클래스 대신에 struct로 쓴 것은 pImpl 멤버 변수가 private이기 때문에 캡슐화 되도록 보장되기 때문이다.

원한다면 PMImpl이 PrettyMenu 객체 안에 Nested 될 수 있지만 패키징 이슈는 여기서는 논외이므로 언급을 생략한다.



### strongly exception-safe는 달성하기 어렵다

copy-and-swap 전략은 객체의 상태에 all-or-nothing 변경을 만들어내고자 할 때 훌륭한 전략이다.

하지만 일반적으로 모든 함수가 strongly exception-safe함을 보장해주지도 않는다.

예를 들어:

```c++
void someFunc() {
    f1();
    f2();
}
```

f1이나 f2가 strong exception-safe하지 않으면, someFunc가 strongly exception-safe하기 어렵다.

만일 f1이 basic guarantee를 제공한다면 f1을 호출하기 전에 모든 프로그램의 상태를 결정하는 코드를 작성하고, f1의 (exception이 발생한다면) 모든 exception을 catch하고, 원래의 상태를 복구해야 한다.



f1, f2가 모두 strongly exception-safe하다고 해도 문제가 있다.

f1이 완료되면 프로그램의 상태는 임의적인 상태로 변경되었을 것이고, 이 때 f2가 throw하면 프로그램의 상태는 someFunc가 호출되기 이전과 같지 않게 되기 때문이다.



문제는 사이드 이펙트다.

함수가 lcoal state에서만 연산하면 상대적으로 strong guarantee를 제공하기가 쉽다.

하지만 사이드 이펙트가 non-local data에 대해 발생하면 훨씬 어려워진다.

f1 호출의 사이드 이펙트가 데이터베이스 변경이라면 someFunc를 strongly exception-safe하게 만들기가 정말 어려워진다.



### 효율성 문제

strong guarantee에는 효율성 문제 또한 존재한다.

copy-and-swap에서는 변경될 객체를 copy 하는 데 시간과 공간이 소모된다.

따라서 strong guarantee는 상당히 바람직하지만, 그것을 쓰는 것이 실용적일 때만 써야 한다. 그리고 그게 항상 실용적인 것은 아니다.



### 일반적으로는 basic guarantee가 낫다

실용적이지 않은 경우라면 basic guarantee를 제공해야 한다.

너는 어떤 함수들에 대해 strong guarantee를 제공할 수 있다는 것을 알아낼 것이지만,

효율성이나 복잡성의 비용 때문에 누군가는 그걸 싫어할 것이다.

실용적일 때에만 strong guarantee를 제공하려고 정말 노력했다면 basic guarantee를 제공한다고 해서 욕할 수는 없다.

많은 함수에 대해서 basic guarantee가 완벽하게 합리적인 선택이다.



### no exception-safety

하지만 exception-safey를 전혀 제공하지 않는 함수를 작성한다면 문제가 달라진다.

너가 무고하다고 입증하기 전까지는 유죄다.(그러니 그러지 마라)

너는 반드시 exeption-safe한 코드를 작성해야 한다.

f2가 exception guarantee를 제공하지 않는다면, f2가 throw 했을 때 프로그램의 리소스가 f2 내부에서 leak된다.

이는 f2가 corrupted 자료구조를 갖게 되는 것을 의미한다.

-> f2를 호출하는 someFunc는 corruption에 대해 보상해줄 수 없고, 따라서 someFunc도 guarantee를 제공할 수 없게 된다.



### 1 or 0

소프트웨어 시스템은 exception-safe하거나 그렇지 않거나 이다.

부분적으로 safe 한 것은 없다.

시스템이 하나의 exception-safe하지 않은 함수를 갖고 있다면 시스템 전체가 exception-safe하지 않은 것이다.



새로운 코드를 작성하거나 존재하는 코드를 수정할 때 어떻게 exception-safe하게 만들 것인지 고민해봐라.

리소스를 관리하기 위한 객체를 쓰는 것부터 시작해라.

그 다음엔 너가 작성하는 함수 각각에서 실용적으로 제공할 수 있는 한에서 가장 strong한 guarantee를 제공해라.

만약 레거시 코드가 어쩔 수 없다면 no-guarantee를 제공해라.

너의 결정을 문서화해라.

함수의 exception-safety guarantee는 인터페이스에서 보이는 부분이므로 함수의 인터페이스의 다른 특성들을 선택할 때와 같이 심사숙고 해서 골라라.



시간은 흐르고 우리는 배우면서 변한다.





## Item 30: inline에서 inline되는 것과 outline 되는 것을 잘 이해해라.

inline은 원더풀하다!

함수처럼 보이고, 함수처럼 작동하지만 매크로보다 훨씬 낫다.

그리고 함수 호출의 오버헤드 없이 호출할 수 있다.



실은 함수 호출 비용을 피하는 것 말고도 얻는 게 더 있다.

컴파일러 최적화는 함수 호출이 없는 코드의 구역을 위해 디자인 되므로,

너는 컴파일러가 함수의 body에 context-specific한 최적화를 수행하도록 만들 수 있다.

대부분의 컴파일러는 outlined 함수 호출에 대해서는 최적화를 수행하지 않는다.



### 공짜 점심은 없다 - inline의 단점

프로그래밍에는 대부분 그렇듯이 공짜 점심은 없다.

inline 함수의 아이디어는 함수의 개별 호출을 코드 body로 대체하는 것이고,

이것은 너의 오브젝트 코드의 양을 늘릴 것이라는 것은 불 보듯 뻔하다.

메모리가 적은 머신에서 과도한 인라인은 가용 공간에 비해 과도한 코드를 만들어낼 수 있다.

가상 메모리가 있어도 inline에 의해 유발된 코드 부풀림은 추가적인 paging, 감소된 명령어 캐시 hit rate, 퍼포먼스 저하를 초래할 수 있다.



### 짧은 body라면 효율적이다

inline 함수의 body가 아주 짧다면, 함수 body를 위한 코드가 함수 호출을 위한 코드보다 작을 수 있다.

이러한 경우에는 inlining이 작은 object code를 만들어낼 것이고 instruction cache hit rate를 높일 것이다.



### inline은 컴파일러에 대한 명령이 아닌, 요청이다(implicit/explicit)

inline은 컴파일러에게 명령하는 것이 아니라 요청하는 것이다.

요청은 암묵적으로/명시적으로 전달될 수 있다.

implicit:

```c++
class Person {
  public:
    int age() const { return theAge; }
    
  private:
	int theAge;
};
```

implicit inline되는 함수는 주로 멤버 함수지만, Item 46에서는 friend 함수도 클래스 안에서 정의될 수 있다고 말하고 있다.

그럴 경우 friend 함수도 implicit inline으로 선언된다.



explicit은 함수 정의 전에 inline 키워드를 선행시키는 것이다.

explicit:

```c++
template<typename T>
inline const T& std::max(const T& a, const T& b)
{ return a < b ? b : a; }
```

max가 템플릿이라는 사실로부터 inline 함수와 템플릿이 주로 헤더 파일에서 정의가 이루어진다는 걸 발견할 수 있다.

이 때문에 어떤 프로그래머들은 **함수 템플릿이 반드시 inline이어야 한다는 잘못된 결론**을 내린다.

이 결론은 유효하지 않으며 잠재적으로 해로우므로 살펴보는 것이 좋다.



### inline, 템플릿 함수는 대체로 헤더 파일에 정의

inline 함수는 반드시 헤더 파일에 있어야 한다. -> 대부분의 빌드 환경은 컴파일 중에 inlining하기 때문이다.

함수의 호출을 호출 함수의 body로 대체하려면, 컴파일러는 함수(의 body)가 어떻게 생겼는지 볼 수 있어야 한다.



템플릿은 전형적으로 헤더 파일에 있다. -> 컴파일러가 템플릿이 사용될 때 instantiate 하기 위해서 템플릿(의 body)이 어떻게 생겼는지 알 필요가 있기 때문이다.



### 템플릿 instantiation은 inlining과는 독립적

템플릿 instantiation은 inlining과는 독립적이다.

함수를 위한 템플릿을 작성하고 있는데 그 함수가 inlined될 필요가 없다면, 그 템플릿을 (암묵적으로든 명시적으로든) inline 선언하는 것을 피하라.

inline에는 code 부풀리기와 다른 추가적인 비용이 따른다.(추가적인 비용을 이 다음에서 논의)



### 컴파일러는 inline을 무시할 수도 있다

대부분의 컴파일러는 아주 복잡해보이는 inline 함수의 inline화를 거부한다.

또한 가장 사소한 호출을 제외하고는 virtual 함수의 inline화를 무시한다. -> virtual은 "어떤 함수가 호출될지 알아내기 위해 런타임까지 기다려라"를 의미하고,  inline은 "실행 전에, 호출 부분을 함수(body)로 대체하라"를 의미한다는 것을 상기해봐라.

컴파일러가 어떤 함수가 호출될지 모르면, 컴파일러가 inline을 하지 않는 것을 비난하기 힘들다.



### inline 함수가 실제로 inline화 되는 것은 빌드 환경에 달려있다

빌드 환경에 달려있다. (주로 컴파일러)

다행스럽게도 대부분의 컴파일러는 당신이 요청한 inline이 실패했을 때 warning을 줄 수 있는 진단 레벨을 가지고 있다.



### 명백한 inline을 무시하는 경우 - inline될 수도, 안 될 수도

때때로 컴파일러는 컴파일러가 함수를 inline하기를 완벽하게 원한다 하더라도 함수의 body를 만들어내는 경우가 있다.

너의 프로그램이 inline 함수의 address를 쓴다면, 컴파일러는 전형적으로 그것에 대한 outlined 함수 body를 생성할 것이다.

컴파일러가 존재하지 않는 함수에 대한 포인터를 생각해낼 수는 없기 때문이다.

컴파일러가 함수 포인터를 통한 호출을 inline하지 않는다는 사실을 함께 고려하면,

inline 함수의 호출은 **호출이 어떻게 만들어지냐에 따라 inline 될 수도, 안 될 수도 있다**는 사실을 알 수 있다.

```c++
inline void f() {...}
void (*pf)() = f;
...
f();		// inlined
pf();		// not-inlined
```

inlined 되지 않는 inline 함수의 유령은 너가 함수 포인터를 쓰지 않더라도 너를 따라다닐 것이다.

왜냐하면 함수 포인터를 요청하는 것이 프로그래머 뿐만이 아니기 때문이다.

때로는 컴파일러가 array 의 객체의 생성과 소멸 동안에 쓰기 위한 용도로 생성자와 소멸자의 out-of-line 복사본을 생성해서 그 함수들에 대한 포인터를 얻어가는 경우가 있다.



### 생성자와 소멸자 inline의 문제

생성자와 소멸자는 inline에 있어서 더욱 문제가 된다.

```c++
class Derived: public Base {
  public:
    Derived() {}
};
```

생성자는 inline을 위한 최고의 후보 같지만 겉보기와는 다르다.



C++은 객체가 생성되고 소멸될 때 다양한 개런티를 만든다.

new를 쓰면 객체는 자동적으로 생성자에 의해 초기화 되고, delete를 쓰면 소멸자가 호출된다.

객체를 생성하면 각각의 데이터 멤버의 base class가 자동적으로 생성된다.

그리고 객체가 소멸될 때는 반대의 과정이 자동적으로 발생한다.

객체의 생성 중에 exception이 throw 됐을 때 그때까지 생성된 객체의 부분들은 자동적으로 소멸된다.

이런 시나리오에서 C++은 무엇이 일어나야 하는지는 말해주지만 어떻게 일어나는지는 말해주지 않는다. -> 컴파일러 구현자들에게 달려있고, C++만으로는 알기 어렵다.

따라서 비어있는 생성자와 소멸자에 담기는 코드가 무엇일지 예상해볼 수 있다.

```c++
Derived::Derived() {
    Base::Base();
    
    try {dm1.std::string::string();}
    catch (...) {
        Base::~Base();
        throw;
    }
}
```

이 코드가 실제 컴파일러가 만드는 코드를 모두 표현할 수는 없지만,

이것은 Derived의 비어있는 생성자가 제공해야 하는 행위들을 정확하게 반영한다.

컴파일러의 exception implementation이 얼마나 정교하게 이루어지든간에

Derived의 생성자는 자신의 데이터 멤버와 base class를 위한 생성자를 호출해야 한다.

그리고 그 생성자는 inline을 할 매력도에 영향을 미친다(컴파일러가 inline을 할 가능성을 줄이게 된다)



Base 생성자에도 같은 추론이 적용되므로,

생성자 코드가 inline됐다면 그것에 삽입된 코드도 Derived 생성자에 삽입되어야 한다.

std::string의 생성자도 inline됐다면 Derived constructor는 5개의 함수 코드 copy를 갖게 된다.(2개는 상속, 3개는 자신이 선언한 멤버)

따라서 Derived의 생성자를 inline하는 것이 쉽지 않다는 것을 알게 되었다.

비슷한 논리가 destructor에도 적용될 수 있다.



### 라이브러리 설계시 inline 유의할 점

라이브러리 설계자는 inline 함수 선언의 임팩트를 잘 따져봐야 한다 -> 클라이언트가 볼 수 있는 inline 함수들에 대한 binary 업그레이드를 제공하는 것이 불가능하기 때문이다.

f가 라이브러리의 인라인 함수라면, 라이브러리의 클라이언트는 f의 body를 어플리케이션에 담아서 컴파일하게 된다.

라이브러리 구현자가 f를 바꾸기로 한다면, f를 쓴 모든 클라이언트는 다시 컴파일해야 한다.

반대로,

f가 non-inline 함수라면 f를 변경한다면 클라이언트는 relink 하기만 하면 된다.

relinking은 리컴파일보다 훨씬 부담이 덜하고, 함수를 가지고 있는 라이브러리가 dynamically link되어있다면 클라이언트에게 완전히 투명한 상태로 수행될 것이다.



### 디버깅에 문제가 되는 inline

프로그램 개발의 목적을 위해, 이런 고려 사항을 염두에 두는 것은 중요하다.

하지만 코딩 시의 실용적인 관점에 있어 엄청나게 중요한 것은:

대부분의 디버거가 inline 함수를 두고 문제를 겪는다는 것이다.

**그곳에 존재하지 않는 함수에 대해 breakpoint를 설정할 수 없다.**

많은 환경의 경우 디버그 빌드를 위해 inline을 disable화 한다.



### 결론

어떤 함수가 inline되고 inline 되지 말아야하는지를 결정하는 논리적인 전략을 논해보자.

먼저, 어느 것도 inline하지 마라,

또는 반드시 inline되어야 하는 함수들(Item 46)이나 정말 사소한 함수(page 135)만 inline해라.



inline을 주의깊게 사용함으로써 디버거의 사용성을 증진시킬 수 있고, 적절한 장소에 inline을 함으로써 최적화를 할 수 있다.

80-20의 법칙을 잊지 마라: 전형적인 프로그램은 20%의 코드를 실행하는 데 80%의 시간을 쓴다.

소프트웨어 개발자의 목표는 프로그램의 전반적인 성능을 향상시킬 수 있는 20%를 규명하는 것이다.























