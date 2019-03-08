import sys
sys.stdin = open('2589.txt', 'r')

from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(s):
    global this_max
    dq.append(s)
    s_row = s[0]
    s_col = s[1]
    visited[s_row][s_col] = 1
    while dq:
        s = dq.popleft()
        s_row = s[0]
        s_col = s[1]
        # print("visited s:", s)
        for i in range(4):
            c_row = s_row + dx[i]
            c_col = s_col + dy[i]
            if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                dq.append([c_row, c_col])
                visited[c_row][c_col] = visited[s_row][s_col] + 1
                if visited[c_row][c_col] > this_max:
                    this_max = visited[c_row][c_col]

N_row, M_col = map(int, input().split())
mat = [[0] * M_col for _ in range(N_row)]
for i in range(N_row):
    aline = list(input())
    for j in range(M_col):
        mat[i][j] = 1 if aline[j] == "L" else 0

# for i in mat:
#     print(i)
# print()

total_max = 0
for i in range(N_row):
    for j in range(M_col):
        if mat[i][j]:
            dq = deque()
            visited = [[0] * M_col for _ in range(N_row)]
            this_max = 0
            bfs([i, j])
            if this_max > total_max:
                total_max = this_max
            # print("start:", i, j, "visited")
            # print("this max:", this_max)
            # for k in visited:
            #     print(k)
            # print()

print(total_max - 1)