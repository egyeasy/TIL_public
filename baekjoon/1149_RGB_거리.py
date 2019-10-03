# 동적계획법에 해당하는 문제 - 내가 DFS라고 생각하고 있었음

import sys
sys.stdin = open('1149.txt', 'r')

def DFS(idx, color, t_cost):
    global min_cost
    if idx == N:
        if t_cost < min_cost:
            min_cost = t_cost
        return
    for i in range(3):
        if i != color:
            current_cost = t_cost + costs[idx][i]
            if not visited[idx]:
                DFS(idx + 1, i, t_cost + costs[idx][i])
            elif i in visited[idx] and current_cost < min_cost:
                DFS(idx + 1, i, t_cost + costs[idx][i])


N = int(input())
costs = []
for i in range(N):
    cost = tuple(map(int, sys.stdin.readline().split()))
    costs.append(cost)

total_cost = 0
min_cost = 1000 * 1000
visited = [[] for _ in range(N + 1)]

for i in range(3):
    DFS(0, i, total_cost)

print(min_cost)