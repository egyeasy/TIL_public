import sys
sys.stdin = open('2798.txt', 'r')

from itertools import combinations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

combs = combinations(nums, 3)
max_sum = -1

for comb in combs:
    comb_sum = sum(comb)
    if comb_sum <= M and comb_sum > max_sum:
        max_sum = comb_sum
    if comb_sum == M:
        break

print(max_sum)