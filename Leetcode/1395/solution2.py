from typing import List

count = 0

def search(nums, N, idx, level, is_up):
    global count
    if level == 3:
        count += 1
        return
    level += 1
    possible_max = N - (3 - level)
    for next_idx in range(idx + 1, possible_max):
        if is_up and nums[idx] < nums[next_idx]:
            search(nums, N, next_idx, level, is_up)
        elif not is_up and nums[idx] > nums[next_idx]:
            search(nums, N, next_idx, level, is_up)
            

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        global count
        count = 0
        N = len(rating)
        
        if N < 3:
            return count
        
        for i in range(N - 2):
            search(rating, N, i, 1, True)
            search(rating, N, i, 1, False)
        
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.numTeams([2,5,3,4,1]))
    print(sol.numTeams([2,1,3]))
    print(sol.numTeams([1,2,3,4]))