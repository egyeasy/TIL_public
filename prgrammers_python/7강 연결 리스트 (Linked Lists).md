# 7강: 연결 리스트 (Linked Lists)

### 추상적 자료구조(Abstract Data Structures)

#### - Data ex) 정수, 문자열, 레코드

#### - A set of operations	ex) 삽입, 삭제, 순회, 정렬, 탐색



### 연결리스트

```python
def getAt(self, pos):
    if pos <= 0 or pos > self.nodeCount:
        return None
    i = 1
    curr = self.head
    while i < pos:
        curr = curr.next
        i += 1
    return curr
```



### 배열과 비교한 연결 리스트

|                | 배열        | 연결 리스트     |
| -------------- | ----------- | --------------- |
| 저장 공간      | 연속한 위치 | 임의의 위치     |
| 특정 원소 지칭 | 매우 간편   | 선형탐색과 유사 |
|                | O(1)        | O(n)            |

데이터 원소들을 순서를 지어 늘어놓는다는 점에서 연결 리스트 (linked list) 는 선형 배열 (linear array) 과 비슷한 면이 있지만, 데이터 원소들을 늘어놓는 방식에서 이 두 가지는 큰 차이가 있습니다. 구체적으로는, 선형 배열이 번호가 붙여진 칸에 원소들을 채워넣는 방식이라고 한다면, 연결 리스트는 각 원소들을 줄줄이 엮어서 관리하는 방식입니다. 그렇다면, 선형 배열에 비해서 연결 리스트가 가지는 이점은 무엇일까요?

연결 리스트에서는 원소들이 링크 (link) 라고 부르는 고리로 연결되어 있으므로, 가운데에서 끊어 하나를 삭제하거나, 아니면 가운데를 끊고 그 자리에 다른 원소를 (원소들을) 삽입하는 것이 선형 배열의 경우보다 쉽습니다. 여기에서 쉽다 라고 표현한 것은, 빠른 시간 내에 처리할 수 있다는 뜻입니다. 이러한 이점 때문에, 원소의 삽입/삭제가 빈번히 일어나는 응용에서는 연결 리스트가 많이 이용됩니다. 컴퓨터 시스템을 구성하는 중요한 요소인 운영체제 (operating system) 의 내부에서도 이러한 연결 리스트가 여러 곳에서 이용되고 있습니다.

그렇다면, 연결 리스트가 선형 배열에 비해서 가지는 단점은 없을까요? 물론 있습니다. 세상에 공짜는 없는 법이어서, 위에서 말한 바와 같이 원소의 삽입과 삭제가 용이하다는 장점은 거저 얻어지지 않습니다. 생각하기 쉬운 하나의 단점은, 선형 배열에 비해서 데이터 구조 표현에 소요되는 저장 공간 (메모리) 소요가 크다는 점입니다. 링크 또한 메모리에 저장되어 있어야 하므로, 연결 리스트를 표현하기 위해서는 동일한 데이터 원소들을 담기 위하여 사용하는 메모리 요구량이 더 큽니다. 그보다 더 우리의 관심을 끄는 단점은, k 번째의 원소 를 찾아가는 데에는 선형 배열의 경우보다 시간이 오래 걸린다는 점입니다. 선형 배열에서는 데이터 원소들이 번호가 붙여진 칸들에 들어 있으므로 그 번호를 이용하여 대번에 특정 번째의 원소를 찾아갈 수 있는 데 비하여, 연결 리스트에서는 단지 원소들이 고리로 연결된 모습을 하고 있으므로 특정 번째의 원소를 접근하려면 앞에서부터 하나씩 링크를 따라가면서 찾아가야 합니다.

이 강의에서는, 몇 종류의 연결 리스트들 중에서 가장 단순한 형태인 단방향 연결 리스트 (singly linked list) 를 추상적 자료 구조로 정의하고, 이 추상적 자료 구조에 가할 수 있는 아래와 같은 연산들을 배웁니다.

- 특정 원소 참조 (k 번째)
- 리스트 순회 (list traversal)
- 길이 얻어내기

다음 강의에서는 위에 나열한 연산들 이외에, 연결 리스트에서 핵심이라고 할 수 있는 원소의 삽입/삭제 등을 포함한 추가의 연산들을 배우게 됩니다. 물론, 이 자료 구조의 표현과 연산의 구현은 Python 예제로 이루어져 있습니다.



# 7강 실습: 연결 리스트 순회 구현하기

``` python
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        i = 1
        idx = self.head
        result = []
        while i <= self.nodeCount:
            result.append(idx.data)
            idx = idx.next
            i += 1
        return result


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0
```

