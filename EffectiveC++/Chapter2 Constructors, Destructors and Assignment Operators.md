## Item 5: Know what functions C++ silently writes and calls.

비어있는 클래스의 경우에도 컴파일러가 선언하는 default constructor와 destructor가 있다. 이것들은 public이고 inline이다.



### copy constructor & copy assignment operator

이 둘을 정의하지 않으면 컴파일러는 non-static data member를 복사하는 방식으로 복사를 수행한다.

copy assignment operator의 경우 결과적으로 code가 legal해야 컴파일러가 컴파일을 수행한다. reference나 const 멤버를 copy assignment할 경우 이 멤버를 어떻게 처리해야할지 컴파일러가 결정할 수 없기 때문. (c++에서는 reference가 다른 object를 가리키는 것이 불가능) 컴파일러는 base class에서 operator가 private하게 선언된 상황에서 derived class가 implicit하게 copy assignment operator를 부를 경우에도 거부한다.



### Things To Remember

컴파일러는 클래스의 default constructor, copy constructor, copy assignment operator와 destructor를 implicit하게 생성한다.





## Item 6: Explicitly disallow the use of compiler generated functions you do not want.

copy constructor나 copy assignment operator를 선언하지 않으면 컴파일러가 알아서 그것들을 선언할 것이다. unique한 object만이 필요한 class에서는 이걸 방지하는 것이 좋다. -> base class에서 copy를 **private**으로 선언해라. 이로써 컴파일러가 자동 생성하거나 사용자가 복사를 하는 것을 막을 수 있다.



하지만, member나 freind에서는 여전히 private을 쓸 수 있다. -> **define 하지 않으면 된다** -> linker error를 띄우게 될 것.



이걸 컴파일 타임 에러로 만들려면? -> base class를 하나 더 만들어서(e.g. Uncopyable) 거기의 private으로 선언. base class의 private 함수에 접근하게 되면서 컴파일 에러를 도출하게 된다.



### Things To Remember

컴파일러에 의해 자동으로 함수가 만들어지는 것을 막기 위해 그 함수들을 private으로 선언하고 구현을 하지 마라. Uncopyable과 같은 base class를 만드는 게 하나의 방법이다.





## Item 7: Declare destructors virtual in polymorphic base classes.

클래스 오브젝트를 쓰고 나서는 delete해주는 것이 중요하다. 하지만 non-virtual desturctor를 가지고 있는 base class의 포인터에 자식 클래스를 담아서 delete하면 derived part는 destroy되지 않는다 -> base class에 virtual destructor를 줘야 한다.

virtual function은 파생 클래스 구현에 커스터마이징을 주기 위해서다.

virtual function이 있으면 dstr도 반드시 virtual해야한다. 하지만 클래스가 가상 함수를 갖고 있지 않으면 이건 대체로 베이스 클래스가 아님을 의미한다. -> virtual destructor를 안 쓰는 것이 좋다.

그 이유는, 가상 함수가 불리면 오브젝트에 추가되는 부분(vptr, vtbl)이 있기 때문이다. 이렇게 되면 C와 같은 다른 언어로 이식하는 것이 불가능해진다.

따라서 적어도 하나의 virtual function을 가질 때에만 virtual destructor를 선언하라.

그리고 STL 컨테이너와 같이 virtual destructor를 갖지 않는 타입들은 상속하지 않는 것이 좋다.



### pure virtual destructor

가상 함수를 recall하면 abstract class가 된다. 이것은 instantiate 될 수 없다. 하지만 종종 abstract class를 원하는데 순수 가상 함수가 없다면? -> **destructor를 pure virtual로 선언해라.** 단 여기서 body를 제공해야 한다. derived class destruction에서 body를 찾을 것인데 body가 없으면 linker 에러를 띄우게 된다.



base class interface를 통해 manipulate하는 경우에만 virtual dtor를 써라.



### Things To Remember

- 다형 원형 클래스는 virtual destructor를 선언해야 한다. 클래스가 하나의 virtual function을 가지고 있기만 하면 virtual destructor를 가져야 한다.
- base class로 디자인된 클래스가 아니거나, 다형적으로 쓰이는 게 아니라면 virtual destructor를 선언하면 안 된다.





## Item 8: Prevent exceptions from leaving destructors.

클래스가 여러 개 담겨 있는 벡터 컨테이너에서 동시에 두 개의 destructor에서 exception이 발생하면 프로그램이 종료되거나 undefined behavior가 뜬다.

