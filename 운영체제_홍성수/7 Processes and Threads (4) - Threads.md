# 7-1. Multithreading (1)

### Server Architecture

server로 request가 전달되는 통로로 queue가 쓰임.

server의 내부는 무한 루프가 있다. 



### 서버 리퀘스트 받는 패턴(아키텍처)

모든 서버 아키텍쳐는 두 가지 방식으로 이루어져있다.

1. iterative server

   서버가 스스로 깨어나서 처리. 병렬성 X

2. concurrent server

   child process(worker)가 request를 처리하게 함. 처리하는 동안 서버는 request queue에서 다른 놈을 받아서 또 다른 worker를 만들어서 처리하게 함. 병렬적 처리.



요즘처럼 복잡 고도화된 시스템에서는 concurrent server를 많이 쓴다. 요즘은 하드웨어 성능 좋고 멀티코어화 -> 병렬성을 높이는 게 좋다. 사용자의 입장에서 볼 때는 response time이 줄어드는 것. 

iterative server는 단순해서 관리하기가 편함



concurrent server의 단점 : request 개수 만큼 process를 만들어야 함.



그래서 고안한 것이 **멀티스레딩** -> concurrency는 높이면서 execution unit을 생성하거나 수행시키는 데 드는 부담을 줄임.



### 아키텍처

아키텍처는 디자인 패턴. 시스템 전체를 디자인 할 수 있는 패턴을 아키텍처라고 한다.

멀티스레딩이 필요하게 된 분야 -> 과학 연산. column과 row의 곱을 병렬적으로 해내는 것. 과거의 수행 entity는 process밖에 없었다. but 프로세스의 개수가 계속 증가. 

프로세스에는 컨텍스트, address mapping이 필요한데 많아지면 성능 저하가 발생 -> 새로운 모델 필요



## Traditional Process Model

### 프로세스의 개념

두 가지 측면에서 이해

1. context
2. execution stream(thread of control)

이 두 개를 분리시켜보자.

context는 프로세스에 부여된 자원.

수행 주체인 thread of control.



하나의 프로세스 안에 여러 개의 thread of control을 넣어보자.

thread of control을 **thread** or **lightweight process**라고 부르게 됨



## Multithreading: Basics (1)

thread of control만 따로 놓고 생각해보자.

스레드가 CPU를 할당받는 주체가 된다.

스레드가 state를 갖게 된다(ready, wait, running, ...)



스레드는 어떻게 구현되는가?

**stack**을 가지고 구현된다. execution stream은 sequence of executed functions이므로 스택에 저장이 된다.

멀티스레딩은 하나의 프로세스가 여러 개의 스택을 갖게 되는 것.



그럼 각 스레드들을 명명할 수 있어야 한다. 스레드의 **id**를 부여.

**Thread Control Block(TCB)**도 필요. 관련 정보를 가지고 있는 것



## Multithreading: Basics (2)

UNIX는 전통적인 Single threading으로 존재해왔다.

thread별로 user stack과 kernel stack이 각각 존재한다.



### OS 서포트

- MS-DOS는 single process, single thread
- Linux는 멀티태스킹. process 여러 개, single thread
- 모든 OS - 여러 process, 여러 thread



### 프로세스의 2가지 측면

1. Design Time

   Decomposition으로 독립적으로 수행 가능한 요소들이 나옴 -> 이게 프로세스

2. Run Time

   OS가 자원을 할당하고 수행 시키는 주체. 멀티스레딩에서는 프로세스 안에 스레드들로 쪼개질 수 있다.

이제 몇 개의 task들은 프로세스들로 매핑된 다음 그 안의 스레드로 매핑되게 된다. -> 1:1이 아니라 복잡해짐



용어 정리를 하자면,
Process
Thread
Task - design time process. 독립적으로 수행 가능한 요소



CMU의 Mark:

Proc = Task(프로세스에 부여된 리소스) + Thread



리눅스에서는,

유저 레벨은 process와 thread

커널 레벨에서는 process와 thread를 구별하지 않는다.

커널이 바라본 수행 entity를 모두 task라 부른다.





# 7-2. Multithreading (2)

왜 멀티스레딩이 필요한가?

