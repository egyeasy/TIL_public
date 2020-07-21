bin의 www가 실행 파일이고 이게 app.js를 참조한다. -> 본체는 app.js

`node ./bin/www` : 실행방법. package.json에 정의된 명령어로 `npm run start`로 실행 가능하다.



app.use 를 통해 url을 맵핑 가능



users의 하위 경로를 만드려면?

### users.js

```js
var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function (req, res, next) {
  res.send('respond with a resource');
});

router.get('/all', function (req, res, next) {
  res.send('all');
});
```



## JSON 보내기

```js

// json을 보낼 수 있다
router.get('/json', function (req, res, next) {
  res.json({ 'a': 1, 'b': 2 });
});

```

key값은 항상 string이어야 함

key에 따옴표를 안써도 알아서 스트링으로 변환. 안 쓰는 것을 컨벤션으로 많이 씀.



## nodemon

매번 서버 껐다가 켜는게 귀찮으면

`npm install nodemon --save`

node monitoring을 설치 가능 -> 변경사항을 모니터링. 자동으로 감지해서 서버 재시작



`nodemon ./bin/www` 으로 실행가능

package.json에 등록해놓다

```js
{
  "name": "server",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start": "nodemon ./bin/www"
  },
```



### index.js

'index'는 view/index.jade를 일컫는 말이다.



### index.jade

jade는 html을 좀 더 팬시하게 작성할 수 있게 해주는 포맷

title이라는 변수에 원하는 값을 넣어서 html에 보여줄 수 있다.

앞으론 jade를 잘 안쓸텐데, html, css로 짜는게 더 풍부하게 할 수 있어서다.

EJS라는 템플릿이 있기 때문에 jade를 파기할 것



### app.js

```js
// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs'); // jade 대신 ejs 쓰겠다.
```



### EJS

`npm install ejs`

jade 파일의 확장자를 ejs로 바꿔주면 된다.



### static 파일

```js
// app.js
app.use(express.static(path.join(__dirname, 'public'))); // static 파일(css, js, 이미지)을 public에서 찾겠다
```





## 서버에 요청해서 JSON 받아오기

```html
// 01home.js
  <script>
    fetch('http://localhost:3000/users/json')
      .then(res => res.json())
      .then(data => {
        alert(data);
        alert(data.b);
      })
  </script>
</body>
```

return으로 응답을 받아서 json 형태로 만들고, 걔를 data로 받아서 alert 해준다.



태그의 text를 바꿔줘보자.

```js
    fetch('http://localhost:3000/users/json')
      .then(res => res.json())
      .then(data => {
        // alert(data);
        // alert(data.b);
        document.getElementById("id").innerHTML = data.b;
      })
```



## 아마존에 올리기

### EC2 - Elastic Cloud Computing

하드웨어와 운영체제를 제공해주는 서비스

인스턴스 시작하면 이미지 선택 가능. 이미지는 운영체제 + a (운영체제에 필수적인 패키지들)

우분투 18.04가 확장하기 좋으므로 이걸 선택

계속 다음 선택한다.



보안 그룹 -> 22번 포트만 열려있다(화이트리스트)

직접 접속해보기 위해 3000번을 뚫어놓도록 하자.



생성하면

새 키 페어 생성

키 페어는 ssh로 접속할 때 신원을 인증하는데 쓰임.

이게 사라지면 절대 접속 못하고, 노출되면 서버가 털림

잘 보관할 것



### 인스턴스 정보 보기

IPv4 퍼블릭 : ip 주소

퍼블릭 DNS : ip의 별칭

AMI ID : 우분투 이미지



### 서버에 소스 가져오기

깃헙에 express 프로젝트를 올리고

터미널에서 `ssh -i ~/Desktop/websnu.pem ubuntu@54.180.125.149` 를 통해서 접속할 수 있다.

`unprotected private key file`이라는 에러 메시지가 뜰 것

맥북에서는 권한 설정을 해줘야 한다.

`chmod 400 ~/Desktop/pem/websnu.pem`

이후 다시 접속하면 된다.



git clone을 받고

npm install 하면 설치가 안된다. npm과 node가 없기 때문



우분투에서는 다운/설치할 수 있는 리스트를 만들어야 한다.

`sudo apt-get update`

`sudo apt-get install nodejs` : node 설치

`sudo apt-get install npm` : npm 설치



프로젝트 경로로 가서

`npm install`

`npm run start`



`{public ip}:3000` 으로 접속할 수 있다.



### pm2 - Process Monitoring

npm run start는 쉽게 끌 수 있으므로 위험하다.

pm2라는 모듈로 관리해보자.

`sudo npm install -g pm2`



`pm2 start ./bin/www`

이제 계속해서 실행해놓을 수 있다.



`pm2 list` : 서버 목록 확인

`pm2 stop {name}` : 서버 멈추기

`pm2 restart {name}` : 서버 재시작

`pm2 delete {name}` : 서버 삭제



### 인스턴스 종료

과금을 막기 위해 인스턴스 보기 > 작업 > 인스턴스 종료































