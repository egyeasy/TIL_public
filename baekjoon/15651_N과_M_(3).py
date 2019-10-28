import sys
sys.stdin = open('15651.txt', 'r')

from itertools import product

N, M = map(int, input().split())

pros = product(range(1, N + 1), repeat=M)

for pro in pros:
    for num in pro:
        print(num, end=" ")
    print()