# 10강: 양방향 연결 리스트 (Doubly Linked Lists)

연결 리스트에 관한 마지막 강의입니다. 지금까지의 연결 리스트에서는 링크가 한 방향으로, 즉 앞에서 뒤로, 다시 말하면 먼저 오는 데이터 원소를 담은 노드로부터 그 뒤에 오는 데이터 원소를 담은 노드를 향하는 방향으로만 연결되어 있었습니다. 여기에서는 새로운 (조금 다른?) 연결 리스트로서 양방향 연결 리스트 (doubly linked list) 를 소개합니다.

말 그대로, 양방향 연결 리스트에서는 노드들이 앞/뒤로 연결되어 있습니다. 즉, 인접한 두 개의 노드들은 앞의 노드로부터 뒤의 노드가 연결되어 있을뿐만 아니라, 뒤의 노드로부터 앞의 노드도 연결되어 있습니다. 한 노드의 입장에서 보자면, 자신보다 앞에 오는 노드를 연결하는 링크와 자신보다 뒤에 오는 노드를 연결하는 링크를 둘 다 가집니다. 따라서 모든 연결은 양방향으로 이루어져 있으며, 그러한 이유로 이런 구조의 연결 리스트를 양방향 연결 리스트 라고 부릅니다.

양방향 연결 리스트는 단방향 연결 리스트에 비해서 어떤 단점을 가지나요? 당연히, 링크를 나타내기 위한 메모리 사용량이 늘어납니다. 또한, 원소를 삽입/삭제하는 연산에 있어서 앞/뒤의 링크를 모두 조정해 주어야 하기 때문에 프로그래머가 조금 더 귀찮아집니다. 그럼에도 불구하고 왜 양방향 연결 리스트를 이용할까요? 당연히, 장점들이 있기 때문이겠죠?

양방향 연결 리스트가 단방향 연결 리스트에 비해서 가지는 장점은, 데이터 원소들을 차례로 방문할 때, 앞에서부터 뒤로도 할 수 있지만 뒤에서부터 앞으로도 할 수 있다는 점입니다. 너무 당연한가요? 하지만, 실제로 (제 7 강에서 언급한 바와 같이) 컴퓨터 시스템의 주요 구성 요소의 하나인 운영체제 (operating system) 등에서는 리스트를 대상으로 앞/뒤로 왔다 갔다 하면서 작업을 행하는 일들이 빈번히 요구되고, 따라서 양방향 연결 리스트가 많이 이용되고 있습니다.

제 9 강에서 했던 것과 마찬가지로, 동일한 모습의 연산을 일관되게 적용하기 위해서는 양방향 연결 리스트의 맨 앞과 맨 뒤에 더미 노드 (dummy node) 를 하나씩 추가할 수 있습니다. 링크를 앞/뒤로 두고, 더미 노드도 맨 앞과 맨 뒤에 두고, 점점 리스트의 모습이 복잡해져 가는 것처럼 느껴지나요? 그러나, (실습을 통해서 느끼게 될 것입니다만) 이렇게 함으로써 오히려 리스트를 대상으로 하는 연산들이 깔끔하게 구현될 수 있다는 장점 - 다시 말하면, 작성해야 하는 코드의 양이 조금 늘어나더라도 코딩은 좀 더 쉬워진다는 - 이 생깁니다. 특별한 경우로 처리해야 하는 것들이 없어지기 (줄어들기) 때문입니다. 이번에는, 아래와 같은 연산들을 모두 연습문제로 풀어보면서 양방향 연결 리스트가 매우 유연한 자료 구조라는 느낌을 받아보시기 바랍니다.

- 리스트 순회 (traversal)
- 원소 삽입 (insertion)
- 원소 삭제 (deletion)
- 리스트 병합 (concatenation)



### 양방향 연결 리스트

- 리스트 처음과 끝에 dummy node를 두자! -> 데이터를 담고 있는 node들은 모두 같은 모양
- insert 코드를 짤 때 self.head와 self.tail을 조정하는 일을 하지 않아도 됨!
- getAt()을 가운데서부터 찾아가는 방식으로 수정 -> 선형시간 O(n) 그대로지만 1/2이 됨!
- pop method에서 맨 마지막의 원소를 제거할 때 바로 앞 원소를 찾아가기 위해 처음부터 와야했으나 앞방향으로의 연결이 가능해지면서 시간이 줄어들게 됨
- 메모리 차지하는 용량이 많아지지만 코딩이 편해진다.



### 원소의 삽입

