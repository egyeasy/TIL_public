import sys
sys.stdin = open('10989.txt', 'r')

N = int(input())
counts = [0] * 10000

for _ in range(N):
    num = int(input())
    counts[num - 1] += 1

for i in range(N):
    count = counts[i]
    if count:
        for _ in range(count):
            print(i + 1)