import sys
sys.stdin = open('15971.txt', 'r')

from collections import deque

def bfs(s):
    dq.append(s)
    visited[s] = 1
    while dq:
        s = dq.popleft()
        for i in range(1, N + 1):
            if mat[s][i] and not visited[i]:
                dq.append(i)
                former[i] = s
                # 최대거리 기록
                if mat[s][i] >= visited[s]:
                    visited[i] = mat[s][i]
                else:
                    visited[i] = visited[s]
                # 누적거리 기록
                mat[s][i] += mat[former[s]][s]
                # 종결
                if i == end:
                    print(mat[s][i] - visited[i])
                    return
                    # for k in mat:
                    #     print(k)
                    # print()
                    # print(visited)


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
if N <= 2:
    print(0)
else:
    bfs(start)
# print(former)

# print()
# print(visited)
# print()
# for i in mat:
#     print(i)
# print()
