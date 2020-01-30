## Item 27: Minimize casting.

C++에서는 compile이 클린하게 된다고 해서 perform이 클린하게 되지 않는다.



cast에는 c-style, function-style과 같은 old-style,

const_cast, dynamic_cast, reinterpret_cast, static_cast와 같은 new-style 또는 c++-style이 있다.



되도록 new-style을 써라.

1. 사람이 찾기가 쉽고
2. 목적이 구체적이라 컴파일러가 에러 진단이 가능하기 때문이다.

(old-style은 function에 object를 pass 하기위해 explicit ctor를 사용할 때만 부른다.)



cast는 컴파일러가 다른 타입으로 처리하는 것이 아니다. 한 오브젝트가 두 개의 주소를 갖는 일이 발생할 수도 있다. 따라서 이런 일이 없을 거라는 가정에서 코드를 짜면 안 되며, 결과물은 컴파일러에 따라 다를 수 있다.



static_cast로 base class로 변환하여 메소드를 수행하게 하면 복사가 일어나서 복사된 오브젝트에 대해 메소드를 수행하게 된다 -> 목적 오브젝트에 반영이 안됨.

=> base 메소드를 직접 호출해야 한다.



### dynamic cast

성능에 민감한 코드를 짤 때 느리다는 것에 주의해야 한다.

이걸 쓰지 않는 방법으로는

1. derived class를 직접 가리키는 포인터를 저장하는 컨테이너를 써라.
2. 모든 종류의 derived class를 한 컨테이너에서 관리하고 싶다면 base class에 아무것도 안하는 virtual 메소드를 정의하라.

둘 다 universally 적용 가능한 방법은 아니다. 하지만 dynamic_cast를 쓰지 않고 가능한 좋은 대안이 된다.



### Things to Remember

- practical한 코드에서 cast를 피하라. 특히 성능에 민감한 코드에서 dynamic_cast를 피하라. 디자인이 cast를 요구하면 cast-free한 대안을 개발해라.
- casting이 필수적이라면, function 안에 숨겨라. 클라이언트는 직접 cast를 자기 코드에 넣는 대신 함수를 부르면 된다.
- old-style cast보다 c++-style cast를 선호해라. 발견하기가 쉽고, 뭘 하는지가 명확하다.