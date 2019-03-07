import sys
from collections import deque
sys.stdin = open('2468.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(s):
    dq.append(s)
    while dq:
        s = dq.popleft()
        s_row = s[0]
        s_col = s[1]
        if not visited[s_row][s_col]:
            # 비가 1 더 왔을 때를 여기서 처리
            mat[s_row][s_col] -= 1
            visited[s_row][s_col] = 1
            for i in range(4):
                c_row = s_row + dx[i]
                c_col = s_col + dy[i]
                if 0 <= c_row < side_N and 0 <= c_col < side_N and not visited[c_row][c_col]:
                    # 안 잠기는 곳이라면 방문
                    if mat[c_row][c_col] - 1 > 0:
                        dq.append([c_row, c_col])


side_N = int(input())
mat = [0] * side_N
for i in range(side_N):
    mat[i] = list(map(int, input().split()))

max_area = 1
all_minus = False
# if max_area == 0 break
while not all_minus:
    dq = deque()
    visited = [[0] * side_N for _ in range(side_N)]
    cnt_area = 0
    all_minus = True
    for i in range(side_N):
        for j in range(side_N):
            # 비가 더 왔을 때 잠기지 않을 곳이라면
            if mat[i][j] - 1 > 0 and not visited[i][j]:
                bfs([i, j])
                cnt_area += 1
                all_minus = False
    if cnt_area > max_area:
        max_area = cnt_area

print(max_area)


