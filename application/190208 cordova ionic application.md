# 안드로이드 앱 출시

https://devkimgoon.tistory.com/8?category=719607

-설치 및 환경 설정은 이 블로그 참조



https://www.youtube.com/watch?v=z4qp7AuqN68

-워드프레스 apk 파일화는 이 유튜브 참조



https://ionicframework.com/docs/publishing/play-store

-출시는 ionic 공식 문서 참조



### 용어 정리

- cordova : 앱 개발을 쉽게 할 수 있도록 돕는 프레임워크
- ionic : cordova 내에서 또 돕는 프레임워크. ios와 안드로이드 버전 모두를 지원한다.



### 단계 정리

1. ionic 프로젝트 생성 

2. 프로젝트 소스에 홈페이지 url을 입력함으로써 웹앱 생성

3. unsigned apk 파일 생성(다양한 옵션을 통해 디버그 모드, 출시 모드 등으로 만들 수 있음)

4. 공식 문서 참조하여 key 생성, sign 후 앱에 등재

   -이 때 주의할 것 : key sign할 때 sudo 써줄 것, zip 설치 경로를 통해 zip을 실행하는 것

   -key 비밀번호는 어디든 적어서 보관해둘 것. key 파일도 하나의 key로 계속 버전업 해야하니 꼭 잘 보관할 것.

```
sudo ~/Library/Android/sdk/build-tools/28.0.3/zipalign -v 4 app-release-unsigned.apk undongjang_release_10101.apk
```



- 출시 이전 단계에서 출시 모드를 낼 때 버전을 변경해야 하는데, `pjt_folder\config.xml` 에서 line 2의 version을 바꿔주는 것이 맞는 듯. 별도 언급 없으면 그런 것으로.



### 안드로이드 에뮬레이터

가지고 있는 안드로이드 폰이 없어서 에뮬레이터를 설치해서 apk 파일을 실행해보기로 함.

1) nox - 실행이 안됨

2) bluestacks

3) android emulator - 가상 디바이스에서 실행

`project_name/platforms/android/` 를 project directory로 설정해서 실행.

debug.apk 파일을 에뮬레이터에 드래그 앤 드롭으로 깔아서 실행 가능

reference : https://mainia.tistory.com/5301


### 참고
동기 컴퓨터 Android SDK Location : C:\Android\Device
