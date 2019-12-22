# 1. Evolution of OS - Phase 1 Up to Batch Monitor

운영체제는 흥미로운 분야다. 모든 분야들을 하나로 모아놓은 것.

기반 과목들에 대한 융합이 필요.



### Course Goals

- OS 제공 기능들을 보게 될 것. 기능 구현에 필요한 이론, practice 공부
- OS의 내부가 어떻게 구성되는지 이해
- 새로운 소프트웨어나 새로운 OS를 만드는 데 지식을 적용



이전에는 데스크탑이나 서버와 같은 환경 내에서만 사용되었다.

지금에는 스마트폰에도 OS가 사용되고 있고, 자동차, TV 등에도 사용되고 있다.



## Three Phases of OS history

1. 처음 컴퓨터 시스템이 개발된 시기(50s 초반 - 60s 중반)
2. 모든 OS의 근간이 되는 Time sharing OS 등장(60s - 90s 중반)
3. 오늘날(90s 중반 - 지금)



### Phase 1

- Hardware expensive, humans cheap

GOAL : make efficient use of the hardware



CPU의 utilization을 최대화하는 것이 목적.

human operator가 OS 역할을 한 것.

프로그램을 수행시키는 기본 단위를 job이라고 함. job은 punch card 형태로 입력된다.  프로그램의 각 line을 typewriter 를 통해 입력. 카드 리더를 통해 읽어들이고 빛이 투과하는 패턴을 통해 입력을 받아들이는 것.

job to job transition : 하나의 job을 처리하고 다른 job을 처리하는 것



IBM 7094는 human operator에 의해 작동.



### phase 1-2

1401 IO machine - 이라는 저렴한 컴퓨터를 개발 ->job to job transition을 가속화하는 데 사용

batch monitor - batch를 단위로 여러 개의 job을 묶어서 저장. reader를 통해 여러 job을 동시에 받는다. 각 job들이 수행한 결과는 테잎에 기록. 사용자는 1401에 의해 테입의 아웃풋이 프린트에 기록, 결과물을 받게 된다.



### Phase 1-4

사람들이 CPU utilization을 더 높일 수 있는 방법 모색

I/O를 하는 동안에는 CPU가 idle해지는 문제. 당시엔 CPU가 입출력을 관장했기 때문.

이 시간에 연산을 할 수 있게 하자.

**I/O channel** - 오버랩 시킬 수 있는 하드웨어 메커니즘. IO 디바이스 컨트롤러라고 보면 된다. Interupt가 최초로 등장. CPU는 IO 시작과 끝만 관리. 인터럽트 최초 도입. 



하지만 문제 - IO 오퍼레이션의 모든 종류가 CPU와 IO를 분리시킬 수 있는가? 그럴 수 없다. 읽고자 하는 데이터가 읽혀져야 다음 오퍼레이션을 수행할 수 있음. 



동기적 IO operation : CPU가 연산 수행하다가 I/O 만들었을 때 I/O수행이 종료되어야 다른 연산을 가능. 대부분의 input 오퍼레이션 -> 이전 데이터에 종속적. 기다리는 것은 busy waiting을 의미.

비동기적 IO operation : 결과를 기다리지 않아도 다음 작업 수행 가능. 대부분의 output operation. I/O 연산을 요청한 다음 바로 CPU operation. 처리가 됐을 때 인터럽트를 받아서 다음을 처리.



비동기적으로 많이 쓰이는 operation을 동기적으로 쓸 수도 있다.



프로그램에서 적지 않은 sync i/o가 존재. 그래서 속도가 낮아지는 문제. 이것에 대한 해결책을 모색. batch monitor를 이용하면 하나의 job만 CPU를 쓸 수 있다. CPU가 대기할 때 놀게 하지 않으려면 동시에 여러 job을 수행하게.



**multi programed batch monitor**



### multiprogramming

메인 메모리에 여러개의 active job이 올라가있는 것

degree of multiprogramming



새로운 문제가 대두되기 시작. OS 360에 multiprogram batch monitor를 장착하려고 했으나 기술적 문제.

1. memory protection
2. memory relocation
3. concurrent programming



### memory protection

multiprogramming 때문에 발생. 포인터 에러가 문제.

포인터 에러가 생겨서 다른 job의 영역 침투. 침투 당한 프로그램의 프로그래머는 제대로 작업을 수행할 수 없게 됨. 자기 잘못이 아니라 다른 job의 잘못 때문에 그렇게 되는 것.

