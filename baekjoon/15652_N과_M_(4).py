import sys
sys.stdin = open('15652.txt', 'r')

from itertools import combinations_with_replacement as comb_r

N, M = map(int, input().split())

combs = comb_r(range(1, N + 1), M)

for comb in combs:
    for num in comb:
        print(num, end=" ")
    print()

