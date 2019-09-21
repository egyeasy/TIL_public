# 14강: 큐 (Queues)

- 자료(data element)를 보관할 수 있는 (선형) 구조

- 단, 넣을 때는 한쪽 끝에서 밀어 넣어야 하고 -> 인큐(enqueue) 연산
- 꺼낼 때에는 반대 쪽에서 뽑아 꺼내야 하는 제약이 있음 -> 디큐(dequeue) 연산

스택 (stack) 과 더불어 매우 빈번하게 이용되는 자료 구조가 큐 (queue) 입니다. 큐 또한 데이터 원소를 한 줄로 늘어세우는 자료 구조, 즉 선형 (linear) 구조라는 점에서는 지금까지 배워온 선형 배열, 연결 리스트, 그리고 스택과 마찬가지입니다만, 스택과는 어떻게 보면 반대인 특성을 가지고 있습니다.

스택에 자료를 넣고 꺼내는 원칙을 기억하나요? 어느 시점에서 스택에 들어 있는 데이터 원소를 꺼내면, 그 이전에 가장 마지막에 넣었던 원소가 꺼내집니다. 이러한 특징을 후입선출 (LIFO; last-in first-out) 이라고 부른다는 것도 제 11 강에서 언급한 바 있습니다.

큐에서는 스택과는 반대로, 어느 시점에서 큐에 들어 있는 데이터 원소를 꺼내면 큐에 들어 있는 원소들 중 가장 먼저 넣었던 것이 꺼내집니다. 따라서 큐를 선입선출 (FIFO; first-in first-out) 이라고도 부릅니다. 실제로, 스택을 일컬어 후입선출이라고 하는 경우보다는 그냥 스택이라고 많이 부르는데, 큐는 파이포 라고도 많이 부릅니다. 이러한 선입선출 구조를 머리 속에 떠올려 보면, 긴 대롱이 있고 한 쪽 끝에서는 내용을 (데이터 원소를) 집어넣고 다른 쪽 끝에서는 꺼내어 쓰는 모양새로 생각할 수 있겠네요.

데이터 원소를 큐에 넣는 동작을 인큐 (enqueue) 연산이라고 부르고, 반대로 큐로부터 데이터 원소를 꺼내는 동작을 디큐 (dequeue) 연산이라고 부릅니다. 이 두 가지 핵심 연산을 포함한 큐의 추상적 자료 구조를, 여느 때와 마찬가지로 Python 코드로 구현해보려 합니다. 스택의 경우에도 그랬지만, 큐의 경우에도 이것을 구현하기 위하여 선형 배열을 이용할 수도 있고 연결 리스트를 이용할 수도 있습니다.

그런데, 선형 배열을 이용한 연결 리스트에서는 디큐 연산이 큐의 길이에 비례하는 만큼의 시간을 소요합니다. 배열에 저장된 데이터 원소들을 하나하나 앞 칸으로 당겨서 위치를 조정해야 하기 때문입니다. 그래서 연산의 시간 복잡도 측면에서는 연결 리스트로 큐를 구현하는 것이 유리합니다. 연습문제에서는 제 10 강에서 배운 (그리고 코드도 마련한) 이중 연결 리스트를 이용하여 큐를 구현하는 실습을 합니다.



### 연산의 정의

- `size()` - 현재 큐에 들어있는 데이터 원소의 수를 구함
- `isEmpty()` - 현재 큐가 비어 있는지를 판단
- `enqueue(x)` - 데이터 원소 x를 큐에 추가
- `dequeue()` - 큐의 맨 앞에 저장된 데이터 원소를 제거(또한, 반환)
- `peek()` - 큐의 맨 앞에 저장된 데이터 원소를 반환(제거하지 않음)



### 배열로 구현한 큐

```python
class ArrayQueue:
    
    def __init__(self):
        self.data = []
        
    def size(self):
        return len(self.data)
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self, item):
        self.data.append(item)
        
    def dequeue(self):
        return self.data.pop(0)
    
    def peek(self):
        return self.data[0]
```



### 배열로 구현한 큐의 연산 복잡도

|   연산    | 복잡도 |
| :-------: | :----: |
|  size()   |  O(1)  |
| isEmpty() |  O(1)  |
| enqueue() |  O(1)  |
| dequeue() |  O(n)  |
|  peek()   |  O(1)  |



### 파이썬 공개 라이브러리의 큐

```python
from pythonds.basic.queue import Queue
Q = Queue()
dir(Q) # peek() 빼고 우리가 언급한 메소드들이 다 있다
```



# 14강 실습: 양방향 연결 리스트로 구현하는 큐

양방향 연결 리스트를 활용하여 큐 (queue) 의 추상적 자료구조 (abstract data structure) 구현을 완성하세요.

정의하고자 하는 큐의 추상적 자료구조는 `class LinkedListQueue` 로 구현됩니다. 이 문제는 해당 클래스의 메서드들의 구현을 빈칸 채우기 형태로 완성하는 것으로 되어 있으며, 이 클래스의 구현은 L120 부터 시작합니다.

그 위에는 (LL1-117) 이 추상적 자료구조를 구현하기 위해서 이용할 `class DoublyLinkedList` 와, 또한 여기서 이용하는 `class Node` 의 구현이 정의되어 있습니다. 이 코드는 이전의 양방향 연결 리스트 강의에서 다루어진 것과 완전히 동일합니다.

정확성 테스트는 `class LinkedListQueue` 의 각 메서드가 올바르게 구현되어 있는지를 검사합니다. 코드 실행 을 눌렀을 때 예시 테스트 케이스를 통과하는 것은 아무런 의미가 없습니다.

```python
class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.size()+1, node)


    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data
```

=> 배열로 구현할 때와는 다르게 linked list에서는 클래스가 사용된다. 따라서 큐의 메서드를 만들 때 반환하는 것인지 노드(클래스)인지 데이터인지 잘 따져볼 필요가 있다. linked list를 구현하는 단에서는 노드를 반환해도 되지만, 최종 구현물인 큐 클래스 단에서는 메서드들이 데이터만을 반환해야 한다.(배열에서는 노드를 사용하지 않고 데이터를 반환하기 때문이기도 하다)