1. 값싸게 concurrency를 얻기 위해

   response time을 줄이는 것 = response의 agility를 높이는 것. 

2. massive parallel scientific programming을 할 때 오버헤드를 줄이기 위해

   프로세스는 한 개 놔두고 스레드만 1만 개 생성. -> stack을 1만 개 만들면 됨.

   프로세스를 전부 다 만들어야 했다면 메모리 세그먼트, 매핑 테이블 할당해야 하는데 안해도 됨.



다시 설명하면

1. effective concurrent programming
2. resource sharing
   스레드가 리소스를 공유하게 됨. synchronization 문제가 발생.
3. effective
   구현이 쉽고 경제적이다. 태스크 생성 시간 적게 걸리고, 메모리도 적게 씀.
4. agility in response
   반응시간을 빠르게 한다.



서버를 구현하기 위해 하나의 프로세스만 존재하면 됨. 그때그때 필요에 따라서 worker thread를 생성.

웹서버라면, 자주 요청되는 페이지는 메인 메모리에 cache(worker thread들이 공유)



### concurrent server architecture 수도 코드

dispatcher는 무한 루프.

request를 queue에서 따온 다음, worker thread는 수행해서 클라이언트에게 제공



### 멀티스레드 웹브라우저

다운로드를 받는 순간 다른 어떤 버튼도 작동하지 않는다. 반응 속도 증가를 이룰 수 있다.





# 7-3. Multithreading (3)

어떻게 구현하는가?

1. kernel이 전혀 모르게 구현
2. kernel이 100% 알고 지원
3. combined(mixture)



## 1. user-level thread implementation

OS는 conventional unit process만 지원. 스레드도 하나. 그 안에 multithread를 구현.

### key entities

1. 스레드용 stack을 구현

2. thread control block을 스레드마다 만든다 -> 유저레벨에 있다.

3. thread 간에 switching(scheduling)을 위한 유저레벨 **스케쥴러**를 구현. 스케줄러가 커널이 아니라 유저레벨에 있게 된다. 똑같이 함수로 구현하고 함수를 묶어서 라이브러리로 만들면 된다. -> **user level thread library**

   

스레드들이 어떻게 동작하는가? 문제는 없는가?

한 thread에서 다른 thread로 스케줄링하는 것이 가장 어렵다.

1. preemptive : 인터럽트가 필요. (인터럽트 - 핸들러 - 서비스 루틴 - 서비스 루틴이 인터럽트 처리할 프로세스를 깨움 -> 그 프로세스로 컨트롤을 넘김) 하지만 프로세스 내부에서는 인터럽트를 할 방법이 없다.
   **blocking system call**, read system call의 문제 - 어떤 스레드가 read system call 호출하면 system call interrupt. kernel이 sys read function 호출. 커널이 I/O 기다리면서 프로세스 전체를 중단시킬 위험이 있다. 다른 스레드까지 중단되는 것.
2. non : 쉽게 구현된다. 스레드에서 yield 함수를 호출해서 다른 스레드에게 넘겨주면 된다.

장점은 OS를 고치지 않고도 멀티스레딩을 할 수 있다는 것. 이게 유용한 곳은 scientific programming 등 외부로부터 input을 받지 않고 연산 및 output만 내는 영역.



## 2. kernel-level thread implementation

스레드 생성, 스케줄링, synchronization이 모두 커널 내에 구현.

커널을 고치니까 천하무적.

windows OS는 kernel level thread. 리눅스도 어떤 의미에서는 해당.



### 장단점

pros : ULTI의 단점 극복. 반응성 향상.

cons : kernel 단의 수행 시간 증가. 오버헤드 발생. scientific 계산할 때 오버헤드가 많이 발생한다.



## 3. Combined UL/KL thread implementation

상당히 많은 기능을 유저레벨이 수행

### 추가되는 기능

1. 인터럽트가 발생했을 때 유저레벨 스케줄러에 알려줘서 어떤 스레드가 깨어나야 하는지 알려준다.
2. 스레드가 blocking system call -> 중단시킨 다음 새로운 커널 스택을 할당해서 유저 프로세스에 붙인 다음 리턴. 유저레벨에 있는 스레드 스캐줄러가 수행.





















































