# 8강: 연결 리스트(Linked List) (2)

### 연결 리스트 원소 삽입의 복잡도

- 맨앞에 삽입하는 경우: O(1)
- 중간에 삽입하는 경우: O(n)
- 맨 끝에 삽입한느 경우: O(1) -> tail이 존재하기 때문에 가능한 것!



### 연결 리스트 원소 삭제의 복잡도

- 맨 앞에서 삭제하는 경우: O(1)
- 중간에서 삭제하는 경우: O(n)
- 맨 끝에서 삭제하는 경우: 'O(n)' -> tail만 가지고는 prev를 찾을 수 없으므로 앞에서부터 찾아와야 한다!



연결 리스트의 두 번째 강의입니다. 여기에서는, 연결 리스트의 핵심 연산으로서 아래와 같은 것들이 등장합니다.

- 원소의 삽입 (insertion)
- 원소의 삭제 (deletion)
- 두 리스트 합치기 (concatenation)

앞서 제 7 강에서 언급한 바와 같이, 이러한 연산이 쉽게 (빠르게) 이루어질 수 있다는 점이 연결 리스트가 선형 배열에 비하여 가지는 특장점입니다. 조금 다르게 표현하면, 이런 연산들이 빨라야 하는 응용처에 적용하기 위함이 연결 리스트의 존재 이유입니다.

그런데, 나열된 데이터 원소들의 사이에 새로운 데이터 원소를 삽입하려면, 앞/뒤의 원소들을 연결하고 있는 링크를 끊어 내고, 그 자리에 새로운 원소를 집어넣기 위해서 링크들을 조정해 주어야 하는, 프로그래머로서는 아주 조금 귀찮은 일들이 수반됩니다. 이 강의에서는 그러한 작업들을 Python 코드로 작성하는 연습을 함으로써 자료 구조를 다루는 프로그래밍 기법의 기초를 익힙니다. 이 기법들은 이후에 조금씩 더 복잡해지는 자료 구조를 프로그램으로 구현하는 데 바탕이 될 것입니다. 늘 그렇듯, 프로그래밍에서 어려운 점은 특이한 경우들에 대해서도 고려해야 한다는 점인데요, 원소의 삽입에 있어서는 맨 앞 또는 맨 뒤에 새로운 원소를 삽입하는 경우가 조금 생각할 꺼리가 되는 일입니다.

마찬가지로, 원소의 삭제에 있어서도 맨 앞 또는 맨 뒤의 원소를 삭제하는 경우가 조금 신경써서 처리할 일들이 생기는 경우들입니다. 이 내용은 동영상 강의에서 자세히 설명하고, 연습문제를 통한 코딩 실습으로 구현 능력을 키우도록 합니다.

마지막으로, 두 리스트를 합치는 일은 생각보다 훨씬 쉽습니다. 눈치가 빠른 분들은 이것이 매우 간단하리라는 것을 (제 7 강을 공부하셨다면) 쉽게 알아차리셨을 것 같네요.

연결 리스트를 다루는 프로그래밍 연습을 해보면서, 두 가지를 염두에 두시기를 바랍니다. 첫째, 이것이 무엇을 위함이냐? 즉, 연결 리스트라는 자료 구조를 착안함으로써 어떤 목적을 이루고자 했는지, 다시 말하면 연결 리스트가 가지는 장점이 어떤 곳에서 발휘되는지, 알고리즘의 복잡도 (제 6 강을 참고하세요) 측면에서 생각해보시기 바랍니다. 둘째, 링크를 조정하는 등의 코딩은 앞으로 나타나게 될 트리 (tree) 라든지, 이 강의 시리즈에서 다루지는 않지만 그래프 (graph) 등을 프로그래밍할 때를 대비한 연습이 된다는 점을 떠올리시고, 이런 종류의 코딩에 익숙해지려 노력해 보시기 바랍니다.



### 예제 소스코드

```python
class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def getLength(self):
        return self.nodeCount


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
```

