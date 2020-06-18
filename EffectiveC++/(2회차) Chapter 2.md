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





## Item 8: desctructor를 두고 오는 exception을 방지하라.

container 안에 들어있는 item들을 destruct 하는 중에 exception이 발생하면 나머지에 대해 destruct를 할 수 없게 된다. 그럴 땐 어떻게 해야할까?



DBConn을 close하는 것을 까먹지 않게 소멸자에서 close 처리를 해준다고 가정해보자.

```cpp
class DBConn {
  public:
    ~DBConn()
    {
        db.close();
    }
  private:
    DBConnection db;
};
```

container의 DBConn들을 destroy할 때 하나의 DBConn의 close()에서 exception이 나면 undefined behavior 에러가 발생할 수 있다.

이에 대한 대응 방안은

- Teminate the program

  ```cpp
  DBConn::~DBConn()
  {
      try {db.close();}
      catch (...) {
          //make log      
          std::abort();
      }
  }
  ```

  

- Swallow the exception

  ```cpp
  DBConn::DBConn()
  {
      try {db.close();}
      catch(...) {
          //make log
      }
  }
  ```



이 두 방안들이 매력적이어 보이지는 않는다. 

다른 방법은 사용자에게 close를 호출할 수 있도록 만들어두는 것이다.

거기서 미처 처리하지 못한 DBConnection을 Destructor에서 체크 후에 close 해두도록 한다.

이것은 사용자에게 짐을 지우는 것이 아니라 유용한 기회를 주는 것이다.

유용하다고 생각되지 않으면 destructor에서 알아서 close 시키게 될 것이고, 거기서 나는 exception에 대해서는 사용자가 책임을 져야 한다.





## Item 9: contruction이나 destruction 중에 virtual 함수를 부르지 마라.

### base constructor에서 virtual 함수를 부를 경우

base class의 constructor 안에서 virtual 함수를 부르면 base class의 virtual 함수가 불리게 된다.

이 virtual 함수는 derived class에서 구현된 virtual 함수를 부르지 않게 된다. base class constructor가 불리는 상황에서는 derived constructor가 불리지 않았고, 따라서 derived class가 초기화도 되지 않는 상황이기 때문이다. C++에서는 이 상황에서 derived로의 접근을 막아놓았다.



### construct 도중 class의 type

또한 base class의 constructor가 불리는 중에는 해당 class의 타입이 base class로 나온다. 이는 destructor에서도 마찬가지로, class의 타입은 derived -> base로 바뀐다.



### base constructor 내의 pure virtual vs normal virtual

base class의 constructor 내에서 init() 함수를 실행하고, pure virtual 함수가 init() 안에 있게 된다면 이것은 linking error를 발생시킬 것이지만, 그냥 virtual 함수일 경우 정상적으로 컴파일 및 링킹될 것이고, 이것은 문제가 된다.

이것은 base class에서 virtual 함수를 쓰지 않고, derived class에서 파라미터를 던져줘서 derived class 별로 logInfo를 다르게 넘겨주도록 만드는 방안으로 해결할 수 있다.

```cpp
class Transaction {
  public:
    explicit Transaction(const std::string& logInfo);
    void logTransaction(const std::string& logInfo) const;
};

Transaction::Transaction(const std::string& logInfo)
{
    logTransaction(logInfo);
}

class BuyTransaction: public Transaction {
  public:
    BuyTransaction(parameters)
        : Transaction(createLogString(parameters))
        {
            //...
        }
  private:
    static std::string createLogString(parameters);
};
```

**참고로, 함수를 static으로 선언함으로써 초기의 BuyTransaction 오브젝트의 초기화되지 않은 데이터 멤버를 참조할 위험이 없어진다.**





## Item 10 : 할당 연산자가 *this의 레퍼런스를 반환하게 하라.

x = y = z = 15;

이 연산은

x = (y = (z = 15));

이런식으로 계산된다.

구체적으로 15가 z에 할당되고, update된 z가 y에 할당되고, update된 y가 x에 할당된다.

이것은 할당 연산자가 항상 왼쪽의 argument에 대한 참조값을 반환하도록 구현되어있고, 이것이 컨벤션이기 때문이다.

따라서 다음과 같은 방식으로 짜지 않으면 컴파일이 되지 않는다.

```cpp
class Widget {
  public:
    Widget& operator+=(const Widget& rhs)
    {
        //...
        return *this;
    }
    Widget& operator=(int rhs)
    {
        //...
        return *this;
    }
}
```



## Item 11: = 연산자에서 자기 자신에게 할당하는 것을 잘 처리해라.

자기 자신에게 할당하는 경우 문제가 될 수 있는 코드

