import sys
sys.stdin = open('10989.txt', 'r')

N = int(input())
counts = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(10001):
    count = counts[i]
    if count:
        for _ in range(count):
            print(i)

