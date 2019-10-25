import sys
sys.stdin = open('1780.txt', 'r')

import math

def go_into(s_row, s_col, log_size):
    size = 3 ** log_size
    start = mat[s_row][s_col]
    is_same = True
    for i in range(s_row, s_row + size):
        for j in range(s_col, s_col + size):
            if mat[i][j] != start:
                is_same = False
                break
        if not is_same:
            break
    if is_same:
        count[start] += 1
    else:
        next_size = 3 ** (log_size - 1)
        for i in range(3):
            for j in range(3):
                go_into(s_row + i * next_size, s_col + j * next_size, log_size - 1)


N = int(input())

mat = [0] * N

for i in range(N):
    aline = list(map(int, input().split()))
    mat[i] = aline

n = round(math.log(N, 3))
count = {-1: 0, 0: 0, 1: 0}

go_into(0, 0, n)

for value in count.values():
    print(value)