# 19. 페이징 : 더 빠른 변환(TLB)

페이징은 상당한 성능 저하 유발 가능

-> 가상 주소에서 물리 주소로의 주소 변환을 위해 메모리에 존재하는 매핑 정보를 읽는 작업이 추가적으로 요구되기 때문



**핵심 질문: 주소 변환 속도를 어떻게 향상할까**



운영체제의 실행 속도를 개선하기 위해 **하드웨어로부터 도움**을 받는다.

-> **변환-색인 버퍼(Translation-Lookaside Buffer, TLB)** 도입

- TLB는 MMU(Memory-Management Unit)의 일부
- 가상 주소-실 주소 변환 정보를 저장하는 하드웨어 캐시
- address-translation cache라고도 할 수 있음



## 19.1 TLB의 기본 알고리즘

주소 변환부가 **선형 페이지 테이블**과 하드웨어로 관리되는 **TLB**로 구성되어있다고 가정.

하드웨어 부분의 알고리즘:

1. 가상 주소에서 가상 페이지 번호(VPN) 추출
2. 해당 VPN의 TLB 존재 여부 검사
   - 만약 존재하면(**TLB Hit**):
     - 해당 TLB 항목에서 PFN(페이지 프레임 번호) 추출
     - 가상 주소의 오프셋과 합쳐서 물리주소 구성 -> 메모리 접근
   - 존재하지 않는다면(**TLB Miss**)
     - 하드웨어가 페이지 테이블에 접근
     - 가상 메모리 참조가 유효하고 접근 가능하면 해당 변환 정보를 TLB에 insert
     - 지금까지의 명령어를 재실행(retry instruction)



TLB 또한 모든 캐시의 설계 철학처럼 "주소 변환 정보가 대부분의 경우 캐시에 있다"는 가정을 전제로 만들어졌다.

메모리 접근 연산은 CPU 연산에 비해 매우 시간이 오래 걸리기 때문에 TLB의 효과는 엄청나게 좋다.



## 19.2 예제: 배열 접근

VPN 06	a[0] a[1] a[2]

VPN 07	a[3] a[4] a[5] a[6]

VPN 08	a[7] a[8] a[9]



배열 a에 순차접근한다고 할 때,

a[0], a[3], a[7]에서만 miss가 발생하게 된다.

같은 VPN 내에 항목들은 **공간 지역성(spatial locality)**가 존재한다.



루프 종료 후에도 배열이 사용되어 히트가 발생한다면

**시간 지역성(temporal locality)**가 존재한다는 뜻이다.

시간 지역성은 한번 참조된 메모리 영역이 짧은 시간 내에 재참조되는 현상을 가리킨다.





## 19.3 TLB 미스는 누가 처리할까

두 가지 방법이 있다. 하드웨어 vs 소프트웨어

1. 하드웨어

   - 하드웨어가 페이지 테이블에 대한 명확한 정보를 가지고 있어야 함
   - 메모리 상 위치와 정확한 형식을 파악하고 있어야 함

   - 미스 발생 시
     1. 페이지 테이블에서 원하는 페이지 테이블 엔트리를 찾고
     2. 필요한 변환 정보 추출
     3. TLB 갱신
     4. TLB 미스가 발생한 명령어를 재실행
   - ex) 인텔 x86 CPU의 멀티 레벨 페이지 테이블

   

