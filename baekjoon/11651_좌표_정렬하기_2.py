import sys
sys.stdin = open('11651.txt', 'r')

N = int(input())
points = [0] * N
for i in range(N):
    point = tuple(map(int, input().split()))
    points[i] = point

points = sorted(points, key=lambda x: (x[1], x[0]))

for point in points:
    for num in point:
        print(num, end=" ")
    print()