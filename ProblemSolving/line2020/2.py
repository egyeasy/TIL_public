import sys
sys.stdin = open('2.txt', 'r')

from itertools import permutations

nums = list(map(int, input().split()))
target = int(input())

nums.sort()

curr = 1
perms = permutations(nums)
for perm in perms:
    if curr == target:
        print(''.join(map(str, perm)))
        break
    curr += 1