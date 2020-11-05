# Chapter 6. Inheritance and Object-Oriented Design

OOP는 대단히 인기가 많다.

C++에서의 OOP는 너가 익숙했던 OOP랑은 약간 다를 것이다.

다양한 상황에서 어떤 것들을 쓰는 게 좋을까?

이 챕터에서는 그것들을 정리한다.



## Item 32: public 상속은 "is-a"를 만든다.

C++ OOP에서 가장 중요한 것은 이거다 : **public 상속은 "is-a"다.**



D가 B를 public 상속하게 되면, D의 모든 객체는 B의 객체이기도 하다(반대는 아니다)

B는 D보다 일반화된 개념이고, D는 B보다 특별화된 개념이다.

B가 쓰일 수 있는 곳에서는 D 또한 쓰일 수 있다. 하지만 그 반대는 아닐 수도 있다.

ex) 사람 - 학생의 관계와 같다 -> 학생의 사람의 특수화된 타입이다.



### "is-a"는 public 상속에서만 유효하다

Person 타입을 인자로 받는 함수는 Student 타입도 인자로 받는다. -> 이것은 public 상속에서만 사실이다.

private 상속은 완전히 다른 것이고(Item 39) protected 상속은 나도 지금까지 이해할 수가 없는 무언가다.



### 부정확한 언어를 조심해라

Bird 클래스에 fly()라는 virtual 함수를 선언하고 Penguin 객체가 Bird를 public 상속 받게 하면 안된다.

Bird 중에는 날지 못하는 새도 있기 때문이다.

Bird - FlyingBird 상속을 따로 두고, Bird - Penguin 상속을 하게 하는 것이 맞다.



### 중요한 것은 '해당 소프트웨어에 필요한 구분인가'이다

하지만 모든 소프트웨어에 이상적인 하나의 디자인은 없다. -> Bird의 flying 함수가 필요하지 않은 경우가 있을 수 있다.

너가 모델링하는 세계에서 flying bird와 non-flying bird 사이에 구분이 필요 없다면, 설계에서도 그런 구분을 두지 않는 것이 좋을 수 있다.



### 펭귄 문제의 다른 방법 - 에러 핸들링

펭귄의 fly 함수에서 런타임 에러를 발생시키도록 재정의하는 방법도 있다.

```c++
class Penguin: public Bird {
  public:
    virtual void fly() { error("Attempt to make a penguin fly!");}
};
```

이런 구현이 의미하는 바는, "펭귄은 날 수 없다"가 아니라, "펭귄은 날 수 있지만, 실제로 펭귄에게 날게 하는 것은 에러다"이다.

둘의 차이는 무엇일까? -> **에러가 감지되는 타이밍이다**

"펭귄은 날 수 없다"는 명령은 컴파일러에 의해 강제되고, "펭귄은 날 수 있지만, 펭귄에게 날게 하는 것은 에러다"는 런타임에 감지된다.



좋은 인터페이스는 컴파일 단계에서 유효하지 않은 코드를 방지하므로, 컴파일 단계에서 펭귄의 비행 시도를 거부하는 디자인을 선호해라.



### 정사각형은 사각형을 public 상속해야 할까?

"정사각형은 사각형이므로(is-a) 당연히 상속해야 한다"라고 한다면 여기서는 옳은 답이 아니다.

```c++
void makeBigger(Rectangle& r) {
    int oldHeight = r.height();
    r.setWidth(r.width() + 10);
    assert(r.height() == oldHeight);
}
```

```c++
class Square: public Rectangle {...};
Square s;

assert(s.width() == s.height());
makeBigger(s);
assert(s.width() == s.height());
```

makeBigger 함수를 수행한 이후에 s의 width와 height가 같다고 할 수 있는가? 그렇지 않다!

여기서의 근본적인 어려움은 사각형이 적용가능한 무언가가 정사각형에는 불가능하다는 것이다.

(하지만 public 상속에서는 base class에 적용되는 **모든 것**이 derived class에 적용 가능해야 한다.)



컴파일러는 위 코드가 컴파일 되게 둘 것이지만, 코드가 정상적으로 동작할 것이라는 보장은 없다. -> 컴파일이 된다고 해서 잘 작동하는 것이 아니라는 것을 명심해야 한다.



그동안 해왔던 것이 OOP를 다루면서 실패한다는 점에 좌절하지 말라.

상속의 적절한 적용을 위해 새로운 인사이트를 가지고 당신의 직관을 향상시켜줄 것이다.



### is-a 외의 다른 관계들

클래스 간에는 "has-a"와 "is-implemented-in-terms-of"라는 common한 inter-class 관계도 있다.(Item 38, 39)

이러한 중요한 관계들이 is-a로 모델링되는 경우도 종종 있으므로 관계들 간의 차이를 이해하는 것이 중요하다.





## Item 33: 상속되는 이름이 가려지는 것을 피하라.

문제는 상속과 관계가 없고, 스코프와 관계가 있다.



### 상속이 아닌 scope

```c++
int x;
void someFunc()
{
    double x;
    std::cin >> x;
}
```

x를 읽는 부분은 글로벌 변수 x가 아닌 로컬 변수 x를 참조한다.

int, double과 같은 타입과는 상관 없이 local x가 global x와 이름만 같다면 global x를 숨기게 된다.



### 상속 scope

```c++
void Derived::mf4() {
    mf2();
}
```

먼저 local scope를 찾고 -> Derived 클래스의 scope를 찾고 -> base 클래스 scope 찾는다 -> 최후에는 global scope



### 오버로드가 있는 경우의 상속 - public

인자 타입을 추가하는 등으로 오버로드를 한 함수명을 Derived 클래스에서 함수명으로 쓴다면, Derived의 함수명에 의해 base의 함수명이 숨겨지게 된다.

만약 public 상속을 하고 있는데 너가 오버로드한 함수를 상속받을 수 없다며 이것은 is-a relationship에 위배된다.

그럴 때의 방법은

```c++
class Derived: public Base {
  public:
    using Base::mf1;
    using Base::mf3;
    
    virtual void mf1();
    void mf3();
    void mf4();
}
```



### 오버로드가 있는 경우의 상속 - private

private 상속의 경우에는 테크닉이 다르다.

Derived에서 인자가 없는 mf1을 상속받고 싶은 경우에, `using` 선언을 하면 해당 이름을 가진 모든 상속 함수들이 보여질 것이기 때문에 안 된다.

대신 **forwarding function**을 쓴다.

```c++
class Derived: private Base {
  public:
    virtual void mf1() {
        Base::mf1();
    }
}
```









