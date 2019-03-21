# 메모리 초과
import sys
sys.stdin = open('10164.txt', 'r')

from collections import deque

# 우 하
dx = [0, 1]
dy = [1, 0]


def bfs(s, end):
    global global_cnt
    dq.append(s)
    part_cnt = 0
    e_row = end[0]
    e_col = end[1]
    while dq:
        s = dq.popleft()
        if s == end:
            part_cnt += 1
        s_row = s[0]
        s_col = s[1]
        for i in range(2):
            c_row = s_row + dx[i]
            c_col = s_col + dy[i]
            if 0 <= c_row <= e_row and 0 <= c_col <= e_col:
                dq.append([c_row, c_col])
    # print("part_cnt", part_cnt)
    global_cnt *= part_cnt


N_row, M_col, K = map(int, input().split())

dq = deque()
global_cnt = 1

if K == 0:
    bfs([0, 0], [N_row - 1, M_col - 1])

else:
    k_row = (K - 1) // M_col
    k_col = (K - 1) % M_col
    bfs([0, 0], [k_row, k_col])
    bfs([k_row, k_col], [N_row - 1, M_col - 1])

print(global_cnt)






# idea
# 1.