from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) >= 2:
            #print(stones)
            first = stones.pop(0)
            second = stones.pop(0)
            diff = first - second
            if diff:
                diff_i = 0
                for i in range(len(stones)):
                    if diff >= stones[i]:
                        diff_i = i
                        break
                if stones and diff < stones[-1]:
                    diff_i = len(stones)
                stones.insert(diff_i, diff)
        return stones[0] if stones else 0


if __name__ == "__main__":
    #nums = [2,7,4,1,8,1]
    nums = [3, 7, 8]
    sol = Solution()
    print(sol.lastStoneWeight(nums))