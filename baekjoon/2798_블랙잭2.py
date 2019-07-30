# 제대로 구현된 combination이 아님. 중복되는 경우의 수가 있음.
import sys
sys.stdin = open('2798.txt')

def backtrack(curr_nums, k):
    global max_sum
    visited[curr_nums[-1]] = 1
    if k == 3:
        print(curr_nums)
        curr_sum = sum(curr_nums)
        if curr_sum > max_sum:
            max_sum = curr_sum
        return
    for cand_num in nums:
        if not visited[cand_num] and sum(curr_nums) + cand_num <= M:
            # visited[cand_num] = 1
            backtrack(curr_nums + [cand_num], k + 1)
            # visited[cand_num] = 0
            


N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [0] * 100001
max_sum = -1

for num in nums:
    visited[num] = 1
    backtrack([num], 1)

print(max_sum)