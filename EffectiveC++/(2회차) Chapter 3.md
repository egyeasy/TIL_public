# Chapter 3. Resource Management

리소스는 쓰고 나면 시스템에 반환해야 하는 것이다. c++에서 주로 리소스는 동적으로 할당한 메모리를 의미하지만, 메모리 뿐만 아니라 파일 디스크립터, mutex lock, font, brush, database connection, network socket이 포함 된다. 

## Item 13: 리소스 관리에 객체를 사용해라.

```cpp
void f()
{
    Investment *plnv = createInvestment();
    //...
    delete plnv;
}
```

이 예제에서 중간에 return이 불리거나, loop 안에 delete를 뒀는데 break 등을 통해 탈출하거나, throw가 발생하는 등으로 delete가 불리지 않게 되면 리소스를 회수하지 못하게 된다.

코드가 오랜 시간 동안 유지보수 되면서 그렇게 바뀌게 될 가능성이 충분히 존재한다.

-> 리소스를 객체 안에 넣어서 그 객체가 소멸될 때 리소스를 반환하도록 하자.



### auto_ptr

block이나 function을 벗어났을 때 알아서 동적 할당된 메모리를 반환해주는 standard library의 리소스 매니징 객체.

```cpp
void f()
{
    std::auto_ptr<Investment> plnv(createInvestment());
}
```

여기서 auto_ptr과 같은 리소스 매니징 객체의 두 가지 특징을 알 수 있다

1. 리소스는 획득된 즉시 리소스 매니징 객체에게 넘겨진다.
2. 리소스 매니징 객체는 자신의 destructor를 이용해서 리소스가 해제될 것을 보장한다.



**copying 방지**

auto_ptr이 소멸되면서 리소스를 반환하게 되면 또 다시 auto_ptr이 가리키는 대상에 접근했을 때 undefined behavior가 발생할 것이다. 이를 방지하기 위해 auto_ptr에서는 copy를 했을 때 copy를 시도한 auto_ptr 객체가 null이 되도록 해놓았다.

따라서 하나의 대상에 대해 여러 auto_ptr이 생길 수 없다. 하지만 STL container들의 경우 자신의 item들이 정상적인 copying behavior를 제공해야 할 것을 요구하기 때문에, 이 경우에는 auto_ptr을 쓸 수 없게 된다.

그럴 때는 RCSP를 쓸 수 있다.



### 레퍼런스 카운팅 스마트 포인터 - shared_ptr 

얼마나 많은 객체가 특정한 리소스를 가리키는지 카운팅하다가, 0개가 될 때 리소스 delete 해주는 포인터.

```cpp
void f()
{
    std::tr1::shared_ptr<Investment>
        plnv(createInvestment());
}

std::tr1::shared_ptr<Investment> plnv2(plnv1);
plnv1 = plnv2;
```

복사나 할당의 경우에도 예상한대로 작동한다.



### 동적 할당 배열에서는 사용하지 말 것

단 auto_ptr이나 tr1::shared_ptr은 동적 할당 배열을 delete할 경우에는 제대로 작동하지 않는다. 그 대안으로 vector나 string과 같은 container를 쓸 것을 권장하지만, 그것도 싫다면 Boost에서 제공하는 boost::scoped_array, boost::shared_array를 사용해라.

```cpp
std::auto_ptr<std::string> aps(new std::string[10]);	// wrong delete가 이루어짐
std::tr1::shared_ptr<int> spi(new int[1024]);			// 마찬가지
```



특정 리소스에 대해서는 auto_ptr이나 shared_ptr을 사용하지 못할 수도 있다. 그 때에는 스스로 리소스 매니징 객체를 만들어서 써야 한다.



추가적으로 덧붙여서, createInvestment라는 팩토리 함수의 return type을 raw pointer로 설정해두는 것은 리소스 leak의 위험을 높인다. 이것은 Item 18에서 다루겠다.





## Item 14: 리소스 매니징 클래스에서 복사하는 것에 대해 신중하게 생각해라.

RAII : Resource Acqusition Is Initialization. 리소스를 할당받음과 동시에 초기화가 일워짐.

heap-based 리소스를 사용하는 게 아니라면 auto_ptr이나 shared_ptr을 쓸 수 없다. 그런 경우라면 너가 직접 리소스 매니징 클래스를 만들어줘야 한다.



### mutex 관리 C API를 쓰는 예제

```cpp
void lock(Mutex *pm);
void unlock(Mutex *pm);
```



