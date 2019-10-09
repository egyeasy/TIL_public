import sys
sys.stdin = open('15650.txt', 'r')

from itertools import combinations

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]

combs = combinations(nums, M)

for comb in combs:
    for num in comb:
        print(num, end=" ")
    print()