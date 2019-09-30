# 동적계획법에 해당하는 문제

import sys
sys.stdin = open('1149.txt', 'r')

N = int(input())
costs = []
costs.append([0, 0, 0])

for i in range(N):
    cost = tuple(map(int, sys.stdin.readline().split()))
    costs.append(cost)

total_costs = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    total_costs[i][0] = min(total_costs[i - 1][1], total_costs[i - 1][2]) + costs[i][0]
    total_costs[i][1] = min(total_costs[i - 1][0], total_costs[i - 1][2]) + costs[i][1]
    total_costs[i][2] = min(total_costs[i - 1][0], total_costs[i - 1][1]) + costs[i][2]

print(min(min(total_costs[N][0], total_costs[N][1]), total_costs[N][2]))