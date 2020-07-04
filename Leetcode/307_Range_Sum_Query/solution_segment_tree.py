from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (4 * len(nums))
        #self.tree_init(0, len(nums) - 1, 1)
        #print(self.tree)
        for key, value in enumerate(nums):
            self.update_(0, len(nums) - 1, 1, key, value)

        
    # def tree_init(self, start: int, end: int, node: int) -> int:
    #     if start == end:
    #         #print(node, start, end)
    #         self.tree[node] = self.nums[start]
    #         return self.tree[node]
    #     mid = (start + end) // 2
    #     self.tree[node] = self.tree_init(start, mid, node * 2) + self.tree_init(mid + 1, end, node * 2 + 1)
    #     return self.tree[node]
    
    def update_(self, start: int, end: int, node: int, index: int, dif: int) -> None:
        if index < start or index > end:
            return
        self.tree[node] += dif
        if start == end:
            return
        mid = (start + end) // 2
        self.update_(start, mid, node * 2, index, dif)
        self.update_(mid + 1, end, node * 2 + 1, index, dif)

    def update(self, i: int, val: int) -> None:
        dif = val - self.nums[i]
        nums[i] = val
        self.update_(0, len(self.nums) - 1, 1, i, dif)
        print("update: ", i, val, self.nums, self.tree)

    def sum_(self, start: int, end: int, node: int, left: int, right: int) -> int:
        if end < left or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.sum_(start, mid, node * 2, left, right) + self.sum_(mid + 1, end, node * 2 + 1, left, right)

    def sumRange(self, i: int, j: int) -> int:
        return self.sum_(0, len(self.nums) - 1, 1, i, j)
        

# Your NumArray object will be instantiated and called as such:
nums = [7, 2, 7, 2, 0]
obj = NumArray(nums)
obj.update(4, 6)
obj.update(0, 2)
obj.update(0, 9)
print(obj.sumRange(4, 4))
obj.update(3, 8)
print(obj.sumRange(0, 4))