lock과 unlock을 클래스로 관리해보자.

```cpp
class Lock {
  public:
	explicit Lock(Mutex *pm)
      : mutexPtr(pm)
      {
          lock(mutexPtr);
      }
    ~Lock() {
        unlock(mutexPtr);
    }
  private:
    Mutex *mutexPtr;   
}
```



그러면 클라이언트는 RAII(Resource Acqusition Is Initialization) 방식으로 Lock을 쓸 수 있게 된다.

```cpp
Mutex m;
{
    Lock ml(&m);
}
```



그런데 Lock object가 복사된다면 어떻게 될까?

```cpp
Lock ml1(&m);
Lock m12(ml1);
```

이 경우의 대처 방안을 선택해야 한다.



1. **복사를 금지한다**

   synchronization primitive를 복사하는 것이 말이 안되기 때문에 금지하는 방법을 쓸 수 있다.

   ```cpp
   class Lock: private Uncopyable {
       
   }
   ```

   Item 6에서 설명한 방식을 통해 Uncopyable의 복사 operation을 private으로 선언해서 상속받게 한다.

   

2. **리소스의 레퍼런스를 카운트한다**

   사용자는 리소스를 쓰는 객체가 모두 파괴되기 전까지 리소스를 들고 있는 것을 원할 수도 있다.

   그 경우 shared_ptr\<Mutex\> 타입의 멤버 변수를 두는 방식으로 설계가 가능하다.

   ```cpp
   class Lock {
     public:
       explicit Lock(Mutex *pm)
         : mutexPtr(pm, unlock)
         {
             lock(mutexPtr.get());
         }
     private:
       std::tr1::shared_ptr<Mutex> mutexPtr;
   }
   ```

   여기서 shared_ptr이 소멸 시에 Mutex를 delete하는 게 아니라 unlock 해줘야 하는데, shared_ptr에서는 소소멸 시 delete 대신 수행할 처리(deleter)를 지정해줄 수 있다(auto_ptr에서는 불가능)

   이렇게 하면 사용자가 Lock의 소멸자에서 unlock을 수행하지 않는 방식으로 unlock이 불리게 된다.(소멸자는 컴파일러가 생성한 default destructor를 쓰게 된다)

   

3. **리소스를 카피한다**

   리소스 매니징 객체를 복사할 때 이것이 감싸고 있는 리소스 또한 복사하게 할 수 있다.(deep copying)

   standard string 타입의 구현체 중에서 heap memory에 대한 포인터를 가지고 있는 경우가 있다. 이 경우에 string을 복사 하게 되면 포인터와 그 heap memory의 주소를 함께 복사해서 deep copying이 발생한다.

   

4. **리소스의 소유권을 넘긴다**

   copied object에서 copying object로 소유권을 넘기는 방법도 있다. 이것은 auto_ptr에서 사용되는 copy 방식이다.





## Item 15: 리소스 매니징 클래스에 raw 리소스에 대한 엑세스를 부여해라.

리소스 매니징 클래스들은 훌륭하지만 그것만으로 모든 경우에 대처할 수 있을 만큼 완벽하지 않다. 따라서 그럴 때를 대비해서 직접 raw 리소스에 접근할 수 있는 통로를 마련해놓아야 한다.



auto_ptr이나 shared_ptr의 경우 그런 통로들이 마련되어있다.

앞서 사용된 예시를 활용하면,

```c++
std::shared_ptr<Investment>plnv(createInvestment());

int daysHeld(const Investment *pi);
```

이 코드는 컴파일이 되지 않을 것이다. 인자로 shared_ptr을 전달하지 않았기 때문.

이를 위해서 마련된 방안이 1) explicit conversion 2) implicit conversion이 있다.

1. explicit conversion - get() 메소드

```c++
int  days = daysHeld(plnv.get());
```



2. implicit conversion - overload pointer dereferencing operators(-> / \*)

```c++
class Investment{
  public:
    bool isTaxFree() const;
    ...
};
Investment* createInvestment();
std::shared_ptr<Investment>
    pi1(createInvestment());
bool taxable1 = !(pi1->isTaxFree());

std::auto_ptr<Investment> pi2(createInvestment());
bool taxable2 = !((*pi2).isTaxFree());
```



RAII 오브젝트 안의 raw 리소스를 얻을 필요가 때때로 있기 때문에, RAII 클래스 디자이너들은 implicit conversion function을 만들어두곤 한다.

