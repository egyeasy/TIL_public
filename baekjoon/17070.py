"""


> input


> output


"""
import sys
sys.stdin = open('17070.txt', 'r')

from collections import deque

# 가로, 대각선, 세로
dx = [0, 1, 1]
dy = [1, 1, 0]

# 가로 -> 세로, 대각선 -> none, 세로 -> 가로
excep = [2, 5, 0]

def bfs(s):
    global total_cnt
    dq.append(s)
    while dq:
        s = dq.popleft()
        s_row = s[0]
        s_col = s[1]
        dir = s[2]
        if s_row == side_N - 1 and s_col == side_N - 1:
            total_cnt += 1
        for i in range(3):
            if i == excep[dir]:
                continue
            c_row = s_row + dx[i]
            c_col = s_col + dy[i]
            if 0 <= c_row < side_N and 0 <= c_col < side_N:
                if i == 1 and not mat[c_row][c_col] and not mat[c_row - 1][c_col] and not mat[c_row][c_col - 1]:
                    dq.append([c_row, c_col, 1])
                elif (i == 0 or i == 2) and not mat[c_row][c_col]:
                    dq.append([c_row, c_col, i])

side_N = int(input())
mat = [0] * side_N
for i in range(side_N):
    mat[i] = list(map(int, input().split()))

dq = deque()
total_cnt = 0
bfs([0, 1, 0])
print(total_cnt)


# idea
# 1.