import sys
sys.stdin = open('2606.txt', 'r')

from collections import deque

def bfs(s):
    global total_cnt
    dq.append(s)
    while dq:
        s = dq.popleft()
        if not visited[s]:
            visited[s] = 1
            total_cnt += 1
        for i in range(1, node_N + 1):
            if mat[s][i] and not visited[i]:
                dq.append(i)

node_N = int(input())
edge_K = int(input())
mat = [[0] * (node_N + 1) for _ in range(node_N + 1)]
for i in range(edge_K):
    start, end = map(int, input().split())
    mat[start][end] = 1
    mat[end][start] = 1

# for i in mat:
#     print(i)

dq = deque()
visited = [0] * (node_N + 1)
total_cnt = 0
bfs(1)

print(total_cnt - 1)
