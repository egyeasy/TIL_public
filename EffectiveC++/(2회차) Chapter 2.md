# Chapter 2. Constructors, Destructors, and Assignment Operators



## Item 5: C++이 조용하게 쓰고 부르는 함수가 무엇인지 알아라.

컴파일러가 알아서 만들어낸 copy constructor와 copy assignment operator는 사용자가 정의하지 않을 경우 알아서 만들어진다. 이 때 값을 그냥 복사하게 되므로 reference나 const 값을 덮어쓰려고 하면 컴파일 단계에서 에러가 발생한다. 이 경우엔 사용자가 직접 정의를 해줘야 한다.



## Item 6: 너가 원치 않는 컴파일러 생성 함수를 명시적으로 불허해라.

copy constructor와 copy assignment operator의 경우 선언하지 않는다고 해서 쓸 수 없는 것이 아니다.

사용자가 이들을 부르기 원치 않을 때는 둘을 **private**으로 선언하라.

하지만 그 경우에도 member나 friend function이 private을 부를 수 있다.

그 때에는 private을 선언만 하고 정의하지 않으면 된다 -> linking error를 발생시키는 트릭

```cpp
class HomeForSale {
    public:
    
    private:
    HomeForSale(const HomeForSale&);		// declarations olny
    HomeForSale& operator=(const HomeForSale&);
};
```

파라미터 이름을 쓰지 않는 것이 컨벤션이다.



컴파일 타임에 에러를 띄우는 방법도 있다.

```cpp
class Uncopyable {
    protected:
    Uncopyable() {}
    ~Uncopyable() {}
    
    private:
    Uncopyable(const Uncopyable&);
    Uncopyable& operator=(const Uncopyable&);
};

class HomeForSale: private Uncopyable {
    
};
```

HomeForSale은 컴파일 시에 알아서 copy constructor, copy assignment operator가 생기고, 이들은 base class의 것들을 호출한다. 하지만 private이기 때문이 그 호출이 거부된다.



## Item 7: 다형성 base class에서 destructor를 virtual로 선언하라.

non-virtual destructor를 가진 base class pointer를 delete하면 base class destructor만 불린다.

하지만 derived class의 부분들은 남아있다 -> undefined behavior

따라서 **base class의 dtor를 virutal로 선언하라.**

TimeKeeper와 같은 base class들은 virtual function을 하나는 가지고 있을 것이고, 이렇게 virtual func가 하나라도 있는 base class는 virtual destructor를 가져야 한다.



하지만 virtual function이 없는 클래스의 경우 virtual dtor를 선언하는 것은 손해다.

vptr(virtual table pointer)는 runtime에 vtbl(virtual table)을 뒤져서 어떤 함수가 불려야할지를 찾아내는데,

이를 위해 클래스는 vptr용의 메모리 공간(32bit 아키텍쳐에서는 32bit, 64bit에서는 64bit)을 추가로 가지고 있어야 하는 비효율이 발생한다.



STL container나 string과 같은 타입들은 virtual dtor가 아니므로 상속받지 마라!



어떤 base class가 abstract 클래스가 되었으면 하는데, pure virtual function이 하나도 없다면?

dtor를 pure virtual로 선언하라

```cpp
class AWOV {	// AWOV = "Abstract w/o Virtuals"
    public:
    virtual ~AWOV() = 0;
};

AWOV::~AWOV() {}
```

여기서 주의할 것은 dtor의 정의를 해줘야 한다는 것이다. 이는 derive class의 dtor가 불릴 때 base인 AWOV의 dtor를 호출하게 되기 때문. 그래서 정의가 없다면 linker 에러가 나게 된다.































