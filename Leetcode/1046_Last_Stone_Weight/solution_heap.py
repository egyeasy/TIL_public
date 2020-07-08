from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-num for num in stones]
        heapq.heapify(arr)
        while len(arr) > 1:
            print(arr)
            heapq.heappush(arr, heapq.heappop(arr) - heapq.heappop(arr))
        
        return -arr[0] if arr else 0


if __name__ == "__main__":
    #nums = [2,7,4,1,8,1]
    nums = [3, 7, 8]
    sol = Solution()
    print(sol.lastStoneWeight(nums))