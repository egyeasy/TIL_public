from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (4 * len(nums))
        
        for key, value in enumerate(self.nums):
            self.update(1, 0, len(self.nums) - 1, key, value)

        # print(nums)
        # print(self.tree)
            

    def update(self, node: int, start: int, end: int, index: int, diff: int) -> None:
        if index < start or end < index:
            return
        self.tree[node] += diff
        if start == end:
            return
        mid = (start + end) // 2
        self.update(node * 2, start, mid, index, diff)
        self.update(node * 2 + 1, mid + 1, end, index, diff)
        

    def sumRange(self, i: int, j: int) -> int:
        summ = self.sum_(1, 0, len(self.nums) - 1, i, j)
        return summ
    
    def sum_(self, node: int, start: int, end: int, range_left: int, range_right: int) -> int:
        if range_right < start or end < range_left:
            return 0
        if range_left <= start and end <= range_right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.sum_(node * 2, start, mid, range_left, range_right) + self.sum_(node * 2 + 1, mid + 1, end, range_left, range_right)


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
#param_1 = obj.sumRange(i,j)