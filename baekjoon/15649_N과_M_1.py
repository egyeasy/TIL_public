import sys
sys.stdin = open('15649.txt', 'r')

from itertools import permutations

N, M = map(int, input().split())
nums = list(range(1, N + 1))
perms = permutations(nums, M)

for perm in perms:
    for num in perm:
        print(num, end=" ")
    print()
