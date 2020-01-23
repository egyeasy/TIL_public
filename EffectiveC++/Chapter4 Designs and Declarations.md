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



