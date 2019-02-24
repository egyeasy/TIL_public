"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

> input
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

> output
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

3
7
8
9

"""

import sys
sys.stdin = open('2667.txt', 'r')

each_cnt = 0

def DFS(s):
    global each_cnt
    visited[s[0]][s[1]] = 1
    each_cnt += 1
    go_list = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for go in go_list:
        if matrix[s[0] + go[0]][s[1] + go[1]] == 1 and not visited[s[0] + go[0]][s[1] + go[1]]:
            DFS([s[0] + go[0], s[1] + go[1]])



m = int(input())
matrix = [[0] * (m + 2) for i in range(m + 2)]
visited = [[0] * (m + 2) for i in range(m + 2)]
for i in range(m):
    aline = list(map(int, input()))
    for j in range(m):
        matrix[i + 1][j + 1] = aline[j]

# for i in matrix:
#     print(i)

total_cnt = 0
each_cnt = 0
cnts = [0] * (m**2)
idx = 0

for i in range(1, m + 2):
    for j in range(1, m + 2):
        if matrix[i][j] == 1 and not visited[i][j]:
            each_cnt = 0
            total_cnt += 1
            DFS([i, j])
            # print(each_cnt)
            cnts[idx] = each_cnt
            idx += 1


print(total_cnt)
for i in sorted(cnts[:total_cnt]):
    print(i)



# idea
# 1. Some details are added in DFS problem.
# 2. Most important: Catching this is DFS problem.