```python
def insertAfter(self, prev, newNode):
    next = prev.next
    newNode.prev = prev
    newNode.next = next
    prev.next = newNode
    next.prev = newNode
    self.nodeCount += 1
    return True
```



### 소스 코드

```python
class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)
    
```





# 10-1강: 양방향 연결 리스트 역방향 순회

제 10 강에서 소개된 추상적 자료구조 `DoublyLinkedList` 에 대하여, 또한 강의 내용에서 언급한 `reverse()` 메서드를 구현하세요.

이 `reverse()` 메서드는 양방향 연결 리스트를 끝에서부터 시작해서 맨 앞에 도달할 때까지 (tail 방향에서 head 방향으로) 순회하면서, 방문하게 되는 node 에 들어 있는 data item 을 순회 순서에 따라 리스트에 담아 리턴합니다.

예를 들어, `DoublyLinkedList` L 에 들어 있는 노드들이 `43 -> 85 -> 62` 라면, 올바른 리턴 값은 `[62, 85, 43]` 입니다.

이 규칙을 적용하면, 빈 연결 리스트에 대한 역방향 순회 결과로 `reverse()` 메서드라 리턴해야 할 올바른 결과는 `[]` 입니다.

```python
    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        
        return result
```



# 10-2강: 양방향 연결 리스트 노드 삽입

제 10 강에서 소개된 추상적 자료구조 `DoublyLinkedList` 의 메서드로 `insertBefore()` 를 구현하세요.

이 `insertBefore()` 메서드에는 두 개의 인자가 주어지는데, `next` 는 어느 node 의 앞에 새로운 node 를 삽입할지를 지정하고, `newNode` 는 삽입할 새로운 node 입니다.

강의 내용에서 소개된 `insertAfter()` 메서드의 구현과 매우 유사하게 할 수 있습니다.

```python
    def insertBefore(self, next, newNode):
        prev = next.prev
        prev.next = newNode
        next.prev = newNode
        newNode.prev = prev
        newNode.next = next
        self.nodeCount += 1

        return True
```



# 10-3강: 양방향 연결 리스트 노드 삭제

제 10 강에서 소개된 추상적 자료구조 `DoublyLinkedList` 에 대하여 node 의 삭제 연산에 관련한 아래와 같은 메서드들을 구현하세요.

```
popAfter()
popBefore()
popAt()
```

`popAfter(prev)` 는 인자 `prev` 에 의하여 주어진 node 의 다음에 있던 node 를 삭제하고, `popBefore(next)` 는 인자 `next` 에 의하여 주어진 node 의 이전에 있던 node 를 삭제합니다. 그리고 삭제되는 node 에 담겨 있던 data item 을 리턴합니다.

`popAt(pos)` 는 인자 `pos` 에 의하여 지정되는 node 를 삭제하고 그 node 에 담겨 있던 data item 을 리턴하는데, 위 `popAfter()` 또는 `popBefore()` 를 호출하여 이용하는 방식으로 구현하세요. 또한, 만약 인자 `pos` 가 올바른 범위 내에 있지 않은 경우에는 `raise IndexError` 를 이용하여 `IndexError` exception 을 일으키도록 구현하세요.

테스트 케이스 1-3 은 각각 (1) `popAfter()`, (2) `popBefore()`, (3) `popAt()` 메서드의 올바른 동작을 검증하는 케이스입니다.

```python
    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        item = curr.data
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return item


    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        item = curr.data
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return item


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
            return False

        prev = self.getAt(pos - 1)
        return self.popAfter(prev)
```



# 10-4강: 양방향 연결 리스트의 병합

제 10 강에서 소개된 추상적 자료구조 `DoublyLinkedList` 에 대하여 두 개의 양방향 연결 리스트를 앞뒤로 이어 붙이는 메서드 `concat()` 을 구현하세요.

예를 들어, 양방향 연결 리스트 L1 에는 `1 -> 2 -> 3` 의 원소가 순서대로 들어 있고, 또다른 양방향 연결 리스트 L2 에는 `4 -> 5` 의 순서로 원소가 들어 있을 때, 메서드 호출 `L1.concat(L2)` 의 결과로 L1 은 `1 -> 2 -> 3 -> 4 -> 5` 의 양방향 연결 리스트가 됩니다. 물론, L1 또는 L2 또는 둘 다가 비어 있는 양방향 연결 리스트인 경우도 고려되도록 코드를 작성해야 합니다.



```python
    def concat(self, L):
        origin_end = self.tail.prev
        origin_end.next = L.head.next
        other_first = L.head.next
        other_first.prev = self.tail.prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount
        return True
```

