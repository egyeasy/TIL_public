from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        N = len(nums)
        self.nums = nums
        self.k = k
        self.nums.sort(reverse=True)

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]
