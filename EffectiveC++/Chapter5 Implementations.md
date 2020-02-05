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





## Item 30: Understand the ins and outs of inlining.

inline function이 만능이라고 생각하고 무분별하게 쓰지 마라. code bloat이 발생하여 instruction cache hit rate가 낮아질 수 있다.

inline은 컴파일러에 대한 request이지, command가 아니다. request는 implicit 또는 explicit한 방식으로 이루어질 수 있다.

인라인 함수와 템플릿은 헤더 파일에서 일반적으로 정의된다. 하지만 함수 템플릿이 항상 inline이어야 할 필요는 없다. 어떤 template 함수를 inline했을 경우 컴파일러가 이를 무시할 수도 있다. command가 아닌 request이기 때문이다.

inline 선언의 파급력을 명시해야 한다. -> inline constructor나 destructor의 경우 derived class에서도 사용될 수 있다.



### 인라인의 단점

1. 라이브러리의 inline 함수에 변화가 생기면 다시 컴파일해야 한다 -> 사용자에게 부담으로 작용한다.

2. 디버깅이 어렵다. 함수를 캐치할 수 없다.



따라서 사소하고 필요한 경우에만 inline화 하라.



### Things to Remember

- inlining을 대부분 작고, 빈번하게 불리는 함수에 대해서만 적용하라. 이는 디버깅과 바이너리 upgradability를 용이하게 하고, code bloat을 최소화하고 program speed를 최대화할 가능성을 높인다.
- 함수 템플릿이 헤더에 있다고 무조건적으로 inline으로 선언하지 마라.