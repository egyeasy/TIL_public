# 6-1. Abstraction and Decomposition

개념이나 메커니즘이 나오면 구현을 생각해야 한다.

근데 막연히 생각한다고 떠오르지는 않는다.

따라서 구현을 할 때는 나누어서 생각해라.

program == data structure + algorithm



1. 자료구조가 어떻게 될 것인가

2. 자료구조가 어떻게 manipulate될 것인가



### Complexity

OS는 complex s/w system

이걸 이해하기 위해

1. Abstraction - Layered Architecture. abstraction을 적용하면 레이어가 나오게 된다.

   H/W 위에 OS 위에 라이브러리 또는 미들웨어 위에 어플리케이션

   OS 안에도 H/W 사이에 더 작은 레이어를 가지고 있다.(HAL)

   OS는 아래의 복잡한 시스템을 보이지 않게 하고 추상화시켜서 꼭 필요한 요소만 위에 보여주는 것

   OS와 middle웨어 사이에는 API(계층과 계층 사이의 통신을 위해 필요한 규약)

   **Layering Principle** - 아래 계층은 위에 추상화를 제공. 위 계층은 아래 계층이 제공하는 기능만을 사용할 수 있음. 그 반대의 경우는 발생하지 않아야 함.

   레이어드 아키텍쳐는 추상화 해서 이해하는 데 유용한 도구.

   그룹화 해서 이해하는 것이 추상화의 기본.

   pyramid principle

   **synthesis(or implementation)** - 레이어드 아키텍쳐의 위 레이어에서 시작해서 점점 아래로 들어가는 것. 

   추상화된 것을 구체화하는 작업이 필요하다 -> 그래야 지식의 생산자가 될 수 있다.

   

2. Decomposition

   구체화하는 과정이 decomposition

   OS라는 레이어를 5조각으로 나눈다. CPU를 관리하는 프로세스 스케쥴러 / 파일 시스템 / 메모리 관리 / I/O 관리 / 네트워크 관리

   

   

### 2번째 강의 intro

커널이 개입돼서 인터럽트가 발생하면서 디스패처 수행.

H/W 인터럽트 - preemptive scheduling이 발생. 언제든지 OS가 CPU를 원하면 내어주는 스케쥴링. 이게 발생하려면 비동기적인 절차가 필요해서 H/W 인터럽트 필요.

S/W 인터럽트 - non-preemptive scheduling이 발생. I/O를 기다리는데 끝나려면 오래 걸릴거 같다. CPU를 양보하려고 할 때 하는 것.



어떤 프로세스가 수행되다가 다른 프로세스로 넘어가는 것은 스택을 통해 컨텍스트를 넘기는 방식으로 진행된다.



오늘은 **process creation & termination**

creation - fake stack을 만드는 등 새로운 프로세스를 만들 때 필요한 작업



# 6-2. Process Creation and Termination (1)

## Process Creation (1)

프로세스가 생성되려면 파일 시스템에 executable file이 있어야 한다.

### 프로그램의 로드

file의 path가 알려져야 한다. 코드 -> code segment에 읽어들여짐

글로벌 변수들의 선언 정보 -> data segment



stack, heap segment : initially empty. 



형성된 process control block을 ready queue에 넣는다.



### UNIX fork

단, UNIX에서는 0번 프로세스만 이 방법으로 생성 -> 나머지는 cloning(fork() 시스템 콜을 통해)

프로세스를 생성하라고 명령 내리는 다른 프로세스가 있어야 함.

**Parent Process**가 **Child Process**를 만든다.

parent process가 fork를 호출하면 parent를 중단하고 컨텍스트의 스냅샷을 찍음. context를 copy하여 child process 생성. Process Control Block의 process id는 다른 값을 같지만 그 외의 모든 값은 다른 값을 가짐.

child process의 PCB를 run queue로 보내면 다시 parent process로 돌아옴



이런 방식이 70년대에 만들어졌는데 아직도 사용되고 있음. 비효율적인 방법이다.

cf. 1) functionally correct 한가?

​     2) non-functional requirement - 빠른가? 오버헤드가 많은가?

또한 처음 만든 프로그램 외의 다른 프로그램은 수행할 수 없게 된다.

그래서 fork를 한 다음에 **exec**을 통해 다른 프로그램을 수행 -> executable file의 코드와 데이터를 새로운 프로세스에 오버라이드하여 새로운 프로그램을 실행시킴.



### Process life cycle in UNIX

