## Item 18: Make interfaces easy to use correctly and hard to use incorrectly.

사용자가 인터페이스를 올바르게 쓰고 싶어함에도 그렇지 못했다면, 어느 정도는 당신의 인터페이스에 책임이 있다.



1. 순서 문제

예를 들어, 클라이언트는 파라미터 순서를 잘못 입력할 수 있다.

연월일의 순서를 잘못 입력한다면, 연, 월, 일 별로 struct를 구성하여 해당 타입의 struct만 파라미터로 받도록 설정할 수 있따.;



2. 파라미터 Value 문제

enum은 int처럼 쓰일 수 있기 때문에 위험하다.

Month 클래스에서 함수의 형태로 1월~12월의 Month를 던져주는 메소드를 정의한다.(Month의 생성자는 private로 선언하여 이외의 오브젝트를 생성할 수 없게 한다)



또한 const를 통해 operator *의 return type의 검증이 가능하다. 다만 사용자 정의 타입에 대한 인터페이스에 있어서는 **일관성**도 중요하다. 특별한 이유가 없다면 int와 같은 빌트인 타입과 호환이 되게 하는 것이 좋다.



### 사용자가 기억해야하는 문제

사용자가 무언가를 기억해야한다면 잘못 쓸 여지도 많아진다.

함수의 return type으로 클래스 포인터를 받았다면, 이걸 delete해줘야 한다. 일단은 함수의 return type에 스마트 포인터를 강제함으로써 사용자가 스마트 포인터를 일부러 써서 delete를 하지 않아도 되는 상황을 만들 수 있다. 따라서 이는 **resource release** 문제로부터 해방시킨다.



만약 포인터를 해제하기 위해 getRidOfInvestment라는 함수에 포인터를 전달해야 한다고 하자. 이는 새로운 client error를 발생시킬 것이다: getRidOfInvestment 대신 delete를 써버리는 상황 말이다. 이를 막기 위해 **커스텀 deleter**로서 getRidOfInvestment를 설정할 수 있다.

그 구현은 다음과 같을 것이다. null 포인터 변수를 만드는 코드를 보도록 하자.

```cpp
std::tr1::shared_ptr<Investment> createInvestment()
{
    std::tr1::shared_ptr<Investment> retVal(static_cast<Investment*>(0),
                                            getRidOfInvestment);
    
    return retVal
}
```

shared_ptr은 cross-DLL 문제를 피할 수 있다. shared_ptr이 생성된 DLL에서 온 delete를 사용하기 때문이다. shared_ptr은 어떤 DLL의 delete가 불리어야 하는지 추적한다.





## Item 19: Treat class design as type design.

class design을 하고 있다면 type design을 하고 있다고 생각해야 한다. 함수와 연산자를 오버로딩하고, 메모리 할당과 해제를 신경쓰고, 오브젝트 초기화와 finalization을 정의해야 한다. good class design이 어려운 이유는 good type design이 어렵기 때문이다. 제약이 존재한다.



- **어떻게 new type이 생성되고 destroy되어야 하는가?**(Chapter 8)
- **오브젝트 initialization이 object assignment와 어떻게 다른가?**(Item 4)
- **new type 오브젝트가 passed-by-value 하는 것은 무엇을 의미하는가?** - copy constructor가 쓰임.
- **new type의 legal value에 가해지는 제약이 무엇인가?**
- **new type이 inheritance graph에 잘 들어맞는가?**(Item 34 and 36)
- **new type을 위해 어떤 type conversion이 허용되나?**(Item 15)
- **new type을 위해 어떤 연산자와 함수가 필요한가?**(Item 23, 24, and 46)
- **어떤 standard function이 허용되지 않아야 하는가?** - private 문제(Item 6)
- **new type의 멤버에 누가 엑세스 권한을 갖는가?**
- **new type의 undeclared interface는 무엇인가?**(Item 29)
- **new type이 얼마나 general 한가?**
- **new type이 정말로 필요한가?** - member function이나 template을 만드는 게 좋을 수도 있다.



### Things To Remember

클래스 디자인은 타입 디자인이다. 새로운 타입을 정의하기 전에 이 Item의 모든 이슈를 확인해라.





## Item 20: Prefer pass-by-reference-to-const to pass-by-value.

function은 기본적으로 parameter와 return 값을 pass-by-value한다. 이건 copy constuctor에 의해 수행됨.

이것에는 ctor와 dtor의 비용이 따른다. 상속하는 베이스 클래스의 멤버들까지도 모두 ctor, dtor해야함.

또한 value 방식은 정의된 클래스 대로 ctor하기 때문에 derived class에서 캐스팅이 일어난 경우 slice 문제가 발생할 수 있다.



=> reference-to-const 해야 한다.

copy에서는 변형이 일어나지 않지만, ref에서는 변형이 일어날 수 있으므로 const를 쓴다.



built-in 타입과 STL의 iterator 및 function object들은 slicing problem을 겪지 않고, copy해도 효율적이다.



but user-defined small type은 pass-by-value가 효율적이지 않을 수도 있다. 컴파일러가 built-in small type과는 다르게 처리할 수도 있기 때문.



### Things to Remember

