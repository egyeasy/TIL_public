# visited 사용 - 메모리 초과
import sys
sys.stdin = open('2178.txt', 'r')

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs():
    dq.append([0, 0, 0])
    while dq:
        s_row, s_col, curr_cnt = dq.popleft()
        curr_cnt += 1
        visited[s_row][s_col] = 1
        if s_row == N_row - 1 and s_col == M_col - 1:
            return curr_cnt
        else:
            for i in range(4):
                c_row = s_row + dx[i]
                c_col = s_col + dy[i]
                if 0 <= c_row < N_row and 0 <= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                    dq.append([c_row, c_col, curr_cnt])


N_row, M_col = map(int, input().split())
mat = [0] * N_row

for i in range(N_row):
    aline = list(map(int, list(input())))
    mat[i] = aline

dq = deque()
visited = [[0] * M_col for _ in range(N_row)]
total_cnt = bfs()

print(total_cnt)