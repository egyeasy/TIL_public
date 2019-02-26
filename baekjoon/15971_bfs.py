import sys
sys.stdin = open('15971.txt', 'r')

def enqueue(item):
    global rear
    if isfull():
        print("isfull")
    else:
        rear = (rear + 1) % len(q)
        q[rear] = item

def dequeue():
    global front
    if isempty():
        print("isempty")
    else:
        front = (front + 1) % len(q)
        de_item = q[front]
        q[front] = 0
        return de_item

def isfull():
    return (rear + 1) % len(q) == front

def isempty():
    return rear == front

def bfs(s):
    global max_floor, max_dis
    enqueue(s)
    floor[s] = 1
    while not isempty():
        s = dequeue()
        if not visited[s]:
            visited[s] = 1
            print(f"visited {s}, former of s is: {former[s]}")
            if not floor[s]:
                print("not floor")
                floor[s] = floor[former[s]] + 1
            if floor[s] > max_floor:
                max_floor = floor[s]
                max_list = [0] * m
                max_idx = 0
                max_list[max_idx] = floor[s]
            elif floor[s] == max_floor:
                max_idx += 1
                max_list[max_idx] = floor[s]

            if s == end:
                return max_list
            print(f"floor: {floor}\nformer: {former}")
            for i in range(m + 1):
                dis = matrix[s][i]
                if dis and not visited[i]:
                    if not former[i]:
                        former[i] = s
                        if former[s]:
                            if dis < max_dis:
                                matrix[s][i] = matrix[former[s]][s] + dis
                            else:
                                matrix[s][i] = matrix[former[s]][s] + max_dis
                                max_dis = dis
                    print(f"matrix:")
                    for k in matrix:
                        print(k)
                    enqueue(i)

T = int(input())
for tc in range(1, T + 1):
    m, start, end = map(int, input().split())
    matrix = [[0] * (m + 1) for i in range(m + 1)]
    visited = [0] * (m + 1)
    former = [0] * (m + 1)
    floor = [0] * (m + 1)
    q = [0] * (m + 1)
    front = 0
    rear = 0
    for i in range(m - 1):
        aline = list(map(int, input().split()))
        matrix[aline[0]][aline[1]] = aline[2]
        matrix[aline[1]][aline[0]] = aline[2]

    for i in matrix:
        print(i)

    max_floor = 0
    max_dis = 0
    max_lists = bfs(start)
    print(max_lists)

    print()