- pass-by-value보다 pass-by-reference-to-const를 선호해라. 일반적으로 더 효율적이고 slicing problem을 피할 수 있게 해준다.
- 이 룰은 built-in type과 STL의 iterator 및 function object type에는 적용되지 않는다. 이들을 위해서는 pass-by-value가 더 적절하다.





## Item 21: Don't try to return a reference when you must return an object.

Item 20의 가르침 때문에 온갖 곳에 reference를 적용하려는 행동을 조심해라. 실제 존재하는 것을 reference하는 것이 중요하다.



### function return 값의 pass-by-reference

1. function 내에서 직접 생성해야 한다.
2. local variable이라 없어진다 -> 과거의 객체'였던 것'을 ref하게 된다. -> undefined behavior



### new를 통해 포인터 동적할당

delete를 누가 부르게 할 것인가?

w = x\*y\*z의 경우처럼 ref를 받을 방법이 없어지는 경우도 있다. 이 때 delete를 할 방법이 없다.



### static object를 생성해서 ref를 반환

if ((a * b) == (c * d))

가 무조건 true가 된다. 같은 static object를 ref하게 되기 때문이다.

static array나 vector를 활용하는 방법도 size를 설정해야 하는 문제, array가 가리키는 대상에 대한 ctor, dtor가 불리는 문제 등이 발생한다.



=> 따라서 그냥 객체를 pass-by-value하는 것이 낫다. 여기서 컴파일러가 안전하게 작동하게 만들면서 최적화를 알아서 해준다.



### Things to Remember

local stack object에 대한 포인터나 ref를 리턴하지 마라. heap-allocated object에 대한 ref, local static object에 대한 포인터나 ref도 리턴하지 마라(하나보다 많은 오브젝트가 필요하게 될 가능성이 있다면) (Item 4는 최소한 싱글 스레드 환경에서는 local static에 대한 ref를 리턴하는 것이 합리적이라는 예제 디자인을 보여준다.)





## Item 22: Declare data members private.

data member를 private으로 선언하면, **syntactic constistency**를 확보할 수 있다. get/set 메소드를 통해 접근성에 대한 정확한 컨트롤이 가능하다.

내부 구현을 바꾸면 사용자는 리컴파일하기만 하면 된다. -> implementation flexibility



### encapsulation

1. 불변 속성(class invariants)이 유지된다.
2. 구현을 바꿀 수 있다.(changeable)



### protected

protected에 data member를 넣는 것도 public과 유사하다. 결국은 derived class의 코드가 broken 될 것이다.



### Things to Remember

- data member를 private으로 선언하라. 이는 클라이언트에게 syntactically uniform access to data를 제공하고 미세한 access control이 가능하게 하고, invariant가 강제되게 하고, 클래스 작성자가 구현에 유연성을 갖게 할 수 있다.
- protected도 public과 유사한 정도로 encapsulated된다.





## Item 23: non-member non-friend 함수를 member 함수보다 선호하라.

member function에 비해 non-member func은 encapsulate를 더 할 수 있다. 컴파일 dependency가 낮아지고 확장성이 높아진다. -> 더 changeable 하다.

이는

1. non-friend에게만 해당
2. 다른 클래스의 멤버여도 된다.



### convenience function

또한 단순히  convenience func이기 때문에 사용자가 필요하지 않다면 직접 멤버 함수를 호출해도 된다.

conv func 내의 영역을 분리할 수도 있다 -> 모든 func를 컴파일하지 않아도 되는 것. 필요한 것만 갖다 쓸 수 있다.

헤더 파일만 만들어서 네임스페이스 선언하고 정의하면 되므로 확장이 쉬움.

이와 반대로 클래스는 쪼갤 수가 없기 때문에 이를 영역별 split이 불가능.



### Things to Remember

- non-member non-friend func를 member func보다 선호하라. 이는 encapsulation, packaging flexibility, fucntional extensibility를 향상시킨다.





## Item 24: Declare non-member functions when type conversions should apply to all parameters.

가급적 클래스가 implicit conversion을 지원하지 않도록 하는 것이 좋다고 introduction에서 얘기했다. 하지만 numerical type에 대해서는 필요한 경우가 있다.



유리수 클래스를 정의하고, 이를 2와 곱셈 연산이 가능하게 하고 싶다면?

교환 법칙이 성립해야 하는데 클래스 멤버 함수(with non-explicit ctor)로 연산자를 정의하면 한쪽에서 컴파일 에러가 나게 된다.(explicit ctor에서는 둘 다 에러남) 이는 함수 parameter로 들어갈 경우에만 implicit type conversion이 이뤄지기 때문이다.



=> non-member 함수로 선언해서 여러 type을 parameter로 넣으면서 implicit type conversion이 가능하게 하라.

```cpp
const Rational operator*(const Rational& lhs, const Rational& rhs)
{
    return Rational(lhs.numerator() * rhs.numerator(),
                   	lhs.denominator() * rhs.denominator());
}
```



non-member함수가 friend일 필요는 없다.



### Things to Remember

- 함수의 모든 parameter에 대해 type conversion이 필요하다면 그 함수는 non-member여야 한다.

























