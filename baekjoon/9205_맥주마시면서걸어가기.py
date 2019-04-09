import sys
sys.stdin = open('9205.txt', 'r')

from collections import deque

def bfs(idx, beer):
    global judge
    dq.append([idx, beer])
    while dq:
        idx, beer = dq.popleft()
        position = total_list[idx]
        visited[idx] = 1
        if idx == total_len - 1:
            judge = "happy"
            return
        for i in range(total_len):
            if not visited[i] or i == total_len - 1:
                cand_position = total_list[i]
                distance = abs(position[0] - cand_position[0]) + abs(position[1] - cand_position[1])
                used_beer = (distance - 1) // 50 + 1
                if beer >= used_beer:
                    dq.append([i, 20])


T = int(input())
for tc in range(1, T + 1):
    N_convs = int(input())
    start = list(map(int, input().split()))
    convs = [0] * N_convs
    for i in range(N_convs):
        convs[i] = list(map(int, input().split()))
    end = list(map(int, input().split()))

    total_list = [start] + convs + [end]
    total_len = N_convs + 2

    dq = deque()
    judge = "sad"
    visited = [0] * total_len
    bfs(0, 20)

    print(judge)