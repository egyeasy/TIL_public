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

















