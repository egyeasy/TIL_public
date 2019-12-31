# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        total_sum = 0
        position = 1
        while l1:
            total_sum += position * l1.val
            print(position, l1.val)
            l1 = l1.next
            position *= 10
        position = 1
        print()
        while l2:
            total_sum += position * l2.val
            print(position, l2.val)
            l2 = l2.next
            position *= 10
        print(total_sum)
        result = ListNode(total_sum % 10)
        current_node = result
        
        while total_sum // 10:
            total_sum //= 10
            current_node.next = ListNode(total_sum % 10)
            current_node = current_node.next
            
        return result