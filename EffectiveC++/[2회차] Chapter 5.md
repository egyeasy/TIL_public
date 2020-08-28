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













