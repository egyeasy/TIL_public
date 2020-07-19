# time limit exceeded
from typing import List

class Node:
    def __init__(self, num=None):
        self.num = num
        self.prev = None
        self.next = None


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.N = len(nums)
        self.k = k
        self.k_node = None
        self.head = None
        self.tail = Node()
        self.no_k_node = False
        if nums:
            nums.sort(reverse=True)
            node = Node(nums[0])
            self.head = node
            prev_node = self.head
            for i in range(1, self.N):
                node = Node(nums[i])
                prev_node.next = node
                node.prev = prev_node
                prev_node = node
            prev_node.next = self.tail
            self.tail.prev = prev_node

            self.k_node = self.head
            for i in range(k - 1):
                self.k_node = self.k_node.next

    def add(self, val: int) -> int:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.tail
            self.tail.prev = new_node
            self.k_node = self.head
            for i in range(self.k - 1):
                self.k_node = self.k_node.next
        else:
            if val >= self.head.num:
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
            else:
                curr_node = self.head
                while curr_node.next != self.tail and curr_node.next.num > val:
                    curr_node = curr_node.next
                new_node.next = curr_node.next
                new_node.prev = curr_node
                if curr_node.next:
                    curr_node.next.prev = new_node
                curr_node.next = new_node

            if self.k_node == self.tail:
                self.k_node = self.tail.prev
            elif val >= self.k_node.num:
                self.k_node = self.k_node.prev

        return self.k_node.num

    def traverse(self):
        curr_node = self.head
        while curr_node.next:
            print(curr_node.num, end=" ")
            curr_node = curr_node.next
        print(curr_node.num)


if __name__ == "__main__":
    arr = [0]
    kthLargest = KthLargest(2, arr)
    print(kthLargest.add(-1))
    kthLargest.traverse()
    print()
    print(kthLargest.add(1))
    kthLargest.traverse()
    print()
    print(kthLargest.add(-2))
    kthLargest.traverse()
    print()
    print(kthLargest.add(-4))
    kthLargest.traverse()
    print()
    print(kthLargest.add(3))
    kthLargest.traverse()
    arr = [4, 5, 8, 2]
    kthLargest = KthLargest(3, arr)
    print(kthLargest.add(3))
    print(kthLargest.traverse())
    print()
    print(kthLargest.add(5))
    print(kthLargest.traverse())
    print()
    print(kthLargest.add(10))
    print(kthLargest.traverse())
    print()
    print(kthLargest.add(9))
    print(kthLargest.traverse())
    print()
    print(kthLargest.add(4))
    print(kthLargest.traverse())
