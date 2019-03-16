"""
동근이는 무인 경비 회사 경비원으로 항상 대기하고 있다가 호출이 들어오면 경비차를 몰고 그 곳으로 달려가야 한다. 동근이가 담당하고 있는 곳은 직사각형 모양의 블록으로 블록 중간을 가로질러 차가 통과할만한 길이 없다. 이 블록 경계에 무인 경비를 의뢰한 상점들이 있다.

예를 들어 가로의 길이가 10, 세로의 길이가 5인 블록의 경계에 무인 경비를 의뢰한 3개의 상점이 있다고 하자. <그림 1>과 같이 이들은 1, 2, 3으로 표시되어 있고, 동근이는 X로 표시한 위치에 있다.

1번 상점에서 호출이 들어 왔을 때 동근이가 블록을 시계방향으로 돌아 이동하면 이동 거리가 12가 된다. 반면 반시계방향으로 돌아 이동하면 이동 거리는 18이 된다. 따라서 동근이가 1번 상점으로 가는 최단 거리는 12가 된다. 마찬가지로 동근이의 위치에서 2번 상점까지의 최단 거리는 6, 3번 상점까지의 최단 거리는 5가 된다.

블록의 크기와 상점의 개수 및 위치 그리고 동근이의 위치가 주어질 때 동근이의 위치와 각 상점 사이의 최단 거리의 합을 구하는 프로그램을 작성하시오.

> input
첫째 줄에 블록의 가로의 길이와 세로의 길이가 차례로 주어진다. 둘째 줄에 상점의 개수가 주어진다. 블록의 가로의 길이와 세로의 길이, 상점의 개수는 모두 100이하의 자연수이다. 이어 한 줄에 하나씩 상점의 위치가 주어진다. 상점의 위치는 두 개의 자연수로 표시된다. 첫째 수는 상점이 위치한 방향을 나타내는데, 1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미한다. 둘째 수는 상점이 블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리를 나타내고, 상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리를 나타낸다. 마지막 줄에는 동근이의 위치가 상점의 위치와 같은 방식으로 주어진다. 상점의 위치나 동근이의 위치는 블록의 꼭짓점이 될 수 없다.

10 5
3
1 4
3 2
2 8
2 3

> output
첫째 줄에 동근이의 위치와 각 상점 사이의 최단 거리의 합을 출력한다.

23

"""
import sys
sys.stdin = open('2564.txt', 'r')

width, height = map(int, input().split())
N = int(input())

points = []

for i in range(N):
    points.append(list(map(int, input().split())))

s_dir, s_point = map(int, input().split())
total_distance = 0

for point in points:
    if s_dir == point[0]:
        total_distance += abs(s_point - point[1])
    elif s_dir + point[0] == 3:
        # print(s_dir, point[0])
        route_1 = s_point + height + point[1]
        route_2 = (width - s_point) + height + (width - point[1])
        if route_1 <= route_2:
            total_distance += route_1
        else:
            total_distance += route_2
        # print(total_distance)
    elif s_dir + point[0] == 7:
        route_1 = s_point + width + point[1]
        route_2 = (height - s_point) + width + (height - point[1])
        if route_1 <= route_2:
            total_distance += route_1
        else:
            total_distance += route_2
        # print(total_distance)
    else:
        if s_dir == 1:
            if point[0] == 3:
                total_distance += s_point + point[1]
                # print(total_distance)
            else:
                total_distance += (width - s_point) + point[1]
                # print(total_distance)
        elif s_dir == 2:
            if point[0] == 3:
                total_distance += s_point + (height - point[1])
                # print(s_dir, point[1])
                # print(total_distance)
            else:
                total_distance += (width - s_point) + (height - point[1])
                # print(s_dir, point[1])
                # print(total_distance)
        elif s_dir == 3:
            if point[0] == 1:
                total_distance += s_point + point[1]
                # print(total_distance)
            else:
                total_distance += (height - s_point) + point[1]
                # print(total_distance)
        else:
            if point[0] == 1:
                total_distance += s_point + (width - point[1])
                # print(total_distance)
            else:
                total_distance += (height - s_point) + (width - point[1])
                # print(total_distance)

print(total_distance)



# idea
# 1. handling if case 
# 2. It can be a shorter code....
