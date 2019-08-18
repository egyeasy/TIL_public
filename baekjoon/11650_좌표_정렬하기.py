import sys
sys.stdin = open('11650.txt', 'r')

N = int(input())

points = [0] * N

for i in range(N):
    point = tuple(map(int, input().split()))
    points[i] = point

points.sort(key=lambda x: (x[0], x[1]))

for point in points:
    for num in point:
        print(num, end=" ")
    print()