(여기 예시에서 implicit conversion이 무엇? - 아마 뒤에 나오는 거 같다)



FontHandle을 다루는 정말 다양한 종류의 C api들이 있으므로 Font 오브젝트를 FontHandle로 바꾸는 **explicit** conversion function 또한 제공될 수 있다.

```c++
class Font {
  public:
    FontHandle get() const {return f;} // explicit conversion function
}
```



explicit 메소드만 구현되어 있다면 raw resource를 사용할 때마다 이 메소드를 호출해야 하는 번거로움이 있다.

```c++
changeFontSize(f.get(), newFontSize);
```

그래서 결국 매니징 클래스를 안 쓰게 된다면, 이는 leak 위험을 증가시킬 것이다.

따라서 그러한 상황을 방지하기 위해 **implicit** conversion function을 마련해놓을 수 있다.



```c++
class Font {
  public:
    operator FontHandle() const	// implicit conversion function
    { return f; }
}
```

위 함수는 특정 함수의 인자로 FontHandle을 받게 되어있는 상황에서 Font 타입의 변수를 전달했을 때, 이를 FontHandle로 바꿔주는 연산을 오버로딩 하는 것을 의미하는 듯하다.



따라서 C api를 쉽고 자연스럽게 쓸 수 있게 된다.

```c++
Font f(getFont());
int newFontSize;

changeFontSize(f, newFontSize);
```



이러한 방법의 단점은 에러의 가능성을 높인다는 것이다.

```c++
Font f1(getFont());

FontHandle f2 = f1;
```

이는 정상 컴파일 되지만, f2에는 f1의 멤버인 FontHandle 변수가 담기게 되고, f1이 destroy되었을 때 f2는 dangle하게 될 것이다.



raw 리소스에 대한 explicit 또는 implicit conversion을 제공할 것이냐 아니냐는 RAII class가 수행하도록 하는 태스크가 무엇인지, 그리고 사용되도록 의도한 환경이 어떠한지에 따라 결정될 것이다.

가장 좋은 디자인은 Item 18의 조언을 따라서 맞게 쓰기는 쉽게, 틀리게 쓰기는 어렵게 만드는 것이다.

get과 같은 explicit conversion은 괜찮은 방향이지만 그 부자연스러움 때문에 implicit conversion으로 가고 싶은 욕구를 증가시킬 것이다.



### encapsulation 관련 문제

RAII class가 raw 리소스를 반환하면 encapsulation에 반하지 않냐는 생각이 들 수 있다. 하지만 RAII 클래스 자체가 캡슐화를 하려고 존재하는 것이 아니라 리소스 릴리즈가 발생하는 것을 보장하기 위해 있는 것이다.

캡슐화를 최우선 순위로 놓는 것도 가능하지만 꼭 필요한 것은 아니다.

어떤 RAII 클래스들은 구현의 캡슐화와 raw 리소스의 캡슐화를 혼합해서 사용하는데, shared_ptr의 경우 reference-counting 요소들은 캡슐화하는 반면 raw pointer에는 쉽게 접근하도록 만들어놓은 것이 그 예다.





## Item 16: new와 delete를 정확한 용도에 맞게 사용해라.

```c++
std::string *stringArray = new std::string[100];

delete stringArray;
```

이 프로그램의 동작은 undefined이다. 100개 중 99개의 destructor는 불리지 않게 된다.



new와 delete가 불릴 때 수행되는 동작은 2개씩 있다.

new : 1) 메모리가 할당된다. 2) 하나 또는 그 이상의 constructor가 불린다.

delete : 1) 하나 또는 그 이상의 destructor가 불린다. 2) 메모리가 해제된다.

delete에 관한 큰 의문은 이것이다 -> delete는 몇 개의 destructor가 불릴지 어떻게 알 수 있을까?



### memory layouts in Single Object vs Array

대부분의 컴파일러들에서, array의 메모리에는 객체들 뿐만 아니라 그 개수 또한 함께 저장되는 layout을 가지고 있다.



여기서 중요한 것은,

**포인터에 delete를 쓸 때 그 메모리 영역에 array가 있다는 것은 니가 직접 말해줘야 한다는 것이다.**

다음 방식대로 하면 된다.

```c++
std::string *stringPtr1 = new std::string;
std::string *stringPtr2 = new std::string[100];

delete stingPtr1;
delete [] stringPtr2;
```



stringPtr1에 delete []를 쓴다면,

