# Chapter7 ROS 기본 프로그래밍

## 프로그래밍 전에 알아둬야 할 사항

- 표준 단위
  - SI 단위 사용(인치)
  - angle - radian
- 좌표 표현 방식
  - x: forward, y: left, z: up
  - 오른손 법칙
- 프로그래밍 규칙 - C++ style guide 피피티 링크에 걸려있음



## 메시지 통신의 종류

토픽, 서비스, 파라미터



### 토픽을 직접 작성해보자

topic / publisher / subscriber

**package.xml** : 패키지 설정 파일 -> 패키지의 이름, 저자, 오픈소스 라이선스, 의존한 패키지

pdf 파일의 내용을 복붙.



name : 패키지 이름

version : 패키지의 버전

description : 패키지에 대한 설명. 두 세줄 정도로 적어주는 게 좋다. 공식 패키지에 대한 위키 페이지가 만들어질 때 사용된다.

author : 복수의 저자면 author 태그를 여러 개 써주면 됨.

maintainer : 유지 보수한 사람.

url type bugtracker : 버그가 있으면 여기로 와서 알려줘라

url type repository : 레포지토리 주소

url type website : 패키지 설명하는 웹사이트

buildtool_depend : 빌드할 때 뭐 쓸지 -> 지금은 catkin 쓴다고 보면 됨.

build_depend : 빌드할 때 의존성(cpp 쓸거라 roscpp, bool이나 int 같은거 쓸거라 std_msgs)

run_depend : 실행할 때 의존성. 대부분 위와 같은데, message_generation(message를 만들어주기 위해) / message_runtime만 다르다.



### 3) 빌드 설정 파일(CMakeLists.txt) 수정

기존의 예제가 들어가있다. 복붙해서 대체.

내용은 빌드할 때 사용되는 옵션이라고 보면 된다.



cmake_minimum_required : cmake가 2.8.3 버전 이상이면 빌드에 큰 문제가 없다.

project(ros_tutorials_topic) : package.xml의 패키지명과 동일하게 써줘야 한다.

find_package : 있어야 하는 패키지를 명시

add_message_files : 특정한 이름의 메시지를 만들어줌

generate_messages : 바로 위 메시지를 빌드할 때 std_msgs에 의존성이 있음을 기술

catkin_packages : LIBRARIES는 ros_tutorials_topic이 필요

include_directories : 써있는 대로 하면 기본 패키지들을 쓸 수 있다. 추가로 'include'를 쓰면 include 폴더를 사용해서 사용자가 추가한 패키지를 쓸 수 있다.



토픽을 보내는/받는 실행파일을 각각 만든다.

add_excutable : topic_publisher라는 노드를 만들 때 src/topic_publisher.cpp 파일을 참고한다.

add_dependencies : topic_publisher라는 노드를 만들 때 뒤의 것들을 의존한다. ex) 메시지는 헤더 파일을 생성하게 되는데, 이 메시지를 빌드하고 나서 topic_publisher.cpp을 빌드해야 한다. 이것을 명시해주는 곳이다.

target_link_libraries



### 4) 메시지 파일 작성

MsgTutorial.msg 파일에

time 형식을 갖는 stamp 메시지를,

int32 형식을 갖는 data라는 메시지를 넣음.



### 5) 퍼블리셔 노드 작성

ros::init : 노드명 초기화. 같은 노드 이름을 사용할 수 없다. 여기서 정해주는 것. 노드 마스터에 노드 이름, 토픽 이름 등을 보내야 하기 때문에 이름은 무조건 있어야 한다. 

NodeHandle : 바로 밑에서 쓰임

nd.advertise : 퍼블리셔를 만든다. "ros_tutorial_msg"라는 토픽 이름을 가진 MsgTutorial을 씀. 100은 publisher queue 사이즈. 네트워크가 늦어졌을 때 이 사이즈 개수 만큼 메시지를 쌓아놓음.



**while** **문**

ros::ok() : 프로그램이 정상적인 한 계속 돌겠다.

msg.stamp : 현재 시간의 stamp 메시지에 담는다.

msg.data : count 값을 data 메시지에 담는다.



ROS_INFO : 세컨드 단위, 나노세컨드 단위, count 값을 표시 -> **printf** 라고 보면 됨(우리의 DLOG(INFO))

warning, error와 같은 종류로도 로깅할 수 있음.



ros_tutorial_pub.publish(msg) : 메시지 발생

loop_rate.sleep() : 0.1초 만큼 쉰다.



### 6) 서브스크라이브 노드 작성

**main 함수**

ros::init : 노드명 초기화

ros_tutorial_sub : 서브스크라이버 선언. 토픽 이름은 위와 동일하게.

msgCallback : 메시지를 받았을 때 수행하는 콜백 함수.

ros::spin() : 메시지가 수신되기를 대기. 수신되었을 경우 콜백함수를 실행.



**msgCallback 함수**

받을 토픽의 형태를 인자로 정해준다.



다 옮겨적은후 `cm`이라고 하면 빌드됨 -> 강사님이 만들어놓은 단축키

build에는 빌드관련 설정

devel에는 MsgTutorial.h라고 헤더파일이 만들어짐.

실행가능한 퍼블리셔, 섭스크라이버 노드 실행 파일도 여기 있음.



단, 하나의 노드에서 복수의 퍼블리셔/서브스크라이버 역할을 수행 가능





## 서비스 프로그램을 작성해보자

토픽과 유사하므로 구두로 넘어감. 나중에 꼭 실행해볼 것.

소스코드 부분 따라서 하면 바로 실행할 수 있다.



클라이언트는 한번 실행되고 result를 받아서 출력하고 연결이 끊기도록 짜놨다. 그렇게 하지 않을 수도 있다.



일회성이어서 rqt_graph는 사용할 수 없다.





## 파라미터

rosmaster가 파라미터 서버 역할도 하게 됨.

외부의 변수를 통해 내부의 프로세스를 바꾸는 프로그램



spinOnce() 한번 돌고 r.sleep으로 재운다.





## roslaunch

**하나 이상의 노드를 실행하는 것**



### \<launch\>

pkg : 패키지의 이름

type : 노드명

name : 노드명 겹치지 않도록 이름을 바꿔서 실행

