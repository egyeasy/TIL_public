# 21강: 이진 탐색 트리 (Binary Search Trees)

### 이진 탐색 트리에서 원소 삭제

1. 키(key)를 이용해서 노드를 찾는다.
   - 해당 키의 노드가 없으면, 삭제할 것도 없음
   - 찾은 노드의 부모 노드도 알고 있어야 함(아래 2번 때문)
2. 찾은 노드를 제거하고도 이진 탐색 트리 성질을 만족하도록 트리의 구조를 정리한다.



### 인터페이스의 설계

입력: 키(key)

출력: 삭제한 경우 True, 노드가 없는 경우 False



### 이진 탐색 트리 구조의 유지

삭제되는 노드가

1. 말단(leaf) 노드인 경우
   그냥 그 노드를 없애면 됨 -> 부모 노드의 링크를 조정(왼쪽이었는지, 오른쪽이었는지 알아내야 함)
2. 자식을 하나 가지고 있는 경우
   삭제되는 노드 자리에 그 자식을 대신 배치 -> 자식이 왼쪽? 오른쪽? / 부모 노드의 링크를 조정(좌/우?)
3. 자식을 둘 가지고 있는 경우
   삭제되는 노드보다 바로 다음 (큰) 키를 가지는 노드를 찾아 그 노드를 삭제되는 노드 자리에 대신 배치하고 이 노드를 대신 삭제



### 말단(Leaf) 노드의 삭제

주의 : 삭제되는 노드가 root node인 경우는? 다른 방식으로 해줘야 할 것



### 자식을 하나 가진 노드의 삭제

삭제되는 노드가 root node인 경우는 어떻게? -> 대신 들어오는 자식이 root가 됨



### 자식이 둘인 노드의 삭제

successor : 바로 다음 큰 키. 오른쪽으로 한번 간 다음 왼쪽이 없을 때까지 찾아가면 될 듯.



### 이진 탐색 트리가 별로 효율적이지 못한 경우

```python
T = BinSearchTree()
T.insert(1, 'John')
T.insert(2, 'Mary')
T.insert(3, 'Anne')
T.insert(4, 'Peter')

T = BinSearchTree()
T.insert(4, 'John')
T.insert(3, 'Mary')
T.insert(2, 'Anne')
T.insert(1, 'Peter')
```

높이의 좌우 균형을 맞추지 못하고 한 쪽으로 치우치게 됨 -> 선형 배열과 다를 바가 없다.



### 보다 나은 성능을 보이는 이진 탐색 트리들

높이의 균형을 유지함으로써 O(logn)의 탐색 복잡도 보장

삽입, 삭제 연산이 보다 복잡

AVL tree - https://ko.wikipedia.org/wiki/AVL_트리

Red-black tree - https://ko.wikipedia.org/wiki/레드-블랙_트리





# 21강 실습: 이진 탐색 트리에서 노드의 삭제 연산 구현

```python
class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        elif key > self.key:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)
        else:
            raise KeyError('Key %s already exists.' % key)


    def lookup(self, key, parent=None):
        if key < self.key:
            if self.left:
                return self.left.lookup(key, self)
            else:
                return None, None
        elif key > self.key:
            if self.right:
                return self.right.lookup(key, self)
            else:
                return None, None
        else:
            return self, parent


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def countChildren(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count


class BinSearchTree:

    def __init__(self):
        self.root = None


    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)


    def lookup(self, key):
        if self.root:
            return self.root.lookup(key)
        else:
            return None, None


    def remove(self, key):
        node, parent = self.lookup(key)
        if node:
            nChildren = node.countChildren()
            # The simplest case of no children
            if nChildren == 0:
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # parent.left 또는 parent.right 를 None 으로 하여
                # leaf node 였던 자식을 트리에서 끊어내어 없앱니다.
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 를 None 으로 하여 빈 트리로 만듭니다.
                else:
                    self.root = None
            # When the node has only one child
            elif nChildren == 1:
                # 하나 있는 자식이 왼쪽인지 오른쪽인지를 판단하여
                # 그 자식을 어떤 변수가 가리키도록 합니다.
                if node.left:
                    child = node.left
                else:
                    child = node.right
                # 만약 parent 가 있으면
                # node 가 왼쪽 자식인지 오른쪽 자식인지 판단하여
                # 위에서 가리킨 자식을 대신 node 의 자리에 넣습니다.
                if parent:
                    if parent.left == node:
                        parent.left = child
                    else:
                        parent.right = child
                # 만약 parent 가 없으면 (node 는 root 인 경우)
                # self.root 에 위에서 가리킨 자식을 대신 넣습니다.
                else:
                    self.root = child
            # When the node has both left and right children
            else:
                parent = node
                successor = node.right
                # parent 는 node 를 가리키고 있고,
                # successor 는 node 의 오른쪽 자식을 가리키고 있으므로
                # successor 로부터 왼쪽 자식의 링크를 반복하여 따라감으로써
                # 순환문이 종료할 때 successor 는 바로 다음 키를 가진 노드를,
                # 그리고 parent 는 그 노드의 부모 노드를 가리키도록 찾아냅니다.
                while successor.left:
                    parent = successor
                    successor = successor.left
                # 삭제하려는 노드인 node 에 successor 의 key 와 data 를 대입합니다.
                node.key = successor.key
                node.data = successor.data
                # 이제, successor 가 parent 의 왼쪽 자식인지 오른쪽 자식인지를 판단하여
                # 그에 따라 parent.left 또는 parent.right 를
                # successor 가 가지고 있던 (없을 수도 있지만) 자식을 가리키도록 합니다.
                if parent.countChildren():
                    if parent.left and parent.left == successor:
                        if successor.right:
                            parent.left = successor.right
                        else:
                            parent.left = None
                    elif parent.right and parent.right == successor:
                        if successor.right:
                            parent.right = successor.right
                        else:
                            parent.right = None

            return True

        else:
            return False


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


def solution(x):
    return 0
```

