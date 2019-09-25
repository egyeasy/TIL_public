# in statement로 확인. PyPy3만 통과.

import sys
sys.stdin = open('1920.txt', 'r')

N = int(input())
N_nums = list(map(int, input().split()))

M = int(input())
M_nums = list(map(int, input().split()))

for m in M_nums:
    if m in N_nums:
        print(1)
    else:
        print(0)