# 9강: 연결 리스트 (Linked Lists) (3)

연결 리스트의 세 번재 강의입니다. 여기에서는, 진짜로 연결 리스트가 힘을 발휘하는 경우에 대해서 진지하게 생각해보기로 합니다. 리스트를 따라서 하나 하나 원소들을 대상으로 어떤 작업을 하다가, 그 위치에 새로운 데이터 원소를 삽입하거나, 아니면 그 위치에 있는 데이터 원소를 삭제하는 경우입니다. 앞의 강의 (제 8 강) 에서는 설명을 명확히 하고 프로그래밍 연습을 쉽게 하기 위해서 특정 번째 를 지정하여 원소를 삽입/삭제하는 연산을 정의하고 코딩으로 구현해보았는데요, 여기에서는 특정 원소의 바로 다음 을 지정하여 원소를 삽입/삭제하는 연산을 정의하고 구현해봅니다.

그러자면, 맨 앞에 원소를 추가 (삽입) 하거나 맨 앞의 원소를 제거 (삭제) 하는 연산을 지정하기가 좀 애매해지는군요. 이런 경우에도 동일한 방법을 적용하기 위해서, 이번에는 연결 리스트의 맨 앞에다가 데이터 원소를 담고 있지 않은, 그냥 자리만 차지하는 노드 (node - 이제는 이런 용어에는 익숙하지요?) 를 추가한, 조금 모습이 달라진 연결 리스트를 정의합니다.

이렇게 맨 앞에 추가된, 데이터 원소를 담고 있지 않은 노드를 더미 노드 (dummy node) 라고 부릅니다. 더미 노드를 가지는 연결 리스트를 대상으로, 지금까지 우리가 정의한 아래와 같은 연산들을 구현해봅니다.

- 길이 얻어내기
- 리스트 순회 (traversal)
- 특정 원소 참조 (k 번째)
- 원소 삽입 (insertion)
- 원소 삭제 (deletion)
- 두 리스트 합치기 (concatenation)

동영상 강의와 연습문제를 통해서 명백해지겠지만, 앞의 두 강의 (제 7 강과 제 8 강) 내용을 잘 이해하고 있다면, 이런 식으로 연결 리스트의 구조를 조금 확장하는 것은 코드를 아주 조금 수정함으로써 쉽게 할 수 있음을 발견하게 됩니다. 이번에도 역시, 원소의 삭제는 동영상 강의의 설명을 충분히 숙지하신 뒤에 연습문제로 풀어보세요.



### 연결 리스트가 힘을 발휘할 때

삽입과 삭제가 유연하다는 것이 가장 큰 장점

but 지난번에 만든 코드는 매번 처음부터 원하는 지점까지 찾아갔다(O(n))



### 조금 변형된 연결 리스트

맨 앞에 dummy node를 추가한 형태로



### 리스트 순회

```python
def traverse(self):
    result = []
    curr = self.head
    #아래가 지난 번과 조금 다르다
    while curr.next:
        curr = curr.next
        result.append(curr.data)
    return result
```



### k번째 원소 얻어내기

```python
def getAt(self, pos):
    if pos < 0 or pos > self.nodeCount:
        return None
    i = 0 #head가 있으므로 0에서부터 시작
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1
    return curr
```



### 원소의 삽입

head node를 삽입함으로써 코드가 더 간단해졌다.

```python
def insertAfter(self, prev, newNode):
    newNode.next = prev.next
    if prev.next is None:
        self.tail = newNode
    prev.next = newNode
    self.nodeCount += 1
    return True
```



### 메서드 insertAt()의 구현

```python
def insertAt(self, pos, newNode):
    if pos < 1 or pos > self.nodeCount + 1:
        return False
    
    if pos != 1 and pos == self.nodeCount + 1:
        prev = self.tail
    
    else:
        prev = self.getAt(pos - 1)
        
    return self.insertAfter(prev, newNode)
```



### 두 리스트의 연결

```python
def concat(self, L):
    self.tail.next = L.head.next
    if L.tail:
        self.tail = L.tail
    self.nodeount += L.nodeCount
```



# 9강 실습: dummy head를 가지는 연결 리스트 노드 삭제

제 9 강에서 소개된 추상적 자료구조 `LinkedList` 는 dummy head node 를 가지는 연결 리스트입니다. 이 클래스의 아래와 같은 메서드들을, 강의 내용에 소개된 요구조건을 만족시키도록 구현하세요.



```
popAfter()
popAt()
```



이 때, `popAt()` 메서드의 구현에서는 `popAfter()` 를 호출하여 이용하도록 합니다. (그렇게 하지 않을 수도 있지만, 여기에서는 `popAfter()` 의 이용에 의해서 코드 구현이 보다 쉬워지는 것을 확인하기 위함입니다.)

초기 코드로 들어 있는 것은 `solution()` 함수를 포함하여 다른 부분은 수정하지 말고, `def popAfter(self, prev):` 와 `def popAt(self, pos):` 의 메서드 몸체만 구현하세요.

만약, `popAt()` 메서드에 인자로 주어진 `pos` 가 올바른 범위의 값을 가지지 않는 경우에는 `IndexError`exception 을 발생시키도록 합니다. 이렇게 하기 위한 코드는 `raise IndexError` 입니다.



```python
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    
    ######## 여기 직접 작성 ############
    def popAfter(self, prev):
        curr = prev.next
        item = curr.data
        if self.nodeCount != 1 and curr.next == None:
            self.tail = prev
            prev.next = None
        else:
            prev.next = curr.next
            
        self.nodeCount -= 1
        return item


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
            return False
        else:
            prev = self.getAt(pos - 1)
        return self.popAfter(prev)
	################################

def solution(x):
    return 0
```



### 8강의 연결 리스트와 비교한 특징

1. pos의 위치를 찾아주는 popAt, 그리고 경우의 수에 따라 제거 및 처리, 출력 행위를 처리해주는 popAfter로 기능을 나눠서 짜는 것이 어려웠다.
2. self.head가 연결 리스트 외부에 있는 느낌이라 경우의 수를 따질 때 크게 고려하지 않아도 된다는 점이 편리했다.