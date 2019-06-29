# 16강: 우선순위 큐 (Priority Queues)

큐가 FIFO 방식을 따르지 않고 원소들의 우선순위에 따라 큐에서 빠져나오는 방식



### 우선순위 큐의 구현

1) 서로 다른 두 가지 방식이 가능할 듯:

(1) Enqueue 할 때 우선순위 순서를 유지하도록 -> 유리함

(2) Dequeue 할 때 우선순위 높은 것을 선택 -> dequeue할 때마다 O(n) 소요



2) 서로 다른 두 가지 재료를 이용할 수 있음:

(1) 선형 배열 이용 -> 중간에 끼워넣으면 뒤에 것들 다 밀어야. 공간적으로는 적은 비용.

(2) 연결 리스트 이용  -> 시간적으로 유리(안에 넣는 것이 간단)



# 16강 실습: 우선순위 큐의 enqueue 연산 구현

- 양방향 연결 리스트
- 우선순위에 따라 순서를 정렬하여 enqueue

앞선 강의에서 소개된 양방향 연결 리스트의 추상적 자료구조 구현인 클래스 `DoublyLinkedList` 를 이용하여 우선순위 큐의 추상적 자료구조인 클래스 `PriorityQueue` 의 구현을 완성하세요.

코드의 윗부분은 양방향 연결 리스트를 이용하기 위한 클래스 `Node` 와 `DoublyLinikedList` 의 구현입니다. 그대로 둔 채, 아래에 있는 `class PriorityQueue` 의 메서드들 중 `enqueue()` 메서드의 구현을 위한 빈 칸 채우기만 완성하면 됩니다.



### 내 코드

```python
    def enqueue(self, x):
        newNode = Node(x)
        curr = self.queue.head
        while curr != self.queue.tail.prev and newNode.data < curr.next.data:
            curr = curr.next
        self.queue.insertAfter(curr, newNode)

    def dequeue(self):
        return self.queue.popAt(self.queue.getLength())

    def peek(self):
        return self.queue.getAt(self.queue.getLength()).data
```

- 우선순위가 높은 것을 뒤로 배치하고, pop이나 peek을 할 때 tail쪽에서부터 뺀다는 것을 캐치했어야 했다. 반대로 생각해서 계속 반대로 놓으려다보니 틀리더라.
- 같은 while 문도 더 쉽게 표현하는 법이 있더라. 쉽게 쓰는 방법이 있다면 그걸 쓰도록 하자.(강사님은  tail로 접근하는 것을 추천)



### 다른 코드

```python
def enqueue(self, x):
    newNode = Node(x)
    curr = self.queue.head
    # while x < curr.next.data and curr.next.data != None :   이 경우 런타임에러
    while curr.next.data != None and x < curr.next.data :
        curr = curr.next
    self.queue.insertAfter(curr, newNode)
```



### 강사님 답변

` curr.next.data != None` 을 먼저 판단하면, 만약 이 조건이 참이 되는 경우에는 뒤의 `x < curr.next.data` 는 쳐다보지 않습니다. 반면, 주석으로 처리된 그 위 코드에서처럼 이 식의 순서를 (`and` 의 앞뒤를) 바꾸어 쓰면, 먼저 `x < curr.next.data` 를 계산하는데, 이 때 만약 `curr.next.data == None` 이라면 정수형 데이터인 `x` 의 값과 `None` 의 크기 대소 비교를 시도하기 때문에 TypeError 입니다. 구체적으로 말하면, 아래와 같은 에러 메시지를 받는 경우입니다.

```
TypeError: '<' not supported between instances of 'int' and 'NoneType'
```

 이해가 되죠? 연결 리스트의 노드들을 차례로 방문하면서 새로운 원소를 삽입할 자리를 찾는 과정에서, 다음 노드가 가지는 데이터 (`curr.next.data`) 를 참조할 때, 먼저 `None` 과 비교하느냐 아니면 먼저 값의 대소를 비교하느냐의 코드 차이가 에러 발생 여부에 영향을 미치는 것입니다.