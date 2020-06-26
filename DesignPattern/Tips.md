## Observer vs Listener

MVC 패턴에서 View가 Controller에게 View의 변화를 통보하고자 할 때 일반적으로 View의 멤버로 observer를 두고 View는 변화가 발생 시 등록된 observer의 메소드를 호출하여 통보한다.

반면 button이 클릭되었을 때 동작을 처리하기 위해 ButtonListener를 두고, 클릭 이벤트가 발생 시 해당 이벤트의 종류와 클릭된 버튼의 포인터가 ButtonListener에게 전달 된다.

두 설계는 서로 상당히 비슷해보인다. 그럼 어떻게 구분해야 할까?



### 혼용되는 경우

실제로도 Listener와 Observer의 개념이 혼용되어서 쓰이기 때문에, 어떤 맥락에서는 listener가 observer를 의미하는 경우도 있다. ([참고 링크](https://stackoverflow.com/questions/3358622/observer-design-pattern-vs-listener)) 구글에 "litener pattern"이라고 검색하면 Observer Pattern에 대한 검색 결과가 뜨기도 한다.



### 구분하는 경우

 다만 'Event' Listener와 Observer로 구분지을 경우에는 차이가 좀 더 명확하게 드러난다. ([참고 링크](https://stackoverflow.com/questions/5941800/is-an-eventlistener-an-observable)) Event Listener는 **Event-Driven** 방식의 설계에서 사용되는 객체다. 여기서는 감지하고 핸들링하는 Event를 객체로 정의하게 되고, 일반적으로 Event Raiser(Button 등)로부터 Event Listener에게 event를 전달하는 signleton event 관리자(e.g. TOS의 eventloop)를 두게 된다.

 반면 Observer는 객체로 구현된 Event가 없고, Observable과 Observer 간의 직접적인 메소드 호출을 통해 변화를 감지하고 핸들링한다.

 구체적인 차이점은 3가지가 있다.

1. **사용 목적**

   Event Listener는 event를 감지/raise하는 코드와 event handling하는 코드를 분리하기 위해 사용한다.

   Observer는 한 객체가 다른 객체의 변화를 follow하기 위해 사용한다.

2. **데이터 구조**

   Event Listener 패턴에서는 여러 event의 타입들이 있고, event의 타입마다 handling method가 일대일로 맵핑된다.

   Observer 패턴에서는 하나의 Observable subject에 여러 observer가 붙을 수 있다.

3. **작동 방식**

   Event Listener 패턴에서는 event가 발생할 때 event raiser(e.g. button)가 global한 event 관리자(Singleton 인스턴스, TOS의 eventloop)에게 event 발생을 통보한다. 이는 event raiser는 event handler가 누구인지 모르기 때문이다.

   Observer 패턴에서는 변화가 발생할 때 observable subject가 등록된 모든 observer들에게 직접적으로 변화를 통보한다.



