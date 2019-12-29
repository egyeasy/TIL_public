## 3-1. Computer Systems Architecture

OS 이해에 필요한 하드웨어 요소를 공부해보자.

하드웨어 메커니즘 중에 OS 필요로 하는 것이 인터럽트

OS 시스템은 정부의 역할을 한다 -> 이해가 상충하는 것을 조정. 재산을 지킴. 재산이 하드웨어라고 할 수 있다.



### Overall Architecture

CPU, 메모리, IO 디바이스

하드웨어 요소를 연결 시키는 기법이 시스템 버스. 디바이스들이 시스템 버스에 연결되어 있다.

IO디바이스는 버스와의 사이에 컨트롤러를 갖고 있다.





### 시스템 버스

- CPU와 메모리, CPU와 i/o 디바이스 등 데이터 전송을 담당

- address - 데이터의 source(destination)을 지정하는 것.

  address bus라는 버스 라인에 의해 전송됨

- data bus - 데이터 전송하는 bus

- 버스에 대해 할 수 있는 operation - read/write

  read : 메모리에서 data를 가져오는 것

  write : 메모리에 데이터를 쓰는 것

- 버스 트랜잭션을 하려면 누군가가 시작하는 역할을 해야 함 -> bus master

  read/write 트랜잭션을 시작한다. 이걸 위해 버스를 장악해야 함. 컴퓨터 시스템 안에는 버스를 장악할 수 있는 버스 마스터가 여러 개가 있기 때문.

- **bus arbiter** - 버스 마스터 간의 장악을 중재. 우선순위가 높은 버스 마스터를 선정하여 버스를 제공. bus master에게 **grant signal**을 준다.

  대표적인 bus master에는 어떤 하드웨어가? - CPU, DMA controller, IO Controller

- **Bus slave** - 데이터를 담고 있는 장치. 메모리 컨트롤러, 디바이스 컨트롤러(I/O device - 정확히는 이 안의 버퍼 메모리나 레지스터가 슬레이브에 해당한다.)

  또한 데이터를 여러 개 담고 있음 - address를 가지고 있다.

  메모리의 address, I/O device의 address는 형태가 달라야 한다. 실제로 구현하는 방식에 따라 같게도, 다르게도 구현할 수 있다. 메모리 address의 일정 영역에 쓰지 않는다. 특정 영역에 접근하려 하면 레지스터에 접근하게 가능.

- I/O 디바이스 컨트롤러

  1. 버퍼 안의 데이터를 실제 디바이스로 출력

  2. I/O 디바이스에서 데이터를 읽어오는 역할

  언제 입출력을 하느냐? - CPU가 데이터를 보내고, I/O 컨트롤러가 가용 상태인지 확인을 하고 가능하면 출력.

  처리가 잘 되었다는 것은 I/O 컨트롤러가 interrupt를 통해 비동기적으로 CPU에게 완료 통지(Interrupt-driven I/O) <-> polling I/O : 출력할 데이터를 CPU가 보내고, output에 직접 관여함. 잘 끝났는지도 체크. 무한 루프를 돌면서 I/O controller에 있는 레지스터의 상태를 체크. 여기서는 인터럽트가 개입하지 않는다.

  메모리에 있는 각 공간에 대한 주소가 필요하고, I/O 컨트롤러에도 여러 개의 레지스터가 있기 때문에 이 레지스터에 대한 어드레싱이 필요(I/O address)

   1. port-mapped I/O

      디바이스 레지스터를 위해 별도의 주소공간을 할애. 메모리 어드레스와는 별도. input, output을 위해 별도의 instruction이 필요. 타겟 주소는 레지스터의 주소. 

  	2. memory-mapped I/O

      메모리 주소 공간의 일부를 할애 -> I/O 디바이스 레지스터들을 맵핑. I/O 오퍼레이션을 위해 별도의 인스트럭션이 필요하지 않다.

      Intel : port-mapped I/O

      motorolla : memory-mapped



### DMA(Direct Memory Access) Operation

interrupt driven I/O, polling 등은 character 방식. data type이 character I/O

block device에 I/O할 때는 블락 데이터를 전송해야. 한 바이트씩 전송하는 character I/O는 인터럽트에 계속 걸려서 코드를 수행해야 하기 때문.

CPU의 intervention을 최소로 하는 방법 고안.

CPU가 initiate. 전송되어야 할 블락의 메모리 시작점, 블락 사이즈, operation command(read, write)를 DMA controller에게 제공

DMA 컨트롤러가 다 옮기게 됨. 버스를 장악하고 메모리에 바로 access한다.

블락 컨트롤이 다 끝나면 CPU에게 완료를 알리는 인터럽트.

DMA가 block data를 옮기는 방식

1. cycle steeling

   CPU의 메모리 엑세스를 간섭하지 않기 위해, CPU가 실행하고 있을 때에만 bus를 사용 -> 성능에 영향을 미치지 않지만 DMA 시간이 오래 걸림.

   블락 단위로 I/O를 해서 CPU에게 notificate. DMA 역시 I/O가 완료되면 Interrupt를 사용해서 I/O를 요청한 프로세스에게 CPU를 넘겨준다. 

2. block transfer

   CPU과 DMA controller가 대등하게 경쟁하여 버스 컨트롤





## 3-2. Interrput Mechanism

시스템을 이해할 때 entity 위주로 생각했는데

가장 중요한 메커니즘.



### interrupt

하드웨어적인 메커니즘 - CPU 외부에서 CPU가 주목해야할 만한 사건이 생긴 것. 현재 흐름과 상관없는 비동기적인 처리를 해야 한다. interrupt service 루틴이라는 function으로 넘어가게 된다.

