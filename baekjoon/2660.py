import sys
sys.stdin = open('2660.txt', 'r')

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

def isfull():
    return (rear + 1) % len(q) == front

def isempty():
    return rear == front

def bfs(s):
    max_point = 0
    enqueue(s)
    visited[s] = 1
    # print(isempty())
    while not isempty():
        s = dequeue()
        # print(f"방문: {s}")
        # print(visited)
        # print(q)
        for i in range(m + 1):
            if mat[s][i] and not visited[i]:
                visited[i] = visited[s] + 1
                enqueue(i)
                if visited[i] > max_point:
                    max_point = visited[i]
    #             print(s, i, visited[s], visited, q)
    #             print("내부", front, rear, isempty())
    #             print(max_point)
    # print("result:", visited)
    return max_point - 1



m = int(input())
mat = [[0] * (m + 1) for i in range(m + 1)]
points = [0] * (m + 1)

while True:
    ad_start, ad_end = map(int, input().split())
    if ad_start == -1:
        break
    mat[ad_start][ad_end] = 1
    mat[ad_end][ad_start] = 1

# for i in mat:
#     print(i)

min_list = []
global_min = m + 2
for i in range(1, m + 1):
    q = [0] * m
    front = 0
    rear = 0
    visited = [0] * (m + 1)
    max_point = bfs(i)
    if max_point < global_min:
        global_min = max_point
        min_list = [i]
    elif max_point == global_min:
        min_list.append(i)
    # print()

# print(f"maxpoint: {global_min}, maxlist: {min_list}")
print(global_min, len(min_list))
for num in sorted(min_list):
    print(num, end=" ")
print()