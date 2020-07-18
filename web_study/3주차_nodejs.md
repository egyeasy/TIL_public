```bash
sudo npm install -g express
sudo npm install -g express-generator
```

generator를 통해서 더 쉽게 구축할 수 있다.



프로젝트 만들 폴더에서

```bash
express {server 이름}
```



bin에는 실행할 수 있는 binary들이 있다.

서버를 돌리려면

```bash
node bin/www
```

module이 설치 안돼있다

-> http-errors 모듈 설치

직접 설치해줘야 하는게 불편하다.



일단 기본적으로 필요한 라이브러리들이 package.json에 명시돼있다.

package.json이 있는 위치에서

```bash
npm install
```

이후에 서버를 돌리면 돌아간다.



그리고 패키지 설치할 때 --save 옵션을 붙여줘야 package.json에 추가 되는 것이 원칙이다.



### node modules

용량이 크므로 .gitignore에 등록하는 것이 중요하다.

따라서 원격에서는 package.json으로 어떤 라이브러리들이 있는지 커뮤니케이션한다.



###  실행 명령어 - scripts

package.json에 단축어가 정의되어있다.

'start'라는 서버 시작 명령어는

```bash
npm run start
```

로 실행할 수 있다.



### 렌더링

routes/index.js -> index라는 페이지를 render해준다.

index라는 페이지를 views/index.jade에서 가져온다.



### 라우팅

app.js 내에서 app.use('/', indexRouter);

를 통해 '/' 주소에 index를 연결시킬 수 있다.





