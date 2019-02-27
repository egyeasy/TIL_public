import sys
sys.stdin = open('2660.txt', 'r')

m = int(input())
mat = [[0] * (m + 1) for i in range(m + 1)]
while True:
    ad_start, ad_end = map(int, input().split())
    if ad_start == -1:
        break
    mat[ad_start][ad_end] = 1
    mat[ad_end][ad_start] = 1

for i in mat:
    print(i)