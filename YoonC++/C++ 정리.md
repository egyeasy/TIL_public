# C++ 정리

### Visual Studio Code 환경설정

(2019.09.09 - MinGW 세팅까지만 해봄) http://blog.naver.com/PostView.nhn?blogId=suwon_man91&logNo=221382448285&parentCategoryNo=&categoryNo=11&viewDate=&isShowPopularPosts=true&from=search



### 헤더파일을 왜 만드는가?

https://downman.tistory.com/6


### 컴파일 및 실행
https://taking.kr/blog/archives/4825.html

coderunner 뭔가 잘 안돼서 그냥 bash에서 g++ 명령어로 컴파일하기로 함

라이브러리 컴파일 : `g++ -c {file.cpp}`
메인 컴파일 : `g++ -o run main.cpp file.o`