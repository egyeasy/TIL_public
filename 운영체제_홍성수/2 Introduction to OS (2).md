창조적 학습을 해야 함.

초중고 교육 학습의 목표는 지식의 소비자가 되는 것이었다 -> 지식의 생산자가 되어야 함.

지식의 소비자는 다른 연구자들의 결과를 공부해서 시험 보고 그러는 것. 

대학원에서 하는 것은 지식을 생산하는 것. 

지식의 생산자가 되기 위해서는 사고방식을 바꿔야 함.

OS는 굉장히 복잡한 시스템 => 추상화라고 하는 개념적 도구를 사용.

추상화의 장벽을 극복하면 지식의 생산자가 될 수 있다.



### 지식의 생산자와 소비자는 어떻게 다른가?

지식 소비자는 각 시기에 무엇이 출현했는지를 공부할 것. fact들을 받아들이고 학습하는 것

왜 각 fact들이 발생했는가, 원인과 결과를 가지고 연결시켜야 한다.

지난 시간에 한 것은 phase 1의 OS 발전을 story화 한 것(원인과 결과)



초기 OS의 등장은 Human operator 대신에 하드웨어를 잘 쓰기 위해서 등장.

따라서 중요한 것은

1. story line

2. 추상화 - 화장실에서 물 내리는 버튼을 누르면 flush된다는 것이 추상화. 실제 작동원리는 잘 몰라도 큰 그림을 알고 있음(blackbox abstraction) 우리는 OS의 internal을 공부하는 것이 목적. OS가 감싸고 있는 추상화를 뚫고 그 안으로 들어가야 함.

   하드웨어의 추상화 레벨 / 소프트웨어의 추상화 레벨이 서로 다르다. 소프트웨어의 추상화가 H/W에 어떻게 mapping되는지를 알아야 한다.

   개념, 단어의 의미를 정확하게 이해해야 함.

3. 호기심을 가져라.





## Evolution of OS - Phase 3

바로 지금의 시대. 90s 후반 ~ 오늘날

1. 가장 큰 특징 - 인터넷이 필수가 되었다.

   3C Convergence 발생

   요즘의 PC OS는 TCP/IP 연결을 알아서 해준다.



2. PC OS와 서버 OS가 크게 차이나지 않는다.
   - 하드웨어 가격이 굉장히 싸짐
   - PC도 성능이 좋아졌다.



우리가 모바일 하드웨어 기기를 사는 이유?

- 모바일 커뮤니케이션
- 멀티미디어

=> 멀티미디어 support가 굉장히 중요해짐



### 멀티미디어

미디어가 여러개 있다. 과거엔 text만 처리해주면 됐는데 이제는 audio, video를 처리해야 한다. 멀티미디어는 continuous media가 가장 중요하다(특정한 시간적 제약에 맞춰 연속적으로 처리해야하는 데이터)

downloading : 전체 데이터를 확보한 다음에 작업을 시작 가능

streaming : 일부의 데이터만 확보한 상태에도 작업 시작 가능

멀티미디어가 되면서 스트리밍이 중요해졌다. 멀티미디어 support 대상이 바뀜 -> 스케쥴링 방식이 바뀜

우선순위 기반 스케쥴링에서 continuous media를 빠르게 처리하기 위해 bandwidth 기반 스케쥴링.



###phase 3-4 : OS as Commodity

OS가 이제는 보편적인 자원이 됨. 제한적인 사람만 OS에 관심을 가졌어도 됐으나, 이제는 아니다. OS가 기기의 eco-system을 결정하는 중요한 요소가 됨.





좀 더 다른 관점에서 보자.

지금까지는 시장 또는 사용자의 필요성에 따라 어떻게 발전해왔는지를 살펴봤다.

이제는 기능 위주로



###OS characteristics

- Large

  1000 man year가 필요.

- Complex

  asyncronous, 다원적, 여러 개의 job이 돌아가고 있다

- Poorly understood

  개발자들이 계속 이동하는 와중에 개발되고 진화해야 된다.



### OS의 기능

1. coordinator

   멀티태스킹 시스템 - 여러 태스크를 수행. 자원을 차지하기 위해 충돌하는데 OS가 중재자 역할을 해야 함

2. illusion generator

   추상화를 제공해야 함. OS가 abstraction을 통해 프로그램할 수 있는 runtime system을 주는 것

3. standard library

   키보드를 써야 되면 OS의 키보드 라이브러리를 쓰면 됨. 모듈을 제공해서 프로그래밍을 쉽게 만든다.



OS가 관장해야하는 H/W 장치가 무엇이 있을까?

-> CPU, I/O device, memory

1. CPU를 관리하는 OS의 부분 : 스케쥴러, 프로세스 매니저

2. I/O 디바이스 요구 조정 : I/O device manager

3. 메모리 관리



실제 OS를 들여다보면 2개의 시스템이 더 있다.

4. File system

5. network system



그러므로 총 5개의 시스템으로 나뉜다고 볼 수 있다.



네트워크는 I/O 디바이스의 일종이다.

왜 컴퓨터 시스템이 network system을 별도로 가져야 할까? 파일 시스템은 디스크라고 하는 하드웨어를 관리하는 I/O system



UNIX에서 분류되는 I/O device 3가지

1. character I/O device

   I/O 단위가 Byte인 장치(키보드, 마우스), 굉장히 소량의 데이터를 전송

2. Block I/O device

   I/O 단위가 block(하드디스크), 1K byte 등. 주로 File I/O 관장

3. Network I/O device

   Network를 제어하는 장치(소켓)



2, 3의 경우 I/O를 관리를 어떻게 하냐에 따라 성능이 크게 변한다.

중앙고속도로에서 강릉을 가는 사람들을 위해 별도의 길을 뚫어준다면 문제가 해소될 수 있음. OS는 이와 같은 것을 신경써줘야 한다. 



Block I/O

컴퓨터 시스템에는 많은 메모리가 있다. CPU에 가까우면 비싸지만 빠르다. 멀어지면 반대(memoery hierarchy)

우리는 많은 데이터를 hard disk에 저장해서 쓰고 있다. 거기에 가서 가져오는 것은 달나라에서 가져오는 것과 같다. 이걸 효율적으로 가능하게 하려면 달나라에서 가져온 것을 빌려주고 받는 것(caching - 하드웨어적으로 구현할 수도, 소프트웨어적으로 구현할 수도 있다 - OS가 소프트웨어적으로 기능을 제공하는 것이 중요하다)




## Illusion generator로서의 OS

추상화와 같은 얘기.

- Application program
- operating system
- hardware



layer가 잘못 구현, 정책이 잘못 구현됐을 때 제대로 작동하지 않게 된다 -> Thrashing

유저의 수가 늘어날수록 response time이 나빠지게 된다. 어느 threshold를 지나면 응답 시간이 급격하게 증가(Time-sharing 시스템에서의 thrashing)



### summary

OS는 정적으로 멈춰져있는 기술이 아니라, 다양한 이유에 의해 진화해왔다. 그 과정에서 다양한 technical discipline을 받아들여왔다. 처음에는 하드웨어의 효율적 사용을 위해, 이제는 사용자의 사용감, 또는 시장의 요구에 따라 진화해옴. 









































































