import sys
sys.stdin = open('1.txt', 'r')

M, C = map(int, input().split())

csmers = [0] * C
min_idx = 0

for i in range(M):
    msg = int(input())
    for j in range(C):
        if csmers[j] < csmers[min_idx]:
            min_idx = j
    csmers[min_idx] += msg

max_idx = 0
for i in range(C):
    if csmers[i] > csmers[max_idx]:
        max_idx = i

print(csmers[max_idx])