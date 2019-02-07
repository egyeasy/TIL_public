# 18강: 이진 트리(Binary Trees)

재귀적 방법으로 구현하면 쉬움



### 이진 트리의 순회 (Traversal)

1. 깊이 우선 순회(depth first traversal)

   1) 중위 순회(in-order traversal)
   left subtree -> 자기 자신 -> right subtree

   2) 전위 순회(pre-order traversal)

   자기 자신 -> left subtree -> right subtree
   

   3) 후위 순회(post-order traversal)

   left subtree -> right subtree -> 자기 자신

   

2. 넓이 우선 순회(breadth first traversal)



# 18-01 이진 트리의 depth() 연산 구현

```python
class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


    def depth(self):
        l = self.left.depth() if self.left else 0
        r = self.right.depth() if self.right else 0
        return max(l, r) + 1


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0


    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0


def solution(x):
    return 0
```



### 18-02, 03 이진트리의 순회 연산 구현

```python
class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal


    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.preorder()
        if self.right:
            traversal += self.right.preorder()
        return traversal
    
    
    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.postorder()
        if self.right:
            traversal += self.right.postorder()
        traversal.append(self.data)
        return traversal


class BinaryTree:

    def __init__(self, r):
        self.root = r


    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []


    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []
        
        
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []


def solution(x):
    return 0
```





