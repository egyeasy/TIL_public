## Intro

OS에서 프로세스는 가장 중요한 엔티티. CPU 할당과 여러 동작들이 이루어짐

OS 설계할 때 가장 먼저 하는 것이 프로세스 설계



## 1. Process Concepts (1)

인터럽트, CPU 프로그램 수행되는 것을 볼 수 있다.

시스템을 들여다보면 굉장히 많은 일들이 일어남. -> 원인과 결과를 귀속시킬 대상이 있어야.

그 대상이 프로세스.

1. 프로세스는 OS 위에서 프로그램을 수행시키는 기본 주체. = 런타임 시스템의 수행 주제 = CPU나 여러 자원을 할당 받는 주체

2. **Decomposition**(시스템 안의 일들을 쪼개서 작업)의 한 유닛이 프로세스

   소프트웨어의 복잡성에 대응하기 위한 도구

   1) Abstraction

   2) Decomposition - 각각의 조각이 manageble할 때까지 쪼갠다. 또한 구현에 있어서도 조각화하여 수행하면 편리하다. 나뉘어진 조각들이 수행의 단위까지 되었을 때 프로세스가 된다. OS는 독립적인 유닛으로서 프로세스라는 개념을 제공한다.



## Process Conceptes (2)

Process = **Program in Execution** = 수행 중인 프로그램

특정 **프로세스 state** 위에서의 **execution stream**



프로그램과 프로세스는 다른 것이다.

프로그램 - 저장매체에 저장된 수동적인 코드 시퀀스

프로세스 - 더블클릭해서 실행한 프로그램은 프로세스가 됨. OS는 메모리에 프로그램을 적재, CPU가 읽어 들이고 I/O 디바이스를 사용. 



프로그램 - 스토리지에 저장된 수동적인 매체

프로세스 - 능동적인 존재. Execution을 갖고 있다. execution stream or execution thread( of control)



**program state** : 프로그램이 수행되는 데 기억해야 할 데이터나 정보를 저장하는 것. 수행의 결과로 영향을 받을 수 있는 **정보들**.

1. Memory 안의 저장장치

   저장 되는 것 : code(기계어), data(프로그램의 전역 변수 내용), stack(지역 변수, function call을 위해 필요한 내용), heap 이를 위해 각각의 segment가 필요

2. CPU 안의 저장장치(메모리)

   Register Values

3. Per-Process Kernel Information

   프로세스 별로 저장하는 정보



**execution stream** : 프로세스가 지금까지 수행한 모든 명령어들의 순서



OS를 공부하면서 주목해야 하는 것 : 스토리를 잘 이해해보자. OS 내부에서 어떻게 프로세스를 구현하는 거지?



## Process Concepts (4) - 몇 가지 중요한 개념

### Multiprogramming vs Uniprogramming

**멀티 프로그래밍** - 여러 개의 액티브한 프로세스가 동시에 수행(메모리의 관점) -> 메모리의 여러 프로세스가 로드

유니 프로그래밍 - 한 개



### Multiprocessing

CPU가 여러 프로세스를 수행. 이거 수행했다가 저거 수행했다가.

멀티프로세싱은 멀티프로그래밍으로 되어있다. 메인 메모리에 프로그램을 탑재해줘야  빠르게 접근할 수 있기 때문.



### Swapping

메모리 부족 문제를 해결하기 위해 CPU가 사용하지 않는 데이터를 교체.

과거 OS에 사용되던 방식.



## Process Concepts (5) - 왜 유용한가?

OS가 정부라면 프로세스는 시민.

수행의 주체 - 수업 듣고 공부한다.

자원 할당의 주체 - 차를 사고 집을 산다.



### 프로세스가 왜 유용한가 - Design time entity vs runtime entity

프로세스는 런타임 엔티티다 : OS가 관리하는 단위, 수행의 주체, OS가 CPU나 메모리, IO 디바이스를 할당하는 주체.(이렇게 해놓으면 관리가 편하기 때문)

프로세스는 디자인타임 엔티티다 : 

​	SW system 개발

  1. 설계

     요구사항 명세서 -> 설계(with decomposition) -> a set of tasks(태스크는 시스템의 독립적인 한 부분)

  2. 구현

     tasks -> 구현의 결과물 -> programs -> 수행되면서 각각의 process가 됨.

**결국 설계 단계의 결과물인 task들이 OS process와 1:1로 맵핑이 돼서 바로 수행이 된다. 이것은 OS가 이미 런타임 엔티티로 process를 갖고 있기 때문에 코드로 짜서 수행하면 바로 대응이 된다.**

사실은 설계가 어려운 것이지 구현은 어렵지 않다. 이미 OS가 decomposition을 통해 산출된 결과물을 바로 수행시킬 능력이 있기 때문이다.





## Process Control Block

