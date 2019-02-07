# -*- coding: utf-8 -*- 
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


    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return False

        if self.nodeCount == 1:
            item = self.head.data
            self.head = None
            self.tail = None
            self.nodeCount -= 1
            return item

        if pos == 1:
            item = self.head.data
            self.head = self.head.next
            self.nodeCount -= 1
            return item
        
        else:
            prev = self.getAt(pos - 1)
            pres = prev.next
            if pos == self.nodeCount:
                self.tail = prev
                prev.next = None
            else:
                # pos가 가리키는 위치의 (1 < pos < nodeCount)
                prev = self.getAt(pos - 1)
                # node를 삭제하고
                prev.next = pres.next
                # 그 node의 데이터를 리턴
                
        self.nodeCount -= 1
        
        # 이미 prev.next가 다른 것으로 바뀐 후여서 아래는 제대로 작동하지 않는다!
        # return prev.next.data
        
        return pres.data


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0

if __name__ == "__main__":
    a = Node(67)
    b = Node(34)
    c = Node(54)
    L = LinkedList()
    L.insertAt(1, a)
    L.insertAt(2, b)
    L.insertAt(1, c)
    print(L.head.next.next.data)