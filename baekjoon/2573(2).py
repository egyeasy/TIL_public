import sys
from collections import deque
sys.stdin = open('2573.txt', 'r')
input = sys.stdin.readline

def enqueue(item):
    global rear
    rear = (rear + 1) % len(q)
    q[rear] = item

def dequeue():
    global front
    front = (front + 1) % len(q)
    de_item = q[front]
    q[front] = 0
    return de_item

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(s):
    global front, rear
    enqueue(s)
    ## q.append(s)
    # lenq = len(q)
    # rear = (rear + 1) % lenq
    # q[rear] = s
    ## while q:
    while not rear == front:
        s = dequeue()
        ## s = q.popleft()
        # front = (front + 1) % lenq
        # s = q[front]
        s_row = s[0]
        s_col = s[1]
        if not visited[s_row][s_col]:
            visited[s_row][s_col] = 1
            water_around = 0
            for i in range(4):
                c_row = s_row + dx[i]
                c_col = s_col + dy[i]
                if c_row < 0 or c_row >= N_row or c_col < 0 or c_col >= M_col:
                    continue
                if not mat[c_row][c_col] and not visited[c_row][c_col]:
                    water_around += 1
                elif mat[c_row][c_col] and not visited[c_row][c_col]:
                    enqueue([c_row, c_col])
                    ## q.append([c_row, c_col])
                    # rear = (rear + 1) % lenq
                    # q[rear] = [c_row, c_col]
            if water_around:
                after_value = mat[s_row][s_col] - water_around
                mat[s_row][s_col] = after_value * (after_value > 0)

            # print("visited", s, "water_around", water_around, after_value * (after_value > 0))

N_row, M_col = map(int, input().split())
mat = [0] * N_row
for i in range(N_row):
    mat[i] = list(map(int, input().split()))

# for i in mat:
#     print(i)
# print()

total_time = 0
all_zero = False
found = False
first_row = 0


while not all_zero:
    q = [0] * (N_row * M_col)
    rear = 0
    front = 0
    # q = deque()
    visited = [[0] * M_col for _ in range(N_row)]
    continent_cnt = 0
    all_zero = True

    for i in range(first_row, N_row):
        for j in range(M_col):
            if mat[i][j]:
                all_zero = False
                if not visited[i][j]:
                    continent_cnt += 1
                    if continent_cnt >= 2:
                        found = True
                        break
                    bfs([i, j])
                    # print([i, j], continent_cnt)
        ##
        if found:
            break
    # print(total_time, continent_cnt)
    # for i in mat:
    #     print(i)
    # print()
    if found:
        break
    ##

    # if continent_cnt >= 2:
    #     break

    total_time += 1

    # for i in mat:
    #     print(i)
    # print()


if found:
    print(total_time)
else:
    print(0)