```cpp
Widget& Widget::operator=(const Widget& rhs)
{
    delete pb;
    pb = new Bitmap(*rhs.pb);
    return *this;
}
```

이미 삭제한 pb에 new를 해버리면 안 된다.



그렇다면 동일성 체크를 하는 방법이 있다.

```cpp
if (this == &rhs) return *this;
```

하지만 이것은 new 연산에서 exception이 발생할 경우 Widget 오브젝트가 delete된 pb를 계속 가지고 있게 되는 문제가 발생한다.



이를 순서를 바꿈으로써 간단하게 해결할 수 있다.

```cpp
Bitmap *pOrig = pb;
pb = new Bitmap(*rhs.pb);
delete pOrig;

return *this;
```



exception-safe 하고 self-assignment-safe한 또다른 방법은 할당 연산하는 객체를 복사해서 그 안의 정보를 swap하는 것이다.

```cpp
class Widget{
    void swap(Widget& rhs);
};

Widget& Widget::operator=(const Widget& rhs)
{
    Widget temp(rhs);
    swap(temp);
    return *this;
}
```

이것은 rhs의 참조를 받아와서 새롭게 복사를 하고, 그것의 데이터 멤버를 this와 바꾸는 로직이다.



이를 pass-by-value가 복사로 이루어진다는 것을 참조하여 다르게 구현할 수도 있다.

```cpp
Widget& Widget::operator=(Widget rhs)
{
    swap(rhs);
    return *this;
}
```

이 방법은 명확성이 좀 떨어지지만 때때로 컴파일러가 더 효율적인 코드를 만들어내게 한다.





## Item 12: 객체의 모든 파트를 복사해라.

정상적으로 디자인된 객체지향 시스템에서 객체를 복사하는 함수에는 복사 함수 (copy constructor, copy assignment operator)만 있다.

Item 5에서 컴파일러가 필요로 한다면(호출이 된다면) 복사 함수를 알아서 생성하는데, 컴파일러 생성 버전에서는 객체의 모든 데이터를 복사한다.

하지만 사용자가 정의한 복사 함수를 사용하면 컴파일러가 사용자에게 잘못된 것을 알려주지 않는다.



### Customer 예제

특정 멤버 변수를 추가했을 때 복사 함수에서 이 멤버를 복사하지 않아도, 컴파일러에서는 경고를 해주지 않는다.

따라서 복사 함수, constructor, = 연산자를 정의할 때 모든 데이터 멤버가 적용되도록 업데이트해줘야 한다.



### Customer 상속 예제

상속을 받게 되는 상황에서 문제는 더 안드러나게 된다. PriorityCustomer가 Customer를 상속받고, 복사 생성자를 정의하면 Customer 부분을 복사해올 수 있는 방법이 없다. 그래서 아무 처리를 해주지 않으면 Customer의 부분은 Customer의 default contstructor로 만들어진다.

 copy assignment operator을 통해 자신의 멤버를 복사하게 되면 Customer에서 선언한 데이터 멤버들이 복사되지 않게 된다. 따라서 Customer의 부분은 바뀌지 않은 채로 남아있게 된다.

-> 복사 생성자든 복사 할당 연산자든 base  class의 copy assignment operator를 불러주어야 한다.

```c++
PriorityCustomer::PriorityCustomer(const PriorityCustomer& rhs)
  : Customer(rhs),	// Customer part
	priority(rhs.priority)
{
        logCall("");
}

PriorityCustomer&
PriorityCustomer::operator=(const PriorityCustomer& rhs)
{
    logCall("");
    
    Customer::operator=(rhs);	// Customer part
    
    priority = rhs.priority;
    return *this;
}
```

따라서 "모든 파트를 복사하는 것"의 의미는

1. 모든 로컬 데이터 멤버를 복사
2. 모든 base class의 적절한 복사 함수를 호출

하는 것이다.



### 코드 중복 방지의 문제

copy constructor와 copy assignment operator의 코드가 비슷해서 한쪽에서 다른 쪽을 부르고 싶게 될 수가 있다. 하지만 이것은 문법적으로 지원되지 않으며, backwards 단에서 그렇게 되게 만드는 방법도 있으나 특정 조건에서 객체가 corrupt 될 수 있으므로 권장하지 않는다.

copy constructor는 새로운 객체를 초기화하는 것이고, copy assignment operator는 초기화된 객체에 적용되는 것이다. 따라서 한쪽에서 다른 쪽을 부르는 게 말이 안 된다.

중복을 방지하고 싶다면 제 3의 함수를 써서 양쪽 모두에서 호출하게 해라. 이것은 주로 init으로 명명되고 private 함수로 선언된다.































