import sys
from collections import deque

sys.stdin = open('1260.txt', 'r')


def DFS(s):
    while dq:
        s = dq.pop()
        # print(s)
        result[0].append(s)
        for c in mat[s]:
            if not visited[c]:
                dq.append(c)
                visited[c] = 1
                DFS(c)

def BFS(s):
    dq.append(s)
    visited[s] = 1
    while dq:
        s = dq.popleft()
        # print(s)
        result[1].append(s)
        for c in mat[s]:
            if not visited[c]:
                dq.append(c)
                visited[c] = 1


N_nodes, M_edges, V_start = map(int, input().split())
mat = [[] for _ in range(N_nodes + 1)]

for i in range(M_edges):
    start, end = map(int, sys.stdin.readline().split())
    mat[start].append(end)
    mat[end].append(start)

# for i in mat:
#     print(i)

for nums in mat:
    nums.sort()

result = [[] for _ in range(2)]

visited = [0] * (N_nodes + 1)
dq = deque()
dq.append(V_start)
visited[V_start] = 1
DFS(V_start)

visited = [0] * (N_nodes + 1)
dq = deque()
BFS(V_start)

for r in result:
    for num in r:
        print(num, end=" ")
    print()