"""


> input


> output


"""

import sys
sys.stdin = open('2667.txt', 'r')

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
# 1.