Niclaus Wirth : Program = Data Structure + Algorithm(자료구조 알고리즘 책 이름)

프로그램을 구현하는 데 data structure가 바뀌면 프로그램도 바뀐다.

먼저 메커니즘의 data structure가 어떨지를 고민 -> algorithm이 무엇일지를 고민



프로세스를 data structure로 구조화시켜보자.

앞에서 세 가지 컨텍스트에 대해 살펴봤다.



### system context

OS 커널이 프로세스를 위해 어떤 정보를 유지해야 하나.

프로세스의 정보 = Process control block. 자원 할당에 필요한 여러 중요한 정보를 가지고 있음.

여러 개의 PCB를 어떻게 관리할 것인가? => array로 만든다(**Process Table**)

최초의 UNIX는 array로 짰다 -> easy to manipulate, simple to implement BUT 한계 존재.  array 방식을 사용하면 최대 PCB 도달했을 때 더이상 추가 못하게 된다 -> Linked List로 바꾸는 것 가능하다.



### process의 state transition

**Process Life Cycle**

프로세스가 어떤 스테이트에 있는가? - New, Ready, Running, Waiting, Terminated

생성이 되면 Ready 상태로 들어감(active한 프로세스인데 CPU를 받지 못함)

OS에 의해 CPU 할당 받아서 수행하게 되면 Running. 싱글 스레드에서는 0-1개가 running

ready 상태에 있는 프로세스가 여러 개 있으면 queue라는 data structure로 구성해서 담는다(**Ready Queue(List)**) 

waiting 상태는 event가 발생하길 기다리며 CPU를 내어주고 대피. -> 발생하면 다시 Ready 상태로

waiting 상태의 여러 프로세스가 존재할 수 있다. OS는 waiting 이유에 따라 다른 Queue를 만든다.



결국 OS는 프로세스가 생성이 되면 PCB를 할당하고, 프로세스를 일련의 조건에 따라 다른 상태로 전이시킨 것 = 알고리듬적 역할

ready queue, waiting queue를 만듦



### 상태 전이가 어떻게 발생하는가?

ready -> running : scheduler

running -> ready : interrupt

waiting -> ready : event





## 4-3. Process Scheduling (1)

스케쥴링에 대해 공부해보자.



### Process Scheduling

스케줄링이라는 행위의 목적 : 각 프로세스들이 **fair**하게 CPU를 **share**할 수 있도록, 다음에 수행시켜야 할 프로세스를 선택하는 작업

스케줄러의 제약 조건 : fair, CPU protection

1. Fair : 상대적인 개념. application specific한 개념이다. 일단 1/n을 받는 것으로 정의해보자.
2. Protection : 다른 프로세스에 양보했을 때 내 프로세스에 문제가 생기면 안되는 것.

어느 프로세스에게 CPU를 넘겨줄 것이냐의 문제.



원자력 발전소 쿨링 펌프 vs 게임

인터럽트가 발생하면 대부분 리스케줄링을 해야 함.

당연히 쿨링 펌프가 우선.

application specific



운전의 기계적인 동작 : mechanism

어디로 갈 것인가? : policy



OS도 마찬가지로 스케줄링 결정을 내릴 때 policy / mechanism을 나눌 필요가 있다.



### Scheduler Design Principle

policy / mechanism

policy : 다음에 수행될 프로세스를 선택하는 기준(Scheduling Policity)

메커니즘 : CPU를 한 프로세스에서 다른 프로세스로 넘겨주는 방법(Dispatcher)



### Dispatcher(mechanism)

디스패처는 다음에 어떤 프로세스가 선택될 지 모르겠지만, 새로운 프로세스가 골라져서 내려오는 상황에서,

OS의 가장 깊숙한 곳에서 다음과 같은 무한 루프를 돈다

```c++
loop forever {
    run the process for a while
    stop it and save its state
    load state of another process
}
```

스케줄링 policy와는 무관하게 지속적으로 돌아간다.

misconception : 프로그램은 수동적, 프로세스는 능동적. OS는 능동적인 존재다. Powerful, monitoring하는 entity. 실제로는 passive한 entity다. 위의 수도 코드는 굉장히 능동적인 느낌을 준다. 저렇게 하려면 dispatcher만 돌리는 CPU가 따로 있어야 함 -> 싱글 스레드가 있게 하기 위해서는 다른 방식이 필요

해결책 : **Enterleaving**. CPU가 돌다가 프로세스를 중단시키고 dispatcher 코드가 돌아야 한다. 시스템의 컨트롤이 user process -> OS -> user process로 넘어간다.



하드웨어 메커니즘으로 만들어져야 한다 -> **인터럽트**

유저 모드에서 커널 모드로 들어가야 한다.

인터럽트 메커니즘을 통해 디스패처가 수행되게 된다.



어떻게 컨트롤이 유저에서 커널로 넘어가는가?





















































