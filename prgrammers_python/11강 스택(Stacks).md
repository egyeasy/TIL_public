# 11강: 스택 (Stacks)

마치 접시를 차곡차곡 쌓았다가 맨 위의 접시부터 다시 꺼내어 사용하는 것처럼, 추가된 데이터 원소들을 끄집어내면 마지막에 넣었던 것부터 넣은 순서의 역순으로 꺼내지는 자료 구조를 스택 (stack) 이라고 부릅니다. 이처럼 마지막에 넣은 것이 가장 먼저 꺼내어지는 성질 때문에 스택을 다른 말로는 후입선출 (LIFO; last-in first-out) 자료 구조라고도 합니다.



- 자료(data element)를 보관할 수 있는 (선형) 구조
- 단, 넣을 때에는 한 쪽 끝에서 밀어 넣어야 하고 -> 푸시(push) 연산
- 꺼낼 때에는 같은 쪽에서 뽑아 꺼내야 하는 제약이 있음 -> 팝(pop) 연산



스택에 데이터 원소를 추가하는 (집어넣는) 동작을 푸시 (push) 연산이라고 하고, 마지막에 추가되었던 원소를 참조하고 삭제하는 (꺼내는) 동작을 팝 (pop) 연산이라고 합니다. 스택은 이 두 연산을 제공하는 간단한 자료 구조인데, 여러 가지의 알고리즘을 구현하는 데 있어서 활용도가 높습니다. 예를 들어, 컴퓨터 내부에서 프로그램이 실행할 때 함수 호출이 일어나고 함수들이 리턴하면 마지막 호출된 곳으로 돌아가는 동작을 구현하는 데에도 스택이 이용되고, 이러한 일은 컴퓨터의 동작에 핵심적인 것이기 때문에 컴퓨터 하드웨어 (프로세서) 는 어떤 방식으로든 스택을 내부적으로 관리하는 기능을 갖고 있습니다. 이것을 떠올려보려면, 제 4 강과 제 5 강에서 배웠던 재귀 함수 가 줄줄이 호출되었다가 줄줄이 리턴하는 모습을 생각해보세요.



#### 스택 언더플로우(stack underflow)

: 비어있는 스택에서 데이터 원소를 꺼내려 할 때


#### 스택 오버플로우(stack overflow)

: 꽉 찬 스택에 데이터 원소를 넣으려 할 때



### 연산의 정의

`size()` : 현재 스택에 들어있는 데이터 원소의 수를 구함

`isEmpty()` : 현재 스택이 비어있는지를 판단

`push(x)` : 데이터 원소 x를 스택에 추가

`pop()` : 스택의 맨 위에 저장된 원소를 제거(또한, 반환)

`peek()` : 스택의 맨 위에 저장된 데이터 원소를 반환(제거하지 않음)



컴퓨터 내부에서뿐만 아니라, 응용 프로그램을 작성하는 데에도 스택을 활용하면 잘 풀어낼 수 있는 종류의 문제들이 많이 있습니다. 스택을 이용하는 알고리즘의 예를 다음 (제 12 강) 과 그 다음 (제 13 강) 에서 맞이하게 됩니다.

이 강의에서는, 먼저 스택이 어떻게 동작하는지를 이해하고, 이후에 이용할 수 있도록 스택을 추상적 자료 구조로 구현해봅니다. 스택을 구현하는 데에는 이미 우리가 알고 있는 선형 배열을 이용할 수도 있고, 앞서 몇 차례의 강의에서 다룬 연결 리스트를 이용할 수도 있습니다. 이처럼, 기본적인 자료 구조는 또다른 자료 구조를 만드는 데 재료로 이용되기도 합니다. 두 가지 방식으로 스택을 구현해보는데, 아래와 같은 연산들을 제공하기로 합니다.

- `size()`: 현재 스택에 들어 있는 데이터 원소의 수를 구함
- `isEmpty()`: 현재 스택이 비어 있는지를 판단 (`size() == 0?`)
- `push(x)`: 데이터 원소 `x` 를 스택에 추가
- `pop()`: 스택에 가장 나중에 저장된 데이터 원소를 제거 (또한, 반환)
- `peek()`: 스택에 가장 나중에 저장된 데이터 원소를 참조 (반환), 그러나 제거하지는 않음

연습문제에서는 스택을 이용하는 간단한 알고리즘으로서 수식의 괄호가 올바르게 구성되어 있는지를 판단하는 코드를 작성해봅니다.



### 스택 구현

```python
from doublylinkedlist import Node
from doublylinkedlist import DoublyLinkedList


class ArrayStack:

	def __init__(self):
		self.data = []

	def size(self):
		return len(self.data)

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		self.data.append(item)

	def pop(self):
		return self.data.pop()

	def peek(self):
		return self.data[-1]


class LinkedListStack:

	def __init__(self):
		self.data = DoublyLinkedList()

	def size(self):
		return self.data.getLength()

	def isEmpty(self):
		return self.size() == 0

	def push(self, item):
		node = Node(item)
		self.data.insertAt(self.size() + 1, node)

	def pop(self):
		return self.data.popAt(self.size())

	def peek(self):
		return self.data.getAt(self.size()).data
```



# 11강 실습: 수식의 괄호 검사(스택)

소괄호: ( )
중괄호: { }
대괄호: [ ]
를 포함할 수 있는 수식을 표현한 문자열 `expr` 이 인자로 주어질 때, 이 수식의 괄호가 올바르게 여닫혀 있는지를 판단하는 함수 `solution()` 을 완성하세요. 이 함수는 수식의 괄호가 유효하면 `True` 를, 그렇지 않으면 `False` 를 리턴합니다.

스택을 활용하여 수식 내의 괄호 여닫음의 유효성을 검사하는 알고리즘에 대해서는 동영상 강의 내용을 참고하세요.

```python
def solution(expr):
    match = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    S = ArrayStack()
    for c in expr:
        if c in '({[':
			S.push(c) # 빈칸

        elif c in match:
            if S.isEmpty(): # 빈칸
                return False
            else:
				t = S.pop() # 빈칸
                if t != match[c]: # match[c] 빈칸
                    return False
    return S.isEmpty() # 빈칸
```

=> match dictionary를 만들어서 괄호 짝을 맞춘다는 아이디어가 참신했다. 또한 마지막 return S.isEmpty()를 생각해내는 것이 제일 오래 걸렸는데, 최후의 경우의 수까지 고려하면서도 효율적인 코드라 감탄했다.