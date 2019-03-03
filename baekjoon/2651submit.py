import sys
sys.stdin = open('2651.txt', 'r')

def enqueue(item):
    global rear
    if not isfull():
        rear = (rear + 1) % len(q)
        q[rear] = item

def dequeue():
    global front
    if not isempty():
        front = (front + 1) % len(q)
        de_item = q[front]
        q[front] = 0
        return de_item

def isfull():
    return (rear + 1) % len(q) == front

def isempty():
    return rear == front


def bfs(s):
    global no_stops
    if mat[s][m + 1]:
        no_stops = True
        return
    enqueue(s)
    while not isempty():
        s = dequeue()
        for i in range(m + 1, 0, -1):
            if mat[s][i]:
                if i == m + 1:
                    if not visited[i] or visited[s] < visited[i]:
                        former[i] = s
                        visited[i] = visited[s]
                else:
                    cand_time = visited[s] + times[i - 1]
                    if not visited[i] or cand_time < visited[i]:
                        visited[i] = cand_time
                        former[i] = s
                        enqueue(i)

one_go = int(input())
m = int(input())
distances = list(map(int, input().split()))
times = list(map(int, input().split()))

mat = [[0] * (m + 2) for _ in range(m + 2)]
visited = [0] * (m + 2)
former = [0] * (m + 2)

for i in range(m + 2):
    for j in range(m + 2):
        if i < j and sum(distances[i:j]) <= one_go:
            mat[i][j] = 1

q = [0] * (m + 2)
front = 0
rear = 0
no_stops = False

bfs(0)
if no_stops:
    print(0)
    print(0)

else:
    p = m + 1
    time_sum = 0
    num = 0
    result = ""
    while former[p]:
        p = former[p]
        time_sum += times[p - 1]
        num += 1
        result = str(p) + " " + result

    print(time_sum)
    print(num)
    print(result)