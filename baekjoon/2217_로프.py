import sys
sys.stdin = open('2217.txt', 'r')

N = int(input())
min_weight = 10001
for i in range(N):
    weight = int(sys.stdin.readline())
    if weight < min_weight:
        min_weight = weight

answer = min_weight * N
print(answer)