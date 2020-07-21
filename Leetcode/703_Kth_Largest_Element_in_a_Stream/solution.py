from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        N = len(nums)
        self.heap = []
        self.k = k
        for i in range(N):
            minus_num = -nums[i]
            heapq.heappush(self.heap, minus_num)
            # print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        self.largers = []
        for i in range(self.k - 1):
            self.largers.append(heapq.heappop(self.heap))
        answer = heapq.heappop(self.heap)
        self.largers.append(answer)
        for num in self.largers:
            heapq.heappush(self.heap, num)
        return -answer


if __name__ == "__main__":
    arr = [4, 5, 8, 2]
    kthLargest = KthLargest(3, arr)
    print(kthLargest.heap)
    print(kthLargest.add(3))
    print()
    print(kthLargest.heap)
    print(kthLargest.add(5))
    print()
    print(kthLargest.heap)
    print(kthLargest.add(10))
    print()
    print(kthLargest.heap)
    print(kthLargest.add(9))
    print()
    print(kthLargest.heap)
    print(kthLargest.add(4))
