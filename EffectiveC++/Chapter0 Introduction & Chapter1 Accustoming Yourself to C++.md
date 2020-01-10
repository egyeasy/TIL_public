# Introduction

- c++은 power와 expressiveness가 있지만 discipline을 가지고 써야 한다.
- 이 책은 55가지의 구체적인 suggestion을 제공하며, 각각의 suggestion을 item이라 부른다.
- standard c++ 기준
- 이 책은 좋은 디자인을 하고, 문제를 피하고, 높은 효율성을 제공하는 가이드라인이지만 만병통치약은 아니다. 따라서 설명을 잘 이해하고 예외 상황에 대응할 것



### 용어

선언(declaration) : 컴파일러에게 특정 대상의 name과 type을 알려줌. detail은 생략.

signature : parameter와 return type.

definition : declaration에서 생략된 detail을 컴파일러에게 제공

initialization :  object에 최초 value를 부여하는 과정. constructor에 의해 수행된다. constructor에는 default constructor, copy constructor, copy assignment operator가 있다.

STL : Standard Template Library. container, iterator, algorithm, related functionality를 위한 c++ 스탠다드 라이브러리.

interface : c++에는 언어 element로서의 interface가 없다. 여기서는 general design idea를 언급하는 데에 interface라는 말을 쓸 것이다.

client : 당신이 쓴 코드를 쓰는 사람 또는 무엇. 클라이언트의 마인드셋을 가지자.



### Naming Conventions

- 왼쪽, 오른쪽 parameter를 lhs, rhs라 부른다.
- "pointer to X"를 `px`
- Widget은 GUI적 의미가 없다. 그냥 쓰는 것.



### Threading Considerations

standard C++에는 스레드 개념이 없다. 여기서는 싱글 스레드를 가정하고 설명하겠지만, 멀티스레드 프로그래밍을 위한 notion을 남겨놓도록 하겠다.



### TR1 and Boost

책의 마지막에 있는데 참고하면 좋다.





# Chapter 1. Accustoming Yourself to C++

C++을 이해하는 데 가장 기초적인 내용을 다뤄보자



## Item 1: View C++ as a federation of languages.

C++을 연관 언어들의 연합으로 봐야 한다. 특정 rule이 다른 영역에서는 작동하지 않을 수 있다.

크게 4가지 - C, Object-Oriented C++, Template C++, the STL로 나뉜다.

일례로 pass-by-value가 built-in types에서는 pass-by-reference보다 빠르게 작동하지만, OOC++나 template c++에서는 더 느리다.





## Item 4: Make sure that objects are initialized before they're used

context에 따라 class의 member object가 초기화 될 수도, 안 될 수도 있다. 이게 C냐 STL이냐 등에 따라 다 다르니 외우는 것보다는 하나의 일관된 법칙을 적용하는 것이 좋다.

"항상 object를 초기화해라"

단, assignment가 아니라 initialization을 해야 한다. 이건 생성자 함수의 body 이전의 부분에서 해줘야 하는 것이다. 이게 arg로부터 copy-construct를 수행하지 않고 바로 값을 넣어주기 때문에 효율적이다.(단, built-in type의 경우에는 차이가 없다.)

사람의 실수로 인해 초기화를 까먹을 수 있기 때문에 모든 멤버에 대해 초기화를 해주는 것이 좋다.

또한 const나 reference member는 built-in type이어도 초기화되어야 한다.

생성자가 여러 개라 반복 작업을 해야 한다면 assignment 방식도 인정. -> file이나 database에서 멤버를 읽어들여야한다면 더 좋은 상황이다



### 초기화 순서

- base 클래스가 derived 클래스보다 먼저 초기화된다
- 먼저 **선언**된 멤버가 먼저 초기화된다. 초기화 순서와는 상관이 없다 -> 따라서 선언 순서와 초기화 순서를 맞춰주는 것이 좋다.



### static object들 간의 초기화 순서

static클래스 내에서 다른 static object를 부르고 있는데 translation unit이 달라서 초기화 순서가 보장되지 않는다면?

일단, 순서를 아는 것은 굉장히 어렵다.

이건 클래스 안에 해당 오브젝트를 static으로 선언해서 reference로 반환하는 메소드를 정의하면서 해결될 수 있다.

멀티스레드에서는 문제의 소지가 있다 -> 스레드 시작할 때마다 reference-returning function을 invoke하는 방법이 있다.



### Things to Remember

- built-in 타입 오브젝트를 수동으로 초기화해라. c++은 때때로 그것들을 알아서 초기화하기 때문이다.
- 생성자에 있어 constructor의 body에서 하는 assignment보다는 member initialization을 선호해라. initialization의 data member 순서와 클래스 내에서의 멤버 선언 순서를 같게 해라.
- 다른 translation unit 간의 초기화 순서 문제는 non-local static object를 local static object로 대체해서 해결해라.









