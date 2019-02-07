# 19강: 이진 트리 - 넓이 우선 순회(BFT; Breadth First Traversal)

### 원칙

- 수준(level)이 낮은 노드를 우선으로 방문
- 같은 수준의 노드들 사이에는,
  부모 노드의 방문 순서에 따라 방문
  왼쪽 자식 노드를 오른쪽 자식보다 먼저 방문
- 재귀적(recursive) 방법이 적합한가? NO!



### 넓이 우선 순회 (Breath First Traversal)

- 한 노드를 방문했을 때, 나중에 방문할 노드들을 순서대로 기록해 두어야
  -> **큐(queue)**를 이용하면 어떨까!
- 큐 안이 비어있으면 방문이 다 끝난 것



### 넓이 우선 순회 알고리즘 구현

1. (초기화) traversal <- 빈 리스트, q <- 빈 큐
2. 빈 트리가 아니면, root node를 q에 추가(enqueue)
3. q가 비어 있지 않은 동안
   3.1. node <- q에서 원소를 추출(dequeue)
   3.2. node를 방문
   3.3. node의 왼쪽, 오른쪽 자식(이 있으면)들을 q에 추가
4. q가 빈 큐가 되면 모든 노드 방문 완료





# 19강 실습: 이진 트리의 넓이 우선 순회

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


class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def bft(self):
        traversal = []
        q = ArrayQueue()
        if self.root:
            q.enqueue(self.root)
            while not q.isEmpty():
                upper = q.dequeue()
                traversal.append(upper.data)
                if upper.left:
                    q.enqueue(upper.left)
                if upper.right:
                    q.enqueue(upper.right)
        return traversal


def solution(x):
    return 0
```