fork() -> exec() (child가 다른 프로그램을 수행하게 됨) -> wait() (by parent. child의 id를 받아서 child가 종료될 때까지 기다리는 명령) -> exit() (by child. 프로세스 종료, zombie state가 됨. 다 빼앗기고 exit status 자료구조만 갖고 있다. parent가 exit status 자료구조를 읽어가기만을 기다리는 상태가 zombie) -> parent 프로세스는 깨어나서 계속 수행.





## 6-3.

### shell example

shell 커맨드라인 인터페이스.

GUI가 아닌 텍스트 기반. 명령어를 넣으라고 심볼이 있는거 = prompt(리눅스는 $)

**Shell or Command Line Interpreter** : 타이핑한 명령어를 받아들여서 새로운 프로세스를 수행 

이 커맨드가 executable file의 path name이 될 것.

쉘은 커맨드를 수행시킬 child process를 만든다. 이를 위해 fork.

(한 가지 convention : system call을 호출해도 return value가 있다. if return value < 0 : 문제가 발생했다. else 정상)

child의 pid가 0인지 아닌지를 체크. 이미 0번 프로세스는 존재. 그래서 존재할 수 없다.(나중에 생각)

0보다 크다면 맨 아랫줄로 오게 되면 parent는 wait를 하게 된다. child process가 끝날 때까지.



pid == 0 : child process가 수행되는 부분. fork가 되고 그 내용이 복사돼서 child로 복사된다. child의 pcb가 선택돼서 수행하게 된다. 그때 parent의 코드와 동일한 코드를 수행하게 되는데, fork 다음부터 수행하게 된다. return address가 fork 다음으로 설정되어있기 때문. + 한가지 트릭 : child process에게는 return value를 0으로 설정. CPU register의 stack field에 parent의 경우에는 child pid, child의 경우에는 0을 넣는다 -> 그래서 pid == 0으로 인식된다. child는 exec을 하게 되고, exec의 paremeter로 cmd(executable file)을 가져와서 수행시킨다. 프로그램이 수행이 종료되면 exit, parent가 wait에서 깨어난다.



- fork 후에 꼭 wait를 하는 것은 아니다. 여러 가지 process를 만들고 wait를 할 수도 있다.

- parent가 child의 종료 상태에 관심이 있는 경우에만 wait를 한다.

  왜 굳이 fork와 같은 방법으로 이렇게 프로세스를 생성할까? 추측하는 바로는, CPU가 있고 memory가 있으면 CPU가 발생시키는 주소와 메모리의 타겟 주소가 같지 않다. 그 사이에 주소를 바꿔주는 장치가 MMU. CPU에서 MMU에 입력이 되는 주소가 논리 주소(logical address). pysical memory로 가는 주소를 physical address라고 부른다. logical address는 실제로 존재하지 않지만, 프로그램이 간주하는 가상적인 메모리. 32bit 머신이 있다면 0 ~ 2^32 - 1까지의 스페이스가 logical address.

  Proc 0이 0~2^32-1, Proc 1이 0~2^32-1의 space를 갖는다. 각자의 100번지는 memory에서 서로 다른 주소. 이게 문제가 되는 것은 proc0이 proc1과 소통을 하고 싶다면, 지역번호 없이 전화를 걸어서는 통신을 할 수 없다. 주소가 중첩되지 않기 때문에 데이터 전달을 위한 방법이 필요하다. 그래서 pipe라고 하는 file을 만들어서 한 놈은 쓰고 한 놈은 읽게 하면 된다. 그럼 file name을 어떻게 알려줄 것인가?

  -> fork라는 방법을 사용.

  ```cc
  int fd;
  foo() {
      fd = open("pipe");
      if (fork() == 0) {
          read(fd, ...)
      } else {
          write(fd, ...)
      }
  }
  ```

  parent와 child가 같은 파일을 연 다음에 child는 읽고 parent는 쓴다. OS가 파일을 열어준 것이라 볼 수 있다.

  초기 UNIX는 이렇게 밖에 통신을 할 수 없었다. abuse에서 이제 모든 곳에 쓰게 하는 상황이 됨.

- fork는 여전히 성능은 나쁘다. 이걸 어떻게 개선할 것인가?

  copy했는데 바로 exec으로 override가 되는 문제 -> COW(Copy On Write). process context를 fork() 시점에 복사하지 않고, data segment에 새 값이 쓰여질 때 복사하는 기법. 웬만하면 child process가 exec을 해서 포인터를 날려버리고 자기 데이터를 쓸 것이다.



### process termination

1. exit올 요청
2. kill시키는 것(abort)









