# Chapter 4. ROS의 중요 컨셉

## ROS 용어

메시지 방식에 여러가지가 있다.

### Topic, Publisher, Subscriber

publisher : 메시지를 보내는 노드

subsrcriber : 메시지를 받는 노드

topic : 날아가는 메시지(?)



Topic에 대해 1:1, 1:N, N:1, N:N 통신도 가능하다.



publisher			->		subsrcriber

(오도메트리 - 위치)		(SLAM)



### Service, Service server, Service client

토픽은 단방향. **일방향**으로 데이터를 **계속** 보낼 때 사용(ex. 센서)

서버 -  클라이언트 간 서비스 요청/응답

특징 -> **양방향** 통신. 주고 받을 수 있다. **일회성**.



### Action, Action server, Action client

많이 쓰이지는 않는다.

서버 - 클라이언트 관계

클라이언트가 서버에게 액션 목표를 전달하면 서버가 처리를 하면서 처리 결과를 중간에 전송.

ex. 복잡한 태스크. 장시간 걸리는 태스크에서 중간에 결과물을 알고 싶을 때





## 메시지 통신

### 개념 잡기

ROS에서 가장 기본이 되는 기술적 포인트 : **노드 간의 메시지 통신**



### 1. 마스터 구동: XMLRPC(XML-Remote Procedure Call)

`$ roscore`

노드 정보를 관리. 각 실행되는 노드 정보를 관리해서 노드의 통신을 연결시키는 역할.

XMLRPC라는 xml 기반의 간단한 서버-클라이언트 시스템



### 2. subscriber 노드(Node) 구동

`$ rosrun {패키지이름} {노드이름}`

이걸 실행시키자마자 노드 정보를 마스터 노드에게 보냄

노드이름, 토픽 이름, 메시지 타입, ip번호, 포트번호 등의 네트워크 정보 등을 마스터에게 보냄.



### 3. publisher 노드 구동

`$rosrun {패키지 이름} {노드 이름}`

노드이름, 토픽 이름, 메시지 타입, ip 및 포트번호



### 4. 퍼블리셔 정보 알림

마스터는 정보를 받아서 토픽 이름, 메시지 타입을 대조해본 뒤 맞으면 매칭해준다.

마스터는 sub 노드에게 새로운 pub 정보를 알린다.



### 5. 퍼블리셔 노드에 접속 요청

sub은 마스터로부터 받은 pub정보를 이용하여 TCPROS 접속을 요청



### 6. sub 노드에 접속 응답



### 7. TCP 접속

TCP/IP 통신으로 바뀌고 접속된다



### 8. 메시지 전송

pub은 sub에게 메시지를 전송(토픽)



### 9. 서비스 요청 및 응답





### 예제 turtlesim

roscore는 한번만 실행

sub: turtlesim_node 노드(정보 구독)

pub: turtle_teleop_key 노드 -> 키보드 입력(정보 발행)





## ROS 메시지

방식 - 토픽, 서비스, 액션, 파라미터



### 파라미터 서버

ROS Master 기능의 일부.

네트워크에 글로벌 변수 같은 것을 지정해놓고 노드들이 접근해서 읽고 쓰는 것.



###  Twist

- linear : 병진 속도(vector {x, y, z})
- angular : 각도 바꾸는 속도(vector {x, y, z})



### 메시지

노드 간에 데이터 주고 받을 때 사용하는 데이터의 형태

- 토픽, 서비스, 액션은 모두 메시지를 사용

- 단순 자료형
- 메시지 안에 메시지를 품고 있는 간단한 데이터 구조
- 메시지들이 나열된 배열과 같은 구조





## Name

- 노드, 메시지가 가지는 **고유의 식별자**
- ROS는 그래프(graph)라는 추상 데이터 형태(abstract data type) 지원





## 좌표 변환(TF, transform)

- 각 조인트(joint)들의 상대 좌표 변환



## 클라이언트 라이브러리(Client Library)

다양한 프로그래밍 언어 지원

우리는 roscpp을 쓸 것



## 이기종 디바이스 간의 통신

### 원격으로 이미지 전송

다른 디바이스의 카메라 정보를 받아와보자.

터미널에서 `eb`를 쳐서 맨 아래로 가보자(강사님이 설정해놓은 명령어)

export ROS_MASTER_URI=http://192.168.0.61:11311 등으로 다른 사람의 ip를 써주기(master를 다른 사람으로 설정)

export ROS_HOSTNAME=192.168.10.87 등으로 자기 ip 써주기



source ~/.bashrc 후에

`rqt_image_view`



master가 turtlebot 창을 켜고

이기종에서 turtlebot key 입력 node를 켜면 조종할 수 있게 된다.

같은 네트워크 내에서 같은 이름의 node를 실행하면 기존 node가 죽음 -> 기존에 조종하고 있던 사람이 못 조종하게 됨



### 안드로이드 스마트폰의 가속도 값을 PC에서 확인하기(App 링크 참고)

휴대폰에서 앱을 실행하고, 그 값을 PC에서 확인

rqt 실행 -> plot -> /imu/linear_acceleration을 선택

스마트폰의 움직임을 plot으로 볼 수 있다(각 축의 가속도 값)



### 안드로이드 스마트폰으로 TurtleBot 제어하기(App 링크 참고 - ROS Control)

PC에서 turtlesim을 띄워놓는다. 이걸 스마트폰에서 조종할 수 있다.(linux - android 간 통신이 되는 것)



terminator라는 터미널 추천 -> 다중 창, 다중 명령 가능, GUI를 통한 스플릿 가능