이 때 resource-managing 클래스를 만들어서 대처하게 할 수 있다. 이 클래스의 소멸자에서 목적으로 하는 클래스의 close 메소드를 부르고, catch문을 통해 exception에 대처하게 하면 된다. 이 대처 방법은

1. 프로그램 종료(`std::abort()`)

2. exception swallowing(무시하기)

   무시되어도 프로그램이 정상작동하는 것이 보장되는 경우에만 쓰는 것이 좋다.

하지만 두 방법에는 클라이언트가 exception을 띄우게 한 condition에 대처할 수 없다는 단점이 있다.



따라서 매니저 클래스의 메소드로 close를 만들고, 이 close안에서 db.close()를 수행하게 하는 방법이 있다. 이는 사용자에게 exception에 대처할 기회를 준다.



### Things To Remember

- 소멸자는 exception을 내면 안된다. 만약 exception을 낼 경우 destructor가 catch해서 삼키거나 프로그램 종료시켜야 한다.
- 클래스 사용자가 수행 중에 exception에 대처할 수 있어야 한다면 클래스는 non-destructor function을 제공해야 한다.





## Item 9: construction 또는 destruction 중에는 절대로 가상 함수를 부르지 마라.

- derived class를 생성할 때 based class의 생성자가 먼저 불리고, 이를 통해 based class의 멤버들만 construct 한다.

- 이 때 virtual function을 통해 derived class의 member에 접근하는 일이 생기면 이건 불가능한 상황이다.
- base construction 중에는 type도 base class다.



### pure-virtual의 경우

정의 되지 않았으므로 link가 되지 않는다. 



### 생성자 내에 private 함수 내에 pure virtual 함수를 포함한 경우

link, compile 단계는 ok.

실행하면서 에러가 발생.

그냥 virtual이었으면 base version의 virtual 함수가 실행됐을 것 -> 왜 이게 실행됐는지 혼돈에 빠지게 된다.



### 해결 방법

로그 찍는 함수(virtual로 만들었던 함수)를 public으로 만들고, derived class가 해당 함수를 쓸 때 인자로 logInfo를 전달하게 만든다.

(private) static function으로 전달하면 uninit된 data member에 접근하지 않게 돼서 안전하다.



### Things To Remember

construction이나 destruction 동안 virtual function을 부르지 마라. 그런 콜은 현재 실행하는 ctor나 dtor보다 더 derived된 클래스로 들어가지 않는다.



## Item 10: assignment operator가 *this에 대한 레퍼런스를 반환하게 해라

강제되는 convention은 아니지만, 모든 built-in 타입과 STL에서는 assignment operator가 *this에 대한 레퍼런스를 반환한다.



### Things To Remember

- assignment operator가 *this에 대한 레퍼런스를 반환하게 하라.





## Item 11: operator =에서 자기 자신에 대한 할당을 핸들해라.

self에 대한 할당은 legal하다. 그러므로 이 경우를 염두에 둬라.

쓰기도 전에 resource를 release하는 트랩에 빠질 수 있다.



### 문제 상황

서로 동일한 오브젝트 간에 할당을 하면

멤버 포인터를 delete 해버린 상태에서 그 포인터를 할당해서 복사를 하는, 결과적으로 delete된 포인터 멤버를 가지고 있는 오브젝트를 복사하는 상황이 생길 수 있다.



=> 함수 초기에 동일성 테스트를 하는 방법이 있다.



### Exception-unsafe 요소

하지만 이 방법도 메모리가 부족하거나, 생성자에서 exception이 발생하는 등으로 인해 멤버 포인터가 delete된 채로 유지되는 상황이 발생할 수 있다.



=> 1) 로직의 순서를 바꿈으로써 self-assignment-safe와 exception-safe를 동시에 달성할 수 있다.

멤버 포인터를 복사한 다음, 새로운 주소를 할당 받고, 복사한 주소를 delete하는 것.



=> 2) 다른 대안 : **Copy and Swap**

클래스 자체를 복사해서 swap하는 방식. 주로 exception safety를 확보하기 위해 쓰는 방법인데, 할당 연산자 정의에도 쓰일 수 있다. by reference 방식과 by value 방식이 있다.



### Things To Remember

- = 연산자가 자기 자신에게 할당할 때 잘 작동하도록 만들어라. 테크닉에는 source와 target 오브젝트의 주소 비교하기, 주의깊게 문장의 순서를 짜기, copy-and-swap이 있다.
- 두 개 이상의 object를 가지고 작동하는 함수의 경우 object가 서로 같을 경우에도 잘 작동하도록 해라.































