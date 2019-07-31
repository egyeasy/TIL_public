import sys
sys.stdin = open('2231.txt', 'r')

N = int(input())

min_M = 0

for M in range(1, N):
    this_sum = M
    calcul_M = M
    while calcul_M:
        this_sum += calcul_M % 10
        calcul_M //= 10
    if this_sum == N:
        min_M = M
        break

print(min_M)