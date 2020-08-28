## Route

다시 로드할 필요 없는 element들은 그대로 두고

필요한 것들만 바꿔서 표현하기

근데 url도 바뀌게 하고 싶다면?

-> Route를 사용하면 된다.



ReactRouter라는 라이브러리를 사용해서 위의 url을 갈아끼울 수 있다.

`npm install react-router-dom --save`



### App.js

각각의 페이지에 대해 컴포넌트 만들고 import해서 link하면 된다.

```js
import React, {Component} from 'react';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';
import Home from './Home';
import MyPage from './MyPage';
import Cart from './Cart';

function App() {
  return (
    <Router>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/mypage">My Page</Link></li>
        <li><Link to="/cart">Cart</Link></li>
      </ul>
      <div className="App">
        <Route exact path="/" component={Home}/>
        <Route path="/mypage" component={MyPage}/>
        <Route path="/cart" component={Cart}/>
      </div>
    </Router>
  );
}

export default App;
```





## build 부분만 단독으로 올리기(Hosting) - Amazon S3 hosting

S3는 Simple Storage Service. 정적인 걸 저장해주는 서비스

사진과 같은 정적인 이미지 저장.

MySQL은 S3의 url을 저장.

사진의 경우는 S3의 url을 url로 설정해서 보여주게 된다.



### 버킷 만들기

버킷 - 저장할 폴더

버킷 이름은 해당 지역 내에서 unique해야 한다.



'모든 퍼블릭 엑세스 차단' - 해제(예제 테스트를 위해)

다음 눌러서 생성



퍼블릭 엑세스를 위해 한 번 더 해제해줘야 한다.

권한 탭 > 버킷 정책 > 정책 생성기

Type : S3 Bucket 

Principal : * (모든 것)

Actions : getObject 선택

ARN : arn:aws:s3:::used-book-200827/*	(*는 모두가 접속 허용)



그렇게 생성된 정책을 정책 편집기로 저장



### 호스팅

S3가 웹사이트처럼 동작하게 해야 한다.

지금은 그냥 데이터 덩어리일 뿐.

속성 탭 > 정적 웹사이트 호스팅 > ~~ 호스팅합니다.

인덱스 문서 : index.html

저장

여기 탭의 '엔드포인트'가 이 웹사이트 주소라고 할 수 있다.



### 업로드

프로젝트 폴더 > build 하위의 파일들을 모두 선택해서 업로드

이제 데이터를 담고 있는 웹사이트가 생겨난 것.



### 도메인 연결

AWS 메뉴 중에서 Route 53 - 도메인을 관리하는 페이지

호스팅 영역 생성 > usedbooktest.com 이라는 이름으로 생성

이 이름은 이 도메인을 소유하고 싶다는 선언 -> 사용하려면 도메인을 사야 함(고데리, 가비아 등)

아마존에서도 살 수 있다.(도메인 등록)



이걸 사서 등록하면 실제로 도메인을 쓸 수 있다.



호스팅 영역 생성 후에 레코드 생성 > 단순 라우팅 > 단순 레코드 정의 > 레코드 이름 정하고(e.g. blog) > S3 엔드포인트에 대한 별칭을 설정할 수 있다.

그렇게 하면 S3 엔드포인트를 등록한 도메인으로 연결해서 쓸 수 있다.



레코드를 api로 하고 IPv4와 연결하면 api용 도메인도 설정할 수 있다.





## 프론트에서 api콜 날려서 데이터 받아오기

`npm install axios --save`

### Home.js

```js
import React, {useState} from 'react';
import axios from 'axios';

function Home(props) {
    const res = await axios.get('http://localhost:8000/users');
    const txt = res.data.data;  

  return (
    <div className="Home">
        this is HOME!
        <p>{txt}</p>
    </div>
  );
}

export default Home;

```





## 컴포넌트 반복 생성하기

```js
import React, {useState} from 'react';
import axios from 'axios';

function Home(props) {
    //const res = await axios.get('http://localhost:8000/users');
    //const txt = res.data.data;
    const txt = "txt";

    const a = [1, 2, 3, 4, 5, 6, 7];

  return (
    <div className="Home">
        this is HOME!
        <p>{txt}</p>
        {a.map((number) => <p>{ number }</p>)}
    </div>
  );
}

export default Home;
n
```







