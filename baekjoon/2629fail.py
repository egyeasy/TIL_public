import sys
from collections import deque
sys.stdin = open('2629.txt', 'r')

def bfs(s):
    dq.append(s)
    while dq:
        s = dq.popleft()
        if not visited[s]:
            visited[s] = 1
            used[s] = 1, 1, 1
            for i in range(chu_N):
                for j in range(3):
                    if not used[i][j]:
                        dq.append([i, j])



chu_N = int(input())
chu_list = list(map(int, input().split()))
goo_M = int(input())
goo_list = list(map(int, input().split()))

for goo in goo_list:
    for chu_idx in range(chu_N):
        dq = deque()
        used = [[0] * 3 for _ in range(chu_N)]
        visited = [0] * chu_N
        bfs(chu_idx)