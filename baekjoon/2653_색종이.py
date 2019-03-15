"""


> input


> output


"""
import sys
sys.stdin = open('2653.txt', 'r')

mat = [[0] * 100 for _ in range(100)]

N = int(input())
for n in range(N):
    row, col = map(int, input().split())
    for i in range(row, row + 10):
        for j in range(col, col + 10):
            mat[i][j] = 1

total_cnt = 0
for i in range(100):
    for j in range(100):
        if mat[i][j]:
            total_cnt += 1

print(total_cnt)



# idea
# 1.