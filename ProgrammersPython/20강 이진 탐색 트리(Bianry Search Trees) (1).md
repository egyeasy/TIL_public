# 20강: 이진 탐색 트리(Bianry Search Trees) (1)

모든 노드에 대해서,

- 왼쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 작고
- 오른쪽 서브트리에 있는 데이터는 모두 현재 노드의 값보다 큰

성질을 만족하는 이진 트리

(중복되는 데이터 원소는 없는 것으로 가정)

- 이진 탐색과 유사한 과정



### (정렬된) 배열을 이용한 이진 탐색과 비교

(장점) 데이터 원소의 추가, 삭제가 용이(이진 탐색은 정렬된 배열 이용)

(단점) 공간 소요가 큼 -> 기록에 필요한 공간 소요

**항상 O(log n)의 탐색 복잡도? 항상 그렇지는 않다**



### 이진 탐색 트리의 추상적 자료구조

- 데이터 표현 - 각 노드는 (key, value)의 쌍으로
- 키를 이용해서 검색 가능
- 보다 복잡한 데이터 레코드로 확장 가능



### 이진 탐색 트리의 추상적 자료구조

연산의 정의

- insert(key, data) - 트리에 주어진 데이터 원소를 추가
- remove(key) - 특정 원소를 트리로부터 삭제(좀 복잡함)
- lookup(key) - 특정 원소를 검색(가장 중요한 기능 중 하나)
- inorder() - 키의 순서대로 데이터 원소를 나열
- min(), max() - 최소 키, 최대 키를 가지는 원소를 각각 탐색



# 20강 실습: 이진 탐색 트리의 원소 삽입 연산 구현

 ```python
class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key == self.key:
            raise KeyError
        else:
            if key < self.key:
                if not self.left:
                    self.left = Node(key, data)
                else:
                    self.left.insert(key, data)
            elif key > self.key:
                if not self.right:
                    self.right = Node(key, data)
                else:
                    self.right.insert(key, data)


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0
 ```