2. 소프트웨어

   - **RISC(Reduced Instruction Set Computing, 축소 명령어 컴퓨터)**에서 소프트웨어 관리 TLB를 사용

   - 미스 발생 시

     1. 하드웨어가 exception 시그널 발생시킴
     2. 운영체제는 명령어 실행을 잠정 중지
     3. 실행 모드를 커널 모드로 변경(특권 레벨로의 상향 조정)
     4. TLB 미스 처리용 **트랩 핸들러** 실행
        - 트랩 핸들러는 페이지 테이블을 검색하여 변환 정보를 찾고
        - 특권 명령어를 사용하여 TLB에 접근해 갱신한 후 리턴
     5. 하드웨어가 명령어를 재실행

   - 시스템 콜 호출 시 트랩 핸들러와의 차이점 1

     - 시스템 콜 호출 시에는 리턴 후 시스템 콜 호출 명령어의 **다음 명령어**를 실행
     - TLB 미스 처리의 경우 트랩을 발생시킨 명령을 **다시 실행**

     -> 운영체제는 트랩 발생의 원인에 따라 현재 명령어의 PC값 혹은 다음 명령어의 PC값을 저장한다.

   - 차이점 2
     - TLB 미스가 무한 반복되지 않도록 주의해야 한다.
     - TLB 미스 핸들러를 접근하는 과정에서 TLB 미스가 발생하는 상황이 있을 수 있다.
     - 이를 위해 방법 1) TLB 미스 핸들러를 물리 메모리에 위치시킬 수 있다.
     - 방법 2) TLB의 일부를 핸들러 코드 주소를 저장하는 데 영구히 할당 -> TLB 핸들러는 항상 TLB 히트(= **연결(wired)** 변환)
   - 소프트웨어 관리 방식은 **유연성**이 높다.
     - 운영체제는 하드웨어 변경 없이 페이지 테이블 구조를 자유로이 변경 가능
   - **단순하다**
     - 미스가 발생했을 때 하드웨어는 별로 할 일이 없다.

   

   ## 19.4 TLB의 구성: 무엇이 있나?

   일반적으로 하드웨어 TLB는 32, 64 혹은 128개의 엔트리를 가진다.

   

   **완전 연관(fully associative)** 방식으로 설계된다.

   - 변환 정보는 TLB 내 어디든 위치할 수 있다.
   - 검색은 TLB 전체에서 병렬적으로 수행된다.

   

   ### TLB의 구성

   VPN	|	PFN	| 다른 비트들

   다른 비트들 - valid bit, protection bit, address-space identifier, dirty bit

   

   ## 19.5 TLB의 문제: 문맥 교환

   TLB의 가상 주소 - 실제 주소 간 변환 정보는 해당 프로세스 내에서만 유효하다.

   

   **핵심 질문: 문맥 교환 시 TLB 내용을 어떻게 관리하는가**

   

   방법 1. 문맥 교환을 수행할 때 다음 프로세스가 실행되기 전에 TLB 내용을 비우기

   - 특권을 갖는 **하드웨어 명령어**를 사용하여 가능하다.
   - (소프트웨어 관리 TLB에서) 페이지 테이블의 베이스 레지스터가 변경될 때 비우기를 하면 된다.
   - (하드웨어 관리 TLB에서) 비우는 작업은 모든 valid bit를 0으로 설정하는 것

   - 비용
     - 새로운 프로세스 실행될 때 데이터와 코드 페이지 접근으로 인한 TLB 미스가 발생
   - 개선 방안
     - TLB 내에 **주소 공간 식별자(Address Space Identifier, ASID)**라는 필드 추가
     - ASID는 PID와 유사하지만 더 적은 비트로 구성
     - ASID 정보를 추가함으로써 여러 프로세스들이 TLB 공간을 공유 가능
     - 여러 프로세스들이 하나의 페이지를 공유하고 있을 경우 **공유**를 하면 사용되는 물리 페이지 수를 줄이고 메모리 부하도 줄일 수 있다.

   

   ## 19.6 이슈 : 교체 정책

   **핵심 질문 : TLB 교체 정책은 어떻게 설계하는가**

   1. 최저 사용 빈도(Least-Recently-Used, LRU)
      - 사용되지 않은지 오래된 항목일수록 사용될 가능성이 작다 -> 교체 대상으로 적합
   2. 랜덤 정책
      - 교체 대상을 무작위로 정함
      - 구현이 간단하고 예상치 못한 예외 상황의 발생 피할 수 있음

   

   

   

   

   

   

   

   

   

