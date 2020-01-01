## Intro

OS의 가장 핵심적인 부분인 dispatcher에 대해 공부

dispatcher는 프로세스와 프로세스 사이에 개입, CPU를 프로세스 A에서 B로 넘겨줌

dispatcher가 되기 위해서는 CPU 점유권이 유저에서 dispatcher로 넘어오는 것이 중요하다.



## 1. Entering and Leaving the Kernel

커널로 execution control이 넘어간다.

user mode execution -> kernel mode execution 넘길때 인터럽트라는 메커니즘을 사용

user mode 함수가 돌다가 kernel mode 함수가 돌아야 한다.

1. mode change 필요(by interrupt) - 인터럽트가 발생하면 무조건 kernel 모드로 바꾼다고 설정돼있음



### OS에 대한 오해

OS를 active한 entity라고들 많이 생각한다.

실제를 들여다보면 OS는 passive -> 라이브러리스러운 측면



OS는 **커널 모드 안에서 수행되는 라이브러리 함수(System Call)들의 집합**



커널 모드 : 보안 등급이 격상된 수행 모드. privileged instruction 수행. 시스템의 메모리를 제약없이 사용.

유저 모드 : 주어진 메모리만 엑세스. privileged instruction 수행 불가.



### 하드웨어적 정의

인터럽트 -> process status bit의 모드 비트가 0(kernel mode)



디스패처가 수행된다는 것은 커널 함수 중 하나인 디스패처가 불리어진다 -> 인터럽트 발생

방법은 두 가지

1. **Non-preemtive scheduling** : 프로세스가 CPU를 스스로 다른 프로세스에게 넘긴다. I/O 불렀는데 아직 준비가 안되면 넘긴다. -> Trap을 사용하면 된다. 스스로 CPU를 yield하는, 소프트웨어 인터럽트를 야기시키는 인스트럭션을 수행시키면 됨.
2. **preemtive scheduling** : 돌고자 하는 의지가 있는데 OS가 강제로 CPU를 빼앗음. timer 하드웨어를 써서 시간이 지나면 뺏아온다. -> H/W interrupt에 의해 촉발된다.



cf. 인터럽트는 두 가지

1. 하드웨어 인터럽트
2. 소프트웨어 인터럽트



**결국 유저 프로세스에서 모드 체인지 -> 하드웨어적인 메커니즘인 인터럽트(s/w or h/w, non-preemtive or preemtive) 발생**



### 타임라인

스케줄링 외에도 모드 체인지가 일어나는 경우가 있다.

OS가 제공하는 서비스(amalloc 등)를 이용할 때도 모드 체인지가 필요. 커널 함수는 커널 모드에서만 수행되기 때문. 이와 같은 경우에는 trap을 발생시키면 된다.

커널 함수를 쓰기 위해 모드 체인지를 하는 경우 -> system call

syscall instruction을 제공하기도 한다.



read 함수 -> interrupt 및 read를 원하다는 call -> mode change -> system call

cf. kernel mode -> user mode는 return instruction. 별 제한 없이 돌아오기 가능



리눅스의 프로세스는 process_id가 있다. 커널 함수가 수행 중인 구간에서 id를 얻어오면 -> 사용자 프로세스의 id가 나온다. 커널 모드 execution 중이라고 하더라도 현재 프로세스는 사용자 프로세스.



수행 중인 프로그램의 상태는 스택을 가지고 하게 된다.

process는 두 가지 요소:

1. state -> context. 메모리의 요소들(데이터, 스택, 코드 세그먼트)
2. thread of control - 프로세스가 시행된 처음부터 지금까지의 시퀀스. 함수는 그런 instruction의 시퀀스를 묶어서 하나의 이름으로 부르는 것(abstraction). 시퀀스는 런타임에 스택을 검사함으로써 알 수 있다. state 중에서 유독 stack만은 thread of control에 해당하는 data structure. **stack을 해당 프로세스의 런타임 컨텍스트라고 하기도 한다.** 

프로세스가 시스템 콜 -> 함수의 결과, 파라미터 등을 위한 스택 공간이 필요 -> kernel mode에서 수행되므로 kernel mode stack을 사용(user mode일 때는 user mode stack이 사용됨). 런타임 컨텍스트(스택)이 변화한다고 볼 수 있다. 다만, 런타임 컨텍스트가 변해도 현재 수행 중인 process는 user process.



### system call vs function call

공통점 : 한 루틴에서 다른 루틴으로 컨트롤이 넘어감

차이점 : system call은 mode change가 발생



# 5-2. Context Switching

커널모드로 들어가서 디스패처 수행이 되면

디스패처는 현재 수행 중인 프로세스의 state를 안전한 곳에 대피시킴.(중단은 인터럽트 메커니즘에 의해 수행)

context switching : 프로세스 A의 컨텍스트에서 프로세스 B의 컨텍스트로 전이하는 작업



## Context Switching (1)

OS의 코딩은 트릭이 필요. OS는 CPU를 자유자재로 넘겨줘야 한다. 프로세스를 왔다갔다 해야 함.



### Context Saving

지금 중단된 프로세스의 state를 안전한 곳으로 대피시키기

프로세스엔 3가지 state가 있다.

1. 메모리의 segment들 : **Memory Context**
2. CPU 레지스터들, I/O 레지스터 value : **H/W Context**
3. OS가 시스템 안에 담고 있는 것들 : **System Context**



무얼 대피시켜야 하는가? - 그냥 내버려뒀을 때 override 되거나 사라져버리는 것

