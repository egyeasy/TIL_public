## React

html로 작성하는 것은 너무 힘들고 구조화되지 못함.

js로 html을 만드는 문법이 만들어지기 시작함 = jsx

jsx문법을 사용하여 컴포넌트라는 단위를 만들어내고, 컴포넌트들을 레고처럼 조합하여 만들어내는 것.

ui에 변경 사항이 있을 때 페이지를 전체를 새로 고치지 않아도 됨 -> **Virtual DOM**

라이브러리 또는 프레임워크다.



express generator를 사용해서 서버 구조를 만든 것처럼 리액트도 가능.

`npx create-react-app hello-react`

 프로젝트 시작 후 폴더에서

`npm install`

`npm run start`

이렇게 구동을 할 수 있다.



서버까지 돌려주는 것은 개발모드에서 보조를 해주는 것이다.

실제로는 리액트가 html을 만들어주는 데까지임.



### 크롬 익스텐션 설치

react developer tools 설치

리액트로 돌아가는 페이지에 가면 아이콘이 활성화된다.

개발자 도구에서 리액트 관련 새로운 탭이 생겨있다.

components -> app 우측의 <> 클릭하면 완성된 html 대신 직접 작성한 js 코드를 볼 수 있다.



### 빌드

`npm run build`

build > static > js에 가보면 소스가 변환되어서 저장되어 있다.

index.js는 난독화됨.(맨 마지막에 static/js의 파일을 가져오고 있는 것이 보임)

빌드 폴더 안에 있는 것만으로도 완전한 실행이 가능하다.



index.js, App.js 외 App.css, App.test.js 등은 삭제

index.js, App.js는 간소화

### App.js

```js
import React from 'react';

function App() {
  return (
    <div className="App">
      hello
    </div>
  );
}

export default App;

```



### index.js

```js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(
    <App />,
  document.getElementById('root')
);

```



index.js를 보면 App을 가져와서 넣어주고 있는게 보인다. 이렇게 컴포넌트들을 가져와서 하나의 페이지에 넣을 수 있다.



## State

### 변수 변경이 html에 즉각적으로 반영되게 하기

App.js

```js
import React, {useState} from 'react';

function App() {
  const [count, setCount] = useState(0); // 변수 이름, 변수 변경할 함수, 초기값 0
  const addOne = () => {
    setCount(count + 1);
  }
  return (
    <div className="App">
      <p>{count}</p>
      <button onClick={addOne}>Click Me!</button>
    </div>
  );
}

export default App;
```



### 컴포넌트 합치기

Sub.js 생성

```js
import React, {useState} from 'react';

function Sub() {
  return (
    <div className="App">
      <p>hohohoho</p>
    </div>
  );
}

export default Sub;
```



App.js에 추가

```js
import React, {useState} from 'react';
import Sub from './Sub'

function App() {
  const [count, setCount] = useState(0); // 변수 이름, 변수 변경할 함수, 초기값 0
  const addOne = () => {
    setCount(count + 1);
  }
  return (
    <div className="App">
      <p>{count}</p>
      <button onClick={addOne}>Click Me!</button>
      <Sub/>
    </div>
  );
}

export default App;
```





## Props

한 컴포넌트에서 다른 컴포넌트로 변수를 내려주기

App.js

```js
import React, {useState} from 'react';
import Sub from './Sub'

function App() {
  const [count, setCount] = useState(0); // 변수 이름, 변수 변경할 함수, 초기값 0
  const addOne = () => {
    setCount(count + 1);
  }
  return (
    <div className="App">
      <p>{count}</p>
      <button onClick={addOne}>Click Me!</button>
      <Sub name="hoho" msg="haha"/>
    </div>
  );
}

export default App;

```



Sub.js

```js
import React, {useState} from 'react';

function Sub(props) {
  return (
    <div className="App">
      <p>{props.name}</p>
      <p>{props.msg}</p>
    </div>
  );
}

export default Sub;
```



### state 변수나 함수도 props로 넘겨줄 수 있다

App.js

```js
import React, {useState} from 'react';
import Sub from './Sub'

function App() {
  const [count, setCount] = useState(0); // 변수 이름, 변수 변경할 함수, 초기값 0
  const addOne = () => {
    setCount(count + 1);
  }
  return (
    <div className="App">
      <p>{count}</p>
      <button onClick={addOne}>Click Me!</button>
      <Sub name="hoho" count={count} addOne={addOne}/>
    </div>
  );
}

export default App;

```



### Redux, Mobx

전역으로 state를 관리할 수 있게 도와줌



### 라이프사이클, useEffect

업데이트가 되는 순간을 라이프 사이클이라고 부른다.

라이프사이클 중에 무언가를 하기 위해 useEffect를 사용



업데이트가 될 때마다 console log를 찍어주고 싶다면

App.js

```js
import React, {useState, useEffect} from 'react';
import Sub from './Sub'

function App() {
  const [count, setCount] = useState(0); // 변수 이름, 변수 변경할 함수, 초기값 0
  useEffect(() => {
    console.log('hello')
  });
  const addOne = () => {
    setCount(count + 1);
  }
  return (
    <div className="App">
      <p>{count}</p>
      <button onClick={addOne}>Click Me!</button>
      <Sub name="hoho" count={count} addOne={addOne}/>
    </div>
  );
}

export default App;

```



첫번째 업데이트 때만 로그를 찍고 싶다면

```js
function App() {
  const [count, setCount] = useState(0); // 변수 이름, 변수 변경할 함수, 초기값 0
  useEffect(() => {
    console.log('hello')
  }, []);
```



### clean up 함수

그리는 걸 마운트라고 하는데, 언마운트 시(그린걸 다시 내릴 시) 동작을 하게 하려면

```js
const [count, setCount] = useState(0); // 변수 이름, 변수 변경할 함수, 초기값 0
  useEffect(() => {
    console.log('hello')
    return () => { // 언마운트 시 동작
      console.log('out!');
    }
  });
```



### react Hook

useState, useEffect를 react hook이라고 한다.

hook은 이벤트가 발생할 때 무언가를 해주는 것.

useXXXX 으로 이름지어지는 다양한 hook들이 있다.



### 클래스형, 함수형 컴포넌트

클래스형 컴포넌트 - App을 Component를 상속하는 클래스로 선언

함수형 컴포넌트 - hook을 통해 함수형에서 불가했던 state가 사용 가능해짐. useEffect를 통해서 mount/unmount 순간을 편리하게 제어할 수 있다.(클래스형에서는 mount/unmount시 따로 처리를 해줘야함)



### axios

`npm install axios`

```js
import React, {useState, useEffect} from 'react';
import Sub from './Sub'
import { axios } from axios;

function App() {
  const [count, setCount] = useState(0); // 변수 이름, 변수 변경할 함수, 초기값 0
  useEffect(() => {
    console.log('hello')
    return () => { // 언마운트 시 동작
      console.log('out!');
    }
  });
  const addOne = () => {
    setCount(count + 1);
    const res = await axios.get('url')
    const data = res.data
  }
```