OS의 영역을 침범하면 더 큰 문제가 생김. memory protection이 필요하다.



### memory relocation

multiprogramming에서는 하나의 job만 메모리의 시작 위치를 알고 프로그램을 작성 가능. 다른 job은 시작 주소를 임의로 부여 받아야 함. batch monitor에서 개발할 때는 임의의 주소에서도 문제 없이 수행 될 수 있어야 함.

하드웨어 메커니즘을 개발 - base register : 프로그램이 로드된 시작 주소를 담고 있는 레지스터. 프로그램은 0번지로부터 만들어진다고 가정. 실제 컴파일 될 때는 시작 주소와 합쳐져서 주소 생성. 이런 작업은 런타임에 자동적으로 이뤄짐

바운더리를 넘어가면 에러를 발생.



논리적 주소 : CPU에 의해 생성. base register의 값과 더해지게 됨. base + bound value를 체크 -> 통과했을 때 물리메모리에 접근. 

물리 주소 : 일련의 변환을 거친 최종 주소



**MMU(memory management unit)** : base register와 더하고 바운더리를 체크하는 과정. 논리 주소를 물리 주소로 바꿔주는 과정

MMU를 소프트웨어로 구현하면 두 가지 문제가 발생.

1. 속도 문제. instruction이 한 번 수행되려면 여러 개의 instruction이 필요할 수 있다.
2. MMU 역시 instruction으로 구성될 거고, MMU도 주소를 부여받을 것 ->재귀적으로 자신의 코드를 쓰게 될 것

=> MMU를 하드웨어로 구성하게 된다.



- OS 관점에서 MMU는 transparent하지 않다. 새로운 job으로 넘어갈 때 새로운 job의 register 값을 설정해줘야 함. MMU는 OS에 의해 programmable한 entity가 된다.

- register의 값을 관리하는 권한은 OS에게만 부여(**priviliged instruction**)



OS는 무어의 법칙에 의해 진화한 하드웨어를 서포트하기 위해 진화. 하드웨어 효율성 향상을 위해 OS multi 등장 -> MMU 하드웨어 등장 -> ...

OS와 하드웨어는 함께 영향을 주며 발전. 



### concurrent programming

공유되는 자원이나 데이터가 문제.



OS를 만들던 사람들이 패닉에 빠짐. 학문적으로 연구해야할 대상이라는 것을 깨닫기 시작.





## Phase 2 - 1960s 후반

하드웨어가 점차 발전하기 시작. 트랜지스터 발명. 집적회로 기술 발전. OS의 역할이 바뀌기 시작. 어떻게 하면 사람들의 생산성을 향상시킬 수 있을까가 목표가 됨. 인건비는 비싼데 idle하게 CPU의 처리를 기다려야 함 -> 개개인에게 컴퓨터를 하나씩 주고 원할때 쓰게 만들면 됨. 

terminal이 쌌다. typowriter 같은 것인데 중앙의 컴퓨터와 연결되어 데이터를 입력하거나 출력할 수 있는 장치

terminal의 요청이 묶여서 TCU에 의해 정리되어 서버 컴퓨터에 전달. 

terminal을 한 대씩 프로그래머에게 전달. interactive하게 사용할 수 있게 됨.



문제 - 여러 명의 유저에게 하나의 CPU를 제공하면서 interactive하게 보이게 해야 한다.

1. 시간을 동일하게 할당해서 나눠준다. 한 명당 100밀리 세컨드 등



### Phase 2-1 - interactive Time sharing operating system

지금 OS의 근간.

1. 이게 생기면서 사람들이 착각하게 됨. 서버를 자기 혼자 소유하고 있는 듯이 착각 -> 개인 정보를 저장하기 시작. file system을 다시 설계하게 됐다. 사용자별로 소속을 규정하고 file에 접근 가능 여부를 설정. 

2. OS를 평가하는 metric이 변함. batch monitor 시대에는 단위 시간 당 얼마나 많은 job을 처리하는가(throughput)

   -> 응답이 얼마나 빨리 오는가(response time), private 정보가 얼마나 잘 보호되는가

Time sharing OS도 정말 많은 문제점을 넘어서야 하게 됐다. 70s, 80s 90s 초반을 거치면서 대부분 OS의 중요한 이론이 정립되게 됨.



















