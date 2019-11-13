### c_row, c_col을 탐색할 때 미리 visited를 처리해줘야 가짓수가 많이 줄어든다.
import sys
from collections import deque

sys.stdin = open('2178.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    dq.append([0, 0])
    while dq:
        s_row, s_col = dq.popleft()
        # if s_row == N_row - 1 and s_col == M_col - 1:
        #     return curr_cnt
        # else:
        for i in range(4):
            c_row = s_row + dx[i]
            c_col = s_col + dy[i]
            if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                    mat[c_row][c_col] = mat[s_row][s_col] + 1
                    visited[c_row][c_col] = 1
                    dq.append([c_row, c_col])


N_row, M_col = map(int, input().split())

mat = [list(map(int, list(input()))) for _ in range(N_row)]

dq = deque()
visited = [[0] * M_col for _ in range(N_row)]
bfs()

print(mat[N_row - 1][M_col - 1])