1. CPU 레지스터
2. kernel data structure
3. 메모리?



### 메모리는 대피시키는가?

방법 1. 전혀 대피시키지 않는다.

multiprogrammed batch 모니터 시절 - 묶어서 배치로 만들어서 모두 메모리에 올려놨다. CPU를 빼앗긴다고 해도 메모리 값은 그대로 있다.

하지만 더 이상 사용하지 않는 것



방법 2. 몽땅 대피시킨다.(roll-in roll-out)

unit programming을 할 때 필요함 - 메인 메모리에 하나의 프로세스만 올려놓고 수행시키다가 cpu를 빼앗기면 디스크에 있던 것이 메모리로 들어옴

느리다.

하지만 과거엔 메모리 용량이 작고 비싸서 이럴 수밖에 없었다.

더 이상 사용하지 않는다.



방법 3. 부분 파트만 디스크로 옮긴다.

최근에 쓰고 있는 방법



Q) CPU 레지스터는 어디로 대피시키는가?

memory hierarchy의 다음 단계로 대피시키는 것이 일반적.

CPU register는 main memory로, main memory는 디스크로 대피.



## Mechanism (1)

대피시키는 메커니즘

**stack** : push 하는 때는 대부분 대피시키는 경우.

0x100에서 ADD라는 instruction 수행 도중 인터럽트 발생. 그러면 일단 이 instruction은 일단 수행한다. 기게 끝나면 인터럽트를 체크. + Process Status Word의 모드 비트가 0으로 바뀜(kernel mode) IRQ 넘버를 확인해서 인터럽트 루틴의 시작 주소를 확인해서 거기로 jump. 인터럽트 수행이 끝나면 다시 복귀해야 한다.

복귀해야할 주소는 0x100의 다음인 0x104. 돌아가는 주소를 어딘가에 대피시켜놔야 하고, 그 주소는 인터럽트 걸릴 당시 stack의 top에 넣어둔다.

무언가가 빠져있다. 끝나고 나서 mode를 회복시켜야 하는데, 돌아갈 모드를 알아야 하므로 PSW 값도 대피시켜 놓는다(PSW가 더 먼저 대피함)



인터럽트가 걸린 다음에 제일 먼저 수행되는 instruction은

interrupt service routine의 첫 번째 instruction. 이건 하드웨어가 지원해준다.

이런 하드웨어적 최소한의 support가 필요하다.



따라서 인터럽트가 걸리면 

1. PSW를 stack에 저장
2. 현재 수행 중인 주소를 stack에 저장



그 다음으로,

인터럽트 서비스 루틴의 초반부에서 프로세스의 CPU 레지스터의 값들을 stack에 저장.



### 정리

디스패처가 수행이 되려면 인터럽트가 필요

인터럽트가 걸리면 -> 스택에 pc 값과 psw 값이 저장

인터럽트 서비스 루틴을 수행(현재 스택에 레지스터 값을 다 저장)



스택 포인터 레지스터가 CPU 레지스터의 하나로 존재함.

OS 안에는 글로벌 변수가 있다. OS-PCB : Process Control Block Cur(현재) 수행 중인 프로세스의 PCB에 대한 포인터

PCB에는 process identifier, context switching 정보(stack pointer field)



### 인터럽트가 걸린 상황

스택의 top에 PSW, return address가 stack에 저장

해당 인터럽트 서비스 루틴으로 점프. with CPU 레지스터 값들을 저장(push all)

여기서 stack pointer 레지스터 값이 엉터리로 변하기 때문에 OS-PCB에 저장한다.

context saving이 다 끝남.



다음에 돌아야 될 프로세스 PCB의 id를 얻고, 자신의 current process pointer 변수에 그걸 기록. 



### 새로운 PCB

새로운 PCB가 등장한다. 이 PCB가 context switching을 한번이라도 했으면 모습이 똑같다.

pop을 하게 되면 새로 수행될 프로세스의 context가 CPU 레지스터로 들어오게 됨.

새로 들어온 프로세스로 점프하려면 return from interrupt하면 된다. PCB는 다 비게 된다.



PCB의 정보는 arrary로 갖고 있다.



Q) 하드웨어적으로 다 push all 하면 안되나?

push all 같은 경우엔 복잡한 sys instruction.

일부 레지스터는 대피하지 않아도 되는 상황이 발생할 수 있기 때문에 software적으로 구현



### 가장 중요한 포인트

인터럽트가 걸렸을 때 하드웨어적으로 PSW, return address 저장

인터럽트 서비스 루틴 초반에서 컨텍스트 saving 한다.

스케줄러가 다음 프로세스 골라주면 다음 프로세스 PCB에서 레지스터 value 얻어온 다음 return from interrupt를 통해 context switching이 이루어진다.



질문을 하나 던진다.

이 게임의 법칙이 적용되지 않는 하나의 경우

==> Process는 한 번은 context switching을 당했어야 한다. 처음으로 당하는 경우.

그 경우 fake stack을 OS가 만들어줘야 한다.

마치 당한 것처럼 PSW와 return address를 넣어놔야.

PSW는 user mode, return address는 이 프로세스의 entry point

레지스터들은 아무 값을 넣어도 상관없다. override 될 것이니까.

PCB에 이 stack의 top 주소를 넣어놓으면 된다.



스택은 어디에 있는가?

메인 메모리에 있다. 메인 메모리는 아무 곳에나 있다.

각 프로세스 별로 별도의 스택을 갖고 있다.

active한 stack은 한 개만 존재한다.





