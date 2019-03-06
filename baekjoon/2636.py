import sys
sys.stdin = open('2636.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def enqueue(item):
    global rear
    if not isfull():
        rear = (rear + 1) % len(q)
        q[rear] = item
    else:
        print("isfull")

def dequeue():
    global front
    if not isempty():
        front = (front + 1) % len(q)
        de_item = q[front]
        q[front] = 0
        return de_item
    else:
        print("isempty")

def isfull():
    return (rear + 1) % len(q) == front

def isempty():
    return rear == front


def bfs(s):
    global all_done
    enqueue(s)
    cnt = 0
    while not isempty():
        s = dequeue()
        s_row = s[0]
        s_col = s[1]
        if not visited[s_row][s_col]:
            visited[s_row][s_col] = 1
            # print("visited", s)
            for i in range(4):
                c_row = s[0] + dx[i]
                c_col = s[1] + dy[i]
                if (0 <= c_row < M) and (0 <= c_col < N):
                    if mat[c_row][c_col] == 0 and not visited[c_row][c_col]:
                        enqueue([c_row, c_col])
                    elif mat[c_row][c_col] == 1 and not visited[c_row][c_col]:
                        mat[c_row][c_col] = 0
                        visited[c_row][c_col] = 1
                        cnt += 1
                        # print("[", c_row, c_col, "]")
                        all_done = False
    if cnt:
        return cnt

M, N = map(int, input().split())
mat = [[0] * N  for _ in range(M)]
# print(M, N)

for i in range(M):
    aline = list(map(int, input().split()))
    for j in range(N):
        mat[i][j] = aline[j]

# for i in mat:
#     print(i)
# print()

timer = 0
all_done = False
results = []
while not all_done:
    q = [0] * (N * M)
    front = 0
    rear = 0
    visited = [[0] * N  for _ in range(M)]
    all_done = True
    count = bfs([0, 0])
    results.append(count)
    # for k in mat:
    #     print(k)
    # print()
    timer += 1
    # print("timer", timer)
    if all_done:
        break

print(timer - 1)
for i in results[::-1]:
    if i:
        print(i)
        break