**hardware interrupt** - CPU 외부에서 사건이 발생하면 발생을 알려주는 것. 비동기적. 

**software interrupt(a.k.a. trap)** - 현재 수행하는 프로그램에 문제가 발생했을 때 문제를 해결하기 위해. exception과 같이 프로그램을 진행시키기 어려운 오류가 발생했을 때. 특정 instruction을 하드웨어 interrupt와 같이 간주. 코드를 보며 어디서 interrupt가 발생했는지 알 수 있다.(divide by 0 등)



### mechanism

CPU 마이크로프로세서의 특정 핀이 interrupt signal을 받아들이는 기능. 핀에는 interrupt 발생시킬 수 있는 interrupt source(ex. I/O device controller, DMA controller)가 물려 있다. 

1. CPU가 핀을 통해 알게 되면 현재 instruction을 완료하고 program counter에 저장.
2. 프로그램 중단

3. IRQ 넘버를 통해 어떤 소스에서 왔는지 확인. 어떤 함수가 불려야하는지 알 수 있다. 

   지금 처리해야 하는 인터럽트의 핸들러 주소가 저장되어 있고, 그 저장된 테이블이 interrupt vector table

4. IVT을 검색해서 handler의 주소를 얻어온다.

5. handler로 점프하게 된다.

처리 된 이후에는,

​	interrupt 당한 프로그램의 시작 주소로 복귀



### 하드웨어적 구성

CPU는 인터럽트 핀을 통해 signal을 받는다. interrupt source의 개수 만큼 핀이 필요 -> 마이크로프로세서는 다양한 곳에 쓰일 수 있게 되는데, 그 때마다 핀의 개수를 조절해줘야 하는 것은 문제. 실제로는 CPU 핀에 소스를 바로 연결하지 않는다.(scalability 문제 - 확장성을 부담하지 못한느 것)

**PIC(Programmable Interrupt Controller)** - 프로그래머블한 서킷이 CPU와 소스 사이에 존재. 핀에 인가되는 output line을 가지고 있음. circuit에는 source로부터 연결되는 입력 라인을 가지고 있음(대체로 16개). 만약 설계 중인 시스템의 I/O device가 16개보다 크다면? PIC를 하나 더 해서 PIC를 이중으로 연결(cascading)
programmable하다는 것은 소프트웨어적으로 동작을 변형 가능하다는 것 - 잠시 동안 특정 interrupt source를 disable 시켜야 하는 경우가 있다. flag bit를 켜고 끄는 것을 소프트웨어적으로 할 수 있다. source 16개라면 16 bit flag register가 있는 것.(interrupt mask register) -> interrupt를 무시하거나 처리 가능. 이 레지스터를 접근하기 위해 register의 port number를 가져야 한다.

CPU는 인터럽트를 받으면 어떤 인터럽트 소스가 발생시켰는지 알아야. IRQ number는 PIC 안의 register에서 가져온다. 





## 3-3. Hardware Protection Mechanism

- Protection이 필요한 이유? 자기 영역이 아닌 다른 프로그램이 있을 때 다른 메모리 영역을 엑세스하면 문제가 생김. 이를 해결하기 위해 base register와 bound register를 사용. job이 바뀔 때마다 OS가 값을 바꿔줘야 한다.

- MMU에 있는 base, bound 레지스터는 아무나 할 수 있또록 하면 안된다.(priivileged instruction : OS만 접근할 수 있는 instruction)
- privilege instruction을 어떻게 구현하는가?



### Basic Mechanism: Dual mode operation

- Motivation

  수행을 할 때 모드가 2가지가 있다. 모드는 Microprocessor 안의 레지스터가 결정한다(control & status register) -> 최근에 수행했던 여러 상황들을 기억하는 중. 다음 instruction 수행에 영향을 미치기 때문. flag 형태로 기억하는데, 그 중의 한 비트가 mode bit. 0이면 OS 수행(kernel mode, prvileged instruction), 1이면 프로그램(user mode, privileged instruction 수행 불가)

CPU가 fetch하는 과정에서 mode bit를 체크. 누군가가 1 mode인데 privileged instuction을 주면 침해한 것.

컴퓨터 시스템은 기본적으로 유저 프로그램을 신뢰하지 않는다. 프로그램을 짜면 반드시 버그가 있다 -> 악영향을 미칠 수 있는 것.

kernel mode에서 가능한 것

- privileged intstruction 수행
- 모든 메모리 영역 엑세스



어떻게 mode change를 통제할 것인가? - 커널모드의 OS가 관장하게 하면 된다. 무한 신뢰의 대상이기 때문. 소프트웨어적인 방법으로는 안된다. 하드웨어적인 방법으로 interrupt가 사용된다. 유저 프로그래밍을 하다가 I/O 엑세스(privileged instruction)가 필요하면, interrupt를 수행시키면 하드웨어적으로 mode bit를 1에서 0으로 바꿔줌.



### system call

모드 체인지는 인터럽트가 관할하는데, 실제로는 그렇게 낮은 수준의 호출이 이루어지지 않는다.

system call을 통해 이루어진다.



### 2. I/O Protection

I/O device는 왜 protection해야할까?

1. I/O register에 값을 쓰면 안 됨
2. I/O device라는 자원을 독점한다면 시스템 비효율

=> I/O instruction을 privileged instruction으로 만든다 = I/O 관련 함수는 커널 내부로 들어간다.



### 3. Memory Protection



### 4. CPU Protection

CPU도 I/O나 메모리처럼 자원이다 => monopolize가 문제가 됨.

어떤 job이 CPU가 monopolize하지 않게 하기 위해 특정한 시간 동안만 사용하게 하는 것-> 시간이 끝나면 mode change해서 못 쓰게 만든다.







