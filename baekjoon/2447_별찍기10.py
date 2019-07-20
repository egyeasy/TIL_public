import sys
sys.stdin = open('2447.txt', 'r')

import math

matrix = []

def capture(n):
    N = 3 ** n
    stamp_mat = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            stamp_mat[i][j] = matrix[i][j]
    return stamp_mat

def paste(stamp, n, stage):
    N = 3 ** n
    row_start = (stage // 3) * N
    # row_end = (stage // 3) * (N + 1)
    col_start = (stage % 3) * N
    # col_end = (stage % 3) * (N + 1)
    for i in range(N):
        for j in range(N):
            # print('stage: ', stage, "n: ", n, "N: ", N, "row: ", row_start + i, "col: ", col_start + j, "i, j: ", "({}, {})".format(i, j))
            matrix[row_start + i][col_start + j] = stamp[i][j]
    

def copy_paste(n, stage):
    stamp = capture(n)
    paste(stamp, n, stage)


def matplot(n):
    for i in range(9):
        if i != 4:
            copy_paste(n, i)
            

N = int(input())

matrix = [[" "] * N for _ in range(N)]
# loggN = math.log(N, 3)
logN = round(math.log(N, 3))
# print(logN)

matrix[0][0] = '*'
for i in range(logN):
    matplot(i)

# for i in matrix:
#     print(i)

# print()

for i in range(N):
    for j in range(N):
        print(matrix[i][j], end="")
    print()