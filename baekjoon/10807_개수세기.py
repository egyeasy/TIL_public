import sys
sys.stdin = open('10807.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
find = int(input())

cnt = 0
for i in range(N):
    if arr[i] == find:
        cnt += 1

print(cnt)