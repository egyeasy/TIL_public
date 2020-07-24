### 새로운 프로젝트를 시작하자

```bash
express test-server
cd test-server
npm install
```



### package.json

```json
{
  "name": "test-server",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "start": "nodemon ./bin/www"
  },
  "dependencies": {
    "cookie-parser": "~1.4.4",
    "debug": "~2.6.9",
    "express": "~4.16.1",
    "http-errors": "~1.6.3",
    "jade": "~1.11.0",
    "morgan": "~1.9.1"
  }
}
```



### routes/test.js

```js
var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function (req, res, next) {
    res.send('respond with a resource');
});

module.exports = router;

```



### app.js

```js
var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var testRouter = require('./routes/test');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'jade');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/test', testRouter);
```



### workbench 테이블 생성

student table에 name, money column으로



### ECMA

ES1, ES2, ... ES6

ES6로 넘어올 때 큰 변화들이 있었다.



### test.js

```js
/* GET users listing. */
router.get('/', function (req, res, next) {
    res.send('respond with a resource');
});

module.exports = router;

```



ES6로 표현

```js

/* GET users listing. */
router.get('/', (req, res, next) => {
    res.send('respond with a resource');
});

module.exports = router;
```

앞으로 웬만하면 arrow를 사용한다.



## MySQL 연동을 해보자

```bash
npm install mysql2
```

### test.js

```js
var express = require('express');
var router = express.Router();

const mysql = require('mysql2'); // 모듈 불러오기
const connection = mysql.createConnection({
    host: 'bookdb.cvjxqasrx3vf.ap-northeast-2.rds.amazonaws.com',
    user: 'admin',
    password: 'adminadmin',
    database: 'bookdb'
})
```

원래는 다른 곳으로 빼야하는데 여기 일단 작성



쿼리를 날려보자

```js
/* GET users listing. */
router.get('/', (req, res, next) => {
    connection.query('SELECT * FROM USER', (err, results) => {
        console.log(results);
        res.send('respond with a resource')
    });
});
```

쿼리문을 날리고 콜백 함수가 실행된다.

nodemon 켜서 /test로 들어가면 정상작동함



### DB 데이터 계산

학생들의 평균값을 보여준다고 하자

```js
/* GET users listing. */
router.get('/', (req, res, next) => {
  connection.query('SELECT * FROM USER', (err, results) => {
    console.log(results);

    let sum = 0;
    for (let user of results) {
      sum += user.money;
    }
    const moneyAvg = sum / results.length;
    console.log(moneyAvg);

    connection.query('SELECT * FROM USER WHERE money > ?', [moneyAvg], (err, results) {
      console.log(results);
      res.json({ status: 200, arr: results })
    })
  });
});
```



indent가 계속해서 안으로 들어가게 된다.

이걸 해결하기 위해 promise를 사용한다.



### promise

쿼리에 promise를 사용해보자



```js
var express = require('express');
var router = express.Router();

const mysql = require('mysql2/promise'); // 모듈 불러오기

const pool = mysql.createPool({
  host: 'bookdb.cvjxqasrx3vf.ap-northeast-2.rds.amazonaws.com',
  user: 'admin',
  password: 'adminadmin',
  database: 'book'
})
```

pool은 connection들의 집합. pool에서 connection을 꺼내와서 쓰게 된다.



```js
router.get('/', (req, res, next) => {
  pool.getConnection()
    .then(connection => {
      return connection.query('SELECT * FROM USER');
    })
    .then(results => {
      console.log(results[0]);
      res.json({ status: 200, arr: results[0] });
    })
});

```



### async await

```js
/* GET users listing. */
router.get('/', async (req, res, next) => {
  const connection = await pool.getConnection();
  const [results] = await connection.query('SELECT * FROM USER');
  console.log(results);
  connection.release(); // connection을 반남
  res.json({ status: 200, arr: results });
});
```

release를 안해주면 connection에 대한 연결이 많아졌을 때 서버가 터질 수 있다.



에러는 어떻게 받게 할까?

```js
/* GET users listing. */
router.get('/', async (req, res, next) => {
  const connection = await pool.getConnection();
  try {
    const [results] = await connection.query('SELECT * FROM USER');
    console.log(results);
    connection.release(); // connection을 반남
  } catch (err) {
    console.log(err);
    res.json({ status: 500, msg: 'error!'})
  } 
  res.json({ status: 200, arr: results });
});
```

[results]는 쿼리 결과에서 데이터만 뽑아오기 위함. 첫 번째 요소만 가져오게 된다.



### connection 설정 분리하기

utils/mysql.js 생성

```js
const mysql = require('mysql2/promise'); // 모듈 불러오기
const pool = mysql.createPool({
    host: 'bookdb.cvjxqasrx3vf.ap-northeast-2.rds.amazonaws.com',
    user: 'admin',
    password: 'adminadmin',
    database: 'book'
})

module.exports = pool;
```

pool을 export해서 다른 곳에 쓸 수 있게 한다.



### test.js

```js
var express = require('express');
var router = express.Router();

const pool = require('../utils/mysql')
```



### .env -> 패스워드 숨기기

```env
DB_HOST="bookdb.cvjxqasrx3vf.ap-northeast-2.rds.amazonaws.com"
DB_USER=admin
DB_PASSWORD=adminadmin
DB_NAME=book
```



### mysql.js

```js
const mysql = require('mysql2/promise'); // 모듈 불러오기

require('dotenv').config();

const pool = mysql.createPool({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    database: process.env.DB_NAME
})

module.exports = pool;
```



### .gitignore

```gitignore
.env
node_modules/
```





### CRUD

RESTful api : 행위는 메소드로(get, post 등), 목적어(자원)를 url로 입력

예외) login, register와 같이 컨트롤 자원을 의미하는 URL에는 동사 허용



## postman

주소에 http://localhost:3000/users

입력해서 요청할 수 있다.



### url 데이터 받기

http://localhost:3000/users?name=jaeyun&money=100

```js
const name = req.query.name;
const money = req.query.money;
```



근데 url에 패스워드를 입력하지 않는다.

body에 입력하면 된다.

postman의 body에서

raw, JSON 타입 설정

```json
{
  "name": "hoho",
  "money": 500
}
```

받아오는 방법은

```js
const name = req.body.name;
const money = req.body.money;
```



### params

특정 id의 유저를 가져오는 api를 만든다고 해보자.

```js
router.get('/:id', async (req, res, next) => {
  const userId = req.params.id;
  const [results] = await connection.query('SELECT * FROM USER WHERE id = ?', [userId]);
});
```







































