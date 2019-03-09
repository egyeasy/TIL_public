import sys
sys.stdin = open('15971_.txt', 'r')

from collections import deque

def bfs(s):
    dq.append(s)
    while dq:
        s = dq.popleft()
        if not visited[s]:
            visited[s] = 1
        for i in range(1, N + 1):
            if mat[s][i] and not visited[i]:
                dq.append(i)
                former[i] = s


N, start, end = map(int, input().split())
mat = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N - 1):
    n_start, n_end, n_dis = map(int, input().split())
    mat[n_start][n_end] = n_dis
    mat[n_end][n_start] = n_dis

# for i in mat:
#     print(i)
# print()
dq = deque()
visited = [0] * (N + 1)
former = [0] * (N + 1)
bfs(start)
# print(former)

s = end
e = former[s]
total_dis = 0
max_dis = 0
while s != start:
    this_dis = mat[s][e]
    total_dis += this_dis
    if this_dis > max_dis:
        max_dis = this_dis
    s = e
    e = former[s]

print(total_dis - max_dis)