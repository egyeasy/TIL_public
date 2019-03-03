# BFS
import sys
sys.stdin = open('2651.txt', 'r')

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
    global no_stops
    if mat[s][m + 1]:
        no_stops = True
        return
    enqueue(s)
    while not isempty():
        s = dequeue()
        for i in range(m + 1, 0, -1):
            if mat[s][i]:
                print(f"방문: {s}, 후보: {i}")
                if i == m + 1:
                    if not visited[i] or visited[s] < visited[i]:
                        former[i] = s
                        visited[i] = visited[s]
                    # print("도착")
                    # print()
                else:
                    cand_time = visited[s] + times[i - 1]
                    if not visited[i] or cand_time < visited[i]:
                        visited[i] = cand_time
                        former[i] = s
                        enqueue(i)
                print(f"visited: {visited}")
                print(f"former: {former}")


T = int(input())
for tc in range(1, T + 1):
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

    for i in mat:
        print(i)
    print(f"distances: {distances}")
    print(f"times: {times}")

    q = [0] * (m + 2)
    front = 0
    rear = 0
    no_stops = False

    bfs(0)
    print(f"#{tc}")
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