결과는 undefined이지만 그런 일이 일어날 가능성은 별로 없다.

delete는 여러 destructor를 부르려고 하지만 메모리에 여러 오브젝트들이 존재하지 않기 때문이다.



stringPtr2에 delete []를 쓰지 않는다면,

이것도 undefined이지만 지나치게 적은 수의 destructor만 불리게 되는 것을 볼 수 있다.

게다가 int와 같은 built-in 타입들은 destructor가 없음에도 undefined 또는 harmful한 결과를 보인다.



규칙은 간단하다:

**new에서 []를 쓰면 delete에서도 []를 쓰고, new에서 안 쓰면 delete에서도 쓰지 마라.**



### 클래스 내에서의 사용 주의

어떤 클래스가 동적 할당된 메모리에 대한 포인터를 가지고 있으면서 여러 개의 constructor를 가지고 있을 때, 특히 주의해야 한다.

여러 contructor들에서 동일한 form의 new를 사용하지 않으면, destructor에서 어떤 delete를 사용할지 알 수가 없다는 문제가 발생한다.



###  typedef에서의 사용 주의

typedef를 사용할 때에도 delete를 어떤 form으로 사용해야하는지를 문서화해야한다는 점에서 이 규칙은 염두에 둘 필요가 있다.

```c++
typedef std::string AddressLines[4];

std::string * pal = new AddressLines; // new AddressLines는 string*를 리턴(like new string[4])

delete pal;		// undefined!
delete [] pal;	// fine
```

혼동을 막기 위해 array 타입에 대해서는 typedef를 쓰지 마라.

대신 간단한 대안은 string이나 vector를 쓰는 것이다. 위의 예제에서는 string들을 담은 vector를 쓰면 된다.





## Item 17: 단독 문장에서만 new된 객체를 스마트 포인터에 저장해라.

```c++
int priority();
void processWidget(std::shared_ptr<Widget> pw, int priority);
```



리소스 매니징 객체를 쓰는게 좋다는 생각에 processWidget에서는 shared_ptr을 쓰고 있다.

processWidget을 호출하는 코드를 생각해보면:

```c++
processWidget(new Widget, priority());
```

하지만 이것은 컴파일되지 않는다. shared_ptr은 explicit 방식으로 raw pointer를 받고 있고, new Widget을 통해 리턴 된 포인터를 shared_ptr로 implicit conversion해주는 기능은 제공하지 않고 있기 때문이다.

따라서 컴파일 되는 코드는 다음과 같다:

```c++
processWidget(std::shared_ptr<Widget>(new Widget), priority());
```

문제는 여기서도 리소스 leak이 발생할 수 있다는 점이다.



구체적으로 설명하자면,

컴파일러가 processWidget의 호출 코드를 생성하기 전에 표현들 간의 수행 우선순위를 따져야 한다.

processWidget이 불리기 위해서는 컴파일러가 다음의 3가지 코드를 생성해야 한다.

1. priority 호출
2. new Widget 실행
3. shared_ptr constructor 호출

Java나 C#에서와는 다르게, C++ 컴파일러들은 이 우선순위를 정할 수 있는 재량을 가지고 있다.

하지만 이 재량 때문에, 효율성 등의 이유로 만약 다음과 같은 순으로 코드가 실행된다면:

1. new Widget 실행
2. priority 호출
3. shared_ptr constructor 호출

게다가 priority를 호출하다가 exception이 발생한다면, new Widget을 받아온 포인터를 잃어버리게 될 것이고, 포인터를 shared_ptr에 담을 수 없게 되어 리소스 leak을 방지할 수 없게 된다. 

**이것은 리소스가 생성되는 시점과 리소스가 리소스 관리 객체에 전달되는 시점에 exception이 개입할 수 있는 데서 발생하는 문제다.**



대처 방안은 간단하다:

**Widget을 생성하고 smart pointer에 저장하는 동작을 하나의 문장에서 수행하고, 그 다음에 processWidget에 스마트 포인터를 넘겨줘라.**

```c++
std::shared_ptr<Widget> pw(new Widget);

processWidget(pw, priority());
```

이것은 컴파일러가 연산의 순서를 재조정할 때  statement 안에서보다는 statement들 사이에서는 재량을 덜 가지기 때문에 통하는 방법이다.

이 때문에 여기서는 priority가 new Widget과 shared_ptr constructor 사이로 끼어들 일이 없다.





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

















































