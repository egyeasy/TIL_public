import sys
sys.stdin = open('1932.txt', 'r')

N = int(input())

mat = [0] * N

for i in range(N):
    aline = list(map(int, input().split()))
    mat[i] = aline

max_mat = [[0] * N for _ in range(N)]

max_mat[0][0] = mat[0][0]
total_max = -1

for row in range(1, N):
    for col in range(row + 1):
        if col == 0:
            max_mat[row][col] = max_mat[row - 1][col] + mat[row][col]
        elif col == row:
            max_mat[row][col] = max_mat[row - 1][col - 1] + mat[row][col]
        else:
            max_mat[row][col] = max(max_mat[row - 1][col - 1], max_mat[row - 1][col]) + mat[row][col]
        if row == N - 1 and max_mat[row][col] > total_max:
            total_max = max_mat[row][col]

print(total_max)