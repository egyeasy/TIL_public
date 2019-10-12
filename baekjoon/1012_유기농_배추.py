# DFS로 통과

import sys
from collections import deque
sys.stdin = open('1012.txt', 'r')

d_row = [-1, 0, 1, 0]
d_col = [0, 1, 0, -1]

def BFS(start_row, start_col):
    dq.append([start_row, start_col])
    while dq:
        s_row, s_col = dq.pop()
        visited[s_row][s_col] = 1
        for i in range(4):
            c_row = s_row + d_row[i]
            c_col = s_col + d_col[i]
            if 0 <= c_row < N_row and 0<= c_col < M_col and mat[c_row][c_col] and not visited[c_row][c_col]:
                dq.append([c_row, c_col])
        

TC = int(input())
for tc in range(TC):
    M_col, N_row, total_cnt = map(int, input().split())
    mat = [[0] * M_col for _ in range(N_row)]
    for i in range(total_cnt):
        col, row = map(int, sys.stdin.readline().rstrip().split())
        mat[row][col] = 1

    visited = [[0] * M_col for _ in range(N_row)]
    dq = deque()
    result = 0

    for row in range(N_row):
        for col in range(M_col):
            if mat[row][col] and not visited[row][col]:
                result += 1
                BFS(row, col)

    print(result)
