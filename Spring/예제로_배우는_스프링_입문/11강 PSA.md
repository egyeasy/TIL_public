# 11강 PSA

Portable Service Abstraction



나의 코드

확장성이 좋지 못한 코드 or 기술에 특화되어 있는 코드



나의 코드

잘 만든 인터페이스(PSA)

확장성이 좋지 못한 코드 or 기술에 특화되어 있는 코드



https://en.wikipedia.org/wiki/Service_abstraction



Service Application : 지금의 controller 상으로는 서블릿을 전혀 사용하지 않고 있음을 볼 수 있다. Servlet으로 Get, Post 등의 요청이 들어오면 그걸 처리한다. 이렇게 url과 매핑을 해야하는데, 지금의 clinic 서비스는 그렇게 하고 있지 않다. @GetMapping을 통해 url을 설정하고 -> 그 때 아래의 메소드를 실행하는 방식으로 짜놓음. 그렇다면 추상화 객체를 사용해서 좀 더 편하게 개발을 해보자(링크를 통해 그 목적을 알 수 있음)



1. 먼저 스프링 MVC와 관련된 추상화

   - @Controller, @GetMapping

   - 이게 왜 추상화 계층인가? - Servelet을 쓰지 않아도 되고, 간편하게 원하는 걸 구현할 수 있기 때문.

   - 'Portable' - 기본적으로 서버는 톰캣 기반으로 돌아감. but 코드를 거의 그대로 둔 상태로(약간만 변경한 상태로) 다른 기술 스택(webflux, Netty, 제티, 언더토우)으로 서버를 돌리는 것도 가능함. 그 때 servelet과는 다른 방식으로 돌아가기 때문에 추상화 계층을 사용해놓으면 돌리는 게 가능하다.

   - cf. spring mvc가 빠지면 model and view 라이브러리를 사용할 수 없다.



### Spring Transaction

데이터베이스와 어떤 데이터를 주고 받을 때, A를 하고 B를 하고 C까지 다 되어야 하나의 작업으로 완료해야하는 경우 -> All or Nothing

ex) 쇼핑몰 앱에서 물건이 없으면 받은 돈도 돌려줘야 하는 것

- JDBC transaction example

  setAutoCommit(false) -> 자동 커밋을 false. 일련의 작업 처리 후 수동으로 커밋할 때만 커밋

- 이걸 쉽게 도와주는 "PSA"로 Transaction annotation이 있다(`@Transactional`. try catch문도 쉽게 구현 가능.



### Spring Cache 캐시

`@Cacheable` 

캐시가 구현체가 다양하고 많다. ehcache 등 -> 구현체를 바꿔쓰더라도 동일한 annotation을 가지고 작동시킬 수 있다.

