# 7-1. Multithreading (1)

### Server Architecture

server로 request가 전달되는 통로로 queue가 쓰임.

server의 내부는 무한 루프가 있다. 



### 서버 리퀘스트 받는 패턴

모든 서버 아키텍쳐는 두 가지 방식으로 이루어져있다.

1. iterative server

   서버가 스스로 깨어나서 처리. 병렬성 X

2. concurrent server

   child process(worker)가 request를 처리하게 함. 처리하는 동안 서버는 request queue에서 다른 놈을 받아서 또 다른 worker를 만들어서 처리하게 함. 병렬적 처리.



요즘처럼 복잡 고도화된 시스템에서는 concurrent server를 많이 쓴다. 요즘은 하드웨어 성능 좋고 멀티코어화 -> 병렬성을 높이는 게 좋다. 사용자의 입장에서 볼 때는 response time이 줄어드는 것. 

iterative server는 단순해서 관리하기가 편함



concurrent server의 단점 : request 개수 만큼 process를 만들어야 함.



그래서 고안한 것이 멀티스레딩 -> concurrency는 높이면서 execution unit을 생성하거나 수행시키는 데 드는 부담을 줄임.



